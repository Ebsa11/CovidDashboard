# -*- coding: utf-8 -*-
"""CovidMain
@author: Andres Vizcarra, Bret Mecham, Ebsa Eshete

Original file is located at
    https://github.com/Ebsa11/CovidDashboard
"""""

import numpy as np
import re
from bokeh.plotting import figure
from ScrapeWebsite import Scrape3Days
from bokeh.layouts import row
from bokeh.models import ColumnDataSource, HoverTool,DataTable, TableColumn
from bokeh.plotting import show, output_file
from bokeh.models import TabPanel, Tabs
from bokeh.transform import dodge
from bokeh.io import output_notebook  # added
from bokeh.resources import INLINE    # added
import os, json
dirname = os.getcwd()
output_notebook(INLINE)               # added


# Save output html
output_file(filename="COVID_results.html", title="Static HTML file")


# ===================================SAVED DATA========================================== START
dirname = os.getcwd()
filename4 = os.path.join(dirname, 'SavedData\WOM12-4-22.json')
filename7 = os.path.join(dirname, 'SavedData\WOM12-7-22.json')
filename8 = os.path.join(dirname, 'SavedData\WOM12-8-22.json')


with open(filename4) as json_file:
    data_12_4_22 = json.load(json_file)

with open(filename7) as json_file:
    data_12_7_22= json.load(json_file)
    
with open(filename8) as json_file:
    data_12_8_22 = json.load(json_file)




# 12_4_22 SECTION
# Get TOTAL 12_4_22's deaths
total_deaths_12_4_22 = list(data_12_4_22['Cumulative Deaths'])
for i in range(len(total_deaths_12_4_22)):
  total_deaths_12_4_22[i] = int(re.sub(",","",total_deaths_12_4_22[i]))
total_deaths_12_4_22_sort_index = np.argsort(total_deaths_12_4_22)
total_deaths_12_4_22_ranks = [0]*len(total_deaths_12_4_22)
for i in range(1,len(total_deaths_12_4_22)):
  total_deaths_12_4_22_ranks[total_deaths_12_4_22_sort_index[-i]] = i

# Get NEW 12_4_22's deaths
new_deaths_12_4_22 = list(data_12_4_22['Daily Deaths'])
for i in range(len(new_deaths_12_4_22)):
  new_deaths_12_4_22[i] = int(re.sub(",","",new_deaths_12_4_22[i]))
new_deaths_12_4_22_sort_index = np.argsort(new_deaths_12_4_22)
new_deaths_12_4_22_ranks = [0]*len(new_deaths_12_4_22)
for i in range(1,len(new_deaths_12_4_22)):
  new_deaths_12_4_22_ranks[new_deaths_12_4_22_sort_index[-i]] = i
  
# Get TOTAL POP 12_4_22's deaths
total_deaths_pop_12_4_22 = list(data_12_4_22['Population Cumulative Deaths'])
for i in range(len(total_deaths_pop_12_4_22)):
  total_deaths_pop_12_4_22[i] = int(re.sub(",","",total_deaths_pop_12_4_22[i]))
total_deaths_pop_12_4_22_sort_index = np.argsort(total_deaths_pop_12_4_22)
total_deaths_pop_12_4_22_ranks = [0]*len(total_deaths_pop_12_4_22)
for i in range(1,len(total_deaths_pop_12_4_22)):
  total_deaths_pop_12_4_22_ranks[total_deaths_pop_12_4_22_sort_index[-i]] = i

# Get NEW POP 12_4_22's deaths
new_deaths_pop_12_4_22 = list(data_12_4_22['Population Daily Deaths'])
new_deaths_pop_12_4_22_sort_index = np.argsort(new_deaths_pop_12_4_22)
new_deaths_pop_12_4_22_ranks = [0]*len(new_deaths_pop_12_4_22)
for i in range(1,len(new_deaths_pop_12_4_22)):
  new_deaths_pop_12_4_22_ranks[new_deaths_pop_12_4_22_sort_index[-i]] = i



# 12_7_22 SECTION
# Get TOTAL 12_7_22's deaths
total_deaths_12_7_22 = list(data_12_7_22['Cumulative Deaths'])
total_deaths_12_7_22_sort_index = np.argsort(total_deaths_12_7_22)
total_deaths_12_7_22_ranks = [0]*len(total_deaths_12_7_22)
for i in range(1,len(total_deaths_12_7_22)):
  total_deaths_12_7_22_ranks[total_deaths_12_7_22_sort_index[-i]] = i

# Get NEW 12_7_22's deaths
new_deaths_12_7_22 = list(data_12_7_22['Daily Deaths'])
new_deaths_12_7_22_sort_index = np.argsort(new_deaths_12_7_22)
new_deaths_12_7_22_ranks = [0]*len(new_deaths_12_7_22)
for i in range(1,len(new_deaths_12_7_22)):
  new_deaths_12_7_22_ranks[new_deaths_12_7_22_sort_index[-i]] = i
  
# Get TOTAL POP 12_7_22's deaths
total_deaths_pop_12_7_22 = list(data_12_7_22['Population Cumulative Deaths'])
total_deaths_pop_12_7_22_sort_index = np.argsort(total_deaths_pop_12_7_22)
total_deaths_pop_12_7_22_ranks = [0]*len(total_deaths_pop_12_7_22)
for i in range(1,len(total_deaths_pop_12_7_22)):
  total_deaths_pop_12_7_22_ranks[total_deaths_pop_12_7_22_sort_index[-i]] = i

# Get NEW POP 12_7_22's deaths
new_deaths_pop_12_7_22 = list(data_12_7_22['Population Daily Deaths'])
new_deaths_pop_12_7_22_sort_index = np.argsort(new_deaths_pop_12_7_22)
new_deaths_pop_12_7_22_ranks = [0]*len(new_deaths_pop_12_7_22)
for i in range(1,len(new_deaths_pop_12_7_22)):
  new_deaths_pop_12_7_22_ranks[new_deaths_pop_12_7_22_sort_index[-i]] = i




# 12_8_22 SECTION
# Get TOTAL 12_8_22's deaths
total_deaths_12_8_22 = list(data_12_8_22['Cumulative Deaths'])
for i in range(len(total_deaths_12_8_22)):
  total_deaths_12_8_22[i] = int(re.sub(",","",total_deaths_12_8_22[i]))
total_deaths_12_8_22_sort_index = np.argsort(total_deaths_12_8_22)
total_deaths_12_8_22_ranks = [0]*len(total_deaths_12_8_22)
for i in range(1,len(total_deaths_12_8_22)):
  total_deaths_12_8_22_ranks[total_deaths_12_8_22_sort_index[-i]] = i

