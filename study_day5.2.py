### EESTI ISIKUKOOOD

# def user_menu():
#     user_choice = input('Please choose: \n1.Get data by ID code\n2.Check if ID is valid\n3.Exit\n-->')
#     if user_choice == '1':
#         condition = True
#         while condition:
#             try:
#                 user_id = (input('Please enter ID: '))
#                 int(user_id)
#                 if len(user_id) != 11:
#                     raise UserWarning
#             except UserWarning:
#                 if len(user_id) < 11:
#                     print('Code is too short')
#                 elif len(user_id) > 11:
#                     print('Code is too long')
#             except:
#                 print('Code is not numeric:')
#             else:
#                 condition = False
#                 get_data_by_id(user_id)
#
#
#     elif user_choice == '2':
#         pass
#     elif user_choice == '3':
#         quit()
#     else:
#         print('Choice out of range')
#         user_menu()
#
# def get_data_by_id(idcode):
#     gender_num = idcode[0]
#     by_num = idcode[1:3]
#     bm_num = idcode[3:5]
#     bd_num = idcode[5:7]
#     region_num = idcode[7:10]
#     chk_num = idcode[10]
#
#     if gender_num == '1':
#         cent_id = '18'
#         gend_id = 'Male'
#     elif gender_num == '2':
#
#         cent_id = '18'
#         gend_id = 'Female'
#     elif gender_num == '3':
#         cent_id = '19'
#         gend_id = 'Male'
#     elif gender_num == '4':
#         cent_id = '19'
#         gend_id = 'Female'
#     if gender_num == '5':
#         cent_id = '20'
#         gend_id = 'Male'
#     elif gender_num == '6':
#         cent_id = '20'
#         gend_id = 'Female'
#
#     if bm_num == '01':
#         cent_id = 'January '
#     if bm_num == '02 ':
#         cent_id = 'February '
#     if bm_num == '03':
#         cent_id = 'March '
#     if bm_num == '04':
#         cent_id = 'April '
#     if bm_num == '05':
#         cent_id = 'May '
#     if bm_num == '06':
#         cent_id = '06. '
#     if bm_num == '07':
#         cent_id = 'July '
#     if bm_num == '08':
#         cent_id = 'August '
#     if bm_num == '09':
#         cent_id = 'September '
#     if bm_num == '10':
#         cent_id = 'October '
#     if bm_num == '11':
#         cent_id = 'November '
#     if bm_num == '12':
#         cent_id = 'December '
  #####  PROVERKA VALIDNOSTI
# chk_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
# chk_2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
#
# id_code = '38803160272'
#
# result = 0
# for num in range(0, 10):
#     result += chk_1[num] * int(id_code[num])
#
# if result % 11 != id_code [-1]:
#     result = 0
#     for num in range(0, 10):
#         result += chk_2[num] * int(id_code[num])
#     if result % 11 == int(id_code[-1]):
#         print('ID code is Valid')
#     else:
#         print('ID Code is not valid')
#
# else:
#     print('ID is valid')


# #
# #     print(idcode)
# #     print('You are ' + gend_id)
# #     print('You was born in ' + bd_num + '.' + cent_id + by_num)
# #
# # user_menu()
# #
# # #######38803160272 : ID TEACHER