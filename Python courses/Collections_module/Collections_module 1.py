# from collections import Counter
#
# sample_string = 'aaaaaaaaaaaaaaaaaabckkkksdfasfdasf'
# my_counter = Counter(sample_string)
#
# print(my_counter)
# print(my_counter.values())
# print(my_counter.most_common(4))
# print(list(my_counter.elements()))
# print(list(sample_string))
#######################
# #
# #
# # from collections import namedtuple
# #
# # Point = namedtuple('Point', 'x,y')
# # pt = Point(56, 67)
# # print(pt)
# # print(type(pt))
# #
# ###################################3
# #
# # from collections import OrderedDict
# #
# # some_dict = {'Name': 'John', 'Surname': 'Smith', 'Age':30}
# #
# # # ## OLD VERSION PYTHON
# # # ordered_dict = OrderedDict()
# # # ordered_dict['Name'] = 'Jack'
# # # ordered_dict['Surename'] = 'Smith'
# # #
# # # print(some_dict)
# # #
# # ###########################
# #
# # default_dict = defaultdict(list)
# # default_dict['a'] = 1
# # default_dict['b'] = 2
# # print(default_dict)
# #
# #
# ##################################
#
# from collections import deque
#
# d = deque()
# print(d)
# d.append(1)
# d.append(2)
# d.append(3)
# print(d)
#
# d.appendleft(5)
# print(d)
# #
# # d.pop()
# # print(d)
# #
# # # d.popleft()
# #
# # pooped_item = d.popleft()
# # print(pooped_item)
# # print(d)
# #
# # d.extend([1, 2, 3, 4])
# # print(d)
# d.rotate()
# print(d)
