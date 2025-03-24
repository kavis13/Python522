while True:
    try:
        days = int(input('Введите кол-во учебных дней: '))      # вводим кол-во дней
        if days >=0 and days <=7:           # проверка дней
            break
        else:
            print('кол-во дней не может быть меньше нуля (0) и больше семи (7) введите еще раз ')
    except ValueError:
        print('неверный ввод! Введите числовое значение! ')
hours = 0
for i in range(1,days+1):           # проверка уч. часов в днях
         while True:
             try:
                 hours_school = float(input(f'Введите кол-во учебных часов за {i} день: '))
                 if hours_school >=0:
                     break
                 else:
                     print('кол-во часов не может быть отрицательным! Введите снова!')
             except ValueError:     # проверка часов на корректный ввод
                 print('неверный ввод! Введите числовое значение!')
             finally:
                 hours = hours_school +hours            # вывод дней и часов  
                 print(f'За день вы занимались {hours_school} часов!')
                 print(f'за неделю вы занимались {hours} часов')
















