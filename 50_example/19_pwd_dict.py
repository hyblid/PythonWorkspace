from collections import defaultdict

def passwd_to_dict(filename):
    users = {}
    with open(filename) as passwd:
        for line in passwd:
            if not line.startswith(('#', '\n')):
                user_info = line.split(':')
                users[user_info[0]] = int(user_info[2])
    return users


def logshell_to_dict(filename="passwd.txt"):
    users = {}
    with open(filename) as passwd:
        for line in passwd:
            if not line.startswith(('#', '\n')):
                user_info = line.split(':')
                users[user_info[0]] = user_info[len(user_info)-1].replace("\n","")
    return users


"""Ask the user to enter integers, separated by spaces. From this input, create a
dict whose keys are the factors for each number, and the values are lists containing
those of the users’ integers that are multiples of those factors."""
def factors():
    output = defaultdict(list)
    numbers = input("Enter numbers, separated by spaces: ").split()
    for one_number in numbers:
        if not one_number.isdigit():
            print(f'Ignoring {one_number}')
            continue

        one_number = int(one_number)
        for i in range(1, one_number):
            if not one_number % i:
                output[one_number].append(i)
        output[one_number].append(one_number)
    return output
    
def factor_to_dict2():
    output = {}
    with open("passwd.txt") as passwd:
        for line in passwd:
            if not line.startswith(('#', '\n')):
                username, passwd, uid, *ignore, homedir, shell = line.split(":")             
                output[username] = { "username" : username,
                                      "homedir" : homedir,
                                      "shell" : shell 
                                    }    
    print(output)            
                
factor_to_dict2()                