import random

def guessing_game():
    number = random.randint(10, 30)
    while True:
        guess = int(input("Please enter number:"))
        if (number > guess):
            print(f"Your guess {guess} is to low") 
        elif (number < guess):
            print(f"Your guess {guess} is to high")  
        elif(number == guess):
            print("Your answer is correct")  
            break
        
def guessing_game1():
    number = random.randint(10, 30)
    print(number)
    counter = 1
    while True:
        guess = int(input("Please enter number:"))
        if(counter > 3):
            print("You've already tried 3 times")
            break
        elif (number > guess):
            print(f"Your guess {guess} is to low") 
        elif (number < guess):
            print(f"Your guess {guess} is to high")  
        elif(number == guess):
            print("Your answer is correct")  
            break
        counter += 1

def guessing_game2():
    number = random.randint(10, 30)
    print(number)
    while True:
        guess = int(input("Please enter number:"))
        base = random.choice([2,8,10,16])
        
        print(f"choice base: {base}")
        if (number > guess):
            print(f"Your guess {guess} is to low") 
        elif (number < guess):
            print(f"Your guess {guess} is to high")  
        elif(number == guess):
            print("Your answer is correct")  
            break

def guessing_game3():
    WORDS = [one_word.strip()
         for one_word in open('words.txt')]
    answer = random.choice(WORDS)
    
    while True:
        user_guess = int(input('What is your guess? '))

        if user_guess == answer:
            print(f'Right!  The answer is {user_guess}')
            break

        if user_guess < answer:
            print(f'Your guess of {user_guess} is too low!')

        else:
            print(f'Your guess of {user_guess} is too high!')

guessing_game3()
    