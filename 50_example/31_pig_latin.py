import collections as collections

def plword(word):
    if word[0] in 'aeiou': 
        return word + 'way'
    return word[1:] + word[0] + 'ay'    

def plfile(filename):
    return ' '.join(plword(one_word)
                for one_line in open(filename)
                    for one_word in one_line.split())
    
def plfile1(filename, func):
    return ' '.join(plword(one_word)
                for one_line in open(filename)
                    for one_word in one_line.split())
    """Use a nested list comprehension to transform a list of dicts into a list of twoelement
(name-value) tuples, each of which represents one of the name-value
pairs in one of the dicts. If more than one dict has the same name-value pair,
then the tuple should appear twice.
    """
list_of_dicts1= [{"one":1},{"two":2},{"three":3},{"two":2}]
list_of_dicts2= [{"name":"howard", "hobbies": {"reading", "eating", "sleeping"}},
                 {"name":"jame", "hobbies": {"reading", "driving", "running"}},
                 {"name":"jennifer", "hobbies": {"reading", "eating", "sleeping"}},
                 {"name":"junny", "hobbies": {"reading", "waling", "sleeping"}},
                 {"name":"sakazaki", "hobbies": {"reading", "eating", "shopping"}},
                 {"name":"kusanaki", "hobbies": {"reading", "playing", "studying"}},
                 {"name":"kenjo", "hobbies": {"reading", "eating", "drinking"}},
                 {"name":"ninka", "hobbies": {"reading", "eating", "waking"}}]
                 
                 
def dicts_to_tuples(list_of_dicts):
    return [one_tuple
            for one_dict in list_of_dicts
            for one_tuple in one_dict.items()]

def most_popular_hobbies(list_of_dicts):
    return collections.Counter([one_hobby
                                for one_person in list_of_dicts
                                for one_hobby in one_person['hobbies']]).most_common(3)

print(most_popular_hobbies(list_of_dicts2))