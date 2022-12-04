# -*- coding: utf-8 -*-

from ScrapeWebsite import scrape_country

#change country name here
countryName = 'South Korea'

#Choose either WHO or worldometer for the website

website = 'worldometer'  # WHO website currently does not include normalized data
#website = 'worldometer'

#Calling scrape_country website to scrape death rate data for today
cumulative_deaths, daily_deaths = scrape_country(countryName, website)


cumulative_deaths, daily_deaths, norm_cumulative_death, norm_daily_death = scrape_country(countryName, website)
