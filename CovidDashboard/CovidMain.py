# -*- coding: utf-8 -*-

from ScrapeWebsite import scrape_country

#change country name here
countryName = 'India'

#Choose either WHO or worldometer for the website

website = 'WHO' #WHO website currently does not include normalized data 
#website = 'worldometer'

#Calling scrape_country website to scrape death rate data for today
cumulative_deaths, daily_deaths = scrape_country(countryName, website)


#worldometer = scrape_country('India','worldometer')


