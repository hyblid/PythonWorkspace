import string

def get_sv(filename):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return { word.strip() for word in open(filename) if vowels < set(word.lower()) }

def different_shells(filename):
    return { one_line.split(':')[-1].strip()
            for one_line in open(filename)
            if not one_line.startswith(('\n', '#')) }

def word_lengths(filename):
    return { len(one_word)
             for one_line in open(filename)
             for one_word in one_line.split() }
    
def letters_in_names():
    list_of_names = ["howard", "jennifer", "james", "junny"]
    return { one_letter
             for one_letter in ''.join(list_of_names)
             if one_letter in string.ascii_letters }
    
print(letters_in_names())
