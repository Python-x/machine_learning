# @Time    : 18-10-22 下午1:41
# @Author  : panzhiwei
# @Site    : 
# @File    : 逻辑分类.py
# @Software: PyCharm
import numpy as np
#加载数据并打印散点图
finily_num = 1e-5
J_num = 2000
alpha = 0.04
# def printScatter(filename):
#     pass

def sigmoid(z):
    return 1/(1+np.exp(-z))

def loodDataset(filename,percent=1):
    data = np.loadtxt(filename,delimiter=',')
    np.random.shuffle(data)
    m = int(len(data)*percent)
    Y = data[:m,-1].reshape(-1,1)
    m = len(Y)
    X = np.hstack((np.ones((m, 1)), data[:m,0:2]))
    n = X.shape[1]
    return X,Y,m,n

def computeCost(theta,X,Y,m):
    z = sigmoid(X*theta)
    # print(z,Y)
    J = -(Y*np.log(z)+(1-Y)*np.log(1-z))/m
    return J
def compute_gradient_descent(X,Y,theta):
    z = sigmoid(X*theta)
    # print((z-Y).shape)
    return (X.T*(z-Y))/m

def compute_slope(X,Y,alpha,m):
    J_list = []
    num = 0
    theta = np.mat([[-100],
                    [1],
                    [3]])
    J_list.append(computeCost(theta,X,Y,m))
    z = sigmoid(X*theta)
    gradient = compute_gradient_descent(X,Y,theta)
    while (not np.all(np.absolute(gradient)<finily_num)) and num<J_num:
        theta = theta-alpha*gradient
        # print(theta)
        J_list.append(computeCost(theta, X, Y, m))
        gradient = compute_gradient_descent(X,Y,theta)
        num+=1
    return theta,gradient,num,J_list
# print(loodDataset('/home/panzhiwei/Desktop/机器学习/ex2data1.txt',0.6))
X,Y,m,n = loodDataset('/home/panzhiwei/Desktop/机器学习/ex2data1.txt')
print(X.shape)
print(Y.shape)

# theta = np.mat(np.ones((n,1)))
# theta = np.mat([[1.1],
#                 [1.1],
#                 [1.1]])
# print(X.shape)
theta,gradient,num,J_list = compute_slope(X,Y,alpha,m)
print(theta,gradient,num)
# print(computeCost(theta,X,Y,m))