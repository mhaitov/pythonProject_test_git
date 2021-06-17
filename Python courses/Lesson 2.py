number = 500  # Integer
number2 = 500.0  # Float
text_string = 'Hello world'  # String
text_string2 ="Hello world"
text_string3 ='''Hello world'''
text_string4 ="""Hello world"""

sample_string = "that's"
sample_string2 = 'His name is "John"'

boolean_var = True  # Boolean
boolean_var2 = False

none_type = None  # None type

a = 500
b = 2.0
some_string = 'Hello world'
string2 = 'Planet'

result = 500 // b
print(result)

print(a+b)
print(type(a+b))
print(string2 + some_string)

print(some_string + str(a) +string2)
print(a)
print(float(a))
 print(int(b))
a = 0
b = 2.5
some_string = '500'
text_string = 'Hello world'

print(int(some_string))
print(type(int(float(some_string))))

print(bool(some_string))
user_input = input('Please enter your solar:')
print(user_input)
print(type(user_input))

a = 0
b = 2.5
bool_var = False
text_string = 'Hello world'
none_var = None

print(str(a) + str(b) +str(bool_var) + text_string + str(none_var))
print(a,b,bool_var,text_string,none_var)

name = 'Marian'
age= '24'
print('Hello' + name + ' you are' + age + ' old')
print('Hello', name, 'you are', age, 'old')

name = 'Marian',24
print(name)
a, b, c = 10, 20, 30
print(a)
print(b)
print(c)
#
a = input('Please enter A: ')
b = input('Please enter B: ')
c = input('Please enter C: ')
a, b, c = input('Please enter sides A, B and C. Use space separate: ').split()  # User input of 3 sides
 Half perimeter
half_perimeter = (int(a) +int(b) + int(c)) / 2
print(half_perimeter)
 # Formula to count triangle area
triangle_area = (half_perimeter * (half_perimeter - int(a)) * (half_perimeter-int(b)) * (half_perimeter - int(c)))
print(triangle_area)

string_sample = "that'/'s"
print(string_sample)
#
string_sample2 = 'Hello \tworld'
print(string_sample2)
