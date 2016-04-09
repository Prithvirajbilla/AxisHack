import requests
import re
from bs4 import BeautifulSoup

ci_url = 'http://www.mca.gov.in/mcafoportal/checkCompanyName.do'
pincode_url = 'http://api.geonames.org/postalCodeLookupJSON?postalcode={0}&country=IN&username=demo'

ci_payload = 'counter=1&name1={0}&name2=&name3=&name4=&name5=&name6=&activityType1=&activityType2='
ci_headers = {'Content-Type': 'application/x-www-form-urlencoded',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Origin': 'http://www.mca.gov.in',
'Referer': 'http://www.mca.gov.in/mcafoportal/checkCompanyName.do',
'Upgrade-Insecure-Requests': '1','Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'en-US,en;q=0.8',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'}

def get_company_information(query):
    r = requests.post(ci_url, data=ci_payload.format(query), headers=ci_headers)
    soup = BeautifulSoup(r.text,"html.parser")
    result = soup.find_all('table',id="companyList")
    names = []
    if result == []:
        return names
    for row in result[0].find_all('tr',class_="table-row"):
        cells = row.find_all('td')
        name = cells[1].find(text=True).strip()
        names.append(name)
        print cells[0].find(text=True)
        print cells[1].find(text=True)
        print cells[2].find(text=True)
        print cells[3].find(text=True)
    return names

def get_pincode_details(query):
    r = requests.get(pincode_url.format(query))
    return r.text

def main():
    names = get_company_information("Global Desi")
    # domain = whois('adoro.in')
    # print domain.name,domain.registrar,domain.creation_date,domain.expiration_date

if __name__ == '__main__':
    main()
