import requests
from bs4 import BeautifulSoup
import re

url="https://cbic-gst.gov.in/gst-goods-services-rates.html"
r=requests.get(url)
c=r.content
s=BeautifulSoup(c,'html.parser')

keyword=r'\boutdoor catering\b'

table=s.find(id='service_table')
rows=table.find_all('tr')

for row in rows:
    datas=row.find_all('td')
    if not datas:
        continue
    else:
        elm=datas[2].find('span')
        if elm:
            description=elm.text
        else:
            description=datas[2].text
        
        match = re.search(keyword, description)
        if match:
            cgst=datas[3].text
            sgst=datas[4].text
            igst=datas[5].text
            break
        
print(cgst," ",sgst," ",igst)