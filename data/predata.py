import pandas as pd
import numpy as np
from datetime import datetime


# import data
dataset = pd.read_csv('data.txt')


# remove unwanted columns
i = [0,1,4,5,6,7,8,9,10,11,12,13,14,15,16,20,21,22]
dataset = dataset.drop(dataset.columns[i], axis='columns')


# remove unwanted characters
dataset['   MAX  '] = dataset['   MAX  '].map(lambda x: x.lstrip(' ').rstrip('* '))
dataset['  MIN  '] = dataset['  MIN  '].map(lambda x: x.lstrip(' ').rstrip('* '))
dataset['PRCP  '] = dataset['PRCP  '].map(lambda x: x.lstrip(' ').rstrip('ABCDEFGHI '))
dataset['PRCP  '] = dataset['PRCP  '].replace('99.99', 00.00)

# change the ugly name =='
dataset = dataset.rename(columns={' YEARMODA': "dateNum", '   TEMP': "meanTemp", '   MAX  ': "maxTemp", '  MIN  ': "minTemp", 'PRCP  ': "prcp"})
dataset['dateNum'] = pd.to_numeric(dataset['dateNum'])
dataset['meanTemp'] = pd.to_numeric(dataset['meanTemp'])
dataset['maxTemp'] = pd.to_numeric(dataset['maxTemp'])
dataset['minTemp'] = pd.to_numeric(dataset['minTemp'])
dataset['prcp'] = pd.to_numeric(dataset['prcp'])


# convert Farenheit to Celcius / convert inch to mm
for index, row in dataset.iterrows():
	dataset.loc[index, 'meanTemp'] = round(((row['meanTemp'] - 32) * 5.0 / 9.0), 2)
	dataset.loc[index, 'maxTemp'] = round(((row['maxTemp'] - 32) * 5.0 / 9.0), 2)
	dataset.loc[index, 'minTemp'] = round(((row['minTemp'] - 32) * 5.0 / 9.0), 2)
	dataset.loc[index, 'prcp'] = round((row['prcp'] * 25.4), 2)


# convert dateNum to date
dataset.insert(0, "date", dataset['dateNum'], True)
dataset['date'] = dataset['date'].apply(lambda x: pd.to_datetime(str(x), format='%Y%m%d'))


# add day number of the year
dataset.insert(2, "dayNum", dataset['date'], True)
for index, row in dataset.iterrows():
	dataset.loc[index, 'dayNum'] = row['dayNum'].timetuple().tm_yday


# change prcp to rain
dataset.insert(6, "rain", True)
dataset['rain'] = dataset['rain'].astype('int64')
for index, row in dataset.iterrows():
	if row['prcp'] != 0:
		dataset.loc[index, 'rain'] = 1
	else:
		dataset.loc[index, 'rain'] = 0


# check data
head = np.array(dataset.columns)
print(dataset)
print(dataset.dtypes)
print(head)


# export
export_csv = dataset.to_csv('dataset.csv', index = None, header = True)