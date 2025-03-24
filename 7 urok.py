# a = [1, 2, 3]
# b=a
# print('a -',a)
# print('b - ',b)
# b.append(20)
# print('a - ',a)
# print('b - ',b)
# a.append(100)
# print('a - ',a)
# print('b - ',b)
# m=[1,3,5,6,2,4,6,1,2,7,]
# print(m)
# m.reverse()
# print(m)
# m.sort()
# print(m)
# s = ['dddddddd','ffffff','gfgfggfgfgfgf']
# s.sort(key=len)
# print(s)

########################################################

# m = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7, ]
# m.sort()
# print(m)
# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# sorted(s)
# print(s)
###################################################

# import random
# print(random.random())
# print(random.randint(5, 10))
# print(random.randrange(5,10))
#
#
# city_list = ['москва', "новосиб","воронеж", "сочи"]
# s = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# print(random.choices(city_list, k=3))
# print(random.choices(s,k=3))
# random.shuffle(city_list)
# print(city_list)

##############################################
#
# import random
#
# mas = [random.randint(30,107) for i in range(7)]
# print(mas)
# print(len(mas))
# print(max(mas))
# print(min(mas))
# print(sum(mas))

######################################################

# import random
# mas = [random.randint(0,100) for i in range(10)]
# print(mas)
# max_ = max(mas)
# print(max_)
# mas.remove(max_)
# mas.insert(0.max_)
# print(mas)
##########################################

# import random
# mas = [random.randint(0,100) for i in range(19)]
# print(mas)
# min_ = min(mas)
# print('min', min_)
# ind = mas.index(min_)
# print('index min = ',ind)
# del mas[0:ind]
# print(mas)
#######################################################

# m = [[11, 22, 33],[25, 37, 40],[5, 6, 7]]
# print(m)
# print(len(m))
# print(m[1][2])
#
# print('вариант 1')
# for row in range(len(m)):
#     print(m[row])
#     for col in range(len(m[row])):
#         print(col)
# print('вариант 2')
# for row in m:
#     print(row)
#     for x in row:
#         print(x, end='\t')
#     print()

##############################################

# import math
# print(math.sqrt(4))


# from math import *
# print(sqrt(45))
# print(ceil(3.2))
# print(floor(4.7))
############################
# import math
# print(dir(math))
##########################
# from  math import pi
# radius = int(input('введите радиус окр  '))
#
# print('длина окр - ', 2*radius*pi, 2)

##########################

import time
print(time.time())
print(time.ctime())
print(time.strftime('Today is %B %d, %Y'))
print(time.strftime('%m/%d/%Y, %H:%M:%S'))
