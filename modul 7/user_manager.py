# user_manager.py

def add_user(users, name, age):
    """Добавляет пользователя в словарь."""
    if name in users:
        raise ValueError(f"Пользователь с именем {name} уже существует.")
    if age < 0:
        raise ValueError("Возраст не может быть отрицательным.")

    users[name] = age
    print(f"Пользователь {name} добавлен успешно.")

def remove_user(users, name):
    """Удаляет пользователя по имени."""
    if name not in users:
        raise ValueError(f"Пользователь с именем {name} не существует.")

    del users[name]
    print(f"Пользователь {name} удален успешно.")

def list_users(users):
    """Выводит список всех пользователей."""
    if not users:
        print("Нет пользователей.")
    else:
        print("Список пользователей:")
        for name, age in users.items():
            print(f"Имя: {name}, Возраст: {age}")

