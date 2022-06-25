from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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

houseList = []
c = 1
for i in range(3, 63):
    try:
        print(i)
        url = "https://nha.chotot.com/mua-ban-nha-dat?page=" + str(i+1)
        driver.get(url)
        # houseTags = driver.find_elements(by=By.CSS_SELECTOR, value=".AdItem_adItem__2O28x")
        # houseUrls = [el.get_attribute("href") for el in houseTags]
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        houseTags = soup.find_all("a", {"class": "AdItem_adItem__2O28x"})
        houseUrls = ['https://nha.chotot.com' + str(el['href']) for el in houseTags]
        # for subUrl in houseUrls:
        for subUrl in houseUrls:
            try:
                print(c)
                print(subUrl)
                driver.get(str(subUrl))
                delay = 5  # seconds

                myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR,
                     '#__next > div > div.container > div.ct-detail.adview > div > div.col-md-8 > div.AdImage_adImageWrapper__15vl2 > div.slick-slider.slick-initialized > div > div > div:nth-child(3) > div > div > div > div > div > img')))

                button = driver.find_element(by=By.CSS_SELECTOR, value="#__next > div > div.container > div.ct-detail.adview > div > div.col-md-4.no-padding.dtView > div > div:nth-child(2) > div.LeadButton_wrapperLeadButtonDesktop__13fEA > div.LeadButton_showPhoneButton__1KVb- > div")
                button.click()
                html = driver.page_source
                soup = BeautifulSoup(html, "html.parser")
                house = {}
                house['Original Link'] = subUrl
                house['Tên người bán'] = soup.find("div", {"class": "SellerProfile_nameDiv__dd88e"}).findChild("b", recursive=False).getText()
                house['Số điện thoại'] = soup.find("div", {"class": "sc-EHOje lnlbMI"}).findChild("span", recursive=False).getText()
                house['Tiêu đề'] = soup.find("h1", {"class": "AdDecription_adTitle__2I0VE"}).getText()
                house['Địa chỉ'] = soup.find("span", {"class":"fz13"}).getText()
                house['Mô tả'] = soup.find("p", {"class": "AdDecription_adBody__1c8SG"}).getText()
                house['Giá'] = soup.find("span", {"class": "AdDecription_price__O6z15"}).findChild("span", recursive=False).find(text=True, recursive=False)
                tags = soup.find_all("div", {"class": "media-body media-middle"})
                for tag in tags:
                    spans = tag.findChildren("span" , recursive=True)
                    house[spans[1].getText()] = spans[2].getText()

                img = soup.find("div", {
                    "class": "slick-slide slick-active slick-current"}).findChild("img", recursive=True)['src']

                house['Ảnh'] = img
                houseList.append(house)
                c += 1
                print(house)
            except Exception as e: print(e)
    except Exception as e:
        print(e)
        continue


print('so luong data: ' + str(len(houseList)))
# s = set()
# for i in houseList:
#     s.update(i)
# header = list(s)
#
# with open("Cho-tot.csv", 'w', encoding="utf-8") as f:
#     writer = csv.writer(f)
#     writer.writerow(header)
#     for d in houseList:
#         writer.writerow([d.get(i, "NULL") for i in header])
with open('Cho-tot2.json', 'w') as fout:
    json.dump(houseList, fout)