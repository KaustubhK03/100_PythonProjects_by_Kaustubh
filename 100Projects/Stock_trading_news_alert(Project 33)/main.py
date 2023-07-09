import requests
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

ALPHAVANTAGE_API_KEY = "Your alpha_advantage api key goes here"
ALPHAVANTAGE_ENDPOINT = "https://www.alphavantage.co/query"

NEWS_API_KEY = "your newsapi key goes here"
NEWSAPI_ENDPOINT = "https://newsapi.org/v2/everything"

account_sid = "your account sid goes here"

email = "your mail goes here"
password = "your app password goes here"

alpha_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_API_KEY,
}
newsapi_parameters = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME,
    "searchIn": "title",
    "from": "2023-07-04",
    "language": "en",
    "sortBy": "popularity",

}

alpha_response = requests.get(url=ALPHAVANTAGE_ENDPOINT, params=alpha_parameters)
alpha_response.raise_for_status()
alpha_data = alpha_response.json()["Time Series (Daily)"]

alpha_lst = [value for (key, value) in alpha_data.items()]

yesterday_s_adjusted_close = float(alpha_lst[0]["4. close"])
day_before_yesterday_adjusted_close = float(alpha_lst[1]["4. close"])

percent = abs(((yesterday_s_adjusted_close - day_before_yesterday_adjusted_close) / yesterday_s_adjusted_close) * 100)

if percent > 5:
    newsapi_response = requests.get(url=NEWSAPI_ENDPOINT, params=newsapi_parameters)
    newsapi_response.raise_for_status()
    articles = newsapi_response.json()["articles"]
    first_3_articles = articles[0:3]

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        for i in range(3):
            message = f"Subject:{first_3_articles[i]['title'].encode('utf-8')}\n\n{first_3_articles[i]['description'].encode('utf-8')}\nurl={first_3_articles[i]['url']}"
            connection.sendmail(
                from_addr=email,
                to_addrs=email,
                msg=message
            )
