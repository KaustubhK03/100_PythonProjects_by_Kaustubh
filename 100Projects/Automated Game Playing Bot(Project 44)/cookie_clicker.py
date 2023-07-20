from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://orteil.dashnet.org/experiments/cookie/")
driver.maximize_window()

timeout = time.time() + 5

five_min_timeout = time.time() + 60 * 5

while True:
    cookie = driver.find_element(By.ID, "cookie")
    cookie.click()
    if time.time() > timeout:
        money = driver.find_element(By.ID, "money")
        cookies_count = int(money.text.replace(",", ""))
        right_panel = [upgrade.text for upgrade in driver.find_elements(By.CSS_SELECTOR, "#rightPanel div div") if
                       upgrade.get_attribute("class") != "grayed"]
        if right_panel[-1] == "":
            right_panel.remove("")
        to_upgrade = [int(price.split("\n")[0].split(" ")[-1].replace(",", "")) for price in right_panel]
        max_upgrade = max(to_upgrade)
        max_upgrade_index = to_upgrade.index(max_upgrade)
        buttons = driver.find_elements(By.CSS_SELECTOR, "#store div")
        buttons.pop()
        buttons[max_upgrade_index].click()
        timeout = time.time() + 5
    if time.time() > five_min_timeout:
        cps = driver.find_element(By.ID, "cps")
        print(cps.text)
        break

driver.quit()
