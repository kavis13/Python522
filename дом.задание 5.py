

my_list = [int(input('---> ')) for  i in range(int(input('n = ')))]
print(my_list)
res = 0
for i in my_list:
    if i < 0:
        res += i
print(res)































