dictionary = {
    "cat": "кошка",
    "bat": "летучая мышь"
}
print(dictionary)

# доступ к значению из словаря
cat = dictionary["cat"]
print(cat)

countries = {
    "Africa": ["Египет", "Конго", "ЮАР"],
    "Asia": ["Китай", "Малайзия", "Вьетнам"]
}
print(countries)

africa = countries["Africa"]
print(africa)
africa_key = "Africa"
print(countries[africa_key])

# добавить к словарю новые ключ-значения
countries["Europe"] = ["Автсрия", "Чехия", "Испания", "Румыния"]
print(countries)
print(countries["Europe"])

africa.append("Эфиопия")
print(africa)
print(len(countries["Africa"]))
