import chart_studio.plotly as py
import plotly.graph_objs as go 
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import pandas as pd
import requests
import json
import csv


url = "https://covid-19-tracking.p.rapidapi.com/v1"
headers = {
    "x-rapidapi-key": "33f91e67a2msh3bcc56a8c22fee9p12a016jsnb9a9f0b837c1",
    "x-rapidapi-host": "covid-19-tracking.p.rapidapi.com",
}
response = requests.request("GET", url, headers=headers)
print(response.text)
a = response.json()

toCSV = a

keys = toCSV[0].keys()

with open("Total_deaths.csv", "w", newline="") as output_file:

    dict_writer = csv.DictWriter(output_file, keys)

    dict_writer.writeheader()

    dict_writer.writerows(toCSV)

df=pd.read_csv('Total_deaths.csv', encoding='latin-1')
print(df)

df.drop(0,inplace=True)
for i in range(220,232):
    df.drop(i,inplace=True)
print(df)


j=[]
for b in df['Total Deaths_text']:
    b=float(b.replace(',', ''))
    j+=[b]

df['TotalDeath']=j


datas = dict(
        type = 'choropleth',
        locations = df['Country_text'],
        locationmode='country names',
        z = df['TotalDeath'],
        text = df['Country_text'],
        colorscale = 'viridis_r',
        colorbar = {'title' : 'Total Deaths'},
      )

layouts = dict(
    title = 'Total Deaths',
    geo = dict(
        showframe = False,
        projection = {'type':'orthographic'}
    )
)

choromaps = go.Figure(data = [datas],layout = layouts)
iplot(choromaps)


