from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import time,os

load_dotenv()
PROMISED_DOWN = 10
PROMISED_UP = 10
PATH = ("/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/"
        "div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
POST_PATH = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button"
class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_experimental_option("detach", True)

        self.drive = webdriver.Chrome(chrome_option)
        self.drive.maximize_window()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.drive.get("https://www.speedtest.net")
        time.sleep(2)
        self.drive.find_element(By.CSS_SELECTOR, value = "div div div div div div div span.start-text").click()
        time.sleep(80)
        self.down = self.drive.find_element(By.CSS_SELECTOR, value = "span.download-speed").get_attribute("textContent")
        self.up = self.drive.find_element(By.CSS_SELECTOR, value = "span.upload-speed").get_attribute("textContent")
        return self.down, self.up

    def tweet_at_provider(self,tweet):
        self.drive.get("https://x.com/")
        time.sleep(5)
        self.drive.find_element(By.XPATH, value = "/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[4]/a/div").click()
        time.sleep(10)
        email = self.drive.find_element(By.CSS_SELECTOR, value = "input[autocapitalize='sentences'][autocorrect='on'][autocomplete='username']")
        email.send_keys(os.getenv("email"))
        time.sleep(2)
        email.send_keys(Keys.ENTER)
        time.sleep(2)
        password = self.drive.find_element(By.CSS_SELECTOR, value = "input[autocapitalize='sentences'][autocorrect='on'][autocomplete='current-password'][name='password']")
        password.send_keys(os.getenv("password"),Keys.ENTER)
        time.sleep(10)
        self.drive.find_element(By.XPATH, value = PATH).send_keys(tweet)
        time.sleep(2)
        self.drive.find_element(By.XPATH, value = POST_PATH).click()

complain = InternetSpeedTwitterBot()
getting_down, getting_up = complain.get_internet_speed()
message = f"Hi\nInternet Provider My internet speed is very low.\nIt had to be {PROMISED_DOWN}down/{PROMISED_UP}up but instead it is {getting_down}down/{getting_up}up... #itworked"
complain.tweet_at_provider(tweet = message)