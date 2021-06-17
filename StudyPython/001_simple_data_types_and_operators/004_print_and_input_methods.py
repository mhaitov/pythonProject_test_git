# Print in input methods

# Printing to command line (Печать в командную строку)
# print() method prints to commadline ( метод print () выводит в командную строку )
print('Hello world')

# different type of data can be printed (можно распечатать разные типы данных)
print(100)   # int
print(0.2)   # float
print('Hello world')   # str
print(True)   # bool

a = 'String inside variable'
print(a)  # variable


# multiple data types in one print() ( несколько типов данных в одном print ())
# ',' separated values don't have to be strings (',' значения, разделенные не обязательно строками)
# Python converts itself  (Python преобразует сам себя )
print(100, 0.2, 'Hello world', True)

# adding items with '+' requires 'str' type items  (# добавление элементов с '+' требует элементов типа 'str')
# conversion must be done first (сначала необходимо выполнить преобразование )
print(str(100) + ' ' + str(0.2) + ' ' + 'Hello world' + str(True) + ' ' + a)


# User input (Пользовательский ввод)
# input() method requires user to enter something  (метод input () требует, чтобы пользователь что-то ввел)
# before program continues (перед продолжением программы )
print(input())

# placeholder can be added to input()  (заполнитель может быть добавлен к input ())
print(input('Please enter some text: '))

# input() value can be stored in variable  (значение input () может быть сохранено в переменной )
user_input = input('Please enter some text: ')
print(user_input)

print(input('Enter u ID:'))