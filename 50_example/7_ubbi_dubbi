import string
#uboctubopubus.ubelubepubant
def ubbi1(word):
    output = []
    for letter in word:
        if letter in 'aeiou':
            output.append(f'ub{letter}')
        else:
            output.append(letter)

    return ''.join(output)

def ubbi2(word):
    output = []
    for letter in word:
        if letter in 'aeiou':
            output.append(f'ub{letter}')
        else:
            output.append(letter)

    if word[0] in string.ascii_uppercase:
        output[0] = output[0].capitalize()

    return ''.join(output)

def ubbi3(text, names):
    output = text

    for one_name in names:
        output = output.replace(one_name, '_' * len(one_name))

    return output

#"https://docs.python.org/3/library/stdtypes.html?#str translate to english from korean"
def ubbi4(text):
    chars = string.whitespace
    output = []

    for one_character in text:
        if one_character in chars:
            output.append(hex(ord(one_character)).replace('0x', '%'))
        else:
            output.append(one_character)

    return ''.join(output)
