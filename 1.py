
# films=[]
# while True:
#     com=input('ведите команду: ')
#     if com=='add':
#         film=input('введите фильм: ')
#         films.append(film)
#         print(f'фильм {film} добавлен')
#     elif com=='remove':
#             films.remove(film)
#             print(f'{film} удален')
#     film=input('введите филм для удаления: ')
#     if film in films:
#         print(f'{film} удален')
#     elif com=='list':
#         print(films)
#################################################






# i=0
# while i<10:
#     print(i)
#     i+=1
# else:
#     print('цикл окончен')

# i=1
# while i<5:
#     print('внешний цикл: =i')
#     j=1
#     while j < 4:
#         print('\tвнутренниий циклЖ о =',j)
#         j+=1
#     i+=1

# i=1
# while i<=9:
#     j = 1
#     while j <= 9:
#         print(i,'*',j, '=', i*j, end='\t' )
#         j+=1
#     print()
#     i+=1


# i=0
# while i<7:
#     j=0
#     while j<6:
#         print('^',end='')
#         j+=1
#     print()
#     i+=1

# for element in collection:
#     print(element)
# for i in 'hello', 'world':
#
#     print(i)
#print(range(0,7,6))
# for i in range(0,9,2):
#     print(i, end=' ')
# print()
# i=0
# while i<8:
#     print(i,end=' ')
#     i+=2


# a=int(input('введите число: '))
# for i in range(1,a+1):
#     if a%i == 0:
#         print(i, end=' ')

#
# for i in range(10,100):
#     if i % 11 == 0:
#         print(i, end=' ')
# print()
# for i in range(11,100,11):
#     print(i,end=' ')
# print()


# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print('цикл закончен')
# for i in range(3):
#     print('+++')
#     for j in range(2):
#         print('-----')

# w=input('введите ширину прмоуг: ')
# h=input("введите высоту прямог: ")

#
# for i in range(h):
#     for j in range(w):
#         if i==0 or i==h-1 or j==0 or j==w-1:
#             print('*',end='')
#         else:
#             print(' ', end='')
#     print()
     # списки
# letter=[i*2 for i in 'hello']
# print(letter)
#
# for i in 'hello':
#     print(i*2)


# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums)
# print(type((nums)))
# print(nums[1])
# print('кол-во - ',len((nums)))

#
# s = []
# print(s)
# print(type(s))
# t = list('python')
#
# print(t)
# print(type(t))
# print(range(0,8,2))
#
# print(list(range(1,18,2)))


#
# a = [1,3,5,7,9]
# b = [11,13,15,17]
# print(a+b)
# print(a*3)

# a=[1,3,5,7,9]
# for i in a:
#     print(i)


# a=[0 for  i in range(5)]
# print(a)

# a=[0] * int(input('введите колво элем списка: '))
# print(a)
# for i in range(len(a)):
#     a[i]=int(input('->'))
#     print(a)


# my_list = [9,6,3,5]
# for i in range(len(my_list)):
#     print(i,end=' ')
# print()
# for i in my_list:
#
#     print(i,end=' ')

