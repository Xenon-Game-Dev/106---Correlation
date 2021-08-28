import plotly_express as px
import csv

with open('./data/cups of coffee vs hours of sleep.csv') as file:
    df = csv.DictReader(file)
    fig = px.scatter(df, x = "Coffee in ml" ,y = 'sleep in hours', color = 'week')
    fig.show()
