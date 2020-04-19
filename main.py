import pandas as pd
from model.train import calc_mean, calc_max, calc_min
from datetime import datetime


print("This is a small Machine Learning model to predict Hanoi's weather.")
choose = input('Type 1 to get weather forecast, 2 to quit: ')
if choose == '1':
	print('Choose the date and you want:')
	day = int(input('Day: '))
	month = int(input('Month: '))
	year = int(input('Year: '))
	date = year*10000 + month*100 + day
	date = pd.to_datetime(str(date),  format='%Y%m%d')
	day_of_year = date.timetuple().tm_yday
	date = date.strftime("%d-%m-%Y")
	meanTemp = round(calc_mean(day_of_year), 2)
	maxTemp = round(calc_max(day_of_year), 2)
	minTemp = round(calc_min(day_of_year), 2)
	print('The average temperature of',date,'is:',meanTemp)
	print('The max temperature of',date,'is:',maxTemp)
	print('The min temperature of',date,'is:',minTemp)

elif choose == '2':
	quit()

else:
	print('Invalid choice.')