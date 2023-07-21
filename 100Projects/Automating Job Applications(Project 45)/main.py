import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv

load_dotenv()

driver = webdriver.Chrome()

driver.get("https://www.linkedin.com/jobs/")

time.sleep(3)


def linked_in_login():
    # putting in email
    email = driver.find_element(By.ID, "session_key")
    email.send_keys(os.getenv("email"))

    # putting the password
    password = driver.find_element(By.ID, "session_password")
    password.send_keys(os.getenv("password"))

    # Clicking on login
    login = driver.find_element(By.LINK_TEXT, "Sign in")
    login.click()
    email2 = driver.find_element(By.ID, "username")
    email2.send_keys(os.getenv("email"))

    password_2 = driver.find_element(By.ID, "password")
    password_2.send_keys(os.getenv("password"))

    password_2.send_keys(Keys.ENTER)

# TODO: Sometimes LinkedIn will throw the captcha to confirm you are a human which yo will have to
# complete manually


def save_and_follow_company():
    time.sleep(20)
    first_job_on_page = driver.find_element(By.LINK_TEXT, "Generative AI Intern (Non Tech)")
    first_job_on_page.click()
    # saving the company
    time.sleep(20)
    save = driver.find_element(By.LINK_TEXT, "Save")
    save.click()

    follow = driver.find_element(By.LINK_TEXT, "Follow")
    follow.click()


linked_in_login()
time.sleep(5)
save_and_follow_company()
time.sleep(7)


driver.quit()