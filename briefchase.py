__author__ = 'conorsg'

import os
import click
import csv
from selenium import webdriver
from briefdata import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@click.command()
@click.option('--home_url', default='http://www.westlaw.com', help='WestLaw home URL')
@click.option('--user', help='WestLaw User', required=True)
@click.password_option()
@click.option('--infile', help='CSV file defining cases to get', required=True)
@click.option('--informat', default='single', help='Format of CSV input file. Use "single" for a single column of queries, or "FJC" for multiple field restrictors in the FJC style')

def main(home_url, user, password, infile, informat):
    if infile is None:
        print('--infile is required')
        exit(1)
    get_briefs(home_url, user, password, infile, informat)


def get_briefs(home_url, user, password, infile, informat):
    # initialize summaries list and selenium vars
    summaries = []
    browser = webdriver.Firefox()
    browser.implicitly_wait(15)
    wait = WebDriverWait(browser, 15)

    # login to westlaw
    browser.get(home_url)
    username = browser.find_element_by_name('Username')
    username.send_keys(user)
    browser.find_element_by_name('Password').send_keys(password)
    signin = browser.find_element_by_id('SignIn')
    signin.click()
    client_id = wait.until(EC.element_to_be_clickable((By.ID, 'co_clientIDTextbox')))
    client_id.send_keys(Keys.ENTER)

    # open input file and run operations on it
    with open(infile) as f:
        for case in f.readlines():

            # set query based on informat
            case_query = {}

            if informat == 'single':
                case_query['name'] = case
                case_query['query'] = case

            elif informat.lower() == 'fjc':
                case_input_list = case.split(',')
                case_query['name'] = case_input_list[1]
                case_query['query'] = 'PR(' + case_input_list[0] + ' Cir.) & DN(' + case_input_list[1] + ') & TI(' + case_input_list[2] + ' & ' + case_input_list[3] + ') & DA(' + case_input_list[4] + ')'

            else:
                print('--informat not recognized. setting to single')
                case_query['name'] = case
                case_query['query'] = case

            # make case folder to store brief downloads
            os.chdir('output')
            os.mkdir(case_query['name'])
            os.chdir(case_query['name'])

            # set search field
            wait.until(EC.element_to_be_clickable((By.ID, 'searchInputId')))
            searchInput = find(browser=browser, by=By.ID, expr='searchInputId', retries=10)
            searchInput.clear()
            searchInput.send_keys(case_query['query'])
            click(by=By.ID, expr='searchButton', wait=wait, retries=10)

            # wait for case to load or click first result if format is 'FJC'
            if informat == 'single':
                try:
                    wait.until(EC.presence_of_element_located((By.ID, 'co_document')))
                    find(browser=browser, by=By.ID, expr='co_docFixedHeader', retries=3)
                    print('evaluating: %s' % (browser.title))
                except:
                    print('No case returned')
                    summary = [case_query['name'], 'No case returned']
                    summaries.append(summary)
                    os.chdir('../../')
                    continue

            elif informat.lower() == 'fjc':
                try:
                    wait.until(EC.presence_of_element_located((By.ID, 'cobalt_search_case_results')))
                    find(browser=browser, by=By.ID, expr='cobalt_result_case_title1', retries=3)
                    click(by=By.ID, expr='cobalt_result_case_title1', wait=wait, retries=10)
                    print('evaluating: %s' % (browser.title))
                except:
                    print('No case returned')
                    summary = [case_query['name'], 'No case returned']
                    summaries.append(summary)
                    os.chdir('../../')
                    continue

            # click filings tab
            wait.until(EC.text_to_be_present_in_element((By.ID, 'coid_relatedInfo_riFilings_link'), 'Filings ('))
            wait.until(EC.element_to_be_clickable((By.ID, 'coid_relatedInfo_riFilings_link')))
            click(by=By.ID, expr='coid_relatedInfo_riFilings_link', wait=wait, retries=10)

            # get dockets and briefs using a bear of an Xpath expression
            wait.until(EC.presence_of_element_located((By.ID, 'co_relatedInfo_table_filings')))

            # skip cases with pages of filings
            if len(browser.find_elements_by_css_selector('.co_navFooter_pagination')) > 0:
                os.chdir('../../')
                continue

            dockets = browser.find_elements_by_xpath('//td[@class="co_detailsTable_content"][following-sibling::td[@class="co_detailsTable_court"][text() != "U.S."] and following-sibling::td[@class="co_detailsTable_type"][text() = "Docket"]]/a')
            briefs = browser.find_elements_by_xpath('//td[@class="co_detailsTable_content"][following-sibling::td[@class="co_detailsTable_court"][text() != "U.S."] and following-sibling::td[@class="co_detailsTable_type"][text() = "Brief"]]/a')
            filings_page_window = browser.current_window_handle

            # get data from dockets
            for docket in dockets:
                docket_url = docket.get_attribute('href')

                browser.execute_script('window.open()')
                browser.switch_to_window(browser.window_handles[1])
                browser.get(docket_url)

                try:
                    try:
                        # update docket
                        wait.until(EC.presence_of_element_located((By.ID, 'co_docketsUpdate')))
                        old_url = browser.current_url
                        click(by=By.ID, expr='co_docketsUpdate', wait=wait, retries=10)
                        try:
                            WebDriverWait(browser, 30).until(lambda browser: browser.current_url != old_url) #waits until docket update is complete by looking for change in URL -- the only way i could figure out how to note the update
                        except:
                            print('Exception!')
                            # write docket summary as timeout
                            summary = []
                            summary.append(str(case_query['name']))
                            summary.append('Docket timeout')
                            continue
                    except:
                        print('No docket update button found')
                        continue

                    # parse docket html and add to master summaries list
                    summary = []
                    summary.append(str(case_query['name']))
                    summary.extend(parse_docket_html(browser.page_source))
                    summaries.append(summary)

                    # write docket summary. hardcode headers. not great, but meh
                    os.chdir('../../output')
                    headers = ['Case', 'Court', 'Docket', 'Case Subtype', 'Nature of Suit', 'Docket Length']
                    write(summaries, headers, 'docket summary.csv')
                    os.chdir(case_query['name'])
                except:
                    print('No docket at URL!')

                # go back
                browser.execute_script('window.close()')
                browser.switch_to_window(filings_page_window)

            # get html and pdf versions of briefs
            for brief in briefs:
                brief_url = brief.get_attribute('href')

                browser.execute_script('window.open()')
                browser.switch_to_window(browser.window_handles[1])
                browser.get(brief_url)

                # check if brief page loads and then download briefs
                try:
                    wait.until(EC.presence_of_element_located((By.ID, 'co_document')))
                    download_briefs(browser.page_source)
                except:
                    print('No brief at URL!')

                # go back
                browser.execute_script('window.close()')
                browser.switch_to_window(filings_page_window)

            os.chdir('../../')

    browser.close()

    #hardcode headers. not great, but meh
    # os.chdir('output')
    # headers = ['Case', 'Court', 'Docket', 'Case Subtype', 'Nature of Suit', 'Docket Length']
    # write(summaries, headers, 'docket summary.csv')


