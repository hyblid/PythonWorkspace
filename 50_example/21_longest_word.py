import os
import hashlib
import glob
import arrow as arrow
import datetime
import collections as collection


def find_longest_word(filename):
    longest_word = ''
    for one_line in open(filename):
        for one_word in one_line.split():
            if len(one_word) > len(longest_word):
             longest_word = one_word
    return longest_word

def find_all_longest_words(dirname):
    return { filename: find_longest_word(os.path.join(dirname,filename))
    for filename in os.listdir(dirname) if os.path.isfile(os.path.join(dirname,filename))}
    
def md5_files(dirname):
    output = {}
    for one_filename in glob.glob(f'{dirname}/*'):
        try:
            m = hashlib.md5()
            m.update(one_filename.encode())
            output[one_filename] = m.hexdigest()
        except:
            pass
    return output
        
def mod_times(dirname):
    output = {}
    for one_filename in glob.glob(f'{dirname}/*'):
        try:
            mod_time = os.stat(one_filename).ST_MTIME
            output[one_filename] = (arrow.now() - arrow.get(1503636889)).days

        except:
            pass
    return output

def response_counts(filename):
    output = collection.Counter()
    for one_line in open(filename):
        output[one_line.split()[8]] += 1
    return output  

                    
print(response_counts("mini_access_log.txt"))