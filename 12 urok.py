#
# def func(a, *args):
#     return a, args
#
#
# print(func(5))
# print(func(1,2,3,4,5))


# def scores(student, *score):
#
#
# scores(student: 'igor', *score: 100, 95,88, 92, 99)

#
# def func(**kwargs):
#     print(func())
#     print(a=1,b=2,c=3)
#     print(func(name='irina'))

# def info(**data):
#     for k, v in data.items():
#         print(k, ':', v)
#     print()
#
#
# info(name='irina', surname='vetrova', age=22)
# def db(**kwargs):
#     my_dict.update(kwargs)


#
# my_dict = {'one': 'first'}
# db(k1=22, k2=31, k3=11, k4=91)
# # db(name='bob', age=31, weight=61, eyes_color='grey')
# print(my_dict)


# def func1(*args):
#     print(args[0])
#
#
# def func2(**kwargs):
#     print(kwargs['one'])
#
#
# func1(1, 2, 3, 4, 5)
# func2(one=123, two=456)


# name=('tom')
#
#
# def hi():
#     name='sam'
#     surname='jjj'
#     print('hello', name)
#
#
# def bye():
#     print('good bye')
#
#
# hi()
# bye()


# max = 5
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(max(lst))

#
# def add_two(a):
#     x = 2
#
#     def add_some():
#         print('x=', x)
#         return a + x
#
#     return add_some()
#     print(x)
#
#
# print(add_two(3))
# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
# #         b = b1 + b2
# def info(**data):
#     for k, v in data.items():
#         print(k, ',', v)
#     print()


# info(name='irina', surname='vetrova', age=22)
# info(name='igor', phone='556677', email='igor@mail.ru', age=22)
# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
# my_dict = {'one': 'first'}
# db(k1=22, k2=31, k3=11, k4=91)
# # db=('bob',age=31,weight=61,eyes_color='grey')
# print(my_dict)

#
# import builtins
# name=dir(builtins)
# for t in name:
#     print(t)


# def outher(who):
#     def inner():
#         print('hello',who)
#     inner()
#
#
# outher('world')

# def outher():
#     a=6
#     def inner(b):
#         a=4
#         print('summa:',a+b)
#
#     print('a - ',a)
#     inner(5)
#
# outher()


# x = 25
#
#
# def fn():
#     global t
#     a = 30
#     t = a
#
#
# fn()
# c = x + t
# print(c)

 