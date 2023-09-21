import string
import random

def create_password_generator(characters):
    def create_password(length):
        output = []
        for i in range(length):
           output.append(random.choice(characters))
        return ''.join(output)
    return create_password
   
def create_password_checker(min_uppercase, min_lowercase, min_punctuation, min_digits):
    uppercase_set = set(string.ascii_uppercase)
    lowercase_set = set(string.ascii_lowercase)
    punctuation_set = set(string.punctuation)
    digits_set = set(string.digits)

    def check_password(password):
        if len([one_character
                for one_character in password
                if one_character in uppercase_set]) < min_uppercase:
            print(f'Not enough uppercase letters; min is {min_uppercase}')
            return False
        elif len([one_character
                  for one_character in password
                  if one_character in lowercase_set]) < min_lowercase:
            print(f'Not enough lowercase letters; min is {min_lowercase}')
            return False
        elif len([one_character
                  for one_character in password
                  if one_character in punctuation_set]) < min_punctuation:
            print(f'Not enough punctuation; min is {min_punctuation}')
            return False
        elif len([one_character
                  for one_character in password
                  if one_character in digits_set]) < min_digits:
            print(f'Not enough digits; min is {min_digits}')
            return False
        else:
            return True
    return check_password
       
def getitem(key):
    def check(seq):
        if seq:
           return seq[key]
        
    return check

def doboth(f1,f2):
    def g(x):
        return f2(f1(x))
    return g    
        
g = doboth(f1,f2)  
print(g(x))       