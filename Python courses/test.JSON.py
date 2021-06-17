# import json
#
# with open('test.JSON.py', 'r', encoding='utf8') as json_file:
#     data = json.load(json_file)
#     print(data)
#
# for person in data['people']:
#     if person['has licence'] == True:
#         print(person)
#
#     if person['has licence'] == False:
#         del person['has_licence']
#
#     print(person)
#
# with open('test2.json', 'w',encoding='utf8') as new_json_file:
#     json.dump(data, new_json_file, indent=2)
#
# print(data['people'][0].keys())
# ####################################
# import csv
#
# with open('testJSON.csv', 'r', encoding='utf8') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for line in csv_reader:
#         print(line['Name'])
#
#
# #
#     with open('csv_files.text.copy.csv', 'w', encoding='utf8') as write_csv_file:
#
#         fieldnames = ['Name','Date of birth', 'Town']
#         csv_writer = csv.DictReader(write_csv_file, delimiter= ',', lineterminator='\n', fieldnames=fieldnimes)
#         csv_writer.writeheader()
#
#
#         for line in csv_reader:
#             csv_writer.writerow(line)
#
#
#
#
#     csv_reader = csv.reader(csv_file)
#     print(csv_reader)
#     next(csv_reader)
#     for line in csv_reader:
#         print(line[0])
    #
    # with open('testJSON.csv/test_copy.csv', 'w', encoding='utf8') as write_csv_file:
    #     csv_writer = csv.writer(write_csv_file, lineterminator='/n')
    #     print(csv_writer)
    #
    #     # for line in csv.writer:
    #     #     csv_writer.writerow(line)


####


import json
import csv

json_string = '''...'''

csv_string = ''
data = json.loads(json_string)
for key in data['people'][0].keys():
    csv_string += key + ','
csv_string += '\n'
for person in data['people']:
    for x in person.values():
        csv_string += str(x) + ','
    csv_string += '\n'
print(csv_string)