# Get NEW 12_8_22's deaths
new_deaths_12_8_22 = list(data_12_8_22['Daily Deaths'])
for i in range(len(new_deaths_12_8_22)):
  new_deaths_12_8_22[i] = int(re.sub(",","",new_deaths_12_8_22[i]))
new_deaths_12_8_22_sort_index = np.argsort(new_deaths_12_8_22)
new_deaths_12_8_22_ranks = [0]*len(new_deaths_12_8_22)
for i in range(1,len(new_deaths_12_8_22)):
  new_deaths_12_8_22_ranks[new_deaths_12_8_22_sort_index[-i]] = i
  
# Get TOTAL POP 12_8_22's deaths
total_deaths_pop_12_8_22 = list(data_12_8_22['Population Cumulative Deaths'])
for i in range(len(total_deaths_pop_12_8_22)):
  total_deaths_pop_12_8_22[i] = int(re.sub(",","",total_deaths_pop_12_8_22[i]))
total_deaths_pop_12_8_22_sort_index = np.argsort(total_deaths_pop_12_8_22)
total_deaths_pop_12_8_22_ranks = [0]*len(total_deaths_pop_12_8_22)
for i in range(1,len(total_deaths_pop_12_8_22)):
  total_deaths_pop_12_8_22_ranks[total_deaths_pop_12_8_22_sort_index[-i]] = i

# Get NEW POP 12_8_22's deaths
new_deaths_pop_12_8_22 = list(data_12_8_22['Population Daily Deaths'])
new_deaths_pop_12_8_22_sort_index = np.argsort(new_deaths_pop_12_8_22)
new_deaths_pop_12_8_22_ranks = [0]*len(new_deaths_pop_12_8_22)
for i in range(1,len(new_deaths_pop_12_8_22)):
  new_deaths_pop_12_8_22_ranks[new_deaths_pop_12_8_22_sort_index[-i]] = i
  


# MAKE DICTIONARY FOR 12_4_22'S DEATHS
data_12_4_22 = {'Countries_12_4_22': np.array(data_12_4_22['Country']),
        'Total_deaths_12_4_22': total_deaths_12_4_22,
        'Total_deaths_12_4_22_ranking': total_deaths_12_4_22_ranks,
        'Total_deaths_12_4_22_str': data_12_4_22["Cumulative Deaths"],
        'New_deaths_12_4_22': new_deaths_12_4_22,
        'New_deaths_12_4_22_ranking': new_deaths_12_4_22_ranks,
        'New_deaths_12_4_22_str': data_12_4_22["Daily Deaths"],
        'Total_deaths_pop_12_4_22': total_deaths_pop_12_4_22,
        'Total_deaths_pop_12_4_22_ranking': total_deaths_pop_12_4_22_ranks,
        'Total_deaths_pop_12_4_22_str': data_12_4_22["Population Cumulative Deaths"],
        'New_deaths_pop_12_4_22': new_deaths_pop_12_4_22,
        'New_deaths_pop_12_4_22_ranking': new_deaths_pop_12_4_22_ranks,
        'New_deaths_pop_12_4_22_str': data_12_4_22["Population Daily Deaths"]}
source_12_4_22 = ColumnDataSource(data_12_4_22)
numCountries_12_4_22 = np.flip(source_12_4_22.data['Countries_12_4_22'].tolist())



# MAKE DICTIONARY FOR 12_7_22'S DEATHS
data_12_7_22 = {'Countries_12_7_22': np.array(data_12_7_22['Country']),
        'Total_deaths_12_7_22': total_deaths_12_7_22,
        'Total_deaths_12_7_22_ranking': total_deaths_12_7_22_ranks,
        'Total_deaths_12_7_22_str': data_12_7_22["Cumulative Deaths"],
        'New_deaths_12_7_22': new_deaths_12_7_22,
        'New_deaths_12_7_22_ranking': new_deaths_12_7_22_ranks,
        'New_deaths_12_7_22_str': data_12_7_22["Daily Deaths"],
        'Total_deaths_pop_12_7_22': total_deaths_pop_12_7_22,
        'Total_deaths_pop_12_7_22_ranking': total_deaths_pop_12_7_22_ranks,
        'Total_deaths_pop_12_7_22_str': data_12_7_22["Population Cumulative Deaths"],
        'New_deaths_pop_12_7_22': new_deaths_pop_12_7_22,
        'New_deaths_pop_12_7_22_ranking': new_deaths_pop_12_7_22_ranks,
        'New_deaths_pop_12_7_22_str': data_12_7_22["Population Daily Deaths"]}
source_12_7_22 = ColumnDataSource(data_12_7_22)
numCountries_12_7_22 = np.flip(source_12_7_22.data['Countries_12_7_22'].tolist())




# MAKE DICTIONARY FOR 12_8_22'S DEATHS
data_12_8_22 = {'Countries_12_8_22': np.array(data_12_8_22['Country']),
        'Total_deaths_12_8_22': total_deaths_12_8_22,
        'Total_deaths_12_8_22_ranking': total_deaths_12_8_22_ranks,
        'Total_deaths_12_8_22_str': data_12_8_22["Cumulative Deaths"],
        'New_deaths_12_8_22': new_deaths_12_8_22,
        'New_deaths_12_8_22_ranking': new_deaths_12_8_22_ranks,
        'New_deaths_12_8_22_str': data_12_8_22["Daily Deaths"],
        'Total_deaths_pop_12_8_22': total_deaths_pop_12_8_22,
        'Total_deaths_pop_12_8_22_ranking': total_deaths_pop_12_8_22_ranks,
        'Total_deaths_pop_12_8_22_str': data_12_8_22["Population Cumulative Deaths"],
        'New_deaths_pop_12_8_22': new_deaths_pop_12_8_22,
        'New_deaths_pop_12_8_22_ranking': new_deaths_pop_12_8_22_ranks,
        'New_deaths_pop_12_8_22_str': data_12_8_22["Population Daily Deaths"]}
source_12_8_22 = ColumnDataSource(data_12_8_22)
numCountries_12_8_22 = np.flip(source_12_8_22.data['Countries_12_8_22'].tolist())


# CREATE FIGURE FOR 12_4_22
p17 = figure(
    y_range=numCountries_12_4_22,
    width=800,
    height=2500,
    title = 'COVID-19 World''s Data - 12_4_22',
    x_axis_label = 'Number of deaths',
    tools="pan,box_select,zoom_in,zoom_out,reset"
    )


# Create Histogram
p17.hbar(
    y=dodge('Countries_12_4_22',0.0, range=p17.y_range),
    right='Total_deaths_12_4_22',
    left=0,
    height=0.4,
    color='red',
    fill_alpha=0.9,
    source=source_12_4_22
    )

