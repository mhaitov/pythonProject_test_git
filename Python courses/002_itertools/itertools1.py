import itertools
# # # ######### BESKONECNYJ CIKL (ne probuj)
# # # counter = itertools.count()
# # # #
# # # # for x in counter:
# # # #     print(x)
# # # #
# #
# # counter = itertools.count()
# #
# # # counter = 0
# # # while counter < 100:
# # #     print(counter)
# # #     counter +=1
# # #
# # # data = [100, 200, 300, 400, 500, 600, 700, 800]
# # # data2 = [1 ,2 ,3 ,4 ,5 ,6 ,7 , 8]
# # #
# # # pairs = zip(data, data2)
# # # print(list(pairs))
# # # ###### prostejshij schetchik
# # # data = [100, 200, 300, 400, 500, 600, 700, 800]
# # # new_list = zip(counter, data)
# # # # print(list(new_list))
# # #
# # # for x in list(new_list):
# # #     if x[0] % 2 == 0:
# # #         print(x)
# # #
# # #
# # #sozdanie dlinnyh par
# # data = [100, 200, 300, 400, 500, 600, 700, 800]
# #
# # data2 = zip(data, range(10))
# # print(list(data2))
# #
# # data3 = itertools.zip_longest(data, range(10), range(12))
# # print(list(data3))
# #
# # data3 = list(data3)
# # for x in data3:
# #     print(type(x[0], type(x[1])))
#
# ##### schestchik celyh i drobnyj chisel
# # counter = itertools.count(start=8, step=-0.5)
# # print(next(counter))
# # print(next(counter))
# # print(next(counter))
# # print(next(counter))
# #
# # counter = itertools.cycle(['On', 'Off', 1, 2])
# # print(next(counter))
# # print(next(counter))
# # print(next(counter))
# # print(next(counter))
# # print(next(counter))
# # print(next(counter))
# # print(next(counter))
# # print(next(counter))
# #
# # counter = itertools.repeat(123123, times=5)
# # print(next(counter))
# # print(next(counter))
# # print(next(counter))
# # print(next(counter))
# # print(next(counter))
# # print(next(counter))
# #
# #
# # def power_number(x, y):
# #     return x ** y
# # #
# # # result = map(power_number, range(10), range(10))
# # # print(list(result))
# #
# # result = map(power_number,[1, 2, 3], [1, 2, 3])
# # print(list(result))
# #
# # result2 = itertools.starmap(power_number, [(2, 8),(3, 3),(4, 2)])
# # print(list(result2))
#
# letters = ['a', 'b', 'c', 'd']
# numbers = [1, 2, 3, 4]
# names = ['Jack', 'Marry']
# numbers2 = [4, 5, 4, 3, 2, 1, 0, 4]
# selectors = [True, False, False, True]
#
# # # # #### combination hoatichno
# # # # result = itertools.combinations(letter, 2)
# # # # for item in result:
# # # #     print(item)
# # # #
# # # # ######### porjadok imeet znachenie (bez povtornyh elimentov)
# # # # result2 = itertools.permutations(letter, 2)
# # # # for item in result2:
# # # #     print(item)
# # # # ########### uporjadochenno (s povtornymi elementami)
# # # # result3 = itertools.product(numbers, repeat=2)
# # # # for item in result3:
# # # #     print(item)
# # # #
# # # # ######### net porjadka i net parnyh elementov
# # # # result4 = itertools.combinations_with_replacement(numbers, 2)
# # # # for item in result4:
# # # #     print(item)
# # # # ########## perechislenie (korotkaja forma zapisi)
# # # # combined = itertools.chain(letters, numbers, names)
# # # # print(list(combined))
# # # # #
# # # # # for item in combined:
# # # # #     print(item)
# # #
# # # ########## brat srezy so spiskov
# # # # combinate = itertools.islice(letters, 2, 4)
# # # combinate = itertools.islice(range(10), 2, 10, 3)
# # # for item in combinate:
# # #     print(item)
# #
# # ############ udobno iterirovat faily
# # with open('demo_logo.txt', 'r', encoding='utf8') as file:
# #     log_header = itertools.islice(file, 3)
# #     for item in log_header:
# #         print(item)
#
# def more_than_two(x):
#     if x >2:
#         return  True
#     return False
#
# letters = ['a', 'b', 'c', 'd']
# numbers = [1, 2, 3, 4]
# names = ['Jack', 'Marry']
# numbers2 = [4, 5, 4, 3, 2, 1, 0, 4]
# selectors = [True, False, False, True]
# # #
# # # result = itertools.compress(letters, selectors)
# # #
# # # for item in result:
# # #     print(item)
# #
# # result = filter(more_than_two, numbers2)
# # print(list(result))
# #
# # result2 = itertools.filterfalse(more_than_two, numbers2)
# # print(list(result2))
#
# result1 = itertools.dropwhile(more_than_two, numbers2)
# print(list(result1))
#
# result1 = itertools.takewhile(more_than_two, numbers2)
# print(list(result1))
#
# ###### pribovljaet kawdoe posledujuwee chislo
# result3 = itertools.accumulate(numbers2)
# for item in result3:
#     print(item)
