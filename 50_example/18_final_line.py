from io import StringIO
import string

def get_final_line(filename):
    final_line = ''
    for current_line in open(filename):
        final_line = current_line
    return final_line
# print(get_final_line('/etc/passwd'))

def sum_ints(filename):
    total = 0
    for one_line in open("score_space.txt"):
        for one_word in one_line.split():
            if one_word.isdigit():
                total += int(one_word)
    return total

def sum_multi(filename):
    total = 0

    for one_line in open("score_tab.txt"):
        fields = one_line.split()

        if len(fields) != 2:
            continue

        first, second = fields

        if not first.isdigit():
            continue

        if not second.isdigit():
            continue

        total += int(first) * int(second)
    return total

def count_vowels(filename):
    output = dict.fromkeys('aeiou', 0)

    for one_line in open("30word.txt"):
        for one_character in one_line.lower():
            if one_character in output:
                output[one_character] += 1
    return output



print(count_vowel("s"))   


 
