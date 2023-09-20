import string
import os
import collections as collection

def reverse_lines(infilename, outfilename):
    with open(infilename) as infile, open(outfilename, 'w') as outfile:
        for one_line in infile:
            outfile.write(f'{one_line.rstrip()[::-1]}\n')

def encrypt(filename, text):
    with open(filename, 'w') as outfile:
        for one_character in text:
            outfile.write(f'{ord(one_character)}\n')


def decrypt(filename):
    characters = [chr(int(one_character))
                  for one_character in open(filename)
                  if one_character.strip().isdigit()]
    return ''.join(characters)

 
def vowels_and_consonants(infilename, vowel_filename, consonant_filename):
    with open(infilename) as infile, open(vowel_filename, 'w') as vowel_out, open(consonant_filename, 'w') as consonant_out:
        for one_line in infile:
            for one_character in one_line:
                if one_character.lower() in 'aeiou':
                    vowel_out.write(one_character)
                elif one_character.lower() in string.ascii_lowercase:
                    consonant_out.write(one_character)
                    
def shell_users(filename, outfilename):
    shells = collection.defaultdict(list)

    with open(filename) as passwd, open(outfilename, 'w') as outfile:
        for one_line in passwd:
            if one_line.startswith(('#', '\n')):
                continue
            username, *fields, shell = one_line.strip().split(':')
            shells[shell].append(username)

        for shell, all_users in shells.items():
            outfile.write(f'{shell}: {",".join(all_users)}\n')

            
                        
            
shell_users("passwd.txt", "passwd_user.txt")
