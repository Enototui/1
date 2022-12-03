# 3.10 Вводим с клавиатуры десятичное число. Необходимо перевести его в шестнадцатиричную систему счисления.
# n = int(input('Введите десятичное число: '))
# s = ''
# h = '0123456789abcdef'
# while n > 0:
#     s = h[n % 16] + s
#     n = n // 16
# print(s)


# 3.11 Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка дробным числом

# text = input("Write some text: ")
# count = 0
# ch = '.'
# eq = ','
# for some in text:
#     if some.isalpha():
#         print("XX It's not a fractional number XX")
#         quit()
#     elif ch in some:
#         count += 1
#     elif eq in some:
#         count += 1
# if count == 1:
#     print("It's a fractional number")
# else:
#     print("XX It's not a fractional number XX")


# 3.12 Вводим с клаиватуры строку. Необходимо вывести строку, где развернём подстроку между первой и последней буквой
# "о" из исходной строки. Если она только одна или её нет - то сообщить, что буква "о" - одна или не встречается.


# 3.12 Вводим с клаиватуры строку. Необходимо развернуть подстроку между первой и последней буквой "о". Если она только одна или её нет - то сообщить, что буква "о" -одна или не встречается
text = str(input('Введите слово: ')).lower()
count = 0
for i in text:
    if i == 'о':
        count += 1
if count > 2:
    min = int(text.find("о")) + 1
    max = int(text.rfind("о"))
    print(text[0:min] + text[min:max][::-1] + text[max:len(text)])
else:
    print('буква "о" одна или не встречается')
