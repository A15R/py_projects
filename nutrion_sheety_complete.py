import requests
import datetime
import json

nutri_api_id=""
nutri_api_key=""
sheety_api_url=""
#get your own nutrionix api id  and key on the website link-https://developer.nutritionix.com/
#documnetation of website- link:https://docx.syndigo.com/developers/docs/natural-language-for-exercise
#sheety api for google sheets modification=https://dashboard.sheety.co/login
#make your own google sheet and link it to sheety api to modify remember to rwad through the all important documentation


headers={
    'x-app-id':nutri_api_id ,
    'x-app-key':nutri_api_key
}

params={
    "query":input("Hey what exercise did you do?")
}
website_url="https://trackapi.nutritionix.com/v2/natural/exercise"

data=requests.post(url=website_url,json=params,headers=headers)
a=data.json()

for nums in range(len(a["exercises"])):
    

    now=datetime.datetime.now()
    
    sheety_api=sheety_api_url
    body={
        "sheet1":{
            "date":str(now.date()),
            "time":f"{str(now.time()).split(".")[0]}",
            "exercise":a["exercises"][nums]["name"].title(),
            "duration":f"{a["exercises"][nums]["duration_min"]} mins",
            "calories":f"{a["exercises"][nums]["nf_calories"]} cals"
            }
    }

    df=requests.post(url=sheety_api,json=body)
    print(df.text)
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('nutrion_sheety_pic.png')

imgplot = plt.imshow(img)
plt.show()
