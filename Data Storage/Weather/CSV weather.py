import csv
from matplotlib import pyplot as plt
from datetime import datetime

file_name = 'death_valley_2014.csv'

# Get's high temperatures and dates from file.
with open(file_name) as file:
    reader = csv.reader(file)
    header = next(reader)

    temp_highs = []
    dates = []
    temp_lows = []
    for row in reader:
        try:
            today_date = datetime.strptime(row[0], "%Y-%m-%d")
            temp_high = int(row[1])
            low = int(row[3])

        except ValueError:
            print(today_date, 'missing data')

        else:
            dates.append(today_date)
            temp_highs.append(temp_high)
            temp_lows.append(low)

    print(temp_highs)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, temp_highs, c='red', alpha = 0.5)
plt.plot(dates, temp_lows, c='blue', alpha = 0.5)
plt.fill_between(dates, temp_highs, temp_lows, facecolor='blue',alpha=0.1)

#Formating the plot
title = "Daily high & low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize = 20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis = 'both', which='major', labelsize = 16)

plt.show()