def click(by, expr, wait, retries=3):
    '''
    A click function with waits and retries
    :param by: means of selection (e.g. ID, class)
    :param expr: DOM selection expression
    :param wait: seconds to wait
    :param retries: max retries
    :return: whether the click occured
    '''
    print("clicking %s %s" % (expr, by))
    clicked = False
    tries = 0
    while not clicked and tries < retries:
        try:
            wait.until(EC.element_to_be_clickable((by, expr))).click()
            clicked = True
        except WebDriverException as e:
            tries += 1
            print('retrying ...')
            pass
    return clicked


def find(browser, by, expr, retries=30):
    '''
    Find an element in the DOM with retries.
    :param browser: reference to the selenium browser driver instance
    :param by: means of selection (e.g. ID, class)
    :param expr: DOM selection expression
    :param retries: max retries
    :return: whether the DOM element was found
    '''
    print("finding %s %s" % (expr, by))
    elem = None
    tries = 0
    while not elem and tries < retries:
        try:
            print('finding %s by %s in %s' % (expr, by, browser.current_url))
            elem = browser.find_element(by=by, value=expr)
        except WebDriverException as e:
            tries += 1
            print(e)
            print('retrying ...')
            pass
    return elem


def write(d, h, out):
    with open (out, 'w+') as f:
        writer = csv.writer(f)
        writer.writerow(h)
        writer.writerows(d)


if __name__ == '__main__':
    main()
