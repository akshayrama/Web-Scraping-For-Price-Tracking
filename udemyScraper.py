import requests
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

def checkPrice(x, priceToCompare):
    if priceToCompare >= x:
        return True
    else:
        return False

def redirect(URL):
    driverPath = '' # Fill in the driver path of your preferred browser's webdriver as part of your inital configuration
    driver = webdriver.Chrome(driverPath) # In this example, I've used the Chrome webdriver
    driver.get(URL)
    return driver

URL = '' # Fill in the URL of this a Udemy course site as part of your inital configuration
headers = { "User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}

print('Enter the price to check:', end = " ")
priceToCompare = float(input())

page = requests.get( URL, headers = headers)
soup = BeautifulSoup(page.content, 'html.parser')

currentPriceFinder = soup.find("span", {"class" : "sr-only"}, text = "Current price:")
currentPrice = currentPriceFinder.nextSibling.strip()
currentPrice = currentPrice[1:len(currentPrice)] # To cut off the rupee symbol

currentPriceInFloat = float(currentPrice)
if(checkPrice(currentPriceInFloat, priceToCompare)):
    print('Hurray! Your course is less than or below the price entered! ')
    print('Shall I redirect you to the course site?', end = " ")
    redirectFlag = input()
    if redirectFlag == "Yes":
        openingBrowser = redirect(URL)
    else:
        pass
else:
    print('Oops, the amount entered was too high, please wait for some time for the price to reduce')

