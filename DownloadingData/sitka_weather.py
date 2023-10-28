from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path = Path('WeatherFolder/sitka_weather_2021_full.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, lows, highs = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2],'%Y-%m-%d')
    try:
        low = int(row[7])
        high = int(row[8])
    except ValueError:
        print(f'current date', {current_date}, 'missing')
    else:
        dates.append(current_date)
        lows.append(low)
        highs.append(high)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(11, 7))
ax.plot(dates, lows, color='red', alpha=0.5)
ax.plot(dates, highs, color='black', alpha=0.5)
ax.fill_between(dates, highs,lows, facecolor='blue', alpha=0.1)

#Format plot
title = "Daily High and Low Temperatures, 2021"
ax.set_title(title, fontsize =18)
ax.set_xlabel('', fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel('Temperature(f)', fontsize=16)
ax.tick_params(labelsize=16)


plt.show()






    
    