# Create Hover Tool
hover = HoverTool()
hover.tooltips = """
<div>
  <h3>@Countries_12_4_22</h3>
  <div><strong>Total Deaths: </strong>@Total_deaths_12_4_22_str</div>
  <div><strong>Ranking: #</strong>@Total_deaths_12_4_22_ranking</div>
</div>
"""
p17.add_tools(hover)

p18 = figure(
    y_range=numCountries_12_4_22,
    width=800,
    height=2500,
    title = 'COVID-19 World''s Data - 12_4_22',
    x_axis_label = 'Number of deaths',
    tools="pan,box_select,zoom_in,zoom_out,reset"
    )

# Create Histogram
p18.hbar(
    y=dodge('Countries_12_4_22',0.0, range=p18.y_range),
    right='New_deaths_12_4_22',
    left=0,
    height=0.4,
    color='blue',
    fill_alpha=0.9,
    source=source_12_4_22
    )

# Create Hover Tool
hover = HoverTool()
hover.tooltips = """
<div>
  <h3>@Countries_12_4_22</h3>
  <div><strong>New Deaths: </strong>@New_deaths_12_4_22_str</div>
  <div><strong>Ranking: #</strong>@New_deaths_12_4_22_ranking</div>
</div>
"""
p18.add_tools(hover)

p19 = figure(
    y_range=numCountries_12_4_22,
    width=800,
    height=2500,
    title = 'COVID-19 World''s Data - 12_4_22',
    x_axis_label = 'Number of deaths',
    tools="pan,box_select,zoom_in,zoom_out,reset"
    )

# Create Histogram
p19.hbar(
    y=dodge('Countries_12_4_22',0.0, range=p19.y_range),
    right='Total_deaths_pop_12_4_22',
    left=0,
    height=0.4,
    color='green',
    fill_alpha=0.9,
    source=source_12_4_22
    )

# Create Hover Tool
hover = HoverTool()
hover.tooltips = """
<div>
  <h3>@Countries_12_4_22</h3>
  <div><strong>Total Deaths: </strong>@Total_deaths_pop_12_4_22_str</div>
  <div><strong>Ranking: #</strong>@Total_deaths_pop_12_4_22_ranking</div>
</div>
"""
p19.add_tools(hover)

p20 = figure(
    y_range=numCountries_12_4_22,
    width=800,
    height=2500,
    title = 'COVID-19 World''s Data - 12_4_22',
    x_axis_label = 'Number of deaths',
    tools="pan,box_select,zoom_in,zoom_out,reset"
    )

# Create Histogram
p20.hbar(
    y=dodge('Countries_12_4_22',0.0, range=p20.y_range),
    right='New_deaths_pop_12_4_22',
    left=0,
    height=0.4,
    color='orange',
    fill_alpha=0.9,
    source=source_12_4_22
    )

# Create Hover Tool
hover = HoverTool()
hover.tooltips = """
<div>
  <h3>@Countries_12_4_22</h3>
  <div><strong>Total Deaths: </strong>@New_deaths_pop_12_4_22_str</div>
  <div><strong>Ranking: #</strong>@New_deaths_pop_12_4_22_ranking</div>
</div>
"""
p20.add_tools(hover)

# Make Table
columns5 = [
        TableColumn(field='Countries_12_4_22', title="Countries"),
        TableColumn(field="Total_deaths_12_4_22", title="Total Deaths"),
        TableColumn(field="New_deaths_12_4_22", title="New Deaths"),
        TableColumn(field="Total_deaths_pop_12_4_22", title="Total Deaths by Population"),
        TableColumn(field="New_deaths_pop_12_4_22", title="New Deaths by Population")
    ]
data_table5 = DataTable(source=source_12_4_22, columns=columns5, width=800, height=3000)




# CREATE FIGURE FOR 12_7_22
p21 = figure(
    y_range=numCountries_12_7_22,
    width=800,
    height=2500,
    title = 'COVID-19 World''s Data - 12_7_22',
    x_axis_label = 'Number of deaths',
    tools="pan,box_select,zoom_in,zoom_out,reset"
    )


# Create Histogram
p21.hbar(
    y=dodge('Countries_12_7_22',0.0, range=p21.y_range),
    right='Total_deaths_12_7_22',
    left=0,
    height=0.4,
    color='red',
    fill_alpha=0.9,
    source=source_12_7_22
    )

# Create Hover Tool
hover = HoverTool()
hover.tooltips = """
<div>
  <h3>@Countries_12_7_22</h3>
  <div><strong>Total Deaths: </strong>@Total_deaths_12_7_22_str</div>
  <div><strong>Ranking: #</strong>@Total_deaths_12_7_22_ranking</div>
</div>
"""
p21.add_tools(hover)

p22 = figure(
    y_range=numCountries_12_7_22,
    width=800,
    height=2500,
    title = 'COVID-19 World''s Data - 12_7_22',
    x_axis_label = 'Number of deaths',
    tools="pan,box_select,zoom_in,zoom_out,reset"
    )

# Create Histogram
p22.hbar(
    y=dodge('Countries_12_7_22',0.0, range=p22.y_range),
    right='New_deaths_12_7_22',
    left=0,
    height=0.4,
    color='blue',
    fill_alpha=0.9,
    source=source_12_7_22
    )

# Create Hover Tool
hover = HoverTool()
hover.tooltips = """
<div>
  <h3>@Countries_12_7_22</h3>
  <div><strong>New Deaths: </strong>@New_deaths_12_7_22_str</div>
  <div><strong>Ranking: #</strong>@New_deaths_12_7_22_ranking</div>
</div>
"""
p22.add_tools(hover)

p23 = figure(
    y_range=numCountries_12_7_22,
    width=800,
    height=2500,
    title = 'COVID-19 World''s Data - 12_7_22',
    x_axis_label = 'Number of deaths',
    tools="pan,box_select,zoom_in,zoom_out,reset"
    )

# Create Histogram
p23.hbar(
    y=dodge('Countries_12_7_22',0.0, range=p23.y_range),
    right='Total_deaths_pop_12_7_22',
    left=0,
    height=0.4,
    color='green',
    fill_alpha=0.9,
    source=source_12_7_22
    )

# Create Hover Tool
hover = HoverTool()
hover.tooltips = """
<div>
  <h3>@Countries_12_7_22</h3>
  <div><strong>Total Deaths: </strong>@Total_deaths_pop_12_7_22_str</div>
  <div><strong>Ranking: #</strong>@Total_deaths_pop_12_7_22_ranking</div>
</div>
"""
p23.add_tools(hover)

p24 = figure(
    y_range=numCountries_12_7_22,
    width=800,
    height=2500,
    title = 'COVID-19 World''s Data - 12_7_22',
    x_axis_label = 'Number of deaths',
    tools="pan,box_select,zoom_in,zoom_out,reset"
    )

