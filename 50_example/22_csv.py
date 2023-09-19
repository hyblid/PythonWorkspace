import csv
import random
import statistics

def passwd_to_csv(passwd_filename, csv_filename):
    with open(passwd_filename) as passwd, open(csv_filename, 'w') as output:
        infile = csv.reader(passwd, delimiter=':')
        outfile = csv.writer(output, delimiter='\t')
        for record in infile:
            if len(record) > 1:
                outfile.writerow((record[0], record[2]))

def passwd_to_csv(passwd_filename, csv_filename, fields_to_pass='1 2', delimiter='\t'):
    fields_to_pass = [int(one_item) for one_item in fields_to_pass]
    with open(passwd_filename) as passwd, open(csv_filename, 'w') as output:
        infile = csv.reader(passwd, delimiter=':')
        outfile = csv.writer(output, delimiter=delimiter)
        for record in infile:
            if len(record) > 1:
                fields = [one_field for index, one_field in enumerate(record) if index in fields_to_pass]
                outfile.writerow(*fields)

def dict_to_csv(d, csv_filename):
    with open(csv_filename, 'w') as output:
        outfile = csv.writer(output, delimiter=d)
        for key, value in d.items():
            outfile.writerow([key, value, type(value)])
            
def random_sum(csv_filename):
    with open(csv_filename, 'w') as output:
        outfile = csv.writer(output)
        for i in range(10):
            output = []
            for j in range(10):
                output.append(random.randint(10, 100))
            outfile.writerow(output)
    
    for one_line in open("random.csv"):               
        num = [int(one_item) for one_item in one_line.split(",")]
        print(sum(num), statistics.mean(num))
        
passwd_to_csv("passwd.txt", "passwd.csv")