# Кортеж - это объект, который содержит в себе ссылки.

t = 1, 2, 3, 4, 5  # кортеж
a, b, *rest = t
*resr, c, d = t
print(t[c])
# распаковка кортежа
print(*t)
print(*t, sep=':', end='!\n')


def hello_n(name: str,
            n: int):
    for i in range(n):
        print('привет', name)


hello_n('Вася', 5)
hello_n('Петя', 3)

vasya = "Вася", 3
hello_n(*vasya)


A = range(1, 6)
print(*A)
print(60*60)
