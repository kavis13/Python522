my_dict = {'john': {'north': 3056, 'south': 8453, 'east': 8441, 'west': 2694},
          'tom': {'north': 4832, 'south': 6786, 'east': 4737, 'west': 3612},
          'anne': {'north': 5239, 'south': 4802, 'east': 5820, 'west': 1859},
          'fiona': {'north': 3904, 'south': 3645, 'east': 8821, 'west': 2451}}
for i in my_dict:
    print(i)
    for j in my_dict[i]:
        print(j, ':', my_dict[i][j])
name = input('введите имя: ')
region = input('введите регион: ')
print(my_dict[name][region])
my_dict1 = int(input('введите значение, которое хотите изменить: '))
my_dict[name][region] = my_dict1
print(my_dict[name])






