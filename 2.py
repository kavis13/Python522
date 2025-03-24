# a=[int(input('--->  '))for i in range(int(input('n = ')))]
# print(a)
# res = 0
# for i in range(len((a))):
#     if a[i] < 0:
#         res +=a[i]
# print(res)
#
#       #######################################################
#
# for i in a:
#     if i <0:
#         res += i
# print(res)

##########################################################

# n = list(range(21,41))
# print(n)
# count = sum_ = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         count += 1
#     else:
#         sum_ += n[i]
# print('кол во четных элем списка:', count)
# print('сумма нечетных элем списка:', sum_)

###############################################

# a=[int(input('--->  '))for i in range(int(input('n = ')))]
# print(a)
# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         print(a[i], end=' ')
# print()

################################################


# a=[int(input('--->  '))for i in range(int(input('n = ')))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=' ')

#################################

# a = [9, 7, 8, 4, 2]
# a[0], a[1] = a[1], a[0]
# print(a)


##########################################
# список[start:stop:step]
# a = [9, 7, 8, 4, 2, 1, 3]
# print(a)
# print(a[1:])

####################################
# lst = list(range(1,8))
# print(lst)
# print(lst)


#####################################################

# методы списков

# print(dir(list))
# s = [9, 7, 8, 4, 2, 1, 3]
# print(s)
# s.append(99) # добавляет элем в конец списка
# print(s)
# s.extend([11,12,13]) # доб список элем в конец списка
# print(s)
# s.extend('add')
# print(s)
# s.insert(4, 100) # добавляет элем (второй параметр) по заданному индексу (первый параметр)
# print(s)
# s.insert(20,5)
# print(s)

##########################################

# s = []
# n = int(input('кол-во элем в списке: '))
# for num in range(n):
#     x = int(input('введите число: '))
#     s.insert(0, x)
# print(s)
##################################################

# a = [9, 7, 8, 4, 2, 1, 3]
# b = [4,2,1,3,7]
# c = []  # 2,1,4,3,
# for i in a:
#     for j in b:
#         if i == j:
#             c.append(i)
# print(c)
###########################################

# a = [9, 7, 8, 4, 2, 1, 3, 5]
# b = [4,2,1,3,7, 5]
# c = []
# for i in a:
#     if i in b:
#         c.append(i)
# print(c)

############################################


# a = [1, 2, 3]
# b = [11, 22, 33]
# c = []
#
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
#
# print(c)

#######################################

s = [9,7,8,4,2,1,3]
print(s)
s.remove(8)
print(s)



