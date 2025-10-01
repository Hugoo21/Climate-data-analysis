import pandas 
import datetime
import matplotlib.pyplot as plt

start_date = pandas.Timestamp('2022-01-01')
end_date = pandas.Timestamp('2022-12-30')

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

df = open_file('climate_data.csv')
filtered_by_dates_df = filter_by_dates(start_date, end_date, df)
