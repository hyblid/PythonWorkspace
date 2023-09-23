import string

def sum_numbers(numbers):
    return sum(int(number) for number in numbers.split() if number.isdigit())

def lines_with_1v20c(filename):
    return [one_line
            for one_line in open(filename)
            if len(one_line) >= 20 and
            len(set('aeiou') & set(one_line)) >= 1]    

numbers =['123-456-7777', '456-333-888', '789-777-9999']
def phone(numbers):
    return [num.replace(num[2],str(int(num[2])+1)) for num in numbers 
                    if len(set(num[4]) & set('012345')) == 1]

def increment_area_code(full_phone_number):
    area_code, phone_number = full_phone_number.split('-', 1)
    if area_code[0] in '012345':
        area_code = str(int(area_code) + 1)
    return f'{area_code}-{phone_number}'

def increment_all_area_codes(area_codes):
    return [increment_area_code(one_phone_number)
            for one_phone_number in area_codes]

    """Define a list of five dicts. Each dict will have two key-value pairs, name and age,
containing a person’s name and age (in years). Use a list comprehension to
produce a list of dicts in which each dict contains three key-value pairs: the original
name, the original age, and a third age_in_months key, containing the person’s
age in months. However, the output should exclude any of the input dicts
representing people over 20 years of age.
    """
    
mylist = [{"name" : "one", "age": 11},
          {"name" : "two", "age": 12},
          {"name" : "three", "age": 13},
          {"name" : "four", "age": 21},
          {"name" : "five", "age": 15}]

#what is difference one_person, **one_person
def age_in_months(list_of_people):
    return [dict(one_person, age_in_months=one_person['age'] * 12)
            for one_person in mylist
            if one_person['age'] <= 20]

print(age_in_months(mylist))
