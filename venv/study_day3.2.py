a = 'Hello'
b = ' world'

print(a + b)
print(a + ' ' + b)
print(a + ' ' + 'Planet')

name = 'Marian'
age = 24
profesion = 'student'

print('Hello',name,age)
print('Hello ' + name + '. Your age ' + str(age) + '. You are ' + profesion + ('.'))
name = 'John'
salary = 1500
string_sample = "John's solary is {}"
print(string_sample.format(salary))

string_sample2 = "{1}'s solary is {0}"
print(string_sample2.format( salary, name))

string_sample = "This {product:} costs {price: .2f} euros"
print(string_sample.format(price = 350, product = 'Compucter'))
#
# x = 12312314.94295489257
# y = 21381274.3332
# z = 'Hello world'
#
#  # Vqchislenie fornul
# print('The value of x is %.4f' % x)
#
# emp_name = 'John'
# emp_age = 45
# emp_salary = 1500
#   # Konvertacija starogo stilja PYTHON2
# emp_string = 'Hi my name is %(name)s! I am %(age)s old. My salary is %(salary).2f' %{'name': emp_name,'age': emp_age, 'salary':emp_salary}
# print(emp_string)
#   # Bolee novaja konvertacija (udobnaja)
# emp_string2 = f'Hi my name is {emp_name}! I am {emp_age} old. My salary is {emp_salary:.2f}'
# print(emp_string2)
#
#  # Formatirovanie Ieroglifov
# byte_string = b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'
# print(byte_string.decode('utf-16'))

  # Upravljajushie konstrukcii

 # Tochnost chisel
# number = 90
#
# if number == 200:
#     print('Number is equal to 200')
# elif number < 100:
#     print('Number is smaller than 100')
# elif number % 2 == 0:
#     print('Whole number')
#
# else:
#     print('NOK')
#
#
# print('Good bye')
#   # SHort or LONG term
# sample_string = 'Hello world'
#
# if len(sample_string) > 10:
#     print('Long string')
# else:
#     print('Short sting')
#
# sample_string2 = 'Planet'
# if len(sample_string2) > 10:
#     print('long string')
# else:
#     print('Short string')
#
# id_code = input('Please input your national ID: ')
#
# if len(id_code) == 11:
#     print('Your ID code is ', id_code)
# elif len (id_code) > 11 and id_code.isdigit():
#     print('Code your enter is longer than 11 digitals')
# else:
#     print('Code your enter is shorter than 11 digitals')
#
