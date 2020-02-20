import csv
from datetime import datetime

from matplotlib import pyplot as plt

#read date and temperature from csv file
filename = 'data/sitka_weather_07-2018_simple.csv'
# ~ filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	#read the high temperate from the csv file
	dates,highs,lows = [],[],[]
	for row in reader:
		try:
			current_date = datetime.strptime(row[2],"%Y-%m-%d")
			high = int(row[5])
			low = int(row[6])
		except ValueError:
			print(current_date,'missing data')
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)
	
#plot the high and low temperature
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates,highs,c='red',alpha=0.5)
ax.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

#Format plot.
plt.title("Daily high and low temperatures - 2018",fontsize=24)
# ~ plt.title("Daily high and low temperatures - 2018\nDeath Valley,CA",fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()
