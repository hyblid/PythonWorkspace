'''
If the word begins with a vowel (a, e, i, o, or u), add “way” to the end of the
word. So “air” becomes “airway” and “eat” becomes “eatway.”
If the word begins with any other letter, then we take the first letter, put it on
the end of the word, and then add “ay.” Thus, “python” becomes “ythonpay”
and “computer” becomes “omputercay.”
'''
import string

def pig_latin1(word):
        if word[0] in "a,e,i,o,u":
            return f"{word}way"
        return f'{word[1:]}{word[0]}ay' 
    
def pig_latin2(word):
        if word[0].lower() in "a,e,i,o,u":
            output =  f"{word}way"
        else:
            output = f'{word[1:]}{word[0]}ay' 
     
        if word[0] in string.ascii_uppercase:
            output= word.capitalize()
        
        return output
    
def pig_latin3(word):
    punctuation = ''
    if word[-1] in '.?!':
        punctuation = word[-1]
        word = word[:-1]

    if word[0].lower() in 'aeiou':
        output = f'{word}way'

    output = f'{word[1:]}{word[0]}ay'

    return output + punctuation

def pig_latin4(word):
    number_of_vowels = len(set(word) & set('aeiou'))

    if number_of_vowels > 1:
        return f'{word}way'

    return f'{word[1:]}{word[0]}ay' 
            
print(pig_latin4("wine"))