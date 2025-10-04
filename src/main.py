import pandas 
import datetime
import matplotlib.pyplot as plt
import generatedata as gd
from maths import statisticalanalysis as sa
from graphs import graphs

start_date = pandas.Timestamp('2022-06-01')
end_date = pandas.Timestamp('2023-08-31')

def open_file(input_file):
    # open and read the csv file created in generatedata.py
    try:
        with open(input_file, 'r') as file:
            df = pandas.read_csv(file, parse_dates=['date'])
            return df
    except FileNotFoundError:
        print("Error : The file", input_file, "was not found.")

def filter_by_dates(start_date, end_date, df):
    df['date'] = pandas.to_datetime(df['date']) # converts the dates to a timestamp format
    filtered_by_dates_df = df[(df["date"] >= start_date) & (df["date"] <= end_date)] # we check if the dates of the date column belong to the given interval
    return filtered_by_dates_df

        
gd.generate_data()
df = open_file('climate_data.csv')
filtered_by_dates_df = filter_by_dates(start_date, end_date, df)
country = 'France'
#print(sa.find_hottest_countries(filtered_by_dates_df))
#print(sa.find_rainfall_anomalies(filtered_by_dates_df))
graphs.plot_daily_temperatures_variations(filtered_by_dates_df, country)
graphs.show_rainfall_as_hist(filtered_by_dates_df, country)

