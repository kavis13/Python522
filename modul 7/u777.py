
# main.py

from user_manager import add_user, remove_user, list_users

def main():
    users = {}

    while True:
        command = input("Введите команду (add, remove, list, exit): ").strip().lower()

        if command == "add":
            name = input("Введите имя пользователя: ").strip()
            try:
                age = int(input("Введите возраст пользователя: ").strip())
                add_user(users, name, age)
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif command == "remove":
            name = input("Введите имя пользователя для удаления: ").strip()
            try:
                remove_user(users, name)
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif command == "list":
            list_users(users)

        elif command == "exit":
            print("Выход из программы.")
            break

        else:
            print("Неизвестная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()