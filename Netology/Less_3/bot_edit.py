HELP = '''
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатеть все добавленные задачи.
exit - выход.'''

tasks = []
today = []
tomorrow = []
other = []

run = True

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print(tasks)
    elif command == "add":
        date = input("Дата выполнения задачи: ")
        if date == "Сегодня":
            task = input("Введите название задачи: ")
            today.append(task)
        elif date == "Завтра":
            task = input("Введите название задачи: ")
            tomorrow.append(task)
        else:
            task = input("Введите название задачи: ")
            other.append(task)

        print("Задача добавлена!")
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        break
    else:
        print("Неизвестная команда")
        break
        #run = False

# print("Пока!")

# как работает цикл While
# x = 1
# while x <= 10:
#     print(x)
#     x += 1
