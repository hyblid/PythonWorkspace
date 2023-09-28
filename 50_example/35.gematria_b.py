import string

def gematria_dict():
    return {char: index for index, char in enumerate(string.ascii_lowercase,1)}

GEMATRIA = gematria_dict()

def gematria_for(word):
    return sum(GEMATRIA.get(one_char,0) for one_char in word)
    

def gematria_equal_words(input_word):
    our_score = gematria_for(input_word.lower())
    return [one_word.strip() for one_word in open('words.txt')
                             if gematria_for(one_word.lower()) == our_score]

temp_dict = {"seoul": 90, "tokyo": 100, "newyork":50, "toronto":75}

def dict_f_to_c(dict_of_temps):
    return {key: (value-32)/1.8
            for key, value in dict_of_temps.items()}
    
books = [("howard hwang", "one" , 123),("jennifer park", "two", 100),("james hwang", "three", 500)]


def book_dict(books):
    return {title: {'first': name.split()[0],
                    'last': name.split()[1],
                    'price': price}
            for name, title, price in books} #auto unpacking tuple to sequential items

conversions = {"cdollar": 1.35, "yen" : 149, "euro": 0.98}

    
"""Create a dict whose keys are currency names and whose values are the price of
that currency in U.S. dollars. Write a function that asks the user what currency
they use, then returns the dict from the previous exercise as before, but with its
prices converted into the requested currency."""

def currency_conversion(books, new_currency):
    return {title: {'first': name.split()[0],
                    'last': name.split()[1],
                    'price': price * conversions[new_currency]}
            for name, title, price in books}

    
    
print(currency_conversion(books, "euro"))