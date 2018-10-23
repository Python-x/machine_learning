# @Time    : 18-10-17 上午10:25
# @Author  : panzhiwei
# @Site    : 
# @File    : 2.8.py
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt
m = 5
alpha = 0.01
finily_change = 1e-5
X1 = np.ones((m,1))
X2 = np.arange(1,m+1).reshape(m,1)
X = np.hstack((X1,X2))
# theta = np.mat((1,1)).reshape(2,1)
Y = np.array([1.1,2.2,3.3,5,5]).reshape(m,1)
def compute_cost(X,Y,theta):
    n = np.dot(X,theta)-Y
    return np.dot(n.T,n)/(2*m)

def gradient_descent(X,Y,theta):
    return np.dot(X.T,np.dot(X,theta)-Y)/m

def compute_slope(X,Y,alpha):
    theta = np.array([1,1]).reshape(2,1)
    gradient = gradient_descent(X,Y,theta)
    while np.all(np.absolute(gradient)>=finily_change):
        theta = theta-alpha*gradient
        gradient = gradient_descent(X, Y, theta)
        # print(theta)
    return theta

# cost = compute_cost(X,Y,theta)
theta = compute_slope(X,Y,alpha)

# print(n)
#
# plt.subplot(figsize=(10,10))
# plt.scatter(x=X2,y=Y,marker='×')
# x = np.linspace(0,21,20)
# y = theta[0][0]+theta[1][0]*x
# plt.plot(x,y,color='green')
# axes = plt.gca()
# axes.legend(['dian','xian'])
# plt.show()



# theta = np.array([1,1]).reshape(2,1)
# print(gradient_descent(theta, X, Y))































# def computeCost(theta,X,Y):
#     error = np.dot(X,theta)-Y
#     J = (1/2*m)*np.dot(error.T,error)
#     return J
#
#
# def gradientDescent(theta,X,Y):
#     error = np.dot(X*theta)-Y
#     theta_gradient = (1/m)*np.dot(X.T,error)
#     return theta_gradient
#
#
#
#
# m = 3   #训练数据集的个数
# X0 = np.ones((m,1))
# # print(X0)
# X1 = np.arange(1,m+1).reshape(m,1)
# # print(X1)
# X = np.hstack((X0,X1))
# # print(X)
# Y = np.array([1.1,2.1,3.1]).reshape(m,1)
# print(Y)
# #学习率
# alpha = 0.01