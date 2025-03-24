#
# def hello(name,age): # аргументы
#     print('hello',name, 'возраст', age)
#
#
# hello('irina',28) # параметры
# hello('ivan',30)

#########################################################

# def get_sum(a,b):
#     print(a+b)
#
#
# get_sum(2,5)

###############################
#
# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a,end='')
#         else:
#             print(b, end='')
#
#     print()
#
# symbol(9,'+','-')
# symbol(7,'x','0')
##########################################

# def get_sum(a, b):
#     return a + b
# x=2
# y=5
# res=get_sum(x,y)
# print(res)
#########################

# def maxi(one,two):
#     if one>two:
#         return one
#     else:
#         return two
# print(maxi(9,5))
# print(maxi(5,15))
###############################

# def razn(a, b):
#     if a > b:
#         return a - b
#     else:
#         return a + b
#
#
# x = int(input('a- '))
# y = int(input('y- '))
# print(razn)
####################################

# def cube(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#
#     print(i, 'в кубе = ', cube(i))
###########################################

def change(lst):
    return lst


print(change([1, 2, 3]))
