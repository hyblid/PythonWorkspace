from decimal import Decimal

def time_percentage(hour):
    return hour / Decimal('24.0')

def calculate_tax(purchase, p_state, p_hour):
    rates = {'Chico': Decimal('0.5'),
              'Groucho': Decimal('0.7'),
              'Harpo': Decimal('0.5'),
              'Zeppo': Decimal('0.4')}
    return purchase + (purchase * rates[p_state] * time_percentage(p_hour))

def tax_brackets(amount, brackets):
    tax_owed = 0

    for one_bracket in brackets:
        if amount < one_bracket['start']:
            continue

        taxed_amount = min(amount, one_bracket['end'])
        taxed_amount -= one_bracket['start']

        tax_owed += taxed_amount * one_bracket['tax']

    return tax_owed

def analyze_string(s):
    output = {'isdigit': 0, 'isalpha': 0, 'isspace': 0}
    #mixed with different for statement
    for one_character in s:
        for methodname in output:
            # if (h,isdigit) - > x.isdigit()
            if getattr(one_character, methodname)():  # a sneaky, cool trick!
                output[methodname] += 1
    return output

def from_keys(keys, func):
    return { key: func(key) for key in keys }
