import pandas 
import matplotlib.pyplot as plt
import csv

def open_file(input_file):
    try:
        with open(input_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("Error : The file", input_file, "was not found.")


open_file('climate_data.csv')