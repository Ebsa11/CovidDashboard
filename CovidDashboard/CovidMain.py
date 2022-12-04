# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 19:51:55 2022

@author: Ebsa
"""

from ScrapeWebsite import scrape_country

#change country name here
countryName = 'India'

#Choose either WHO or worldometer for the website
website = 'WHO'

#Calling function
cumulative_deaths, daily_deaths = scrape_country(countryName, website)


worldometer = scrape_country('India','worldometer')


