#final project-----
#link for website=https://pixe.la/v1/users/ray12345678/graphs/b2b12da4e522acc.html
# or matplotlib code to view in editor
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('my_pixela_miles.png')

imgplot = plt.imshow(img)
plt.show()
#---------------------------------------code to get your own--------------------------------------#

import requests as req
import datetime as dt

token=str(input("What is your token id?rule:[ -~]{8,128}"))
graph_id=str(input("What is your graph id?rule:Ex:b2b12d4522cc"))
username=str(input('What is your username?Ex:Ray'))

#1.creating a user
pixela_website_url="https://pixe.la/v1/users"
paramss={
    "token":token,

    "username":username,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"}
user=req.post(url=pixela_website_url,json=paramss)
print(user.text)

#2.creating a graph----
"""creating a graph for how many miles i ran each day-----"""

pixela_website_url="https://pixe.la/v1/users/ray12345678/graphs/"
headers={
    "X-USER-TOKEN":token
}
params={
    "id":graph_id,
    "name":"Miles",
    "unit":"kilometer",
    "type":"float",
    "color":"momiji",
}
graph=req.post(url=pixela_website_url,headers=headers,json=params)
print(graph.text)

""" user profile--(for patreon members only to update features)"""
#pixela_endpoint_url="https://pixe.la/v1/users/ray12345678"
# header={
#     "X-USER-TOKEN":token
# }
# params={
#     "displayName":"your name",
#     "gravatarIconEmail":"email registered on gravatar",
    

# }
# udate=req.put(url=pixela_endpoint_url,headers=header,json=params)
# print(udate.text)


##3.posting values
"""input for pixel allotment--------"""

###miles input
imp=str(input("How many miles did you run today?"))
# #####date in given format input--
today=(dt.datetime.now()).strftime("%Y%m%d")#-dt.timedelta(days=3)
pixela_url=pixela_website_url+graph_id
headers={
        "X-USER-TOKEN":token
}
params={
        "date":today,
        "quantity":imp
}
user=req.post(url=pixela_url,headers=headers,json=params)
print(user.text)

