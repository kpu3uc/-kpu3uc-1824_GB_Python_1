strange_words = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
strange_list = []  # это считается за второй список in place? :)
strange_final = []
i = 0

while i < len(strange_words):
    if strange_words[i].isdigit():
        strange_list.append(i)
    elif '+' in strange_words[i]:
        temp = strange_words[i].replace("+", "")
        if temp.isdigit():
            strange_list.append(i)
    i += 1

# temp = 0

for i in reversed(strange_list):
    if '+' in strange_words[i]:
        temp = strange_words[i].replace("+", "")
        if len(temp) == 1:
            strange_words[i] = "+0" + temp
    if len(strange_words[i]) == 1:
        strange_words[i] = "0" + strange_words[i]
    strange_words.insert(i, '"')
    strange_words.insert(i + 2, '"')

# print(strange_words)

i = 0

while i < len(strange_words):  # я худею с этой конструкции, но работает же! о_О
    if strange_words[i] != '"':
        strange_final += strange_words[i]
        strange_final += " "
        i += 1
    else:
        strange_final += strange_words[i]
        strange_final += strange_words[i + 1]
        strange_final += strange_words[i + 2]
        strange_final += " "
        i += 3

# print(strange_final)

strange_final = "".join(strange_final)  # у меня смутное ощущение что я где-то свернул не туда, но задача выполнена...

print(strange_final)
