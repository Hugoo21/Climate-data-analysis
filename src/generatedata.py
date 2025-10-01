import datetime 
import numpy
import pandas

def generate_date():
    # generates a list with each date from 01/01/2021 to 31/12/2024
    dates_list = []
    date = datetime.date(2021, 1, 1)
    while date.year < 2025:
        dates_list.append(date)
        date += datetime.timedelta(days=1)
    return dates_list

def generate_countries():
    # there must be 5 countries
    return ['France', 'Argentina', 'Denmark', 'China','Australia']

def generate_data():
    # datas are generated randomly
    dates = generate_date()
    countries = generate_countries()
    data_list = []
    for date in dates:
        for country in countries:
            temperature = numpy.random.randint(-10, 55) # in Celsius
            rainfall = numpy.random.randint(0, 350) # in mm
            data_list.append([date, country, temperature, rainfall])
    df = pandas.DataFrame(data_list, columns=["date", "country", "temperature", "rainfall"])
    return df

    

