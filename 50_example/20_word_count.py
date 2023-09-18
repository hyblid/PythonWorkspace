import os
import string
import collections as collection
import glob


def wordcount(filename):
    counts = {'characters': 0,
              'words': 0,
              'lines': 0}
    unique_words = set()

    for one_line in open(filename):
        counts['lines'] += 1
        counts['characters'] += len(one_line)
        counts['words'] += len(one_line.split())
        unique_words.update(one_line.split())
        counts['unique words'] = len(unique_words)
    for key, value in counts.items():
        print(f'{key}: {value}')

def count_certain_words():
    s = input("Enter a filename, and then words you want to track: ").strip()

    if not s:
        return None

    filename, *words = s.split()

    counts = dict.fromkeys(words, 0)

    for one_line in open(filename):
        for one_word in one_line:
            if one_word in counts:
                counts[one_word] += 1
    return counts

    
def file_sizes(dirname):
    counts = {one_filename: os.stat(one_filename).st_size
              for one_filename in glob.glob(f'{dirname}/*')
              if os.path.isfile(one_filename)}

    print(counts)
 
def most_common_letters(dirname):
    counts = collection.Counter()

    for one_filename in glob.glob(f'{dirname}/*'):
        try:
            for one_line in open(one_filename):
                counts.update(one_line)
        except:
            pass

    return list(dict(counts.most_common(5)).keys())
 
 
    
print(most_common_letters("Container"))