from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('C:/Users/Alejo/Documents/python_work/Project/visualization/weather_data/death_valley_2021_simple.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract high temperatures and dates
highs, lows, dates = [], [],[]
for row in reader:
    current_date = datetime.strptime(row[2],'%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)

# Protting data
# Plot the high temperatures
plt.style.use('seaborn-v0_8')
fig , ax  = plt.subplots()
ax.plot(dates, highs, c='r', alpha = 0.5)
ax.plot(dates, lows, c='b', alpha = 0.5)
ax.fill_between(dates, highs, lows, facecolor='b', alpha = 0.1)

# Format plot
ax.set_title("Daily high and low temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize = 16)
ax.tick_params(labelsize=16)

plt.show()