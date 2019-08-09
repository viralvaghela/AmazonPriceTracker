import requests
import os
from bs4 import BeautifulSoup
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

def send_sms(b):
    message = client.messages \
                    .create(
                         body=b,
                         from_='+18052887240',
                         to='+917485994073'
                     )

    print("Message sent, ID: ",message.sid)

url=input("Enter Url:")
headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

page=requests.get(url,headers=headers)
soup=BeautifulSoup(page.content,'html.parser')
price=soup.find(id="priceblock_ourprice").get_text()
title=soup.find(id="productTitle").get_text()

price=price.replace(",","")
price=float(price.replace("₹","").strip())
title=title.strip()
print("\n\nPrice of ",title,"is ",price)
if(price < 65000):
    body="Buy now "+title+ "Price is " +str(price)+" Link is here "+url
    #print(body)
    #send_sms(body)
    print(account_sid)
input("Press any key to exit")
