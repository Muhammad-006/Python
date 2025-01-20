import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
response = response.text

soup = BeautifulSoup(response, "html.parser")
a_tags = soup.select(selector="ul[class='List-c11n-8-84-3-photo-cards'] a")
address_tag = soup.select(selector="ul[class='List-c11n-8-84-3-photo-cards'] address")
price_tag = soup.select(selector="ul[class='List-c11n-8-84-3-photo-cards'] span")

links = [link.get('href') for link in a_tags]
addresses = []
for link in address_tag:
    new_link = (link.text).split("\n")
    address = new_link[1].strip()
    addresses.append(address)
prices = [(link.text)[0:6] for link in price_tag if (link.text)[0] == "$"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
drive = webdriver.Chrome(chrome_options)

wait = WebDriverWait(drive, timeout = 60)
drive.get("https://docs.google.com/forms/d/e/1FAIpQLSen7F6gZb9nXJtsIaL5SjMuOfXPCSQr4p2JZM7jIC6FYAYjEQ/viewform?vc=0&c=0&w=1&flr=0")

while (links != []) and (addresses != []) and (prices != []):
    link = links[0]
    address = addresses[0]
    price = prices[0]
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='button']")))
    item= drive.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    item.send_keys(address)
    drive.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(price)
    drive.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(link)

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='button']"))).click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='c2gzEf'] a"))).click()

    links.pop(0)
    addresses.pop(0)
    prices.pop(0)

drive.quit()



