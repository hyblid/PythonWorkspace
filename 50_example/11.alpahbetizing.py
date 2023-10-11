import operator

PEOPLE = [{'first':'Reuven', 'last':'Lerner','email':'reuven@lerner.co.il'},
          {'first':'Donald', 'last':'Trump','email':'president@whitehouse.gov'},
          {'first':'Vladimir', 'last':'Putin','email':'president@kremvax.ru'}
         ]

config = {'server': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'Py1thon!Xt12'}

numbers1 = [[1,2],[4,3,4],[3,2,1],[4,3,2]]
numbers2 = [1,-2,3,4,-5]


"""Take a list of dicts describing people,
each with first/last/email as keys.

Return a new list of dicts,
sorted first by last name and then by first name.

If passed an empty list, then return an empty list.
"""
def alphabetize_names(list_of_dicts):
    return sorted(list_of_dicts, key=operator.itemgetter('last', 'first'))

"""Given an iterable of numbers, return
a list of those numbers sorted by absolute value.
"""
def sort_absolute(numbers):
    return sorted(numbers, key=abs)


def alphabetizing3(list_of_dicts):
    return sorted(list_of_dicts, key=lambda word : sum(ch in 'aeiou' for ch in word))

"""Given a list of lists, with each list containing zero or more numbers, sort by the
sum of each inner list’s numbers.
"""
def by_vowel_count(one_word):
    total = 0
    for one_character in one_word.lower():
        if one_character in 'aeiou':
            total += 1
    return total

def sort_by_vowel_count(words):
    return sorted(words, key=by_vowel_count)

   
def sort_sum(numbers):
    return sorted(numbers, key=sum)


print(sort_absolute(numbers2))

# print(sort_sum(numbers1))
