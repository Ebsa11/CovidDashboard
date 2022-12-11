# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 13:23:32 2022

@author: Ebsa Eshete, Bret Mecham, Andres Vizcarra

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10-Fqz5OJdE3rrK9n8E8zbJdAmGfYUdm-
"""

import numpy as np
import re
from bokeh.plotting import figure
from WOMScrapeFunc import Scrape3Days
from bokeh.layouts import row
from bokeh.models import ColumnDataSource, HoverTool,DataTable, TableColumn
from bokeh.plotting import show, output_file



from bokeh.models.widgets import Panel, Tabs
from bokeh.transform import dodge
from bokeh.io import output_notebook  # added
from bokeh.resources import INLINE    # added
output_notebook(INLINE)               # added



# Uncomment to save output html to a file
# output_file(filename="COVID_results.html", title="Static HTML file")

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
        'New_deaths_pop_yesterday2_str': data_yesterday2["Population Daily Deaths yesterday2"]}
source_yesterday2 = ColumnDataSource(data_yesterday2)
numCountries_yesterday2 = np.flip(source_yesterday2.data['Countries_yesterday2'].tolist())





# CREATE FIGURE FOR TODAY
p1 = figure(
    y_range=numCountries_today,
    plot_width=800,
    plot_height=2500,
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
    plot_width=800,
    plot_height=2500,
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
    plot_width=800,
    plot_height=2500,
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

# Make Table
columns1 = [
        TableColumn(field='Countries_today', title="Countries"),
        TableColumn(field="Total_deaths_today_str", title="Total Deaths"),
        TableColumn(field="New_deaths_today_str", title="New Deaths"),
        TableColumn(field="Total_deaths_pop_today_str", title="Total Deaths by Population"),
        TableColumn(field="New_deaths_pop_today_str", title="New Deaths by Population")
    ]
data_table1 = DataTable(source=source_today, columns=columns1, width=800, height=3000)




# CREATE FIGURE FOR YESTERDAY
p4 = figure(
    y_range=numCountries_yesterday,
    plot_width=800,
    plot_height=2500,
    title = 'COVID-19 World''s Data - Yesterday',
    x_axis_label = 'Number of deaths',
    tools="pan,box_select,zoom_in,zoom_out,reset"
    )


# Create Histogram
p4.hbar(
    y=dodge('Countries_yesterday',0.0, range=p4.y_range),
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
p4.add_tools(hover)

p5 = figure(
    y_range=numCountries_yesterday,
    plot_width=800,
    plot_height=2500,
    title = 'COVID-19 World''s Data - Yesterday',
    x_axis_label = 'Number of deaths',
    tools="pan,box_select,zoom_in,zoom_out,reset"
    )

# Create Histogram
p5.hbar(
    y=dodge('Countries_yesterday',0.0, range=p5.y_range),
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
p5.add_tools(hover)

p6 = figure(
    y_range=numCountries_yesterday,
    plot_width=800,
    plot_height=2500,
    title = 'COVID-19 World''s Data - Yesterday',
    x_axis_label = 'Number of deaths',
    tools="pan,box_select,zoom_in,zoom_out,reset"
    )

# Create Histogram
p6.hbar(
    y=dodge('Countries_yesterday',0.0, range=p6.y_range),
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
p6.add_tools(hover)

# Make Table
columns2 = [
        TableColumn(field='Countries_yesterday', title="Countries"),
        TableColumn(field="Total_deaths_yesterday_str", title="Total Deaths"),
        TableColumn(field="New_deaths_yesterday_str", title="New Deaths"),
        TableColumn(field="Total_deaths_pop_yesterday_str", title="Total Deaths by Population"),
        TableColumn(field="New_deaths_pop_yesterday_str", title="New Deaths by Population")
    ]
data_table2 = DataTable(source=source_yesterday, columns=columns2, width=800, height=3000)




# CREATE FIGURE FOR 2 DAYS AGO
p7 = figure(
    y_range=numCountries_yesterday2,
    plot_width=800,
    plot_height=2500,
    title = 'COVID-19 World''s Data - 2 Days Ago',
    x_axis_label = 'Number of deaths',
    tools="pan,box_select,zoom_in,zoom_out,reset"
    )


# Create Histogram
p7.hbar(
    y=dodge('Countries_yesterday2',0.0, range=p7.y_range),
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
p7.add_tools(hover)

p8 = figure(
    y_range=numCountries_yesterday2,
    plot_width=800,
    plot_height=2500,
    title = 'COVID-19 World''s Data - 2 Days Ago',
    x_axis_label = 'Number of deaths',
    tools="pan,box_select,zoom_in,zoom_out,reset"
    )

# Create Histogram
p8.hbar(
    y=dodge('Countries_yesterday2',0.0, range=p8.y_range),
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
p8.add_tools(hover)

p9 = figure(
    y_range=numCountries_yesterday2,
    plot_width=800,
    plot_height=2500,
    title = 'COVID-19 World''s Data - 2 Days Ago',
    x_axis_label = 'Number of deaths',
    tools="pan,box_select,zoom_in,zoom_out,reset"
    )

# Create Histogram
p9.hbar(
    y=dodge('Countries_yesterday2',0.0, range=p9.y_range),
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
p9.add_tools(hover)

# Make Table
columns3= [
        TableColumn(field='Countries_yesterday2', title="Countries"),
        TableColumn(field="Total_deaths_pop_yesterday2_str", title="Total Deaths"),
        TableColumn(field="New_deaths_pop_yesterday2_str", title="New Deaths"),
        TableColumn(field="Total_deaths_pop_yesterday2_str", title="Total Deaths by Population"),
        TableColumn(field="New_deaths_pop_yesterday2_str", title="New Deaths by Population")
    ]
data_table3 = DataTable(source=source_yesterday2, columns=columns3, width=800, height=3000)




#TODAY TABS
fig1 = row(p1, data_table1)
tab1 = Panel(child=fig1, title="Total Deaths")


fig2 = row(p2, data_table1)
tab2 = Panel(child=fig2, title="New Deaths")


fig3 = row(p3, data_table1)
tab3 = Panel(child=fig3, title="Total Deaths Population")

#Yesterday tabs
fig4 = row(p4, data_table2)
tab4 = Panel(child=fig4, title="Total Deaths")


fig5 = row(p5, data_table2)
tab5 = Panel(child=fig5, title="New Deaths")


fig6 = row(p6, data_table2)
tab6 = Panel(child=fig6, title="Total Deaths Population")


#2 Days ago tabs
fig7 = row(p7, data_table3)
tab7 = Panel(child=fig7, title="Total Deaths")


fig8 = row(p8, data_table3)
tab8 = Panel(child=fig8, title="New Deaths")


fig9 = row(p9, data_table3)
tab9 = Panel(child=fig9, title="Total Deaths Population")



#SUB TABS
tabs1 = Tabs(tabs=[ tab1, tab2, tab3])
tabs2 = Tabs(tabs=[ tab4, tab5, tab6])
tabs3 = Tabs(tabs=[ tab7, tab8, tab9])



#MAIN TABS
MainTab1 = Panel(child=tabs1, title= "Today")
MainTab2 = Panel(child=tabs2, title= "Yesterday")
MainTab3 = Panel(child=tabs3, title= "2 Days Ago")



#FINAL TAB
finaltab = Tabs(tabs=[MainTab1,MainTab2,MainTab3])

show(finaltab)


















