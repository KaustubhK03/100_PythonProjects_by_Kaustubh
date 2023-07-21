from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import time
import os

load_dotenv()

EMAIL = os.getenv("EMAIL")
PHONE_NO = os.getenv("PHONE_NO")
PASSWORD = os.getenv("PASSWORD")


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.Up = 0
        self.Down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)
        # close popup 1
        close_popup = self.driver.find_element(By.XPATH, '//*[@id="onetrust-close-btn-container"]/button')
        close_popup.click()
        # Pressing the go button
        go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
                                                       'div[1]/a')
        go_button.click()
        time.sleep(45)
        # closing popup 2
        close_pop_up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]'
                                                          '/div[3]/div/div[8]/div/div/div[2]/a')
        close_pop_up.click()
        time.sleep(5)
        # getting the respective speeds
        down_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
                                                        'div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div'
                                                        '/div[2]/span')
        self.Down = down_speed.text
        up_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/'
                                                      'div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]'
                                                      '/div/div[2]/span')
        self.Up = up_speed.text
        return self.Down, self.Up

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(7)
        email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/'
                                                   'div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(PHONE_NO)
        email.send_keys(Keys.ENTER)
        time.sleep(5)
        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div'
                                                      '/div/div[2]/div[2]/div[1]/div/div/div[2]/div/label/div/div[2]'
                                                      '/div[1]/input')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(50)
        # Enter email
        tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div'
                                                   '/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div'
                                                   '/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div'
                                                   '/div[2]/div/div/div/div')
        tweet.send_keys("This is a text to test the selenium software")
        time.sleep(5)
        self.driver.quit()
