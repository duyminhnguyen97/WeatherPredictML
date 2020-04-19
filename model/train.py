import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# import data (remember to change datetime type)
data = pd.read_csv("./data/dataset.csv")
data['date'] = data['date'].astype('datetime64[ns]')
#print(data)
#print(data.dtypes)


# X and Y data:
X = data.iloc[:, 2:3].values			# X is dayNum
Y_mean = data.iloc[:, 3].values			# Y is meanTemp
Y_max = data.iloc[:, 4].values			# Y is maxTemp
Y_min = data.iloc[:, 5].values				# Y is minTemp
#print(X)
#print(Y)


# init for all models
deg = 8
poly_reg = PolynomialFeatures(degree = deg)
X_poly = poly_reg.fit_transform(X)


#------------------------------------------------------------------
# mean temp model training on whole dataset
lin_reg_mean = LinearRegression()
lin_reg_mean.fit(X_poly, Y_mean)
coef_mean = lin_reg_mean.coef_
intercp_mean = lin_reg_mean.intercept_
#print('The coefficients are: ', coef_mean)
#print('The intercept is: ', intercp_mean)


# calculate mean temp function
def calc_mean(dateNum):
	x = dateNum
	y = intercp_mean
	for i in range(0, deg+1):
		y = y + (coef_mean[i] * x**i)
	return y


#------------------------------------------------------------------
# max temp model training on whole dataset
lin_reg_max = LinearRegression()
lin_reg_max.fit(X_poly, Y_max)
coef_max = lin_reg_max.coef_
intercp_max = lin_reg_max.intercept_
#print('The coefficients are: ', coef_max)
#print('The intercept is: ', intercp_max)


# calculate mean temp function
def calc_max(dateNum):
	x = dateNum
	y = intercp_max
	for i in range(0, deg+1):
		y = y + (coef_max[i] * x**i)
	return y


#------------------------------------------------------------------
# min temp model training on whole dataset
lin_reg_min = LinearRegression()
lin_reg_min.fit(X_poly, Y_min)
coef_min = lin_reg_min.coef_
intercp_min = lin_reg_min.intercept_
#print('The coefficients are: ', coef_min)
#print('The intercept is: ', intercp_min)


# calculate mean temp function
def calc_min(dateNum):
	x = dateNum
	y = intercp_min
	for i in range(0, deg+1):
		y = y + (coef_min[i] * x**i)
	return y



'''
plt.scatter(X, Y, color='red')
plt.scatter(X, lin_reg.predict(poly_reg.fit_transform(X)), color='blue')
plt.show()
'''
