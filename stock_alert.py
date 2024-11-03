import requests
import datetime
from twilio.rest import Client

API_KEY_TWILIO=""
account_sid=""
auth_token=""

API_KEY_STOCKS=""
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
link="https://www.alphavantage.co/"


API_KEY_NEWS=""
NEWS_URL="https://newsapi.org/v2/top-headlines"
object="tesla"

parameters={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":API_KEY_STOCKS

}


news_parameters={
    "q":object,
    "apiKey":API_KEY_NEWS

}

news_response=requests.get(url=NEWS_URL,params=news_parameters)
news_response.raise_for_status()
news_data=news_response.json()





now = datetime.date.today()
if now.weekday()==5 or now.weekday()==6:
    today = now - datetime.timedelta(days=2)
    yesterday = now - datetime.timedelta(days=3)
else:
    today = now - datetime.timedelta(days=1)
    yesterday = now - datetime.timedelta(days=2)


response=(requests.get(url="https://www.alphavantage.co/query",params=parameters))
response.raise_for_status()
data=response.json()


#using data
today_close=float(data["Time Series (Daily)"][str(today)]["4. close"])
yesterday_close=float(data["Time Series (Daily)"][str(yesterday)]["4. close"])

is_profit=False
is_loss=False
profit=(((today_close)-(yesterday_close)) / today_close)*100
def change():
    global today_close
    global yesterday_close
    global is_profit
    global profit
    global is_loss

    if int(profit)>0:
        is_profit=True

    elif int(profit)<=0:
        is_loss=True
change()

#sending msg
while is_profit:
    client=Client(account_sid,auth_token)
    message=client.messages.create(
        body=f"TSLA 🔺{int(profit)}"
             f"Headline:{news_data["articles"][1]["title"]}"
             f"Brief:{news_data["articles"][1]["description"]}",
        from_="+12408443400",
        to="+919937542280",

    )

    print(message.status)
    is_profit=False

while is_loss:
    client=Client(account_sid,auth_token)
    message=client.messages.create(
        body=f"TSLA 🔺{int(profit)}"
             f"Headline:{news_data["articles"][1]["title"]}"
             f"Brief:{news_data["articles"][1]["description"]}",
        from_="+12408443400",
        to="+919937542280",

    )
    print(message.status)
    is_loss=False


