import telebot
import random

token = "5252699878:AAEkDWgXWJdn9mKG9j2_GPPKQ7StOOWn65U"
bot = telebot.TeleBot(token)

HELP = '''
/help - вывести список доступных команд.
/add - добавить задачу в список (название задачи запрашиваем у пользователя).
/show - напечатеть все добавленные задачи.
/exit - выход.
/random - добавить случайную задачу на "Сегодня"'''

RANDOM_TASKS = ["Записаться на курс по Python",
                "Помыть машину", "Накормить слона", "Купить продуктов"]

tasks = {}


def add_todo(date, task):
    if date in tasks:
        # Дата есть в словаре, добавляем в список задачу
        tasks[date].append(task)
    else:
        # Даты в словаре нет, создаемзапись с ключем date (tasks[date] = [task])
        tasks[date] = []
        tasks[date].append(task)


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=["add", "todo"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['random'])
def random_add(message):
    date = "сегодня"
    task = random.choice(RANDOM_TASKS)
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["show", "print"])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ""
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + "[] " + task + "\n"
    else:
        text = "Задач на эту дату нет"
    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)

# print(dir(telebot.__name__))
