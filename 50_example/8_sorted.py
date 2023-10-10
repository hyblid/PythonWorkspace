import string

def strsort1(a_string):
    return ''.join(sorted(a_string))

def strsort2(full_name):
    return ','.join(one_word
                     for one_word in sorted(full_name.replace(",", "").split()))
    
def strsort3(filename):
    output = ''
    for one_line in open(filename): # read each line
        for one_word in one_line.split(): # split each word
            if not one_word.isalpha(): # check word is alphabet
                continue
            if one_word > output: #get the lastest word
                output = one_word
    return output 

def strsort4(filename):
    output = ''
    for one_line in open(filename):
        for one_word in one_line.split():
            if not one_word.isalpha():
                continue
            if len(one_word) > len(output): #get the longest words
                output = one_word
    return output 

print(strsort2("Tom Dick Harry,"))