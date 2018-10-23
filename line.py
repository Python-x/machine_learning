# @Time    : 18-10-17 下午6:31
# @Author  : panzhiwei
# @Site    : 
# @File    : line.py
# @Software: PyCharm


import numpy as np
# import matplotlib.pyplot as plt
#size of the points dataset
m = 20
#points x-ccordinate and dummy value(x0,x1)
X0 = np.ones((m,1))
X1 = np.arange(1,m+1).reshape(m,1)
X = np.hstack((X0,X1))
#points y-coordinate
Y= np.array([3,4,5,5,2,4,7,8,11,8,12,
             11,13,13,16,17,18,17,19,21]).reshape(m,1)
#the learning rate alpha
alpha = 0.01  #学习率
finaly_change = 1e-5 #最小变化幅度
#接下来我们以矩阵向量的形式定义代价函数和梯度下降函数
# 计算代价函数
def computeCost(theta,X,Y):
    error = np.dot(X,theta) - Y
    J = (1/2*m)*np.dot(error.T,error)
    return J
#梯度下降
def gradientDescent(theta,X,Y):
    error = np.dot(X,theta) - Y
    theta_gradient = (1/m)*np.dot(X.T,error)
    return theta_gradient



#最后就是算法的核心部分，梯度下降迭代计算
# def gradient_descent(X,Y,alpha):
#     theta = np.array([1,1]).reshape(2,1)#初始值分别为1,1
#     gradient = gradientDescent(theta,X,Y)
#     while not np.all(np.absolute(gradient)<=finaly_change):
#         theta = theta - alpha * gradient
#         gradient = gradientDescent(theta,X,Y)
#     return theta
# #开始执行代码
# theta = gradient_descent(X, Y, alpha)
# print('theta:', theta)
# print('cost J:', computeCost(theta,X,Y))
# #打印散点图和拟合直线
plt.subplots(figsize=(10,10))
plt.scatter(X1,Y,marker='+')
# x = np.linspace(0,20,20)
# y = theta[0][0] + theta[1][0]*x
# plt.plot(x,y,color="red")
axes = plt.gca()
axes.legend(['line regression','dataset'])
# plt.show()
