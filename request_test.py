import requests
from bs4 import BeautifulSoup
import csv

r = requests.get('http://seaofindia.com/')
r.encoding = 'utf-8'
req = r.text

# with open('req.html', 'r', encoding='utf-8') as f:
#     req = f.read()

soup = BeautifulSoup(req, 'lxml')

dat = soup.find(class_='quotes-title').get_text().strip()
trs = soup.find_all('tr')
p_list = [[dat], ['Price', 'Commodities']]

for tr in trs:
    ui = []
    for td in tr:
        string = str(td.string).strip()
        ui.append(string)
    p_list.append(ui)

for price in p_list:
    while '' in price:
        price.remove('')

with open('india_%s.csv' % dat, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(p_list)



