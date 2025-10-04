import pandas

# it is supposed that the dataframe has been filtered by dates before
def mean_temperature(df): 
    return df['temperature'].mean()

def max_temperature(df):
    return df['temperature'].max()

def min_temperature(df):
    return df['temperature'].min()

def find_hottest_countries(df): #return the 3 hottest countries
    countries = df['country'].unique()
    results = []
    for country in countries:
        sublist = df[df['country'] == country]
        average = sublist['temperature'].mean()
        results.append((country, average))
    return pandas.DataFrame(results, columns=['country', 'temperature']).sort_values(by='temperature', ascending=False).head(3)

def find_rainfall_anomalies(df): # detect drought / heavy rainfall days
    results = []
    for i, row in df.iterrows():
        if row['rainfall'] < 10:
            results.append((row['country'], row['date'], row['rainfall'], 'Sécheresse'))
        elif row['rainfall'] > 250:
            results.append((row['country'], row['date'], row['rainfall'], 'Fortes précipitations'))
   
    return pandas.DataFrame(results, columns=['country', 'date', 'rainfall', 'anomaly_type'])