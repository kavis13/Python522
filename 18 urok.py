# def negativ_num(n):
#     if not n:
#         return 0
#     count = 0
#     if n[0] < 0:
#         count += 1
#     return count + negativ_num(n[1:])
#
#
# lst = [-2, 3, 6, -11, -4, 6]
# print(negativ_num(lst))

########################################################################################################

#
# file = 'text2.txt'
# f = open(file, 'w')
# f.write('замена строки в текст файле; \n'
#         'изменить строку в списке;\n'
#         'записать писок в файл;\n')
# f.close()
#
# f = open(file)
# data=f.readlines()
# print(data)
# data[1]='hello world\n'
# print(data)
# f.close
#
# f=open(file,'w')
# f.writelines(data)
# f.close()
###################################################
#
# f = open('text3.txt', 'w')
# lst = [i for i in range(1, 100, 5)]
# print(lst)
# for index in lst:
#     f.write(str(index) + 't')
# f.close()
##################################
# f=open('text.txt')
# print(f.read(3))
# print(f.tell())
# print(f.seek(1))
# print(f.read())
# f.close()
# ##########################
#
#
# f=open('text.txt','w')
# print(f.write('i am learning python'))
# print(f.seek(3))
# print(f.write('-new strinjg'))
# print(f.tell())
# f.close()


