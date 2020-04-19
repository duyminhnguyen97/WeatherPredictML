import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
from sklearn.metrics import r2_score


# import data (remember to change datetime type)
data = pd.read_csv('../data/dataset.csv')
data['date'] = data['date'].astype('datetime64[ns]')
#print(data)
#print(data.dtypes)


# X and Y data:
X = data.iloc[:, 2:3].values		# X is dayNum
Y = data.iloc[:, 3].values			# Y is meanTemp
#Y = data.iloc[:, 4].values			# Y is maxTemp
#Y = data.iloc[:, 5].values			# Y is minTemp

#print(X)
#print(Y)


# split test and train set using K-fold cross validation
kf = KFold(n_splits=5, shuffle = False)
for i in range(2,10):
	score = []
	lin_reg = LinearRegression()
	poly_reg = PolynomialFeatures(degree = i)
	print('----------------------------------------------------------------------')
	print('Degree = ',i)
	for train_index, test_index in kf.split(X):
		X_train, X_test = X[train_index], X[test_index]
		Y_train, Y_test = Y[train_index], Y[test_index]
		X_poly = poly_reg.fit_transform(X_train)
		lin_reg.fit(X_poly, Y_train)
		Y_predict = lin_reg.predict(poly_reg.fit_transform(X_test))
		score.append(round(r2_score(Y_test, Y_predict), 3))
		print('The coefficients are: ', lin_reg.coef_)
		print('The intercept is: ', lin_reg.intercept_)
		plt.plot(X, lin_reg.predict(poly_reg.fit_transform(X)), color='blue')
	print('Score ',i,' is: ',score)
	print('Average score is: ', round(np.average(score), 3))

#print('The r2 score is: ',round(r2_score(Y_test, Y_predict), 2))
#print('The coefficients are: ', lin_reg.coef_)
plt.scatter(X, Y, color='red')
plt.show()


# select degree 8 with best accuracy score for average temperature
# select degree 8 with best accuracy score for max temperature
# select degree 8 with best accuracy score for min temperature