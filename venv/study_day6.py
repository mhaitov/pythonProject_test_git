# def squares(x):
#     return x ** 2
#
# numbers = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]
# numbers_list = []
#
#
# for x in numbers:
#     numbers_list.append(squares(x))
#
# print(numbers_list)
### OR
# result = list(map(squares, numbers))
# print(result)

### OR
# print([squares(x) for x in numbers ])
# ////
# print([squares(x) for x in numbers if x % 2 == 0])
#
#
# data1 =[100,200,300,400,500,600,700,800,900]
# data2 = ['Mon','Tue','Wed','Thu','Fri','Sat', 'Sun']
# data3 = [1,2,3,4,5,6,7]
#
# ### 'ZIP' soedenjaet pary
# combination = zip(data1, data2, data3)
# # print(list(combination))
#
# #### OR
# # for x in range(0, 7):
# #     data3.append([data1[x], data2[x], data3[x]])
# # print(data3)
# #
# # def func(num1, num2):
# #     return num1 * num2
# #
# # print(list(map(func,data1, data3)))
# ### OR
# # for x,y,z in combination:
# #     print(func(x,z))
# #
# #
#
#######
###Rasmotrenie bibliotek####
# import calendar
# ####
# # w= v shirinu
# # l= v dlinnu
# # c= rastojanie mewdu kalendarjami
# # m= kol-vo mesjacrv v stroke
#
# # print(calendar.month(2021, 3, w=1, l=1))
#
# # print(calendar.calendar(2021))
#
# print(calendar.weekday(2021,3, 28))
#
# print(calendar.isleap(2020))
#
# print(calendar.leapdays(2000, 2021))
#####
# print('Mon Thu\n 1 2')
#
# #######
# import time
#
# start = time.time()
# # time.sleep(7)
#
#
# time.sleep(7)
# print('Hello world')
# time.sleep(7)
# print('Hello world')
# ###Time schitaetsja s 01.01.1970(nachalo epohi)
# print(time.time())
#
# print(time.asctime())

# print(time.gmtime())
# print(type(time.gmtime()))
#
# print(time.gmtime()[0])
#
# now = time.gmtime()
#
# print(now[2])
# stop = time.time()
# print(stop - start)
#######
# import datetime
#
# date = datetime.date(2018,7, 22)
# # print(date)
# # print(type(date))
#
# today = datetime.date.today()
# # # print(today)
# # #
# # # print(today - date)
# #
# # print(today.year)
# # print(type(today.year))
# #
# # print(date.day)
# # print(today.month)
#
# print(today.weekday()) # 0-6
# print(today.isoweekday()) # 1-7
#
# #tdelta =
# #
# # today - some_date = timedelta
# # today = timedelta + some_date
# # some_date =today - timedata
#
# # tdelta = datetime.timedelta(days=7, hours=,min=,microseconds=)
# tdelta = datetime.timedelta(days=7)
# print(today + tdelta)
#
#
# bday = datetime.date(2021,6,29)
# till_bday = bday - today
# print(till_bday)
#
# print(type(till_bday))
# print(till_bday.seconds)
# print(till_bday.total_seconds())
####
# import datetime
#
# t = datetime.time(13,6,19,)
# print(t)
# print(type(t))
#
# print(t.hour)
# print(t.second)
#
# dt = datetime.datetime(2020, 11, 30, 18, 50, 20, 1000)
# # print(dt)
# print(dt.date())
# print(dt.time())
# dt_today = datetime.datetime.today()
# # print(dt_today)
# # dt_now = datetime.datetime.now()
# # print(dt_now)
#
# print(dt_today.strftime('%B, %d-%m-%y, %Y'))
#
# dt_string = 'November 30, 2020'
# dt_string2 = 'Sun, 28.03.2021, March, 14:29:30'
#
# str_to_date = datetime.datetime.strptime(dt_string,'%B %d, %Y')
# print(str_to_date)
# print(type(str_to_date))
#
#
# str_to_date2 = datetime.datetime.strptime(dt_string2, '%a, %d.%m.%Y, %B, %H:%M:%S')
# print(str_to_date2)
