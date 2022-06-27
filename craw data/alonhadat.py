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
for page in range(1,150,1):
 try:

   page_url = "https://alonhadat.com.vn/can-ban-nha-ha-noi-t1/trang-" + str(page)+str(".htm")
   driver = webdriver.Chrome(ChromeDriverManager().install())
   driver.get(page_url)
   html = driver.page_source
   soup = BeautifulSoup(html,"html.parser")
   houseTags = driver.find_elements(By.CSS_SELECTOR, value=".vip")
   houseUrls = [el.get_attribute("href") for el in houseTags]
   for sub in houseUrls:
    try:
      print(sub)
      driver.get(str(sub))
      delay = 5

      html = driver.page_source
      soup = BeautifulSoup(html, "html.parser")
      house = {}
      house['Original Link'] = sub
      na = soup.find("div",{"class":"contact"})
      nahs = na.find("div", {"class":"contact-info"})
      house['Tên người bán'] = nahs.find("div",{"class":"content"}).findChild("div", {"class":"name"}, recursive=False).getText()
      print(house['Tên người bán'])
      ha = soup.find("div", {"class": "property"})
      ham = soup.find("div", {"class":"title"})

      house['Tiêu đề'] = ham.find("h1", recursive=False).getText()
      print(house['Tiêu đề'])

      has = ha.find("div",{"class":"address"})
      house['Địa chỉ'] = has.find("span", {"class":"value"}).getText()
      print(house['Địa chỉ'])
      house['Mô tả'] = ha.find("div",{"class" : "detail text-content"}).getText()
      #h = t.text.strip().split('\n\n')
      #print(h)
      #print(house['Mô tả'])
      nahs = ha.find("div", {"class": "moreinfor"})
      cu = nahs.find("span",{"class":"price"})

      house['Gia'] = cu.find("span",{"class":"value"}).getText()
      print(house['Gia'])
      nahs1 = ha.find("div",{"class":"moreinfor1"})
      ci = nahs1.find("div",{"class":"infor"})
      ce = ci.find("table").find("tbody")
      rows = ce.find_all("tr")
      for row in rows:
        cells = row.find_all("td")
        house[cells[0].getText()] = cells[1].getText()
        house[cells[2].getText()] = cells[3].getText()
      #divs = soup.find("div",{"class": "info-attrs clearfix"})
      #tags = divs.find_all("div",{"class":"info-attr clearfix"},recursive = False)
      #for tag in tags:
        #spans = tag.findChildren("span", recursive=True)
        #print(spans[0].getText())
        #print(spans[1].getText())
        #house[spans[0].getText()] = spans[1].getText()
      hoh = ha.find("div", {"class": "images"})
      img= hoh.find("div",{"class":"imageview"}).findChild("img")['src']
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
df.to_csv('alonhadat.csv')
driver.close()



