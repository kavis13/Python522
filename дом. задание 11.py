
# Запрашиваем количество студентов
n = int(input("Введите количество студентов: "))

# Создаем список для хранения данных о студентах
students = []

# Вводим данные о каждом студенте
for i in range(n):
    surname = input(f'Введите фамилию студента {i+1}: ')
    name = input(f'Введите имя студента {i+1}: ')
    score = float(input(f'Введите балл студента {i+1}: '))
    students.append({'surname': surname, 'name': name, 'score': score})

# Вычисляем средний балл
total_score = sum(student['score'] for student in students)
sr_score = total_score / n

# Выводим средний балл
print(f'\nСредний балл: {sr_score:.2f}')

# Выводим студентов с баллом выше среднего
print('\nСтуденты с баллом выше среднего:')
for student in students:
    if student['score'] > sr_score:
        print(f'{student['surname']} {student['name']} - {student['score']}')

