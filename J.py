# @Time    : 18-10-16 上午10:42
# @Author  : panzhiwei
# @Site    : 
# @File    : J.py
# @Software: PyCharm

def calculation(tuple1,site):
    return (site*tuple1[0]-tuple1[1])**2

def J(list1,range_num):
    min_num = 10
    site = 0
    dict1 = {}
    for num in range_num:
        sum1 = 0
        for i in list1:
            # print(calculation(i,num))
            sum1+=calculation(i,num)
        # print(sum1/(len(list1)*2))
        if sum1/(len(list1)*2)<min_num:
            min_num = sum1/(len(list1)*2)
            site = num
    return (site,min_num)

if __name__ == '__main__':
    list1 = [(1,1),(2,2),(3,3)]
    range_num = range(-50,50,1)
    print(J(list1,range_num))
