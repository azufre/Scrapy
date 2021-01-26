import requests 
import json

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')

driver = webdriver.Chrome(r"C:\\Users\\Bob\\Downloads\\chromedriver_win32\\chromedriver.exe", chrome_options=options)

urls = ["https://huubsh.com/l/gibson-slash-les-paul-standard-november--3569", "https://huubsh.com/l/tv-plus-2963"]

for index, url in enumerate(urls):
    
    obj = {}

    driver.get(url)

    title_tag = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "p"))
        )

    obj['title'] = title_tag.text
    obj['data'] = {}

    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "description"))
    )

    elem = element.find_elements_by_xpath('.//*')

    Notitle = 'Notitle'
    lastTitle = ''

    for e in elem:
        if(e.tag_name == 'h3'):

            obj['data'][e.text] = []
            lastTitle = e.text

        if(e.tag_name == 'p'):

            if lastTitle == '':
                obj['data'][Notitle] = []
                lastTitle = Notitle

            obj['data'][lastTitle].append(e.text)

    with open(f'Data{index}.json', 'x') as text:
        text.write(json.dumps(obj))
        text.close()

print("Scrappy completed!")