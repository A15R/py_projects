#for test purposes i have already appended the condition that it's going to rain hence if you 
#correctly fill the crdentials you should get a SMS.

import requests
from twilio.rest import Client

##Make a twilio account to get all the details listed below
##link=https://www.twilio.com/en-us

API_KEY=""
account_sid=""
auth_token=""
Twilio_phn_no=""

MY_PHN_NO=""


##feed your current latitude and longitude link for website below-
##link=https://www.latlong.net/
MY_LAT= None
MY_LON= None

parameters={
    "lat":MY_LAT,
    "lon":MY_LON,
    "appid":API_KEY,
    "cnt":4
}
response=requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
data=response.json()


x=0
weather_codes=[600]
for code in range(4):
    add_code=data["list"][x]["weather"][0]["id"]
    weather_codes.append(add_code)
    x+=1
Is_raining=False
print(weather_codes)
for item in weather_codes:
    if item<700:
        Is_raining=True
    else:
        pass
if Is_raining==True:
    client=Client(account_sid,auth_token)
    message=client.messages.create(
        body="its gonna rain today carry an umbrella",
        from_=Twilio_phn_no,
        to=MY_PHN_NO)
    print(message.sid)

else:
    pass

