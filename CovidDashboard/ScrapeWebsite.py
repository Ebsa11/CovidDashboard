import scrapy
from scrapy.crawler import CrawlerProcess
from datetime import date
from datetime import timedelta
import requests
import json
from bs4 import BeautifulSoup

class worldometer(scrapy.Spider):
    name = 'worldometer'
    #allowed_domains = ['worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus/']

    #settings for savinga a json file
    yesterday = date.today() - timedelta(days=1)
    custom_settings = {
        'FEEDS': {f'worldometerYesterday_{yesterday}.json': {'format': 'jsonlines', 'overwrite': True}}
    }

    def parse(self, response):
        for row in response.xpath('//*[@id="main_table_countries_yesterday"]//tbody/tr'):
            yield{
                'Country': row.xpath('td[2]//text()').extract(),
                'Cumulative Deaths': row.xpath('td[5]//text()').extract(),
                'Cumulative Deaths/1M pop': row.xpath('td[12]//text()').extract(),
                'New Deaths': row.xpath('td[6]//text()').extract(),
                'New Deaths/1M pop': row.xpath('td[21]//text()').extract(),
            }
            
def scrape_country(countryName, website):
    print('Test')
    if website == 'worldometer':
        
            yesterday = date.today() - timedelta(days=1)
            custom_settings = {
               'FEEDS': {f'worldometer_{yesterday}.json': {'format': 'jsonlines', 'overwrite': True}}
               }
            process = CrawlerProcess(custom_settings)
            process.crawl(worldometer)
            process.start() # the script will block here until the crawling is finished
            
    elif website == 'WHO':

        url = "https://covid19.who.int/table"
        req = requests.get(url)
        doc = BeautifulSoup(req.text, 'html.parser')
        
        found_daily_deaths = doc.find_all("div",{"class": "column_Last_7_Days_Deaths td"})
        found_cumulative_deaths = doc.find_all("div",{"class": "column_Cumulative_Deaths td"})
        found_countries = doc.find_all("div",{"class": "column_name td"})
        
        countries = []
        cumulative_deaths = []
        daily_deaths = []
        
        #scraping data
        for i in range(len(found_countries)):
          if found_countries[i].text[0] == '+':
            continue
        
          countries.append(found_countries[i].text)
              
        
          if found_cumulative_deaths[i].text == '':
            cumulative_deaths.append("N/A")
          else:
            cumulative_deaths.append(found_cumulative_deaths[i].text)
        
          if found_daily_deaths[i].text == '':
            daily_deaths.append("N/A")
          else:
            daily_deaths.append(found_daily_deaths[i].text)
        
        #finding index for countryName
        for i in range(len(countries)):
            if countries[i] == countryName:
                print('Test Index')
                return cumulative_deaths[i], daily_deaths[i]

        data = {
            "Country": countries,
            "Cumulative Deaths": cumulative_deaths,
            "Daily Deaths": daily_deaths
        }
        
        json_object = json.dumps(data, indent=4)
         
        with open("Covid_data2.json", "w") as outfile:
            outfile.write(json_object)

        
