from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get(url="https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors")
time.sleep(2)

total_ranks = []
total_degrees = []
total_early_career_pay_lst = []
total_mid_career_pay_lst = []

constant = '//*[@id="__next"]/div/div[1]/article/div[2]/table/tbody'
constant2 = '//*[@id="__next"]/div/div[1]/article/div[3]/a[7]'

for _ in range(33):
    if _ == 3:
        constant2 = '//*[@id="__next"]/div/div[1]/article/div[3]/a[9]'
    if _ == 31:
        constant2 = '//*[@id="__next"]/div/div[1]/article/div[3]/a[5]'
    table = driver.find_element(By.XPATH, value=constant)
    ranks = [table.text.split("\n")[i] for i in range(70) if i % 3 == 0]
    total_ranks.extend(ranks)
    degrees = [table.text.split("\n")[i] for i in range(1, 76, 3)]
    total_degrees.extend(degrees)
    early_career_pay_lst = [table.text.split("\n")[i].split(" ")[1] for i in range(2, 76, 3)]
    total_early_career_pay_lst.extend(early_career_pay_lst)
    mid_career_pay_lst = [table.text.split("\n")[i].split(" ")[2] for i in range(2, 76, 3)]
    total_mid_career_pay_lst.extend(mid_career_pay_lst)
    next_page = driver.find_element(By.XPATH, value=constant2)
    next_page.click()
print(total_ranks)
print(len(total_ranks))

print(total_degrees)
print(len(total_degrees))

print(total_early_career_pay_lst)
print(len(total_early_career_pay_lst))

print(total_mid_career_pay_lst)
print(len(total_mid_career_pay_lst))

driver.quit()
