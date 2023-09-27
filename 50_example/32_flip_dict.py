import glob
import os

d = {'a':1, 'b':2, 'c':3}
def flip_dict(dicts):
    return {value:key for key, value in dicts.items()}

text = "this is an easy test,"
def word_vowels(s):
    return {one_word: vowel_count(one_word)
            for one_word in s.split()}

def vowel_count(word):
    total =0
    for w in word.lower():
        if w in "aioeu":
            total += 1
    return total

def file_info(dirname):
    return {one_filename: os.stat(one_filename).st_size
            for one_filename in glob.glob(f'{dirname}/*')
            if os.path.isfile(one_filename)}

def read_config(filename):
    return {one_line.split('=')[0]: one_line.split('=')[1].strip()
            for one_line in open(filename)}

print(read_config("config.txt"))