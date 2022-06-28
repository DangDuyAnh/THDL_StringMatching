from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json
import csv
import re
import pandas as pd
list = []
for page in range(1,120,1):
 try:

   page_url = "https://mogi.vn/ha-noi/mua-nha-dat?cp=" + str(page)
   driver = webdriver.Chrome(ChromeDriverManager().install())
   driver.get(page_url)
   html = driver.page_source
   soup = BeautifulSoup(html,"html.parser")
   houseTags = soup.find_all("a", {"class": "link-overlay"})
   houseUrls = [str(el['href']) for el in houseTags]
   for sub in houseUrls:
    try:
      print(sub)
      driver.get(str(sub))
      delay = 5

      html = driver.page_source
      soup = BeautifulSoup(html, "html.parser")
      house = {}
      house['Original Link'] = sub
      house['Tên người bán'] = soup.find("div", {"class": "agent-name"}).findChild("a",recursive = False).getText()
      print(house['Tên người bán'])
      house['Tiêu đề'] = soup.find("div", {"class": "title"}).findChild("h1", recursive=False).getText()
      print(house['Tiêu đề'])
      house['Địa chỉ'] = soup.find("div", {"class": "address"}).getText()
      print(house['Địa chỉ'])
      t = soup.find("div",{"class" : "info-content-body"}).getText()
      s = re.sub('<br\s*?>', ' ', t)
      house['Mô tả'] = s
      #h = t.text.strip().split('\n\n')
      #print(h)
      #print(house['Mô tả'])
      house['Giá'] = soup.find("div", {"class": "price"}).getText()
      divs = soup.find("div",{"class": "info-attrs clearfix"})
      tags = divs.find_all("div",{"class":"info-attr clearfix"},recursive = False)
      for tag in tags:
        spans = tag.findChildren("span", recursive=True)
        #print(spans[0].getText())
        #print(spans[1].getText())
        house[spans[0].getText()] = spans[1].getText()
      img = soup.find("div", {"class": "media-item"}).findChild("img", recursive=True)['src']

      house['Ảnh'] = img
      list.append(house)

      print(house)

      print(house)
    except Exception as e: print(e)
 except Exception as e:
   print(e)
   continue

print('so luong data: ' + str(len(list)))

df = pd.DataFrame(list)
df.to_csv('mogi.csv')
driver.close()



