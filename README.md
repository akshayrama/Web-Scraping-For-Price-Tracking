# Web-Scraping-For-Price-Tracking
This repository contains code which enables us to automate tracking the prices for Udemy courses. 

## Initial Configuration ##
After cloning this repository, you will have to set up some inital configuration for this code to work. 
* You are required to add the URL of the Udemy course site that you wish to track. 
* And lastly, you are requirerd to provive the path of your desirable browser's webdriver.

The places for these provisions are mentioned as part of the code indicated by comments.

## Description ## 
This project utilises Web Scraping libraries such as Beautiful Soup and Selenium. After the inital configuration the program takes in another input from the user which is the "priceToCompare". This defines the maximum price the user is willing to pay for that course. Suppose the price of the course is lesser than or equal to the priceToCompare specified by the user, the program asked for if the user wants to redirect to that site in order to purchase the course. The actual price of the course is obtained using the bs4 or Beautiful Soup library. The redirection to the Udemy website is handled by Selenium. 

Further enhancements for this project would include running the program as a Windows Service or using the Task Scheduler to run the program at specific times and initiating a notification in form of an e-mail or text once the price reduces to the desired amount. If the priceToCheck is also hard-coded into the program, the code can run without any addtional input from the user. 
