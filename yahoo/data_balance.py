import re
import urllib.request
from lxml.html import fromstring, parse
from yahoo.parse_number import parse_content

def get_balance_data(ticker):
    url = "https://finance.yahoo.com/quote/{0}/balance-sheet?p={1}".format(ticker, ticker)
    content = urllib.request.urlopen(url).read()
    doc = fromstring(content)
    
    data = dict()
    
    row_num = len(doc.xpath('//div[contains(@id, "Financials-Proxy")]/section/div[3]/table/tbody/tr'))
    
    for i in range(1, row_num + 1):
        label = ""
        col_num = len(doc.xpath('//div[contains(@id, "Financials-Proxy")]/section/div[3]/table/tbody/tr[{}]/td'.format(i)))
        
        for j in range(1, col_num + 1):
            text = doc.xpath('//div[contains(@id, "Financials-Proxy")]/section/div[3]/table/tbody/tr[{}]/td[{}]'.format(i, j))[0].text_content().strip()
            if re.search('[a-zA-Z]{3,}', text): 
                label = text
            elif re.search('[0-9\-\,\.\/]+', text):
                row = data.get(label, [])
                row.append(parse_content(text))
                data[label] = row

    return data


# print(get_balance_data("NVDA"))