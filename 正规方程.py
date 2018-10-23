# @Time    : 18-10-19 上午9:38
# @Author  : panzhiwei
# @Site    : 
# @File    : 正规方程.py
# @Software: PyCharm

import numpy as np

X = np.mat([[1,1],
            [1,-1]])

Y = np.mat([[1],
            [-1]])
theta = np.linalg.pinv((X.T*X))*X.T*Y
print(theta)