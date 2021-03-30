#### RAZLICHNYE REZHIMI V PUTHON
## 'r' - read
## 'a' - append
## 'w' - write
## 'x' - create
## 'r+' -  read and write

##file = open('text_file/lorem.txt', 'r', encoding='utf8')
# file = open('lorem.txt', 'r', encoding='utf8')
# print(file.name)
# print(file.mode)
# print(file.closed)
# file.close()
# print(file.closed)

# with open('lorem.txt', 'r', encoding='utf8') as file2:
#     print(file2.name)
#     print(file2.closed)
#
#
# print(file2.closed)

# with open('lorem.txt', 'r', encoding='utf8') as file:
    # file_content = file.read()
    # print(file_content)
    # print(type(file_content))

    # file_content = file.readlines()


    # file_content = file.read()
    # print(file_content, end='\n\n\n')
    # print('Hello world')
    # # file_content = file.readline()
    # print(file_content)
    # file_content = file.readline()
    # print(type(file_content))

    # size_to_read = 1000
    # file_content = file.read()
    # file_content = file.read(size_to_read)
    # while len(file_content) != 0:
    #     print(file_content)
    #     print(len(file_content))
    #     file_content = file.read(size_to_read)
    #
    # file_content = file.readline()
    # print(file_content)
    # file.seek(2)
    # file_content = file.readline()
    # print(file_content)
#
# with open('lorem_copy.txt', 'w', encoding='utf8') as file:
#     file.write('TEST')


# with open('lorem_copy.txt', 'a', encoding='utf8') as file:
#     file.write('WEST')

# with open('lorem_copy.txt', 'r+', encoding='utf8') as file:
#     data = file.read()
#     print(data)
#     file.write(' \n.HELLO WORLD ')
#
#
# with open('lorem_copy.txt', 'w', encoding='utf8') as file:
#     file.write('Hello world')
#     file.seek(0)
#     file.write('****')
#
#
# ???????????????????????????
# with open('lorem_copy.txt', 'r', encoding='utf8') as file:
#     with open('lorem_copy.txt', 'w', encoding='utf8') as write_file:
#
#         for line in read_file:
#             if int(line[0]) % 2 == 0:
#                 write_file.write(line)
#
#
#### FOR IMAGES
#
# with open('text_files/random-dice.jpg', 'rb', encoding='utf8') as read_file:
#     with open('text_files/random-dice.jpg', 'wb') as write_file:
#         chunk_size = "write the size"
#         data = read_file.read('write tha size or chunk_size')
#         with len(data) > 0:
#             write_file.write(data)
#             data = read_file.read(chunk_size)
#


