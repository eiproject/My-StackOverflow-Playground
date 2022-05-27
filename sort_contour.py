# import csv
# with open('test.csv', 'r') as data, open('output.csv','a', newline='') as output:    
#     reader = csv.reader(data)
#     writer = csv.writer(output)

#     for line in reader:
#         writer.writerow(line)

# with open('test.csv', 'r') as data, open('output.txt','w') as output:
#     bad_size = False
#     bad_line = None
#     for line in data:
#         columns = line.split(',')
        
#         if (len(columns) - 1) < 3:
#             if bad_size:
#                 line = bad_line.rstrip('\n') + line
#                 bad_size = False
#             else:
#                 bad_size = True
#                 bad_line = line
#         if not bad_size:
#           output.write(line)

with open('test.csv', 'r') as data, open('output.csv','w') as output:                          
    for line in data:
        if not line.endswith(',\n'):
            line = line.rstrip()
        output.write(line)