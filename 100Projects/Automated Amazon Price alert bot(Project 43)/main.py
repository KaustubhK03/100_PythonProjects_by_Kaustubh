import requests
import os
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv

load_dotenv()

PRODUCT_URL = os.getenv("PRODUCT_URL")
USER_AGENT = os.getenv("USER_AGENT")
ACCEPT_LANGUAGE = os.getenv("ACCEPT_LANGUAGE")
EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")
TARGET_PRICE = 9000

headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE,
}
response = requests.get(url=PRODUCT_URL, headers=headers)
html_code = response.text

# Making Soup
soup = BeautifulSoup(html_code, "lxml")
product_html = soup.prettify()

price_lst = soup.find(name="span", class_="a-price-whole").get_text().split(".")[0].split(",")
current_price = float(price_lst[0] + price_lst[1])

if TARGET_PRICE > current_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=APP_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Midi Controller price alert\n\nThe product is now {TARGET_PRICE} "
                f"below your target price. BUY NOW!"
        )