# Create Histogram
p24.hbar(
    y=dodge('Countries_12_7_22',0.0, range=p24.y_range),
    right='New_deaths_pop_12_7_22',
    left=0,
    height=0.4,
    color='orange',
    fill_alpha=0.9,
    source=source_12_7_22
    )

# Create Hover Tool
hover = HoverTool()
hover.tooltips = """
<div>
  <h3>@Countries_12_7_22</h3>
  <div><strong>Total Deaths: </strong>@New_deaths_pop_12_7_22_str</div>
  <div><strong>Ranking: #</strong>@New_deaths_pop_12_7_22_ranking</div>
</div>
"""
p24.add_tools(hover)

# Make Table
columns6= [
        TableColumn(field='Countries_12_7_22', title="Countries"),
        TableColumn(field="Total_deaths_pop_12_7_22", title="Total Deaths"),
        TableColumn(field="New_deaths_pop_12_7_22", title="New Deaths"),
        TableColumn(field="Total_deaths_pop_12_7_22", title="Total Deaths by Population"),
        TableColumn(field="New_deaths_pop_12_7_22", title="New Deaths by Population")
    ]
data_table6 = DataTable(source=source_12_7_22, columns=columns6, width=800, height=3000)



# CREATE FIGURE FOR 12_8_22
p25 = figure(
    y_range=numCountries_12_8_22,
    width=800,
    height=2500,
    title = 'COVID-19 World''s Data - 12_8_22',
    x_axis_label = 'Number of deaths',
    tools="pan,box_select,zoom_in,zoom_out,reset"
    )

# Create Histogram
p25.hbar(
    y=dodge('Countries_12_8_22',0.0, range=p25.y_range),
    right='Total_deaths_12_8_22',
    left=0,
    height=0.4,
    color='red',
    fill_alpha=0.9,
    source=source_12_8_22
    )

# Create Hover Tool
hover = HoverTool()
hover.tooltips = """
<div>
  <h3>@Countries_12_8_22</h3>
  <div><strong>Total Deaths: </strong>@Total_deaths_12_8_22_str</div>
  <div><strong>Ranking: #</strong>@Total_deaths_12_8_22_ranking</div>
</div>
"""
p25.add_tools(hover)


p26 = figure(
    y_range=numCountries_12_8_22,
    width=800,
    height=2500,
    title = 'COVID-19 World''s Data - 12_8_22',
    x_axis_label = 'Number of deaths',
    tools="pan,box_select,zoom_in,zoom_out,reset"
    )

# Create Histogram
p26.hbar(
    y=dodge('Countries_12_8_22',0.0, range=p26.y_range),
    right='New_deaths_12_8_22',
    left=0,
    height=0.4,
    color='blue',
    fill_alpha=0.9,
    source=source_12_8_22
    )

# Create Hover Tool
hover = HoverTool()
hover.tooltips = """
<div>
  <h3>@Countries_12_8_22</h3>
  <div><strong>New Deaths: </strong>@New_deaths_12_8_22_str</div>
  <div><strong>Ranking: #</strong>@New_deaths_12_8_22_ranking</div>
</div>
"""
p26.add_tools(hover)

p27 = figure(
    y_range=numCountries_12_8_22,
    width=800,
    height=2500,
    title = 'COVID-19 World''s Data - 12_8_22',
    x_axis_label = 'Number of deaths',
    tools="pan,box_select,zoom_in,zoom_out,reset"
    )

# Create Histogram
p27.hbar(
    y=dodge('Countries_12_8_22',0.0, range=p27.y_range),
    right='Total_deaths_pop_12_8_22',
    left=0,
    height=0.4,
    color='green',
    fill_alpha=0.9,
    source=source_12_8_22
    )

# Create Hover Tool
hover = HoverTool()
hover.tooltips = """
<div>
  <h3>@Countries_12_8_22</h3>
  <div><strong>Total Deaths: </strong>@Total_deaths_pop_12_8_22_str</div>
  <div><strong>Ranking: #</strong>@Total_deaths_pop_12_8_22_ranking</div>
</div>
"""
p27.add_tools(hover)

p28 = figure(
    y_range=numCountries_12_8_22,
    width=800,
    height=2500,
    title = 'COVID-19 World''s Data - 12_8_22',
    x_axis_label = 'Number of deaths',
    tools="pan,box_select,zoom_in,zoom_out,reset"
    )

# Create Histogram
p28.hbar(
    y=dodge('Countries_12_8_22',0.0, range=p28.y_range),
    right='New_deaths_pop_12_8_22',
    left=0,
    height=0.4,
    color='orange',
    fill_alpha=0.9,
    source=source_12_8_22
    )

# Create Hover Tool
hover = HoverTool()
hover.tooltips = """
<div>
  <h3>@Countries_12_8_22</h3>
  <div><strong>Total Deaths: </strong>@New_deaths_pop_12_8_22_str</div>
  <div><strong>Ranking: #</strong>@New_deaths_pop_12_8_22_ranking</div>
</div>
"""
p28.add_tools(hover)

# Make Table
columns7 = [
        TableColumn(field='Countries_12_8_22', title="Countries"),
        TableColumn(field="Total_deaths_12_8_22", title="Total Deaths"),
        TableColumn(field="New_deaths_12_8_22", title="New Deaths"),
        TableColumn(field="Total_deaths_pop_12_8_22", title="Total Deaths by Population"),
        TableColumn(field="New_deaths_pop_12_8_22", title="New Deaths by Population")
    ]
data_table7 = DataTable(source=source_12_8_22, columns=columns7, width=800, height=3000)


#12_4_22 TABS
fig17 = row(p17, data_table5)
tab17 = TabPanel(child=fig17, title="Total Deaths")


fig18 = row(p18, data_table5)
tab18 = TabPanel(child=fig18, title="New Deaths")


fig19 = row(p19, data_table5)
tab19 = TabPanel(child=fig19, title="Total Deaths by Population")

fig20 = row(p20, data_table5)
tab20 = TabPanel(child=fig20, title="New Deaths by Population")


#12_7_22 TABS
fig21 = row(p21, data_table6)
tab21 = TabPanel(child=fig21, title="Total Deaths")


fig22 = row(p22, data_table6)
tab22 = TabPanel(child=fig22, title="New Deaths")


fig23 = row(p23, data_table6)
tab23 = TabPanel(child=fig23, title="Total Deaths by Population")

fig24 = row(p24, data_table6)
tab24 = TabPanel(child=fig24, title="New Deaths by Population")


#12_8_22 TABS
fig25 = row(p25, data_table7)
tab25 = TabPanel(child=fig25, title="Total Deaths")


fig26 = row(p26, data_table7)
tab26 = TabPanel(child=fig26, title="New Deaths")


