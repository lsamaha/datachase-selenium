__author__ = 'conorsg'

from bs4 import BeautifulSoup
import re

def parse_docket_html(html):
    soup = BeautifulSoup(html)

    try:
        ct = soup.find('td', string='Court:').next_sibling.getText()
    except:
        ct = 'NA'
    try:
        d = soup.find('td', string='Case Number:').next_sibling.getText()
    except:
        d = 'NA'
    try:
        s = soup.find('td', string='Case Subtype:').next_sibling.getText()
    except:
        s = 'NA'
    try:
        n = soup.find('td', string='Nature of Suit:').next_sibling.getText()
    except:
        n = 'NA'
    try:
        dn = soup.select('#co_docketDocketProceedings')[0].getText()
        dn = re.findall('[0-9]{1,3}', dn)[0]
    except:
        dn = 'NA'

    data = [ct, d, s, n, dn]

    return(data)

def download_briefs(html):
    soup = BeautifulSoup(html)
    outname = soup.select('#title')[0].getText()
    for ch in ['/', ':']:
        outname = outname.replace(ch, '-')

    # download pdf of brief
    # broken: have to figure out auth headers to pass to pdf_url
    # pdf_url = soup.select('.co_blobLink')[0]['href']
    # response = requests.get(pdf_url)
    # with open(outname + '.pdf', 'wb') as f:
    #     f.write(response.content)

    # download html of brief
    brief_html = soup.select('#co_document')
    with open(outname + '.html', 'w') as f:
        f.write(str(brief_html))
