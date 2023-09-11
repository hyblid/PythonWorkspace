import operator

def alphabetizing1(list_of_dicts):
    return sorted(list_of_dicts, key=operator.itemgetter('last', 'first'))

def alphabetizing2(*list_of_dicts):
    return sorted(list_of_dicts, key=abs)

def alphabetizing3(list_of_dicts):
    return sorted(list_of_dicts, key=lambda word : sum(ch in 'aeiou' for ch in word))

def by_vowel_count(one_word):
    total = 0
    for one_character in one_word.lower():
        if one_character in 'aeiou':
            total += 1
    return total


def sort_by_vowel_count(words):
    return sorted(words, key=by_vowel_count)


def print_kwargs(**kwargs):
    print(kwargs)
    
def sort_sum(numbers):
    return sorted(numbers, key=sum)


PEOPLE = [{'first':'Reuven', 'last':'Lerner','email':'reuven@lerner.co.il'},
          {'first':'Donald', 'last':'Trump','email':'president@whitehouse.gov'},
          {'first':'Vladimir', 'last':'Putin','email':'president@kremvax.ru'}
         ]

config = {'server': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'Py1thon!Xt12'}

numbers = [[1,2],[4,3,4],[3,2,1],[4,3,2]]

print(sort_sum(numbers))
