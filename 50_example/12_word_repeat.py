from collections import Counter
from collections import defaultdict
import operator

WORDS = ['this', 'is', 'an','elementary', 'test', 'example']

"""The (1)[0][1]. It means the following:
1 We only want the most commonly appearing letter, returned in a one-element
list of tuples.
2 We then want the first element from that list, a tuple.----? [0]
3 We then want the count for that most common element, at index 1 in the tuple-------> value.
[[('t', 1),('h', 1),('i', 1)],
 [('i',1),('s',1)],
 [('a',1),('n',1)],
 [('e',3),('l',1),('m',1),('n',1),('t',1),('a',1),('r',1),('y',1)],
 [('t',2),('e',1),('s',1)],
 [('e',2),('x',1),('a',1),('m',1),('p',1),('l',1)]]
(1) one element [('e',3),('l',1),('m',1),('n',1),('t',1),('a',1),('r',1),('y',1)]
[0] first tuple ('e',3)
[1] first tuple's index 1 ---> 3
"""
def most_repeating_word(words):
    return max(words, key=most_repeating_letter_count)
def most_repeating_letter_count(word):
    return Counter(word).most_common(1)[0][1]

def most_repeating_vowel_count(word):
    vowels_in_word = ''
    for one_character in word.lower():
        if one_character in 'aeiou':
            vowels_in_word += one_character
    #return integer
    return Counter(vowels_in_word).most_common(1)[0][1]
 
#shells return dict and operator.itemgetter(1) get value
def shells_by_popularity(filename):
    shells = Counter(one_line.split(':')[-1].strip()
                     for one_line in open(filename)
                     if not one_line.startswith(('#', '\n')))
    return sorted(shells.items(),
                  key=operator.itemgetter(1), reverse=True)
"""
[('/usr/bin/ksh', ['root', 'invscout', 'paul', 'jdoe']),
('', ['daemon', 'bin', 'sys', 'adm', 'uucp', 'guest','nobody', 'lpd']), 
('/bin/false', ['lp']), 
('/usr/sbin/uucp/uucico', ['nuucp'])]
"""    
def shells_and_users_by_popularity(filename):
    shells = defaultdict(list)
    for one_line in open(filename):
        if one_line.startswith(('#', '\n')):
            continue
        username, *rest, shell = one_line.strip().split(':')
        shells[shell].append(username)
    return sorted(shells.items(), key=len)    

print(most_repeating_word(WORDS))       
# print(shells_and_users_by_popularity("etc_password.txt"))

# print(Counter('abcabcabbbc').most_common(1)[0])

"""Get the most common elements: most_common()
The Counter's most_common() method returns a list of (element, count) tuples sorted by counts.

l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']

c = collections.Counter(l)
print(c)
# Counter({'a': 4, 'c': 2, 'b': 1}) ---> dictionaries

print(c.most_common())
# [('a', 4), ('c', 2), ('b', 1)] ---> list of tuples

print(c.most_common(1))
# [('a', 4)]
source: collections_counter.py
You can access the most frequent element via [0] and the least frequent via [-1] indices. To extract only the element or the count, specify the index accordingly.

print(c.most_common()[0])
# ('a', 4)

print(c.most_common()[-1])
# ('b', 1)

print(c.most_common()[0][0])
# a

print(c.most_common()[0][1])
# 4
    """