# ### Slozhnye tipy dannyh
# empty_list = []
# print(type(empty_list))
#
# world = 'world'
# orld, True, [1, 23, 0.453],None ]
# print(some_list)
# # print(len(some_list))
# # print(some_list[-2])
# # print(some_list[1:5])
# # print(some_list[::-1])
# print(some_list[2])
# some_list[2] = 'Planet'
# print(some_list)
#   #Metod dobavlenija v stroki
# courses = ['History', 'Programing','Math', 'Literatur', 'Physics']
#
# print(len(courses))
# #
#   # Dobavljaet v konec
# courses.append('Art')
# print(courses)
# print(len(courses))
# print(courses[5])
#
#   # Dobavljaet posle ukazannogo slova
# courses.insert(2, 'English')
# print(courses)
# print(courses[5])

#
# print(courses)
# print(courses[2][4])
# courses2 = ['Art','English']
# courses.extend(courses2)
# print(courses)
#   Sposoby udalenija elementov (udaljaet i ne zapominaet element)
# courses.remove('Math')
# print(courses)
#
# deleted = courses.pop(0)
# print(courses)
# print(deleted)
#
#
#   # Perevernut i sohranit'
# print(courses[0])
# courses.reverse()
# print(courses[0])
#
#  ###Perevort na 1 raz
# print(list(reversed(courses)))
# print(courses)
#
# print(courses[::-1])
# print(courses)
# numbers = [1,4,6,8,2,3]
# print(courses)
#
# numbers.sort()
# print(numbers)
#
# courses.sort(reverse=True)
# print(courses)
#
# print(sorted(courses))
# print(courses)
#
# print(sum(numbers))
# print(min(numbers))
# print(max(numbers))
#
# print(min(courses))
# print(max(courses))
# random_list = [[1,9],[3, 4,5],[1,1,1,1]]
# # print(min(random_list))
#
# # print(max(random_list))
# #
# # print(courses.index('Math'))
# # print(courses[courses.index('Math')])
#
# # courses_str = str(courses)
# #
# # print(courses_str)
# # print(courses_str[2])
# #
# # courses_str = ', '.join(courses)
# # print(courses_str)
#
# new_list = courses_str.split('a')
# print(new_list)
# print(len(new_list))
# #
# # print(courses + numbers)
# # courses.extend(numbers)
# # print(courses)
# #
# # courses2 = courses.copy()
# # print(courses)
# # print(courses2)
# #
# # courses[0] = 'Sports'
# # courses2[1] = 'Art'
# #
# # print(courses)
# # print(courses2)
# #
# # print(numbers.count(6))
# # numbers.clear()
# # print(numbers.clear())
#
////////////////////////////

# courses = ('History', 'Programing','Math', 'Literature', 'Physics')
# courses2 = ('Art', 'English')
#
# print(courses.count('History'))
# print(courses.index('History'))
#
# new_courses = courses + courses2
# print(new_courses)
#
# courses_tuple = 1, 2, 'Jungle'
# print(courses_tuple)
#
#
# courses = list(courses)
# print(courses)
#
# courses[0] = 'Art'
# courses = tuple(courses)
# print(courses)
#
# # empty_list = []
# empty_list = list()
# print(type(empty_list))
#
# empty_tuple = (2313)
# print(type(empty_tuple))
#
# empty_tuple = (213123,)
# print(type(empty_tuple))
#
# empty_set = {}
# print(type(empty_set))
#
#
# courses = {'History', 'Programing','Math', 'Literature', 'Physics'}
# courses2 = {'Art', 'English', 'Design', 'Physics', 'History'}
#
# print(courses.intersection(courses2))
#
# print(courses.difference(courses2))
# print(courses2.difference(courses))
#  # Collect
# print(courses2.union(courses))
# #
#   # Vkljuchaet v sebja chast' 1 kusra ko 2
# print(courses.issuperset(courses2))
# print(courses.issubset(courses2))
#
# some_dict = dict()
#
# print(type(some_dict))
#
# x = 5
# student = {'name': 'John', 'age': 32, 'courses': ['Math', 'Art', 'Programing'],1: 'int key',
#            0.2 : 'float key', x: 'variable', 'var key': x, True: 'Hello'}
#
# some_set = {'Art', ' Math'}
#
# print(student)
# print(some_set)
#
# print(student['courses'])
# print(student['age'])
# print(student['courses'][2])
#
# print(student[5])
# print(student[x])
#
# print(student[True])
# print(student.get('courses'))
#
# student['name'] = 'Mary'
# student['phone'] = '555-555-55'
# # print(student)
#
# new_data = {'name': 'Mary', 'age': 27, 'phone': '555-555-555'}
# student.update(new_data)
# print(student)
#
# del student['age']
# deleted = student.pop('name')
# print(student)
# print(deleted)
#
#
# print(len(student))
# print(student.keys())
# print(type(student.keys()))
# print(list(student.keys()))
# print(student.values())
# print(list(student.values()))
# print(student.items())
# print(list(student.items()))
#
#   ##
# people = ['Jack','Mary', 'Anna', 'Oscar']
#
# ###for <variable> in <iterable:
# for person in people:
#     print(person)
#
# print('Finished')
#
# numbers = [1,2,3,4,5,6,7,8,9]
# for num in numbers:
#     print(num ** 2)

# print('Finished')
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for num1 in numbers:
#     x = num1 ** 2
#     if num1 % 2 == 0:
#         print(num1,'Even')
#     else:
#         print(num1, 'Odd')
# print('Fin')
#  ###
# for x in student:
#     print(x)
#
# for key in student:
#     print(student[key])
#
# print(student.items)
#
# for key, value in student.items():
#     print(key, value)
# people = [['John','New-York',35, 'male'],['Alex','Tallinn',20,'male'],['Jane','London',25,'female']]
# for person in people:
#     print(person[0])
#     print(person[1])
#     print(person[2])
#
# # for name,town,age,gender in people:
# #     print(name,town,age,gender)
# #
# for person in people:
#    if gender = ('male'):
#     print('This is ' + '. He lives in' + town + '. He is ' + str(age) + ' years old')
# elif gender = ('female'):
# print('This is ' + '. She lives in' + town + '. She is ' + str(age) + ' years old')
#
#
# ##
# # ####
# number = (1,2,3,4,5,6,7,8,9,10)
# for number in range (0,10):
#     if number % 2 == 0:
#         print(number, 'MODULUS NA 2')
