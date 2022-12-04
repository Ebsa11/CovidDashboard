import requests
import json
import re
from bs4 import BeautifulSoup


def scrape_country(countryName, website):
    #The function scrapes a website for the death rate data, creates a json file, and then returns the death rates.
    #Currently only WHO and worldometer are supported.
    #The worldometer is not working in the function, however it will work in the python command line.
    #Run the following in the command line: scrapy crawl worldometer
    #Further documentation for scrapy https://docs.scrapy.org/en/latest/topics/commands.html

    if website == 'worldometer':

        url = "https://www.worldometers.info/coronavirus/"
        req = requests.get(url)
        doc = BeautifulSoup(req.text, 'html.parser')

        data = doc.find_all("tr", {"style": ""})

        found_countries = []
        found_total_deaths = []
        found_new_deaths = []
        found_total_deaths_pop = []
        found_new_deaths_pop = []
        for i in range(2, 223):
          found_countries.append(data[i].find_all("td")[1].text)

          if data[i].find_all("td")[4].text != "":
            found_total_deaths.append(data[i].find_all("td")[4].text)
          else:
            found_total_deaths.append("N/A")

          if data[i].find_all("td")[5].text != "":
            found_new_deaths.append(data[i].find_all("td")[5].text)
            found_new_deaths_pop.append((int(data[i].find_all(
                "td")[5].text)*1000000)/int(re.sub(",", "", data[i].find_all("td")[14].text)))
          else:
            found_new_deaths.append("N/A")
            found_new_deaths_pop.append("0")

          if data[i].find_all("td")[11].text != "":
            found_total_deaths_pop.append(data[i].find_all("td")[11].text)
          else:
            found_total_deaths_pop.append("N/A")

        #finding index for countryName
        for i in range(len(found_countries)):
            if found_countries[i] == countryName:
                return found_total_deaths[i], found_new_deaths[i], found_total_deaths_pop[i], found_new_deaths_pop[i]

        return "Country not found"

        data = {
            "Country": found_countries,
            "Cumulative Deaths": found_total_deaths,
            "Daily Deaths": found_new_deaths,
            "Population Cumulative Deaths": found_total_deaths_pop,
            "Population Daily Deaths": found_new_deaths_pop,
        }

        json_object = json.dumps(data, indent=4)

        with open("Covid_data2.json", "w") as outfile:
            outfile.write(json_object)

    elif website == 'WHO':

        url = "https://covid19.who.int/table"
        req = requests.get(url)
        doc = BeautifulSoup(req.text, 'html.parser')

        found_daily_deaths = doc.find_all(
            "div", {"class": "column_Last_7_Days_Deaths td"})
        found_cumulative_deaths = doc.find_all(
            "div", {"class": "column_Cumulative_Deaths td"})
        found_countries = doc.find_all("div", {"class": "column_name td"})

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
                return cumulative_deaths[i], daily_deaths[i]
        
        return "Country not found"
        

        data = {
            "Country": countries,
            "Cumulative Deaths": cumulative_deaths,
            "Daily Deaths": daily_deaths
        }

        json_object = json.dumps(data, indent=4)

        with open("Covid_data2.json", "w") as outfile:
            outfile.write(json_object)
