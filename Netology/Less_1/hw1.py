# date = input("Введите дату: ")
# task = input("Введите задачу: ")

# print(date, task)


# date_first = input("Введите дату: ")
# task_first = input("Введите задачу: ")

# date_second = input("Введите дату: ")
# task_second = input("Введите задачу: ")

# date_third = input("Введите дату: ")
# task_third = input("Введите задачу: ")


# print(date_first, task_first, "\n", date_second,
#       task_second, "\n", date_third, task_third)

dict = {}
date_first = input("Введите дату: ")
task_first = input("Введите задачу: ")
date_second = input("Введите дату: ")
task_second = input("Введите задачу: ")
date_third = input("Введите дату: ")
task_third = input("Введите задачу: ")

dict[date_first] = [task_first]
dict[date_second] = [task_second]
dict[date_third] = [task_third]

print(dict)
