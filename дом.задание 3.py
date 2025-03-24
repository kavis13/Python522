

tasks = []      #  Создаем пустой список задач

                #  ввод команды для работы с задачами
while True:
    team = input('введите команду(add; remove; list; exit): ')
    if team == 'add':
        task = input('введите задачу: ')
        tasks.append(task)
        print(f'задача: {task}, добавлена')

                #  ввод команды на удаление задачи
    elif team=='remove':
        try:
            index=int(input('введите индекс для удаления задачи: '))
            if 0 <= index < len(tasks):
                remove_task=tasks.pop(index)
                print(f'задача: {task}, удалена')
            else:

                #  проверка на правильность ввода
                print('индекс вне диапазона')
        except ValueError:
            print('введите корректный индекс')

                #  вывод списка задач
    elif team=='list':
        if tasks:
            print('список задач')
            for i,task in enumerate(tasks):
                print(f"{i}: {task}")
            else:
                print('список задач пуст')

                #  запрос на выход из программы
    elif team==('exit'):
        print('Выход из программы')
        break
    else:
        print('ошибка ввода! Введите еще раз! (add; remove; list; exit)')

        '''К сожалению я так и не смог разобраться, как работать с циклами.
        Где и как правильно их использовать. Поэтому работа сделана с большой помощью 
        и всё-равно работает криво. Я уже ничего понять не могу, совсем запутался.
        '''





































































