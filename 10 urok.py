# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b)
from itertools import count

# print(c)
# a |= b
# a &= b
# print(a)

# c =a-b
#
# print(c)
#
# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# c = a >= b
# c = a<= b
# print(c)
# print(b)


# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = {6, 2}
# d = a ^ b ^ c
# print(d)
#
# a = {1, 2}
# b = {3}
# c = {4, 5}
# d = {3, 2, 6}
# i = {6}
# f = {7, 8}
# g = {9, 8}
# s=a|b|c|d|i|f|g
# print(s)
# print(f'кол-во уник элем = ,{len(s)}')
# print(f'миним элем =,  {min(s)}')
# print(f'макс элем =,{max(s)}')

#
# a = 'Hello'
# b = 'How are you'
# s = set(a) & set(b)
# print(s)
# for i in s:
#     print(i, end='|')


# s = frozenset([1,2,3,4,5,6])
# print(s)
#
# s1 = frozenset('hello')
# print(s1)
#

#
# lst = ['one','two']
# d = {'first':'one','second': 'two'}
# print(lst)
# print(d)

# a = {0: 'text', 'one': 45, (1, 2): 'кортеж', True:[5,6,7],'one':'список'}
#
# print(a)

#
# d = {'first':'one','second': 'two'}
# print(d)
# print(type(d))

#
# tro = [
#     ['one',1],
#     ['two',2],
#     ['three',3]
# ]
# print(tro)
# d = dict(tro)
# print(d)


# d = {i: i**2 for i in range(1,7)}
# print(d)
# for i in d:
#     print('key =', i, 'value = ', d[i])

#
# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# res = 1
# for key in d:
#     res *= d[key]
# print(res)


# p = dict()
# p[1] = input('--->')
# p[2] = input('--->')
# p[3] = input('--->')
# p[4] = input('--->')
# print(p)

#
# d = {i: input('->')for i in range(1,5)}
# print(d)
# rem = int(input('какой элем удалить?: '))
# del d[rem]
# print(d)


goods = {
    '1': ['core-i3-4330', 9, 4500],
    '2': ['core-i5-4670', 3, 8500],
    '3': ['AMD FX-6300', 6, 3700],
    '4': ['Pentium G3220', 8, 2100],
    '5': ['core i5-4350', 5, 6500],
}
for i in goods:
    print(i, ')', goods[i][0],' - ',goods[i][1], 'шт. по ',goods[i][2], 'руб',sep='')

while True:
    n = input('№: ')
    if n =='0':
        break
    else:
        count = int(input('количество: '))
        goods[n][1] = count
for i in goods:
    print(i, ')', goods[i][0], ' - ', goods[i][1], 'шт. по ', goods[i][2], 'руб', sep='')




