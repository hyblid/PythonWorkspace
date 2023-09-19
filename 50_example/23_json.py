import json
import glob
import collections
import csv
import os

#print_scores("C:\\test\\PythonWorkspace")
def print_scores(dirname):
    scores = {}

    for filename in glob.glob(f'{dirname}/9a.json'):
        scores[filename] = {}

        with open(filename) as infile:
            for result in json.load(infile):
                for subject, score in result.items():
                    scores[filename].setdefault(subject, [])
                    scores[filename][subject].append(score)

    for one_class in scores:
        print(one_class)
        for subject, subject_scores in scores[one_class].items():
            min_score = min(subject_scores)
            max_score = max(subject_scores)
            average_score = (sum(subject_scores) / len(subject_scores))

            print(subject)
            print(f'\tmin {min_score}')
            print(f'\tmax {max_score}')
            print(f'\taverage {average_score}')

def json_passwd(filename):
    output = []
    with open("C:\\test\\PythonWorkspace\\passwd.json", 'w', encoding = 'utf-8') as json_file_handler:
        for one_line in open(filename):
            if one_line.startswith('#'):
                continue
            if one_line.strip().startswith('\n'):
                continue

            output.append(tuple(one_line.split(':')))
        
        #Step 4
        json_file_handler.write(json.dumps(output, indent = 4))
    return json_file_handler

def json_passwd_dict(filename):
    fields = ['username', 'password', 'uid', 'gid', 'name', 'homedir', 'shell']
    output = []
    json_file = open("C:\\test\\PythonWorkspace\\passwd.json", 'w', encoding = 'utf-8')
    for one_line in open(filename):
            if one_line.startswith('#'):
                continue
            if one_line.strip().startswith('\n'):
                continue
            output.append(dict(zip(fields, one_line.split(':'))))
    json_file.write(json.dumps(output, indent = 4))
    return json_file

#write_file_info("C:/test/PythonWorkspace/Container", "files.json")
def write_file_info(dirname, outputfile):
    output = []
    for one_filename in glob.glob(f'{dirname}/*'):
        if not os.path.isfile(one_filename):
            continue
        try:
            output.append({'filename': one_filename,
                           'size': os.stat(one_filename).st_size,
                           'mtime': os.stat(one_filename).st_mtime})
        except:
            print(f'Error reading {one_filename}; skipping')
    return json.dump(output, open(outputfile, 'w'))

def read_file_info(filename):
    output = {}
    file_info = json.load(filename)
    return output

write_file_info("C:/test/PythonWorkspace/Container", "files.json")