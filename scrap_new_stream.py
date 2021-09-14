from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import smtplib
import ssl
import time
import streamlit as st
page_url = "https://premiery.adrenaline.pl"
port = 465  # For SSL
password = input()
gmail_user = 'f.spronk2@gmail.com'
to = ['pawo161@gmail.com']
uClient = uReq(page_url)
data0 = []
page_soup = soup(uClient.read(), "html.parser")
uClient.close()


# finds each product from the store page
containers = page_soup.findAll("div", {"class": "nazwa"})
for container in containers:
    product_name = container.h5.text.strip()
    data0.append(product_name)


message = """\
Subject: Nowa premiera!

https://premiery.adrenaline.pl"""


while True:
    # opens the connection and downloads html page from url
    uClient = uReq(page_url)
    data = []
    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    # finds each product from the store page
    containers = page_soup.findAll("div", {"class": "nazwa"})

    # loops over each product and grabs attributes about
    # each product
    for container in containers:
        product_name = container.h5.text.strip()
        data.append(product_name)

    if(data0 == data):
        print("no changes so far")
        pass
    else:
        # Create a secure SSL context
        print("changes noticed")
        context = ssl.create_default_context()
        data0 = data
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login('f.spronk2@gmail.com', password)
            server.sendmail(gmail_user, to, message)

    time.sleep(120)
