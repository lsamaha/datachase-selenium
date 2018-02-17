__author__ = 'lsamaha'

import os
import click
import csv
from selenium import webdriver
from westwebdata import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@click.command()
@click.option('--home_url', default="http://www.westlaw.com", help='WestLaw home URL')
@click.option('--user', help='WestLaw User', required=True)
@click.password_option()
@click.option('--query', help='Query to retrieve work (if no CSV input is specified)')
@click.option('--infile', help='CSV file defining cases to get (if no query is specified)')
@click.option('--outfile', help='File where results will be written', required=True)
@click.option('--perjudge/--no-perjudge', default=False, help='Summarize by judge', required=True)
def main(home_url, user, password, query, infile, outfile, perjudge):
    print(os.environ["PATH"])
    if query is None and infile is None:
        print("Either --infile or --query is required")
        exit(1)
    write(get_case_summaries(home_url, user, password, query, infile), outfile, perjudge)


def get_options(params):
    if len(params) < 5:
        raise (Exception("Invalid number of params"))
    opts = {'user': params[1], 'password': params[2], 'outfile': params[4]}
    if params[3].endswith('.csv'):
        opts['infile'] = params[3]
    else:
        opts['query'] = params[3]
    opts['per_judge'] = True if len(params) > 5 and params[5].lower() == 'true' else False
    return opts


def get_case_summaries(home_url, user, password, query, infile, page_size=100):
    case_summary_ids = set()
    case_summaries = []
    browser = webdriver.Firefox()
    browser.implicitly_wait(15)
    wait = WebDriverWait(browser, 15)

    browser.get(home_url)
    username = browser.find_element_by_name("Username")
    username.send_keys(user)
    browser.find_element_by_name("Password").send_keys(password)
    signin = browser.find_element_by_id("SignIn")
    signin.click()
    client_id = wait.until(EC.element_to_be_clickable((By.ID, 'co_clientIDTextbox')))
    client_id.clear()
    client_id.send_keys('Q')
    client_id.send_keys(Keys.ENTER)

    # caselaw query string
    if query is not None:
        # set search field
        wait.until(EC.element_to_be_clickable((By.ID, 'searchInputId'))).send_keys(opts['query'])
        click(By.ID, 'searchButton', wait=wait)
        click(By.ID, 'co_search_contentNav_link_CASE', wait=wait)
        # get result counts
        count_elem = browser.find_element_by_class_name('co_search_titleCount')
        total = int(count_elem.text[1:-1])
        # assumed page size
        next_page_at = page_size
        for count in range(1, total + 1):
            # get each case by ID on this page
            if count % (next_page_at + 1) == 0:
                click(by=By.ID, expr='co_search_footer_pagination_next', retries=10, wait=wait)
            click(by=By.ID, expr="cobalt_result_case_title%d" % (count), wait=wait)
            try:
                # test to see if we got a plain single doc result page
                find(browser=browser, by=By.ID, expr='co_docFixedHeader', retries=1)
                # test if browser url matches a case
                if browser.current_url not in case_summary_ids:
                    # summarize this case
                    summary = parse_westlaw_html(browser.page_source)
                    print(summary)
                    case_summaries.append(summary)
                case_summary_ids.add(browser.current_url)
            except:
                print("unable to evaluate %s %d" % (browser.current_url, count))
            # return to page with list of case links
            click(by=By.LINK_TEXT, expr='Return to list', wait=wait)
            print("%d/%d" % (count, total))
    elif infile is not None:
        # query using an input file with one cases per line
        count = 0
        total = 0
        with open(infile) as f:
            for n in f.readlines():
                total += 1
        with open(infile) as f:
            for case in f.readlines():
                if case in case_summary_ids:
                    print("skipping %s" % case)
                else:
                    # use search field
                    case_summary_ids.add(case)
                    wait.until(EC.element_to_be_clickable((By.ID, 'searchInputId')))
                    searchInput = find(browser=browser, by=By.ID, expr='searchInputId', retries=10)
                    searchInput.clear()
                    searchInput.send_keys(case)
                    click(by=By.ID, expr='searchButton', wait=wait, retries=10)
                    try:
                        find(by=By.ID, expr='co_search_result_heading_content', retries=3)
                        print("warning: ignoring multiple results for %s" % ())
                    except:
                        try:
                            # did we link to a doc or list
                            find(browser=browser, by=By.ID, expr='co_docFixedHeader', retries=3)
                            print("evaluating: %s" % (browser.title))
                            summary = parse_westlaw_html(browser.page_source)
                            print(summary)
                            case_summaries.append(summary)
                            browser.back()
                        except WebDriverException as e:
                            print(e)
                            print("warning: unable to evaluate %s (multiple results?)" % (case))
                count += 1
                print("%d/%d" % (count, total))
    browser.close()
    return case_summaries


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
            print("retrying ...")
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
            print("finding %s by %s in %s" % (expr, by, browser.current_url))
            elem = browser.find_element(by=by, value=expr)
        except WebDriverException as e:
            tries += 1
            print(e)
            print("retrying ...")
            pass
    return elem


def write(case_summaries, outfile, per_judge):
    '''
    Write a case summary to a file.
    :param case_summaries: A list of case summaries
    :param outfile: An output file
    :param per_judge: If true, write a separate row for each judge on a case
    '''
    with open(outfile, 'w') as f:
        print("writing %d summaries to %s" % (len(case_summaries), outfile))
        writer = csv.writer(f)
        cols = set()
        for case in case_summaries:
            for col in sorted(case):
                cols.add(col)
        cols = sorted(cols)
        writer.writerow(cols)
        for case_summary in case_summaries:
            if per_judge:
                if 'panel' in case_summary:
                    per_judge_case_summary = case_summary.copy()
                    for judge in case_summary['panel']:
                        per_judge_case_summary['panel'] = judge
                        writer.writerow(record_to_list(per_judge_case_summary, cols))
            else:
                writer.writerow(record_to_list(case_summary, cols))


def record_to_list(row_in, cols):
    '''
    Create a list of values containing provided coluumns. Represent list fields as compound delimited values.
    :param row_in: A row to parse
    :param cols: Columns to include
    :return: A list of strings
    '''
    row_out = []
    for col in cols:
        if col in row_in:
            val = row_in[col]
            if type(val) is list or type(val) is tuple:
                val = ', '.join(val)
            row_out.append(val)
        else:
            row_out.append('')
    return row_out


if __name__ == '__main__':
    main()
