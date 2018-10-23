# @Time    : 18-10-17 下午2:28
# @Author  : panzhiwei
# @Site    : 
# @File    : text.py
# @Software: PyCharm
import numpy as np
#
# # print(np.array([1,22,3]))
# print(np.mat([(1,2,3)]).reshape(-1,3))



# list1 = [1,200,20,782,203]

def featureScale(data):
    one = data[:,0]
    last = data[:,-1]
    l = data[:,1:-1]
    # for i in
    avg = np.mean(l)
    std = np.std(l)
    return np.hstack((one,(l-avg)/std)),last
    # list_scale = []
    # avg = np.mean(list1)
    # print(avg)
    # std = np.std(list1)
    # print(std)
    # list_scale = [ (i-avg)/std for i in list1]
    # return list_scale

    # # print(l)
    # for i in range(len(l)):
    #     # print(l[i])
    #     # avg = np.full(1,len(l.T),np.mean(l[i]))
    #     # std = np.full(len(l.T),1,np.std(l[i]))
    #     avg = np.mean(l[i])
    #     std = np.std(l[i])
    #     # print(avg,std)
    #     new_l = (l[i]-avg)/std
    #     print(new_l)
    #     one = np.vstack((one,new_l))
    # return np.vstack((one,last)).T
if __name__ == '__main__':
    data = np.mat(np.loadtxt('old_text.txt', delimiter=',').reshape(4, 4))
    print(data)
    new_data = featureScale(data)
    np.savetxt('new_text.txt',X=new_data,delimiter=',',fmt='%.8f')
    # print(data)
