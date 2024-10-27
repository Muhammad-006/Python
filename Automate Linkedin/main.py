
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from selenium.common.exceptions import NoSuchElementException
import os, time

cover_letter = ("I am writing to express my interest in the Python Developer position at [Company Name]. "
                "With a solid foundation in Python, experience in building scalable applications, and a "
                "passion for problem-solving, I am confident in my ability to contribute effectively to "
                "your team. I have worked on diverse projects, including data processing, automation, and"
                " web development, and am eager to bring my expertise to [Company Name]. I look forward to"
                " the opportunity to further discuss how my skills align with your needs.)"
                "\nSincerely,"
                "\nMuhammad Bilal")

button_easy = "button[class='jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view']"
load_dotenv()

searching_job_for = input("What is your field of interest? ") or "Python Developer"
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

drive = webdriver.Chrome(options = chrome_option)
wait = WebDriverWait(drive, timeout = 60 * 5)

drive.maximize_window()

drive.get("https://www.linkedin.com/feed/")
wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(os.getenv("email", Keys.ENTER))
wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(os.getenv("password", Keys.ENTER))
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label = 'Sign in']"))).click()
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[title = 'Jobs']"))).click()
time.sleep(5)
drive.find_element(By.CSS_SELECTOR,"input[aria-label = 'Search by title, skill, or company']").send_keys(searching_job_for, Keys.ENTER)
time.sleep(2)
drive.find_element(By.CSS_SELECTOR,"button[aria-label = 'Easy Apply filter.']").click()
time.sleep(2)
all_jobs = drive.find_elements(By.CSS_SELECTOR, value = ".job-card-container--clickable")

for single_job in all_jobs:
    try:
        single_job.click()
        time.sleep(2)
        try:
            drive.find_element(By.CSS_SELECTOR, button_easy).click()
        except:
            continue
        time.sleep(2)
        phone = drive.find_element(By.XPATH, value = "/html/body/div[4]/div/div/div[2]/div/div[2]/form/div/div/div[4]/div/div/div[1]/div/input")
        for i in range(20):
            phone.send_keys(Keys.BACKSPACE)
        phone.send_keys("03399454475")
        time.sleep(1)
        drive.find_element(By.CSS_SELECTOR,"footer div button[aria-label='Continue to next step']").click()
        time.sleep(1)
        drive.find_element(By.CSS_SELECTOR,"footer div button[aria-label='Continue to next step']").click()

        all_columns = drive.find_elements(By.CSS_SELECTOR, "form div div div div div input")
        for each_column in all_columns:
            try:
                each_column.send_keys('0')
                time.sleep(1)
            except:
                pass

        select = drive.find_elements(By.CSS_SELECTOR,"option[value='Yes']")
        for single_opt in select:
            single_opt.click()
            time.sleep(1)

        drive.find_element(By.CSS_SELECTOR,"footer div button[aria-label='Review your application']").click()
        time.sleep(1)

        drive.find_element(By.CSS_SELECTOR, "footer div button[aria-label='Submit application']").click()
        time.sleep(1)
        print("Applied")
    except NoSuchElementException:
        print("No such Element")
        try:
            drive.find_element(By.CSS_SELECTOR, "div div div button svg[data-test-icon='close-medium']").click()
            time.sleep(1)
            drive.find_element(By.CSS_SELECTOR, "div div div button[data-control-name='discard_application_confirm_btn']").click()
            time.sleep(1)

        except:
            pass
        print("Unable to Applied")
        continue

drive.quit()
