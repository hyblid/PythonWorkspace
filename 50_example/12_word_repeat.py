from collections import Counter
from collections import defaultdict
import operator

WORDS = ['this', 'is', 'an','elementary', 'test', 'example']

"""The (1)[0][1]. It means the following:
1 We only want the most commonly appearing letter, returned in a one-element
list of tuples.
2 We then want the first element from that list, a tuple.
3 We then want the count for that most common element, at index 1 in the tuple.
"""
def most_repeating_word(words):
    return max(words, key=most_repeating_letter_count)
def most_repeating_letter_count(word):
    return Counter(word).most_common(1)[0][1]

def most_repeating_word2(words):
    return max(words, key=most_repeating_vowel_count)
def most_repeating_vowel_count(word):
    vowels_in_word = ''
    for one_character in word.lower():
        if one_character in 'aeiou':
            vowels_in_word += one_character
    #return integer
    return Counter(vowels_in_word).most_common(1)[0][1]
 
#shells return dict and operator.temgetter(1) get value
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
       
print(shells_and_users_by_popularity("etc_password.txt"))