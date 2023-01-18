from bs4 import BeautifulSoup
import requests
import csv

url='http://quotes.toscrape.com'

html=requests.get(url)
bs=BeautifulSoup(html.text,'html.parser')

try:
    csv_file=open('quote_list.csv','w')
    fieldnames=['quote','author','tags']
    dictwriter=csv.DictWriter(csv_file,fieldnames=fieldnames)

    dictwriter.writeheader()

    while True:
        for quote in bs.findAll('div',{'class':'quote'}):
            text=quote.find('span',{'class':'text'}).text
            author=quote.find('small',{'class':'author'}).text
            tags=[]
            for tag in quote.findAll('a',{'class':'tag'}):
                tags.append(tag.text)
            dictwriter.writerow({'quote':text,'author':author,'tags':tags})
        
        next=bs.find('li',{'class':'next'})
        if not next: 
            break

        html=requests.get(url+next.a.attrs['href'])
        bs=BeautifulSoup(html.text,'html.parser')
except:
    print('Unknown Error!!!')
finally:
    csv_file.close()
