from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import csv
element_list = []
for page in range(1,400,1):
 page_url = "https://mogi.vn/ha-noi/mua-nha-dat?cp=" + str(page)
 driver = webdriver.Chrome(ChromeDriverManager().install())
 driver.get(page_url)
 for id in range(1,15,1):
  title = driver.find_elements(By.CSS_SELECTOR,value="#property > div.property-listing > ul > li:nth-child("+str(id)+") > div.prop-info > a")
  vitri = driver.find_elements(By.CSS_SELECTOR,value="#property > div.property-listing > ul > li:nth-child("+str(id)+") > div.prop-info > div.prop-addr.ng-binding")
  price = driver.find_elements(By.CSS_SELECTOR,value="#property > div.property-listing > ul > li:nth-child("+str(id)+") > div.prop-info > div.price")
  dientich = driver.find_elements(By.CSS_SELECTOR,value= "#property > div.property-listing > ul > li:nth-child("+str(id)+") > div.prop-info > ul > li:nth-child(1)")
  phongngu = driver.find_elements(By.CSS_SELECTOR, value="#property > div.property-listing > ul > li:nth-child("+str(id)+") > div.prop-info > ul > li:nth-child(2)")
  nhavs = driver.find_elements(By.CSS_SELECTOR, value="#property > div.property-listing > ul > li:nth-child("+str(id)+") > div.prop-info > ul > li:nth-child(3)")
  for i in range(len(vitri)):
   element_list.append([title[i].text,vitri[i].text,price[i].text,dientich[i].text, phongngu[i].text, nhavs[i].text])


df = pd.DataFrame(element_list)
df.to_csv('table.csv')
driver.close()
