# CovidDashboard

This repository includes a main file CovidMain.py, a module to scrape data from websites ScrapeWebsites.py, and json files for 2 consecutive days of global COVID death rate data. The code is dependent on the following libraries: BeautifulSoup, json, and requests. 

**Using CovidMain.py**

  * To use this code, open the CovidMain.py file and input the country name and the website you wish to scrape. The daily and cumulative death rates will be output as well as a .json file with all of country data. Scrapy is included additionally to scrape the data.
       *   *Run the following in the python command line to use scrapy:*
      
                  scrapy crawl worldometer
                  
**Data Collection**
  * Data collection was done using BeautifulSoup. The initial json file created using the scrapy library and was replaced with BeautifulSoup due to being more flexible.
  * Currently two websites can be scraped, worldometers.info and covid19.who.int.
  * Normalized death rate data is only available for worldometer.
                  
**JSON organization**
  *	The .json files contains multiple rows in which each country scraped from worldometers.info has its corresponding values of total deaths and new deaths on individual column cells.
         
