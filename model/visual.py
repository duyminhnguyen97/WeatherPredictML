import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


# import (remember to change datetime type)
data = pd.read_csv('../data/dataset.csv')
data['date'] = data['date'].astype('datetime64[ns]')
print(data)
print(data.dtypes)


# plot for visualize
new_plot = data.plot(kind = 'scatter', x = 'dayNum' , y = 'meanTemp', color='red')
#new_plot = data.plot(x = 'date' , y = 'meanTemp', color='red')
#new_plot.set_xlim(pd.Timestamp('2012-09-04'), pd.Timestamp('2013-01-01'))
#new_plot.set_xlim(pd.Timestamp('2013-01-01'), pd.Timestamp('2014-01-01'))
#new_plot.set_xlim(pd.Timestamp('2014-01-01'), pd.Timestamp('2015-01-01'))
#new_plot.set_xlim(pd.Timestamp('2015-01-01'), pd.Timestamp('2016-01-01'))
#new_plot.set_xlim(pd.Timestamp('2016-01-01'), pd.Timestamp('2017-01-01'))
#new_plot.set_xlim(pd.Timestamp('2017-01-01'), pd.Timestamp('2018-01-01'))
#new_plot.set_xlim(pd.Timestamp('2018-01-01'), pd.Timestamp('2019-01-01'))
#new_plot.set_xlim(pd.Timestamp('2019-01-01'), pd.Timestamp('2020-01-01'))
#new_plot.set_xlim(pd.Timestamp('2020-01-01'), pd.Timestamp('2020-04-01'))


plt.show()


#new_plot = data.plot(x = 'date' , y = 'meanTemp', color='red')