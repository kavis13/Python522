from random import randint


def ran(a,b):
    return tuple(randint(a,b) for i in range(10))


tuple_1 = ran(0,5)
print(tuple_1)
tuple_2 = ran(-5,0)
print(tuple_2)
tuple_3 = tuple_2 + tuple_1
print(tuple_3)
print('0 = ',tuple_3.count(0))
