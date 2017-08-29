from numpy import genfromtxt
import numpy as np
import matplotlib.pyplot as plt

# getting data from data.csv
data = genfromtxt('data.csv',delimiter=',',dtype=float)
x, y  = data.T
plt.plot(x, y, '--')
plt.scatter(x,y)


def LR(data):
	# mean of [x,y] = [x', y'] , m[0] = x' ,m[1] = y'
	m = np.mean(data,axis=0)

	# diff[0] = x - x' ,diff[0] = y - y' for each element in dataset
	diff = np.subtract(data,m)

	# x2 = (x-x')^2
	x2 = np.multiply(diff[:,0],diff[:,0])	

	#sumX2  = sum of each x2
	sumX2 = np.sum(x2,axis=0)

	# xy = (x-x')*(y-y')
	xy = np.multiply(diff[:,0],diff[:,1])	

	#sumXY  = sum of each xy
	sumXY = np.sum(xy,axis=0)

	# Y  =  theta0 + theta1*X regression line
	theta0 = 0;
	theta1 = 0;

	theta1 = sumXY / sumX2;
	theta0 = m[1] - theta1*m[0];

	return theta0,theta1

def prediction(value):
	d0,d1 = LR(data)
	abline_values = [d1 * i + d0 for i in x]
	plt.plot(x, abline_values, 'b')
	plt.title('Linear Regression')
	return d0 + d1*value
	
	

if __name__ == '__main__':
	print prediction(7.5)
	plt.scatter(7.5,prediction(7.5))

	plt.show()