fig27 = row(p27, data_table7)
tab27 = TabPanel(child=fig27, title="Total Deaths by Population")

fig28 = row(p28, data_table7)
tab28 = TabPanel(child=fig28, title="New Deaths by Population")




tabs5 = Tabs(tabs=[ tab17, tab18, tab19, tab20])
tabs6 = Tabs(tabs=[ tab21, tab22, tab23, tab24])
tabs7 = Tabs(tabs=[ tab25, tab26, tab27, tab28])


MainTab5 = TabPanel(child=tabs5, title= "Data of 12-4-22")
MainTab6 = TabPanel(child=tabs6, title= "Data of 12-7-22")
MainTab7 = TabPanel(child=tabs7, title= "Data of 12-8-22")



# ===================================SAVED DATA========================================== FINISH



# GET DATA
data_today,data_yesterday,data_yesterday2 = Scrape3Days()




# TODAY SECTION
# Get TOTAL today's deaths
total_deaths_today = list(data_today['Cumulative Deaths'])
for i in range(len(total_deaths_today)):
  total_deaths_today[i] = int(re.sub(",","",total_deaths_today[i]))
total_deaths_today_sort_index = np.argsort(total_deaths_today)
total_deaths_today_ranks = [0]*len(total_deaths_today)
for i in range(1,len(total_deaths_today)):
  total_deaths_today_ranks[total_deaths_today_sort_index[-i]] = i

# Get NEW today's deaths
new_deaths_today = list(data_today['Daily Deaths'])
for i in range(len(new_deaths_today)):
  new_deaths_today[i] = int(re.sub(",","",new_deaths_today[i]))
new_deaths_today_sort_index = np.argsort(new_deaths_today)
new_deaths_today_ranks = [0]*len(new_deaths_today)
for i in range(1,len(new_deaths_today)):
  new_deaths_today_ranks[new_deaths_today_sort_index[-i]] = i
  
# Get TOTAL POP today's deaths
total_deaths_pop_today = list(data_today['Population Cumulative Deaths'])
for i in range(len(total_deaths_pop_today)):
  total_deaths_pop_today[i] = int(re.sub(",","",total_deaths_pop_today[i]))
total_deaths_pop_today_sort_index = np.argsort(total_deaths_pop_today)
total_deaths_pop_today_ranks = [0]*len(total_deaths_pop_today)
for i in range(1,len(total_deaths_pop_today)):
  total_deaths_pop_today_ranks[total_deaths_pop_today_sort_index[-i]] = i

# Get NEW POP today's deaths
new_deaths_pop_today = list(data_today['Population Daily Deaths'])
#for i in range(len(new_deaths_pop_today)):
#  new_deaths_pop_today[i] = int(re.sub(",","",new_deaths_pop_today[i]))
new_deaths_pop_today_sort_index = np.argsort(new_deaths_pop_today)
new_deaths_pop_today_ranks = [0]*len(new_deaths_pop_today)
for i in range(1,len(new_deaths_pop_today)):
  new_deaths_pop_today_ranks[new_deaths_pop_today_sort_index[-i]] = i
  
  


# YESTERDAY SECTION
# Get TOTAL yesterday's deaths
total_deaths_yesterday = list(data_yesterday['Cumulative Deaths yesterday'])
for i in range(len(total_deaths_yesterday)):
  total_deaths_yesterday[i] = int(re.sub(",","",total_deaths_yesterday[i]))
total_deaths_yesterday_sort_index = np.argsort(total_deaths_yesterday)
total_deaths_yesterday_ranks = [0]*len(total_deaths_yesterday)
for i in range(1,len(total_deaths_yesterday)):
  total_deaths_yesterday_ranks[total_deaths_yesterday_sort_index[-i]] = i
  
# Get NEW yesterday's deaths
new_deaths_yesterday = list(data_yesterday['Daily Deaths yesterday'])
for i in range(len(new_deaths_yesterday)):
  new_deaths_yesterday[i] = int(re.sub(",","",new_deaths_yesterday[i]))
new_deaths_yesterday_sort_index = np.argsort(new_deaths_yesterday)
new_deaths_yesterday_ranks = [0]*len(new_deaths_yesterday)
for i in range(1,len(new_deaths_yesterday)):
  new_deaths_yesterday_ranks[new_deaths_yesterday_sort_index[-i]] = i

# Get TOTAL POP yesterday's deaths
total_deaths_pop_yesterday = list(data_yesterday['Population Cumulative Deaths yesterday'])
for i in range(len(total_deaths_pop_yesterday)):
  total_deaths_pop_yesterday[i] = int(re.sub(",","",total_deaths_pop_yesterday[i]))
total_deaths_pop_yesterday_sort_index = np.argsort(total_deaths_pop_yesterday)
total_deaths_pop_yesterday_ranks = [0]*len(total_deaths_pop_yesterday)
for i in range(1,len(total_deaths_pop_yesterday)):
  total_deaths_pop_yesterday_ranks[total_deaths_pop_yesterday_sort_index[-i]] = i

# Get NEW POP yesterday's deaths
new_deaths_pop_yesterday = list(data_yesterday['Population Daily Deaths yesterday'])
#for i in range(len(new_deaths_pop_yesterday)):
#  new_deaths_pop_yesterday[i] = int(re.sub(",","",new_deaths_pop_yesterday[i]))
new_deaths_pop_yesterday_sort_index = np.argsort(new_deaths_pop_yesterday)
new_deaths_pop_yesterday_ranks = [0]*len(new_deaths_pop_yesterday)
for i in range(1,len(new_deaths_pop_yesterday)):
  new_deaths_pop_yesterday_ranks[new_deaths_pop_yesterday_sort_index[-i]] = i




# 2 DAYS AGO SECTION (yesterday2)
# Get TOTAL yesterday2's deaths
total_deaths_yesterday2 = list(data_yesterday2['Cumulative Deaths yesterday2'])
for i in range(len(total_deaths_yesterday2)):
  total_deaths_yesterday2[i] = int(re.sub(",","",total_deaths_yesterday2[i]))
total_deaths_yesterday2_sort_index = np.argsort(total_deaths_yesterday2)
total_deaths_yesterday2_ranks = [0]*len(total_deaths_yesterday2)
for i in range(1,len(total_deaths_yesterday2)):
  total_deaths_yesterday2_ranks[total_deaths_yesterday2_sort_index[-i]] = i
  
# Get NEW yesterday2's deaths
new_deaths_yesterday2 = list(data_yesterday2['Daily Deaths yesterday2'])
for i in range(len(new_deaths_yesterday2)):
  new_deaths_yesterday2[i] = int(re.sub(",","",new_deaths_yesterday2[i]))
