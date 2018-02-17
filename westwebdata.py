__author__ = 'lsamaha'

from lxml.html.soupparser import fromstring
from dateutil import parser

'''
Takes a westlaw html presentation of a case and inspects style markers to parse data fields.
'''

def parse_westlaw_html(html):
    '''
    Creates a structured set of values from a Westlaw case in HTML format.
    :param html: a string containing the entire case page
    :return: a map of discovered data
    :raises ValueError if the string does not contain the expected html style and formatting
    '''
    data = {}
    if not html:
        raise(ValueError('A non-empty value is required'))
    try:
        doc = get_dom(html)
        for key in ['title']:
            val = get_val(doc, key)
            if val.endswith(' | Westlaw'):
                val = val[:-1 * len(' | Westlaw')]
            if not val:
                raise(ValueError("(Attribute is required %s)" % (key)))
            set_val(data, key, val)
        set_val(data, 'court', get_by_id(doc, 'span', 'courtline'))
        set_date_val(data, 'filedate', get_by_id(doc, 'span', 'filedate'))
        panel_divs = get_divs(doc, 'co_contentBlock co_briefItState co_panelBlock')
        if panel_divs:
            judges = parse_panel_block(panel_divs[0])
            set_val(data, 'panel', judges)
        decision = get_decision(get_divs(doc, 'co_contentBlock x_opinionBody'))
        if decision:
            print("*** co_contentBlock x_opinionBody %s" % (decision))
            set_val(data, 'decision', decision)
        if 'decision' not in data:
            decision = get_decision(get_divs(doc, 'co_contentBlock co_briefItState co_synopsis'))
            if decision:
                print("*** co_contentBlock co_briefItState co_synopsis %s" % (decision))
                set_val(data, 'decision', decision)
        if 'decision' not in data:
            print("warning: no decision")
    except Exception as e:
        raise(ValueError("Valid HTML input is required %s" % (e)))
    return data


def get_decision(in_divs):
    '''
    Construct a decision summary from relevant div blocks within a case document.
    :param in_divs: The divs containing the decision
    :return: A text summary of the decision (if any is found in the divs)
    '''
    decision = None
    if in_divs:
        if not isinstance(in_divs, list):
            in_divs = [in_divs]
        for in_div in in_divs:
            paragraph_divs = get_divs(in_div, 'co_paragraphText')
            for paragraph_div in paragraph_divs:
                if paragraph_div.text:
                    paragraph = paragraph_div.xpath('strong')
                    if paragraph:
                        decision_text = paragraph[0].text
                        if decision_text:
                            decision_parts = decision_text.split(';')
                            parsed_decision_parts = []
                            for part in decision_parts:
                                if part.startswith(' and '):
                                    part = part[4:]
                                if part.endswith('.'):
                                    part = part[:-1]
                                parsed_decision_parts.append(part.strip())
                            if len(parsed_decision_parts) > 0:
                                decision = ','.join(parsed_decision_parts)
                                print("*** using first case %s" % (decision))
                    if decision:
                        break
                    else:
                        if paragraph_div.text and \
                                (paragraph_div.text[0:8] == 'Affirmed' or paragraph_div.text[0:8] == 'Reversed'
                                 or paragraph_div.text[0:7] == 'Vacated' or paragraph_div.text[0:6] == 'Motion'
                                 or paragraph_div.text[0:7] == 'APPEAL '):
                            decision = paragraph_div.text
                            if decision.endswith('.'):
                                decision = decision[:-1]
                            print("*** using last case %s" % (decision))
    return decision


def parse_val(val):
    '''
    Clean up values from text
    :param val: The raw calue
    :return: A value for reporting/summary purposes
    '''
    new_val = val
    if val:
        try:
            new_val = val.strip()
            if val.endswith(' | Westlaw'):
                new_val = new_val[0:-10].strip()
            if new_val.endswith('.'):
                new_val = new_val[0:-1]
        except:
            pass
    return new_val


def get_divs(parent, divclass):
    '''
    Get divs of a given class beneath a given parent (recursively)
    :param parent: The parent div to search
    :param divclass: The class name to find
    :return: The matching divs
    '''
    return parent.xpath(".//div[@class='%s']" % (divclass))


def parse_panel_block(panel_element):
    '''
    Describe the panel of judges within a given DOM element
    :param panel_element: The DOM element containing the judge panel
    :return: A text description of the panel (if it exists)
    '''
    panel = []
    judge_other_text = panel_element.xpath('./div/text()')
    judge_last_names = panel_element.xpath('./div/a/text()')
    for last_name in judge_last_names:
        if last_name.isupper():
              panel.append(last_name)
    for text in judge_other_text:
        if ', and ' in text:
            panel.append(text.split(', and ')[1])
    return [x for x in panel if len(x.strip()) > 0]


# DOM utils

def get_dom(html):
    return fromstring(html)


def set_date_val(data, key, val):
    if val:
        set_val(data, key, parser.parse(val).strftime('%m/%d/%Y'))


def set_val(data, key, val):
    if val:
        data[key] = parse_val(val)


def get_val(parent, tag):
    val = None
    nodes = parent.xpath(".//%s" % (tag))
    for n in nodes:
        val = n.text
        break
    return val.strip()


def get_by_id(parent, tag, id):
    val = None
    nodes = parent.xpath("//%s[@id='%s']" % (tag, id))
    for n in nodes:
        if n != None and n.text != None:
            val = n.text
            break
    return val


def get_by_attr(parent, tag, attr, val):
    xpath = "%s[@%s='%s']" % (tag, attr, val)
    return get_by_xpath(parent, xpath)


def get_by_xpath(parent, xpath):
    n = parent.xpathall(xpath)
    return n.text if n != None and n.text != None else None