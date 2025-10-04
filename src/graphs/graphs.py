import matplotlib.pyplot as plt


def plot_daily_temperatures_variations(df, country):  
    filtered_df = df[df['country'] == country].copy()
    
    plt.figure(figsize=(10, 5))
    plt.plot(filtered_df['date'], filtered_df['temperature'], color='green', linewidth=2)
    
    #hot and cold days are plotted in a different colors
    hot_points =filtered_df[filtered_df['temperature'] >= 40]
    cold_points =filtered_df[filtered_df['temperature'] < 0]
    plt.scatter(hot_points['date'], hot_points['temperature'], color='red', s=50, label='Température')
    plt.scatter(cold_points['date'], cold_points['temperature'], color='blue', s=50, label='Température')


    plt.title(f"Variations quotidiennes de la température en {country}")
    plt.xlabel("Date")
    plt.ylabel("Température (°C)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def show_rainfall_as_hist(df, country):
    filtered_df = df[df['country'] == country].copy()
    rainfall_by_months = filtered_df.groupby(filtered_df['date'].dt.to_period('M'))['rainfall'].sum()
    rainfall_by_months_idx = rainfall_by_months.index.to_timestamp()

    plt.figure(figsize=(10,6))

    colors = []
    #different colors according to how rainy the month was
    for val in rainfall_by_months.values:
        if val > 5800:  
            colors.append('green')
        elif val < 4500:  
            colors.append('black')
        else:  
            colors.append('blue')

    plt.bar(rainfall_by_months_idx, rainfall_by_months.values, color=colors, width=20)
    plt.title(f"Variations mensuelles des précipitations en {country}")
    plt.xlabel("Date")
    plt.ylabel('Précipitations (en mm)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()