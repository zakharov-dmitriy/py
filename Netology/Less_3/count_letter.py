list = ['python', 'c++', 'java script', 'ruby', 'react']
letter = ''


def count_letter():
    for word in list:
        print(' - ', word)

    for letter in word:
        if letter == "c":
            print("111")


count_letter()
