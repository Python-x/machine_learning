# @Time    : 18-10-18 下午3:56
# @Author  : panzhiwei
# @Site    : 
# @File    : 3.1.py
# @Software: PyCharm


import numpy as np
from text import featureScale
# import matplotlib.pyplot as plt
alpha = 0.01
finily_change = 1e-5
data = np.mat(np.loadtxt('ex1data2.txt', delimiter=','))
m = len(data)
def compute_cost(X,Y,theta):
    n = np.dot(X,theta)-Y
    return np.dot(n.T,n)/(2*m)

def gradient_descent(X,Y,theta):
    return np.dot(X.T,np.dot(X,theta)-Y)/m

def compute_slope(X,Y,alpha):
    theta = np.array([1,1,1]).reshape(3,1)
    gradient = gradient_descent(X,Y,theta)
    num = 0
    while np.all(np.absolute(gradient)>=finily_change):
        theta = theta-alpha*gradient
        print(theta)
        num+=1
        gradient = gradient_descent(X, Y, theta)
        # print(theta)
    return theta,num
if __name__ == '__main__':


    # print(type(data))
    # print(len(data))
    X0 = np.ones((30, 1))
    s = X0.shape[0]
    X1_2 = data[0:30, 0:-1]
    # print(X1_2)
    avg = np.mean(X1_2,axis=0)
    std = np.std(X1_2,axis=0)
    X1_2_zoom = (X1_2-avg)/std
    print(X1_2_zoom)
    X = np.hstack((X0, X1_2_zoom))
    # print(X)
    Y = data[0:30, -1:]
    print('---------------------')
    print(Y)
    theta,num = compute_slope(X, Y, alpha)
    cost = compute_cost(X, Y, theta)
    print('theta:'+str(theta))
    print(str(num)+'次')
    price_mat_X1 = np.mat(data[30:,0:-1])
    price_mat_X_Y = np.hstack((np.ones((len(price_mat_X1),1)),price_mat_X1,data[30:,-1:]))
    price_mat_x,price_mat_y = featureScale(price_mat_X_Y)

    # print(price_mat_X.shape)
    #给定数据缩放拼接
    # price_mat_scale = np.hstack((price_mat[:,0],(price_mat[:,1:]-avg)/std))
    #价格
    # price = price_mat_scale*theta
    # print('估计1650平面,3居室大概'+str(np.array(price)[0][0])+'元')