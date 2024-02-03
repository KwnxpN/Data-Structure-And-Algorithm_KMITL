import random
"""Guess the number game!!"""

def guess_the_number():
    """The user need to input the number and we'll tell useer that number is higher or lower"""
    guess_count = 0
    the_correct = random.randrange(1, 100)
    print()
    print("==========================================")
    print("Hello! Welcome to Guess the number game!!!")
    print("==========================================", "\n")
    guess = int(input("Input the number between 1 - 100 : "))
    while guess != the_correct:
        if (guess > the_correct) and (guess_count == 4):
            guess_count += 1
            print("++ You guess for 5 times now It's too high! ++")
            guess = int(input("Try again : "))
        elif (guess < the_correct) and (guess_count == 4):
            guess_count += 1
            print("-- You guess for 5 times now It's too low! --")
            guess = int(input("Try again : "))
        elif (guess > the_correct) and (guess_count == 9):
            guess_count += 1
            print("++ You guess for 10 times and you still WRONG?? It's too high! ++")
            guess = int(input("Try again : "))
        elif (guess < the_correct) and (guess_count == 9):
            guess_count += 1
            print("-- You guess for 10 times and you still WRONG?? It's too low! --")
            guess = int(input("Try again : "))
        elif guess > the_correct:
            guess_count += 1
            print("++ It's too high! ++")
            guess = int(input("Try again : "))
        elif guess < the_correct:
            guess_count += 1
            print("-- It's too low! --")
            guess = int(input("Try again : "))
    print("Correct! The number is", guess)
    print("Your guess count :", guess_count)
    if guess_count >= 10:
        print("You use so much guesses isn't it?")
    elif guess_count > 5:
        print("You use your guesses more than I thought")
    elif guess_count == 5:
        print("It's great that you use only 5 guesses")
    else:
        print("Great job!")
guess_the_number()
