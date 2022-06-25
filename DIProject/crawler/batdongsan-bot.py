from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
import json

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--single-process')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--incognito")
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("disable-infobars")
ser = Service("./chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options ,service=ser)

mainUrl = "https://batdongsan.com.vn/nha-dat-ban"

houseList = []
c = 1
for i in range(1):
    url = "https://batdongsan.com.vn/nha-dat-ban/p" + str(i+1)
    driver.get(url)
    houseTags = driver.find_elements(by=By.CSS_SELECTOR, value=".js__product-link-for-product-id")
    houseUrls = [el.get_attribute("href") for el in houseTags]
    # for subUrl in houseUrls:
    for subUrl in houseUrls:
        print(c)
        print(subUrl)
        driver.get(subUrl)
        delay = 5  # seconds
        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.re__media-thumb-item.js__media-thumbs-item.slick-slide.slick-active')))
        except Exception as e:
            print(e)
            continue
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        house = {}
        try:
            house['Original Link'] = subUrl
            house['Tên người bán'] = soup.select_one('body > div.re__main > div > div.re__main-sidebar > div.re__sidebar-box.re__contact-box.js__contact-box > div.re__contact-name.js_contact-name')['title']
            house['Số điện thoại'] = soup.select_one('body > div.re__main > div > div.re__main-sidebar > div.re__sidebar-box.re__contact-box.js__contact-box > div.re__btn.re__btn-cyan-solid--md.phone > span')['mobile']
            house['Tiêu đề'] = soup.select_one('#product-detail-web > h1').getText()
            house['Địa chỉ'] = soup.find(class_ = "re__pr-short-description").getText()
            moTa = soup.find(class_="re__section-body re__detail-content js__section-body js__pr-description js__tracking").getText()
            s = re.sub('<br\s*?>', ' ', moTa)
            house['Mô tả'] = s
            elements = soup.find_all(class_ = "re__pr-specs-content-item-title")
            elements2 = soup.find_all(class_ = "re__pr-specs-content-item-value")
            for i in range(len(elements)):
                a = elements2[i].getText()
                b = str(a)
                house[str(elements[i].getText())] = b
            house['Ngày đăng'] = soup.select_one('#product-detail-web > div.re__pr-short-info.re__pr-config.js__pr-config > div:nth-child(1) > span.value').getText()
            house['Ngày hết hạn'] = soup.select_one('#product-detail-web > div.re__pr-short-info.re__pr-config.js__pr-config > div:nth-child(1) > span.value').getText()
            house['Mã tin'] = soup.select_one('#product-detail-web > div.re__pr-short-info.re__pr-config.js__pr-config > div:nth-child(4) > span.value').getText()
            elements = soup.find_all("div", {"class":"re__media-thumb-item js__media-thumbs-item slick-slide slick-active"})
            ImgArr = []
            for el in elements:
                ImgArr.append(el.findChild("img", recursive=False)['data-src'])
            rs_s = ''
            for i in range(len(ImgArr)- 1):
                rs_s = rs_s + ImgArr[i] + ', '
            house['Ảnh'] = rs_s
            houseList.append(house)
            c += 1
            print(house)
        except Exception as e:
            print(e)
            continue
print('so luong data: ' + str(len(houseList)))
s = set()
for i in houseList:
    s.update(i)
header = list(s)

with open("Bat-dong-san2.csv", 'w', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for d in houseList:
        writer.writerow([d.get(i, "NULL") for i in header])

# with open('outputfile.json', 'w') as fout:
#     json.dump(houseList, fout)