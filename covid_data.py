import pandas as pd
import plotly.express as px

df = pd.read_csv("C:/Users/HP/OneDrive/Documents/Python (WhiteHatJr)/.py/csv files/covid_data.csv")

print(df)

figure = px.scatter(df, x = "date", y = "cases", color="country", title = "No. of cases in a country on a specific Date", size = "cases", size_max = 25)

figure.show()