new_deaths_yesterday2_sort_index = np.argsort(new_deaths_yesterday2)
new_deaths_yesterday2_ranks = [0]*len(new_deaths_yesterday2)
for i in range(1,len(new_deaths_yesterday2)):
  new_deaths_yesterday2_ranks[new_deaths_yesterday2_sort_index[-i]] = i
    
# Get TOTAL POP yesterday2's deaths
total_deaths_pop_yesterday2 = list(data_yesterday2['Population Cumulative Deaths yesterday2'])
for i in range(len(total_deaths_pop_yesterday2)):
  total_deaths_pop_yesterday2[i] = int(re.sub(",","",total_deaths_pop_yesterday2[i]))
total_deaths_pop_yesterday2_sort_index = np.argsort(total_deaths_pop_yesterday2)
total_deaths_pop_yesterday2_ranks = [0]*len(total_deaths_pop_yesterday2)
for i in range(1,len(total_deaths_pop_yesterday2)):
  total_deaths_pop_yesterday2_ranks[total_deaths_pop_yesterday2_sort_index[-i]] = i

# Get NEW POP yesterday2's deaths
new_deaths_pop_yesterday2 = list(data_yesterday2['Population Daily Deaths yesterday2'])
#for i in range(len(new_deaths_pop_yesterday2)):
#  new_deaths_pop_yesterday2[i] = int(re.sub(",","",new_deaths_pop_yesterday2[i]))
new_deaths_pop_yesterday2_sort_index = np.argsort(new_deaths_pop_yesterday2)
new_deaths_pop_yesterday2_ranks = [0]*len(new_deaths_pop_yesterday2)
for i in range(1,len(new_deaths_pop_yesterday2)):
  new_deaths_pop_yesterday2_ranks[new_deaths_pop_yesterday2_sort_index[-i]] = i




# MAKE DICTIONARY FOR TODAY'S DEATHS
data_today = {'Countries_today': np.array(data_today['Country']),
        'Total_deaths_today': total_deaths_today,
        'Total_deaths_today_ranking': total_deaths_today_ranks,
        'Total_deaths_today_str': data_today["Cumulative Deaths"],
        'New_deaths_today': new_deaths_today,
        'New_deaths_today_ranking': new_deaths_today_ranks,
        'New_deaths_today_str': data_today["Daily Deaths"],
        'Total_deaths_pop_today': total_deaths_pop_today,
        'Total_deaths_pop_today_ranking': total_deaths_pop_today_ranks,
        'Total_deaths_pop_today_str': data_today["Population Cumulative Deaths"],
        'New_deaths_pop_today': new_deaths_pop_today,
        'New_deaths_pop_today_ranking': new_deaths_pop_today_ranks,
        'New_deaths_pop_today_str': data_today["Population Daily Deaths"]}
source_today = ColumnDataSource(data_today)
numCountries_today = np.flip(source_today.data['Countries_today'].tolist())




# MAKE DICTIONARY FOR YESTERDAY' DEATHS
data_yesterday = {'Countries_yesterday': np.array(data_yesterday['Country yesterday']),
        'Total_deaths_yesterday': total_deaths_yesterday,
        'Total_deaths_yesterday_ranking': total_deaths_yesterday_ranks,
        'Total_deaths_yesterday_str': data_yesterday["Cumulative Deaths yesterday"],
        'New_deaths_yesterday': new_deaths_yesterday,
        'New_deaths_yesterday_ranking': new_deaths_yesterday_ranks,
        'New_deaths_yesterday_str': data_yesterday["Daily Deaths yesterday"],
        'Total_deaths_pop_yesterday': total_deaths_pop_yesterday,
        'Total_deaths_pop_yesterday_ranking': total_deaths_pop_yesterday_ranks,
        'Total_deaths_pop_yesterday_str': data_yesterday["Population Cumulative Deaths yesterday"],
        'New_deaths_pop_yesterday': new_deaths_pop_yesterday,
        'New_deaths_pop_yesterday_ranking': new_deaths_pop_yesterday_ranks,
        'New_deaths_pop_yesterday_str': data_yesterday["Population Daily Deaths yesterday"]}
source_yesterday = ColumnDataSource(data_yesterday)
numCountries_yesterday = np.flip(source_yesterday.data['Countries_yesterday'].tolist())




# MAKE DICTIONARY FOR 2 DAYS AGO DEATHS
data_yesterday2 = {'Countries_yesterday2': np.array(data_yesterday2['Country yesterday2']),
        'Total_deaths_yesterday2': total_deaths_yesterday2,
        'Total_deaths_yesterday2_ranking': total_deaths_yesterday2_ranks,
        'Total_deaths_yesterday2_str': data_yesterday2["Cumulative Deaths yesterday2"],
        'New_deaths_yesterday2': new_deaths_yesterday2,
        'New_deaths_yesterday2_ranking': new_deaths_yesterday2_ranks,
        'New_deaths_yesterday2_str': data_yesterday2["Daily Deaths yesterday2"],
        'Total_deaths_pop_yesterday2': total_deaths_pop_yesterday2,
        'Total_deaths_pop_yesterday2_ranking': total_deaths_pop_yesterday2_ranks,
        'Total_deaths_pop_yesterday2_str': data_yesterday2["Population Cumulative Deaths yesterday2"],
        'New_deaths_pop_yesterday2': new_deaths_pop_yesterday2,
        'New_deaths_pop_yesterday2_ranking': new_deaths_pop_yesterday2_ranks,
        'New_deaths_pop_yesterday2_str': data_yesterday2["Population Daily Deaths yesterday2"]}
source_yesterday2 = ColumnDataSource(data_yesterday2)
numCountries_yesterday2 = np.flip(source_yesterday2.data['Countries_yesterday2'].tolist())





# CREATE FIGURE FOR TODAY
p1 = figure(
    y_range=numCountries_today,
    width=800,
    height=2500,
    title = 'COVID-19 World''s Data - Today',
    x_axis_label = 'Number of deaths',
    tools="pan,box_select,zoom_in,zoom_out,reset"
    )

# Create Histogram
p1.hbar(
    y=dodge('Countries_today',0.0, range=p1.y_range),
    right='Total_deaths_today',
    left=0,
    height=0.4,
    color='red',
    fill_alpha=0.9,
    source=source_today
    )

# Create Hover Tool
hover = HoverTool()
hover.tooltips = """
<div>
  <h3>@Countries_today</h3>
  <div><strong>Total Deaths: </strong>@Total_deaths_today_str</div>
  <div><strong>Ranking: #</strong>@Total_deaths_today_ranking</div>
</div>
"""
p1.add_tools(hover)


p2 = figure(
    y_range=numCountries_today,
    width=800,
    height=2500,
    title = 'COVID-19 World''s Data - Today',
    x_axis_label = 'Number of deaths',
    tools="pan,box_select,zoom_in,zoom_out,reset"
    )

