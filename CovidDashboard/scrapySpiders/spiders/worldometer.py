import scrapy
from scrapy.crawler import CrawlerProcess

from datetime import date
from datetime import timedelta

        
class worldometerYesterdaySpider(scrapy.Spider):
    name = 'worldometerYesterday'
    allowed_domains = ['worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus/']
    
    yesterday = date.today() - timedelta(days=1)
    custom_settings = {
       'FEEDS': {f'worldometerYesterday_{yesterday}.json': {'format': 'jsonlines', 'overwrite': True}}
       }
            
    def parse(self,response):
        for row in response.xpath('//*[@id="main_table_countries_yesterday"]//tbody/tr'):
            yield{
                'Country' : row.xpath('td[2]//text()').extract(),
                'Cumulative Deaths' : row.xpath('td[5]//text()').extract(),
                'New Deaths' : row.xpath('td[6]//text()').extract(),
                }


class worldometer2DaysagoSpider(scrapy.Spider):    
    name = 'worldometer2Daysago'
    allowed_domains = ['worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus/']
    
    yesteryesterday = date.today() - timedelta(days=2)
    custom_settings = {
       'FEEDS': {f'worldometer_{yesteryesterday}.json': {'format': 'jsonlines', 'overwrite': True}}
       }

    def parse(self,response):
        for row in response.xpath('//*[@id="main_table_countries_yesterday2"]//tbody/tr'):
            yield{
                'Country' : row.xpath('td[2]//text()').extract(),
                'Cumulative Deaths' : row.xpath('td[5]//text()').extract(),
                'Cumulative Deaths/1M pop' : row.xpath('td[12]//text()').extract(),
                'New Deaths' : row.xpath('td[6]//text()').extract(),
                'New Deaths/1M pop' : row.xpath('td[21]//text()').extract(),
                }
            
yesteryesterday = date.today() - timedelta(days=2)
custom_settings = {
   'FEEDS': {f'worldometer_{yesteryesterday}.json': {'format': 'jsonlines', 'overwrite': True}}
   }
process = CrawlerProcess(custom_settings)
process.crawl(worldometerYesterdaySpider)
process.crawl(worldometer2DaysagoSpider)
process.start() # the script will block here until the crawling is finished
        
        
        
        
        