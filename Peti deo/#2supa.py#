from bs4 import BeautifulSoup as bs
import requests as rq
from fake_useragent import UserAgent 

fajl1=open("fajl.txt", mode="wt")
fajl2=open("fajlSpan.txt", mode="a")
ua = UserAgent()
header={
        'User-Agent':str(ua.chrome)
        }
print(header)


def ceneKupujemProdajem(url):
    zahtev= rq.get(url, headers=header)
    corba = bs(zahtev.text, 'html.parser')
    fajl1.write(str(corba))
    cena = corba.find_all('span', {'class' : 'priceClassified'})
    print("#############")
    klasa = 'priceClassified'
    o=1
    for i in cena:
        print(i.text)
        fajl2.write(str(i))

   

ceneKupujemProdajem('https://www.polovniautomobili.com/auto-oglasi/22313727/audi-a4?attp=p8_pv0_pc1_pl9_plv0')
    
