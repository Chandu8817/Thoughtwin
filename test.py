# import csv

# with open('demodata.csv', mode='r') as csv_file:

#     csv_read= csv.reader(csv_file)

#     for row in csv_read:
#         print(row)



































# with open('demodata.txt', mode='r') as csv_file:

#     csv_read = csv.DictReader(csv_file,delimiter=',')
#     line_count=0
#     for row in csv_read:
#         if line_count ==0:
#             print(','.join(row))
#             line_count += 1
       
#         print(row['name'],row['department'],row['birthday month'])
#         line_count += 1
#     print(line_count)

# with open('demodata.txt') as csv_file:

#     csv_reader= csv.reader(csv_file, delimiter=',')

#     line_count=0

#     for row in csv_reader:

#         if line_count==0:
#             print(f'colunm names are {",".join(row)}')

#             line_count += 1

#         else:
#             print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#             line_count += 1
#     print(f'Processed {line_count} lines.')





