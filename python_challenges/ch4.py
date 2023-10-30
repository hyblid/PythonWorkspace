"""Q.4.2.a.Based on a string, implement a validation for binary numbers and a conversion to it. 
Repeat both for hexadecimal numbers."""
"""Q.4.2.1.a.Write function is_binary_number(number) that checks that a given string consists 
only of the characters 0 and 1 (i. e., represents a binary number)."""
def is_binary_number(number):
    for n in number:
        if n not in ["0","1"]:
            return False
    return True
# print(is_binary_number("10101"))
"""Q.4.2.1.b.Write function binary_to_decimal(number) that 
converts a (valid) binary number represented as a string to the corresponding decimal number."""
def binary_to_decimal(number):
    sum = 0
    for index, n in enumerate(reversed(number)):
        sum += int(n) * pow(2, index)
    return sum    
# print(binary_to_decimal("111"))        
"""Q.4.2.1.c.Write the entire conversion again, but this time for hexadecimal numbers."""
def hex_to_decimal(number):
    sum = 0
    for index, n in enumerate(reversed(number)):
        if n in ["A","B","C","D","E","F"]:
            n = ord(n) - 55
        sum += int(n) * pow(16, index)
    return sum
# print(hex_to_decimal("AB"))
"""Q.4.2.Write function join (values, delimiter) that joins a list of strings with the given delimiter and returns it as one string. 
Implement this yourself without using any special Python functionality like join() provided by type str."""
def join(values, delimiter):
    str = ""
    for v in values:
        str += v + delimiter
    return str
# print(join(["hello", "world", "message"], "+++"))
"""Q.4.3.Write function reverse(text) that reverses the letters in a string and returns it as a result. 
Implement this yourself; in other words, do not use any special Python functionality, such as [::-1]."""
def reverse(text):
    result = ""
    for index in range(len(text)-1,-1,-1):
        result += text[index]
    return result
# print(reverse("hello"))

"""Q.4.4.a.Write function is_palindrome(text) that checks whether a given string is a palindrome regardless of case. 
A palindrome is a word that reads the same from the front and the back.""" 
def is_palindrome(text):
    original_str = text
    result = ""
    for index in range(len(text)-1,-1,-1):
        result += text[index]
    return original_str.lower() == result.lower()
# print(is_palindrome("ABCBX"))

"""Q.4.4.b.Write an extension that does not consider spaces and punctuation as relevant, 
allowing whole sentences to be checked, such as this one:"""
import string
def is_palindrome_sentence(text):
    sentence_test = text.split(" ")
    for s in sentence_test:
        s = remove_puntuation(s)
        print(f"{s} is palidrome: {s == reversed(s)}")

def remove_puntuation(word):
    result = ""
    for w in word:
        if w in string.punctuation:
            result += ""
        else:
            result +=w
    return result
# print(is_palindrome_sentence("Was it a car or a cat I saw?"))    
"""Q.4.5 Determine if a given string contains duplicate letters. 
Uppercase and lowercase letters should not make any difference. 
Write function check_no_duplicate_chars(text) for this purpose."""
def check_no_duplicate_chars(text):
    result = set()
    for current_char in text.upper():
        if current_char in result:
            return False
        result.add(current_char)
    return True
# print(check_no_duplicate_chars("Otta"))
"""Q.4.6.Write function remove_duplicates(text) that keeps each letter only once in a given text, 
thus deleting all subsequent duplicates regardless of case. However, 
the original order of the letters should be preserved."""
def remove_duplicates(text):
    result = set()
    for current_char in text:
        if current_char not in result:
            result.add(current_char)
    return "".join(result)
# print(remove_duplicates("bananas"))
"""Q.4.7.a.Write function capitalize(text) that converts a given text into an English 
title format where each word starts with a capital letter.
You must explicitly not use the built-in function title() of the type str."""
def capitalize(text):
    result = "" 
    for t in text.split():
            if len(t) == 1:
                result += t[0].upper() + " "
            else:    
                t = t[0].upper() + t[1:]
                result += t + " "
    return result
# print(capitalize("This is a special title"))
"""Q.4.7.b.Assume now that the input is a list of strings 
and that a list of strings should be returned, 
with the individual words and then starting with a capital letter."""
def capitalize_mod(text):
    return [t[0].upper() + t[1:] for t in text] 
# print(capitalize_mod(["this", "is", "a", "very","special", "title"]))

"""Q.4.7.c.In headings, it is common to encounter special treatment of words. For example, 
“is” and “a” are not capitalized. Implement this as function capitalize_special_2(words, ignorable_words), 
which gets the words excluded from the conversion as the second parameter."""
def capitalize_special_2(text, ignorable_words):
    # result = "" 
    # for t in text.split():
    #     if t not in ignorable_words:  
    #         t = t[0].upper() + t[1:]
    #         result += t + " "
    # return result
    return [t[0].upper() + t[1:] for t in text.split() if t not in ignorable_words]
# print(capitalize_special_2("This is a special title", ["is", "a"]))

"""Q.4.8.Consider two strings, str1 and str2, where the first string is supposed to be longer than the second. Figure out if the first one contains the other one. In doing so, the characters within the first string may also be rotated. Characters can be moved from the beginning or the end to the opposite position (even repeatedly). 
To do this, create function contains_rotation(str1, str2), which is case-insensitive during the check."""
def contains_rotation(str1, str2):
    l_str1 = list(str1)
    l_str2 = list(str2)
    result = False
    for _ in range(len(str1)):
        first = l_str1.pop(0)
        l_str1.append(first)
        if "".join(l_str2).lower() in "".join(l_str1).lower():
            result = True    
    return result
# print(contains_rotation("ABCDEF","EFAB"))
"""Q.4.9.Write function check_braces(text) that checks whether the sequence 
of round braces passed as a string contains matching (properly nested) pairs of braces."""
def check_braces(text):
    text_list = list(text.replace(" ", ""))
    result = False
    while len(text_list) > 0:
        index = text_list.index(")")
        if index != -1 and text_list[index-1] == "(":
            text_list.pop(index)
            text_list.pop(index-1)
            result = True
            print(text_list)
        else: 
            return False
    return result

# print(check_braces("(())"))
# print(check_braces("( )( )"))
print(check_braces("(( )))((( ))"))
# print(check_braces("((( )"))