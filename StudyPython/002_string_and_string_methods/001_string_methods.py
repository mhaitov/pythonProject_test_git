empty_string = ''
string_sample = "Hello world WORLD"
string_sample2 = "first letteR is lowErcase"
string_sample3 = "      extra whitespace string      "
german_sample = "der Fluß"
#
# print(string_sample)  # Will return string  (Вернет строку)
# print(string_sample[0])  # Will return first letter of string  (Вернет первую букву строки)
# print(string_sample[6])  # Will return 6th index of string  (Вернет шестой индекс строки)
# print(string_sample[-1])  # Will return last letter of string  (Вернет последнюю букву строки)
# print(string_sample[0:5])  # Will return letters from index 0 to index 4 included
# # (Вернет буквы от индекса 0 до индекса 4 включены)
# print(string_sample[:5])  # Will return letters from beginning to index 4 included
# # (Вернет буквы от начала до индекса 4, включенного)
# print(string_sample[5:])  # Will return letters from index 5 to the end (Вернет буквы с 5 индекса до конца)
# print(string_sample[::-1])  # Will return all letters in backwards order  (Вернет все буквы в обратном порядке)
#
# print(len(string_sample)) # Will return length of string
#
# print("world" in string_sample) # Will return True if given argument is part of the string, or False if not. (not in is opposite)
# # Вернет True, если данный аргумент является частью строки, или False, если нет. (не в противоположность)
#
# print(string_sample.upper())    #Will convert string to uppercase
#
# print(string_sample.lower())    # Will convert string to lowercase
#
# print(german_sample.lower())
# print(german_sample.casefold())   # Will return lowercase string  (Вернет строку в нижнем регистре с Англ. грамматикой)

print(string_sample2.capitalize())  # Will return string with first letter in uppercase
# Вернет строку с первой буквой в верхнем регистре

print(string_sample3.strip())  # Will remove extra whitespaces (begining and end of string)
# (Удалит лишние пробелы (начало и конец строки)

print(string_sample.replace('world', 'people'))