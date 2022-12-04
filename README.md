# CovidDashboard

**Data Collection from worldometers.info**

  * Using scrapy, the worldometer.py file contains a code that extracts the total deaths and new deaths from a day and two days ago.
  *	This file contains two classes:
    *	```class worldometerYesterdaySpider(scrapy.Spider):``` - corresponding to the data from a day ago
    * ```class worldometer2DaysagoSpider(scrapy.Spider):``` - corresponding to the data from two days ago
  *	The class has the following components:
    *	‘Name’ assigned to the class to be called in the future
    *	An allowed domain
    *	A ‘starting url’ for the class to use as a starting point to scrape data
    *	It has a custom setting used to save the scraped data as a .json file with the specific date on which the data was scraped
        * This setting is set to overwrite itself as long as the data has been extracted during the same day
       
         ```  
              name = 'worldometerYesterday'
              allowed_domains = ['worldometers.info']
              start_urls = ['https://www.worldometers.info/coronavirus/']

              custom_settings = {
                 'FEEDS': {f'worldometerYesterday_{date.today()}.json': {'format': 'jsonlines', 'overwrite': True}}
                   }
          ```
        
    *	It contains two definitions:
        *	```def start_requests(self):```
        *	```def parse(self,response):```
        
  *	The function ‘start_requests’ specifies the url from which we want to scrape data from
  *	The function ‘parse’ helps split the source code into specific sections
    *	From the used url we are interested in using the table containing all of the desired data
        *	Using ‘.xpath’ we are able to pinpoint the path of the table containing the data

         ```
               for row in response.xpath('//*[@id="main_table_countries_yesterday"]//tbody/tr'):]
         ```

    *	The for loop is used to extract each row from the table individually
        *	This helps to organize the total deaths and new deaths data to its corresponding country
    *	As the code looks through each row it will yield only the columns containing the numeric values that we want to obtain (total deaths and new deaths
    
         ```
               yield{
                      'Country' : row.xpath('td[2]//text()').extract(),
                      'Cumulative Deaths' : row.xpath('td[5]//text()').extract(),
                      'New Deaths' : row.xpath('td[6]//text()').extract(),
                      }
         ```
                
                
**JSON organization**
  *	The .json files contains multiple rows in which each country scraped from worldometers.info has its corresponding values of total deaths and new deaths on individual column cells 