# Create Histogram
p2.hbar(
    y=dodge('Countries_today',0.0, range=p2.y_range),
    right='New_deaths_today',
    left=0,
    height=0.4,
    color='blue',
    fill_alpha=0.9,
    source=source_today
    )

# Create Hover Tool
hover = HoverTool()
hover.tooltips = """
<div>
  <h3>@Countries_today</h3>
  <div><strong>New Deaths: </strong>@New_deaths_today_str</div>
  <div><strong>Ranking: #</strong>@New_deaths_today_ranking</div>
</div>
"""
p2.add_tools(hover)

p3 = figure(
    y_range=numCountries_today,
    width=800,
    height=2500,
    title = 'COVID-19 World''s Data - Today',
    x_axis_label = 'Number of deaths',
    tools="pan,box_select,zoom_in,zoom_out,reset"
    )

# Create Histogram
p3.hbar(
    y=dodge('Countries_today',0.0, range=p3.y_range),
    right='Total_deaths_pop_today',
    left=0,
    height=0.4,
    color='green',
    fill_alpha=0.9,
    source=source_today
    )

# Create Hover Tool
hover = HoverTool()
hover.tooltips = """
<div>
  <h3>@Countries_today</h3>
  <div><strong>Total Deaths: </strong>@Total_deaths_pop_today_str</div>
  <div><strong>Ranking: #</strong>@Total_deaths_pop_today_ranking</div>
</div>
"""
p3.add_tools(hover)

p4 = figure(
    y_range=numCountries_today,
    width=800,
    height=2500,
    title = 'COVID-19 World''s Data - Today',
    x_axis_label = 'Number of deaths',
    tools="pan,box_select,zoom_in,zoom_out,reset"
    )

# Create Histogram
p4.hbar(
    y=dodge('Countries_today',0.0, range=p4.y_range),
    right='New_deaths_pop_today',
    left=0,
    height=0.4,
    color='orange',
    fill_alpha=0.9,
    source=source_today
    )

# Create Hover Tool
hover = HoverTool()
hover.tooltips = """
<div>
  <h3>@Countries_today</h3>
  <div><strong>Total Deaths: </strong>@New_deaths_pop_today_str</div>
  <div><strong>Ranking: #</strong>@New_deaths_pop_today_ranking</div>
</div>
"""
p4.add_tools(hover)

# Make Table
columns1 = [
        TableColumn(field='Countries_today', title="Countries"),
        TableColumn(field="Total_deaths_today", title="Total Deaths"),
        TableColumn(field="New_deaths_today", title="New Deaths"),
        TableColumn(field="Total_deaths_pop_today", title="Total Deaths by Population"),
        TableColumn(field="New_deaths_pop_today", title="New Deaths by Population")
    ]
data_table1 = DataTable(source=source_today, columns=columns1, width=800, height=3000)




# CREATE FIGURE FOR YESTERDAY
p5 = figure(
    y_range=numCountries_yesterday,
    width=800,
    height=2500,
    title = 'COVID-19 World''s Data - Yesterday',
    x_axis_label = 'Number of deaths',
    tools="pan,box_select,zoom_in,zoom_out,reset"
    )


# Create Histogram
p5.hbar(
    y=dodge('Countries_yesterday',0.0, range=p5.y_range),
    right='Total_deaths_yesterday',
    left=0,
    height=0.4,
    color='red',
    fill_alpha=0.9,
    source=source_yesterday
    )

# Create Hover Tool
hover = HoverTool()
hover.tooltips = """
<div>
  <h3>@Countries_yesterday</h3>
  <div><strong>Total Deaths: </strong>@Total_deaths_yesterday_str</div>
  <div><strong>Ranking: #</strong>@Total_deaths_yesterday_ranking</div>
</div>
"""
p5.add_tools(hover)

p6 = figure(
    y_range=numCountries_yesterday,
    width=800,
    height=2500,
    title = 'COVID-19 World''s Data - Yesterday',
    x_axis_label = 'Number of deaths',
    tools="pan,box_select,zoom_in,zoom_out,reset"
    )

# Create Histogram
p6.hbar(
    y=dodge('Countries_yesterday',0.0, range=p6.y_range),
    right='New_deaths_yesterday',
    left=0,
    height=0.4,
    color='blue',
    fill_alpha=0.9,
    source=source_yesterday
    )

# Create Hover Tool
hover = HoverTool()
hover.tooltips = """
<div>
  <h3>@Countries_yesterday</h3>
  <div><strong>New Deaths: </strong>@New_deaths_yesterday_str</div>
  <div><strong>Ranking: #</strong>@New_deaths_yesterday_ranking</div>
</div>
"""
p6.add_tools(hover)

p7 = figure(
    y_range=numCountries_yesterday,
    width=800,
    height=2500,
    title = 'COVID-19 World''s Data - Yesterday',
    x_axis_label = 'Number of deaths',
    tools="pan,box_select,zoom_in,zoom_out,reset"
    )

# Create Histogram
p7.hbar(
    y=dodge('Countries_yesterday',0.0, range=p7.y_range),
    right='Total_deaths_pop_yesterday',
    left=0,
    height=0.4,
    color='green',
    fill_alpha=0.9,
    source=source_yesterday
    )

# Create Hover Tool
hover = HoverTool()
hover.tooltips = """
<div>
  <h3>@Countries_yesterday</h3>
  <div><strong>Total Deaths: </strong>@Total_deaths_pop_yesterday_str</div>
  <div><strong>Ranking: #</strong>@Total_deaths_pop_yesterday_ranking</div>
</div>
"""
p7.add_tools(hover)

p8 = figure(
    y_range=numCountries_yesterday,
    width=800,
    height=2500,
    title = 'COVID-19 World''s Data - Yesterday',
    x_axis_label = 'Number of deaths',
    tools="pan,box_select,zoom_in,zoom_out,reset"
    )

# Create Histogram
p8.hbar(
    y=dodge('Countries_yesterday',0.0, range=p8.y_range),
    right='New_deaths_pop_yesterday',
    left=0,
    height=0.4,
    color='orange',
    fill_alpha=0.9,
    source=source_yesterday
    )

# Create Hover Tool
hover = HoverTool()
hover.tooltips = """
<div>
  <h3>@Countries_yesterday</h3>
  <div><strong>Total Deaths: </strong>@New_deaths_pop_yesterday_str</div>
  <div><strong>Ranking: #</strong>@New_deaths_pop_yesterday_ranking</div>
</div>
"""
p8.add_tools(hover)

# Make Table
columns2 = [
        TableColumn(field='Countries_yesterday', title="Countries"),
        TableColumn(field="Total_deaths_yesterday", title="Total Deaths"),
        TableColumn(field="New_deaths_yesterday", title="New Deaths"),
        TableColumn(field="Total_deaths_pop_yesterday", title="Total Deaths by Population"),
        TableColumn(field="New_deaths_pop_yesterday", title="New Deaths by Population")
    ]
