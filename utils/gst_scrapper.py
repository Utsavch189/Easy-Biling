import requests
from bs4 import BeautifulSoup
import re

class GstScrapper:

    def __init__(self,url:str,keyword:str) -> None:
        self.url=url
        self.keyword=fr'\b{keyword}\b'

    def get_rates(self)->dict:
        try:
            with requests.Session() as session:
                req=session.get(self.url)
                c=req.content
                s=BeautifulSoup(c,'html.parser')
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

                        match = re.search(self.keyword, description)
                        if match:
                            return {
                                "cgst":datas[3].text,
                                "sgst":datas[4].text,
                                "igst":datas[5].text
                            }
        except Exception as e:
            print(e)

if __name__=="__main__":
    g=GstScrapper("https://cbic-gst.gov.in/gst-goods-services-rates.html","outdoor catering")
    print(g.get_rates())

