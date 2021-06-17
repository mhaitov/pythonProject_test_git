# ## Propis v stolbik
# for letter in 'Hello world':
#     print(letter)
#
#
# ### Uslovno beskonechnyj cykl
#
# while True:
#     print('I can\'t stop')
# ###Cikl While  - posle nego dolwno byt uslovie
#
# condition =  True
# cnt = 0
#
# while condition:
#     if cnt < 1000:
#         print(cnt)
#         cnt = cnt + 1
#
#     elif cnt == 1000:
#         condition = False
#
# print('Fin')
#
# condition = True
# while condition:
#     user_input = input(' Choose: \n1: Check ID\n2: Exit\n-->')
#     if user_input == '1':
#         input_id = input('Please enter ID')
#         if len(input_id) != 11:
#             print('Error')
#         else:
#             print(input_id)
#             condition = False
#     elif user_input == '2':
#         condition = False
#
# distance_to_target = float(input('Please enter distance in meters: '))
# current_position = 0
# step_cnt = 0
#
# while current_position < distance_to_target:
#     current_position = current_position + 0.5
#     # step_cnt = step_cnt +1
#     # step_cnt += 1
#     print(current_position)
#
# print(step_cnt)
# print('FIN')
#
# # 'PASS' zamenjaet code, no nichego ne delaet (pomogaet delat skip bez owibki)
#
# condition = True
#
# while condition:
#     pass

  ## 'BREAK' razryvaet cikl
# cnt = 0
# while cnt < 1000:
#     cnt += 1
#     print(cnt)
#     if cnt == 1000:
#         break
#     print('TEST')
#
# print('FIN')

#
# condition = True
# cnt = 0
# while condition:
#     cnt += 1
#     if cnt == 1000:
#         condition = False
#     print('TEST')
#
#   ## Continue ( prodolzhit cikl nachav s nachalo)
# while True:
#     user_input = input('Please choose: \n1:Print\n0:Exit')
#     if user_input == '1':
#         print('All is good')
#         continue
#     elif user_input == '0':
#         break
#     else:
#         pass
#     print('test')
#
#
# print('you have exited while logo')
#   ### First example
# for letter in 'Python':
#     if letter == 'h':
#         continue
#     print('Current letter :', letter)
#
#
# ##
# ##########
# # "LIST" razbivaet po bukvam v skobkah
# somer_string = 'Hello world'
# print(list(somer_string))
# ## 'DEF" oboznachenie funkcii
# def number_squares(x):
#     return x ** 2
#
# def number_double(x):
#     return x * 2
#
# def number_triple(x):
#     return x * 3
#
# for number in range(0, 101):
#     print(number_squares(number))  # print(number **2)
#     print(number_double(number))   # print (number *2)
#     print(number_triple(number))   # print (number *3)
#     print()
#
# #
# # messange = number_squares()
# # # print(number_squares())
# # print(messange)
#
# def number_power(x, y):
#     return x ** y
#
# print(number_power(10, 10))
#
#
# x = 10
#
# def squares(x):
#     x = 5
#     return x ** 2
#
# print(x)
#
# print(squares(x))
#
# def square():
#     x = 5
#     return x ** y
#
# y = 2
# print(square())
# ## Kostrukcija poiska oshibok
#
# user_iput = input('Enter number: ')
# if user_iput.isdigit() == True:
#     result = float(user_iput) ** 2
#     print(result)
#
#
# print('Hello world')
# ## 'TRY AND EXCEPT" objazatelnye
# user_input = input('Enter number: ')

# try:
#     result = float(user_input) ** 2
#     print('TEST')
# except:                            #  'EXCEPT' v sluchae owibki
#     print('Error')
# else:
#     print(result)
# finally:
#     print('FIN')
#
#
# user_input = input('Enter number: ')
#
# try:
#     # result = float(user_input) ** 2
#     user_input.insert('Hello')
#
# except  ValueError:
#     print('Error')
# except AttributeError:
#     print(result)
# finally:
#     print('FIN')

# print('Hello world')
#
#
# user_input = input('Enter ID: ')
#
# try:
#     int(user_input)
#     if len(user_input) !=11:
#         raise UserWarning
# except UserWarning:
#     print('Code your entred is not 11 digits long ')
# except:
#     print('ID your entered is not numeric ')

# //////////////////////////////

### EESTI ISIKUKOOOD

def user_menu():
    user_choice = input('Please choose: \n1.Get data by ID code\n2.Check if ID is valid\n3.Exit\n-->')
    if user_choice == '1':
        condition = True
        while condition:
            try:
                user_id = (input('Please enter ID: '))
                int(user_id)
                if len(user_id) != 11:
                    raise UserWarning
            except UserWarning:
                if len(user_id) < 11:
                    print('Code is too short')
                elif len(user_id) > 11:
                    print('Code is too long')
            except:
                print('Code is not numeric:')
            else:
                condition = False
                get_data_by_id(user_id)

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
#     #
#     # if gender_num == '1':
    #     cent_id = '18'
    #     gend_id = 'Male'
    # elif gender_num == '2':
    #
    #     cent_id = '18'
    #     gend_id = 'Female'
    # elif gender_num == '3':
    #     cent_id = '19'
    #     gend_id = 'Male'
    # elif gender_num == '4':
    #     cent_id = '19'
    #     gend_id = 'Female'
    if gender_num == '5':
        cent_id = '20'
        gend_id = 'Male'
    elif gender_num == '6':
        cent_id = '20'
        gend_id = 'Female'

    if bm_num == '01':
        cent_id = 'January '
    if bm_num == '02 ':
        cent_id = 'February '
    if bm_num == '03':
        cent_id = 'March '
    if bm_num == '04':
        cent_id = 'April '
    if bm_num == '05':
        cent_id = 'May '
    if bm_num == '06':
        cent_id = '06. '
    if bm_num == '07':
        cent_id = 'July '
    if bm_num == '08':
        cent_id = 'August '
    if bm_num == '09':
        cent_id = 'September '
    if bm_num == '10':
        cent_id = 'October '
    if bm_num == '11':
        cent_id = 'November '
    if bm_num == '12':
        cent_id = 'December '
  ####  PROVERKA VALIDNOSTI
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
#
#
#
#     print(idcode)
#     print('You are ' + gend_id)
#     print('You was born in ' + bd_num + '.' + cent_id + by_num)
#
# # user_menu()
# #
# #######38803160272 : ID TEACHER