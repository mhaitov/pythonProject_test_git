import csv

with open('csv_files/test_copy.csv', 'r', encoding='utf8') as csv_file:
    csv_reader = csv.reader(csv_file)
    # for line in csv_reader:
    #     print(line)
    with open('csv_files/test_copy.csv', 'w', encoding='utf8') as csv_file:
        csv_writer = csv.writer(write.csv_file, lineterminator='\n', delimiter='-')

        for line in csv_reader:
            csv_writer.writerow(line)
