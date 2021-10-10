# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
# Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для
# перевода: какой тип данных выбрать, в теле функции или снаружи.
# 2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной буквы —
# результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

def num_translate(num: str):
    """поддержка устаревшей функции"""

    return num_translate_adv(num)


def num_translate_adv(num: str):
    """
    translates numbers from one to ten* from English to Russian and vice versa

    *actually up to fourteen
    """

    dic = {
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять",
        "eleven": "одиннадцать",  # пасхалочка
        "twelve": "двенадцать",
        "thirteen": "тринадцать",
        "fourteen": "четырнадцать",
        "One": "Один",  # самый простой и очевидный путь
        "Two": "Два",
        "Three": "Три",
        "Four": "Четыре",
        "Five": "Пять",
        "Six": "Шесть",
        "Seven": "Семь",
        "Eight": "Восемь",
        "Nine": "Девять",
        "Ten": "Десять",
        "Eleven": "Одиннадцать",  # поддержка пасхалочки и для заглавных букв
        "Twelve": "Двенадцать",
        "Thirteen": "Тринадцать",
        "Fourteen": "Четырнадцать"
    }
    for i in dic.items():
        # print(i[0])
        if num == i[0]:
            return i[1]

    for i in dic.items():
        # print(i[0])
        if num == i[1]:
            return i[0]


print(num_translate_adv("One"), num_translate("seven"))
print(num_translate_adv("Один"), num_translate("семь"))
print(num_translate_adv("bOne"), num_translate("восимь"))
