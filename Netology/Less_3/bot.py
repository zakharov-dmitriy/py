HELP = '''
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатеть все добавленные задачи.
exit - выход.'''

tasks = {}

run = True

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        date = input("Введите дату для отображения списка зачач: ")
        if date in tasks:
            for elem in tasks[date]:
                print('- ', elem)
        else:
            print("Такой даты нет.")
    elif command == "add":
        date = input("Введите дату для добавления задачи: ")
        task = input("Введите название задачи: ")
        if date in tasks:
            # Дата есть в словаре, добавляем в список задачу
            tasks[date].append(task)
        else:
            # Даты в словаре нет, создаемзапись с ключем date (tasks[date] = [task])
            tasks[date] = []
            tasks[date].append(task)

        print("Задача ", task, " добавлена на дату ", date)
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        break
    else:
        print("Неизвестная команда")
        break
        #run = False

# как работает цикл While
# x = 1
# while x <= 10:
#     print(x)
#     x += 1
