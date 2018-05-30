from requests import get
from bs4 import BeautifulSoup
import re

#getting the company name from the code or CIK
def company_name(ticker):
    url='http://www.sec.gov/cgi-bin/browse-edgar?CIK={}&Find=Search&owner=exclude&action=getcompany'
    web=get(url.format(ticker)).content
    soup=BeautifulSoup(web, 'lxml')
    if soup.find('span', attrs='companyName'):
        a=soup.find('span', attrs='companyName').get_text()
    else:
        a=soup.find('span', attrs='companyname').get_text()
    parse=re.compile(r'[A-Z,a-z]+')
    print(a)
    name=parse.findall(a)
    co_name=[]
    #building the company name
    c=name.index('CIK')
    for i in range(c):
        co_name.append(name[i])
    final=' '.join(co_name)
    return final

ticker=input('input the company ticker: ')

print(company_name(ticker))