data_table2 = DataTable(source=source_yesterday, columns=columns2, width=800, height=3000)




# CREATE FIGURE FOR 2 DAYS AGO
p9 = figure(
    y_range=numCountries_yesterday2,
    width=800,
    height=2500,
    title = 'COVID-19 World''s Data - 2 Days Ago',
    x_axis_label = 'Number of deaths',
    tools="pan,box_select,zoom_in,zoom_out,reset"
    )


# Create Histogram
p9.hbar(
    y=dodge('Countries_yesterday2',0.0, range=p9.y_range),
    right='Total_deaths_yesterday2',
    left=0,
    height=0.4,
    color='red',
    fill_alpha=0.9,
    source=source_yesterday2
    )

# Create Hover Tool
hover = HoverTool()
hover.tooltips = """
<div>
  <h3>@Countries_yesterday2</h3>
  <div><strong>Total Deaths: </strong>@Total_deaths_yesterday2_str</div>
  <div><strong>Ranking: #</strong>@Total_deaths_yesterday2_ranking</div>
</div>
"""
p9.add_tools(hover)

p10 = figure(
    y_range=numCountries_yesterday2,
    width=800,
    height=2500,
    title = 'COVID-19 World''s Data - 2 Days Ago',
    x_axis_label = 'Number of deaths',
    tools="pan,box_select,zoom_in,zoom_out,reset"
    )

# Create Histogram
p10.hbar(
    y=dodge('Countries_yesterday2',0.0, range=p10.y_range),
    right='New_deaths_yesterday2',
    left=0,
    height=0.4,
    color='blue',
    fill_alpha=0.9,
    source=source_yesterday2
    )

# Create Hover Tool
hover = HoverTool()
hover.tooltips = """
<div>
  <h3>@Countries_yesterday2</h3>
  <div><strong>New Deaths: </strong>@New_deaths_yesterday2_str</div>
  <div><strong>Ranking: #</strong>@New_deaths_yesterday2_ranking</div>
</div>
"""
p10.add_tools(hover)

p11 = figure(
    y_range=numCountries_yesterday2,
    width=800,
    height=2500,
    title = 'COVID-19 World''s Data - 2 Days Ago',
    x_axis_label = 'Number of deaths',
    tools="pan,box_select,zoom_in,zoom_out,reset"
    )

# Create Histogram
p11.hbar(
    y=dodge('Countries_yesterday2',0.0, range=p11.y_range),
    right='Total_deaths_pop_yesterday2',
    left=0,
    height=0.4,
    color='green',
    fill_alpha=0.9,
    source=source_yesterday2
    )

# Create Hover Tool
hover = HoverTool()
hover.tooltips = """
<div>
  <h3>@Countries_yesterday2</h3>
  <div><strong>Total Deaths: </strong>@Total_deaths_pop_yesterday2_str</div>
  <div><strong>Ranking: #</strong>@Total_deaths_pop_yesterday2_ranking</div>
</div>
"""
p11.add_tools(hover)

p12 = figure(
    y_range=numCountries_yesterday2,
    width=800,
    height=2500,
    title = 'COVID-19 World''s Data - 2 Days Ago',
    x_axis_label = 'Number of deaths',
    tools="pan,box_select,zoom_in,zoom_out,reset"
    )

# Create Histogram
p12.hbar(
    y=dodge('Countries_yesterday2',0.0, range=p12.y_range),
    right='New_deaths_pop_yesterday2',
    left=0,
    height=0.4,
    color='orange',
    fill_alpha=0.9,
    source=source_yesterday2
    )

# Create Hover Tool
hover = HoverTool()
hover.tooltips = """
<div>
  <h3>@Countries_yesterday2</h3>
  <div><strong>Total Deaths: </strong>@New_deaths_pop_yesterday2_str</div>
  <div><strong>Ranking: #</strong>@New_deaths_pop_yesterday2_ranking</div>
</div>
"""
p12.add_tools(hover)

# Make Table
columns3= [
        TableColumn(field='Countries_yesterday2', title="Countries"),
        TableColumn(field="Total_deaths_pop_yesterday2", title="Total Deaths"),
        TableColumn(field="New_deaths_pop_yesterday2", title="New Deaths"),
        TableColumn(field="Total_deaths_pop_yesterday2", title="Total Deaths by Population"),
        TableColumn(field="New_deaths_pop_yesterday2", title="New Deaths by Population")
    ]
data_table3 = DataTable(source=source_yesterday2, columns=columns3, width=800, height=3000)




#TODAY TABS
fig1 = row(p1, data_table1)
tab1 = TabPanel(child=fig1, title="Total Deaths")


fig2 = row(p2, data_table1)
tab2 = TabPanel(child=fig2, title="New Deaths")


fig3 = row(p3, data_table1)
tab3 = TabPanel(child=fig3, title="Total Deaths by Population")

fig4 = row(p4, data_table1)
tab4 = TabPanel(child=fig4, title="New Deaths by Population")

#Yesterday tabs
fig5 = row(p5, data_table2)
tab5 = TabPanel(child=fig5, title="Total Deaths")


fig6 = row(p6, data_table2)
tab6 = TabPanel(child=fig6, title="New Deaths")


fig7 = row(p7, data_table2)
tab7 = TabPanel(child=fig7, title="Total Deaths by Population")

fig8 = row(p8, data_table2)
tab8 = TabPanel(child=fig8, title="New Deaths by Population")


#2 Days ago tabs
fig9 = row(p9, data_table3)
tab9 = TabPanel(child=fig9, title="Total Deaths")


fig10 = row(p10, data_table3)
tab10 = TabPanel(child=fig10, title="New Deaths")


fig11 = row(p11, data_table3)
tab11 = TabPanel(child=fig11, title="Total Deaths by Population")

fig12 = row(p12, data_table3)
tab12 = TabPanel(child=fig12, title="New Deaths by Population")



#SUB TABS
tabs1 = Tabs(tabs=[ tab1, tab2, tab3, tab4])
tabs2 = Tabs(tabs=[ tab5, tab6, tab7, tab8])
tabs3 = Tabs(tabs=[ tab9, tab10, tab11, tab12])




#MAIN TABS
MainTab1 = TabPanel(child=tabs1, title= "Today")
MainTab2 = TabPanel(child=tabs2, title= "Yesterday")
MainTab3 = TabPanel(child=tabs3, title= "2 Days Ago")




#FINAL TAB
finaltab = Tabs(tabs=[MainTab1,MainTab2,MainTab3,MainTab5,MainTab6,MainTab7])

show(finaltab)



















