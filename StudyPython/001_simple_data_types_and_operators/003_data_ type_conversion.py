# Data type conversion in Python (Преобразование типов данных в Python)
int_var = 500
float_var = 50.9
string_var_num = '123.2'
string_var_txt = 'Hello world'

# Converting data types (Преобразование типов данных)
# Convert 'int' into 'float' and backwards
# (Преобразовать int в float и обратно)
print(int_var, type(int_var))
int_var = float(int_var)
print(int_var, type(int_var))

print(float_var, type(float_var))
float_var = int(float_var)
print(float_var, type(float_var))

# Convert 'str' into 'float' or 'int' (Преобразовать строку в float или int)
print(string_var_num, type(string_var_num))
string_var_num = float(string_var_num)
print(string_var_num, type(string_var_num))

print(string_var_num, type(string_var_num))
string_var_num = int(string_var_num)
print(string_var_num, type(string_var_num))

# # Impossible conversion (will cause error) (Невозможное преобразование (вызовет ошибку)
# print(string_var_txt, type(string_var_txt))
# string_var_txt = int(string_var_txt)
# print(string_var_txt, type(string_var_txt))

# Converting into 'boolean' (Преобразование в логическое)
# 'int' into 'bool' - 0 will turn into 'False' other numbers into 'True'
# ('int' в 'bool' - 0 превратится в 'False', другие числа в 'True' )
print(int_var, type(int_var))
int_var = bool(int_var)
print(int_var, type(int_var))

# 'float' into 'bool' - 0.0 will turn into 'False' other numbers into 'True'
# ('float' в 'bool' - 0.0 превратится в 'False', другие числа в 'True' )
print(float_var, type(float_var))
float_var = bool(float_var)
print(float_var, type(float_var))

# 'str' into 'bool' ('str' в 'bool')
str_var = 'True'
# str_var = 'true'
# str_var = 'Hello world!'
# str_var = 'False'  # Will still return 'True'
# str_var = ''  # Only empty 'str' will return 'False'

print(str_var, type(str_var))
str_var = bool(str_var)
print(str_var, type(str_var))
