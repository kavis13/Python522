# /# a=5
# # b=7
# # c=3
# # x=(a+b+c)/3
# # print(a+b+c)
# # print(a*b*c)
# # print(x)
#
# #######################################
# a=int(input('1: '))
# b=int(input('2: '))
# c=int(input('3: '))
# d=int(input('4: '))
# res1=a+b
# res2=c+d
# print('res1:', res1)
# print('res2:', res2)
# res3=res1/res2
# print(round(res3,2))
########################################

# number = int(input('введите пятизначное число: '))
# # разделяем цифры
# num1 = number//10000%10
# num2 = number//1000%10
# num3 = number//100%10
# num4 = number//10%10
# num5 = number%10
#
# print(num1, num2, num3, num4, num5)
# print(f'сложение цифр числа - {number}, равна - {num1+num2+num3+num4+num5}')
# print(f'произведение цифр числа - {number}, равно {num1*num2*num3*num4*num5}')
# print(f'среднее арифметическое числа {number}, равняется {(num1+num2+num3+num4+num5)/5}')
##################################################################################################

# my_list = [int(input('---> ')) for  i in range(int(input('n = ')))]
# print(my_list)
# res = 0
# for i in range(len(my_list)):
#     if my_list[i] < 0:
#         res += my_list[i]
# print(res)
#####################################

# a = 10
# b = 10
# if a > b:
#     print(a, '>', b)
# if b > a:
#     print(b, ' > ', a)
# if b == a:
#     print(b, '==', a)
#######################################

# cnt = 5
# if cnt < 10:
#     cnt = cnt+1
# print(cnt)
  ########################################
# age = int(input('ВВЕДите свой возраст: '))
# if age>=18:
#       print('доступ рвзрешен')
# else:
#     print('нельзя')
##############################################

a = int(input('введите пкрвую сторону: '))
b = int(input('введите вторую сторону: '))
c = int(input('введите третью сторону: '))
if a == b == c:
    print('треуг раносторон')
elif a ==b or a == c or b == c:
    print('треуг равнобедр')
else:
    print('теуг разносторн')






