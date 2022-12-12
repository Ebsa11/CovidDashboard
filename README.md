# CovidDashboard

This repository includes:
 * CovidMain.py to visualize Covid death rates using Bokeh
 * ScrapeWebsite.py and ScrapeCountry.py modules to collect Covid death rate data from websites
 * Data in JSON files for 5 days of global COVID death rate data. 
 
The code is dependent on the following libraries: BeautifulSoup, Bokeh, numpy, re, json, and requests. 

**Using CovidMain.py**

When this code is run, an HTML file is automatically created and opened in your browswer to display the Covid Dashboard. This can also be optionally be opened in an online notebook such as Jupyter Lab simply by running the code in the respective editors. Data for today, yesterday, and two days ago are updated everyday while the death rates from 12-3-22 12-4-22, 12-7-22, and 12-8-22 are from the saved JSON files included to demonstrate the ability to display saved data.

**CovidMain.py versions*
There are two versions for the CovidMain.py program. 
  * The file CovidMain.py is designed for users using Bokeh version 3.0.3
  * The file CovidMain_2.4.3.py is designed for users using Bokeh version 2.4.3

**Using ScrapeWebsite and ScrapeCountry**

ScrapeWebsite takes no input and outputs the death rate data of every country available from the website worldometer. Alternatively, the ScrapeCountry module takes the input of a country name and a website and outputs the Covid death rates as well as a .json file wwith the data. As an alternative. Scrapy is included to scrape the data.
  * *Run the following in the python command line to use scrapy:*
  
                  scrapy crawl worldometer
                  
**Data Collection**
  * Currently two websites can be scraped, worldometers.info and covid19.who.int
  * Normalized death rate data and data for yesterday and two days ago are only available for worldometer
                  
**JSON organization**

The .json files contains multiple rows in which each country scraped from worldometers.info has its corresponding values of total deaths and new deaths on individual column cells.
         
