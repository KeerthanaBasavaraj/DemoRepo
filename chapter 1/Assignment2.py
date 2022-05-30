#The below program is to guess the correct number between 1 to 100
import random
def valid_user_guess(user_guess):
    if user_guess.isdigit() and 1<= int(user_guess) <=100:
        return True
    else:
        return False

def main():
    number_to_guess=random.randint(1,100)
    correct_guess=False
    user_guess=input("Guess a number between 1 and 100:")
    guess_count=0
    while not correct_guess:
        if not valid_user_guess(user_guess):
            user_guess=input("I wont count this one Please enter a number between 1 to 100")
            continue
        else:
            guess_count+=1
            user_guess=int(user_guess)

        if user_guess<number_to_guess:
            user_guess=input("Too low. Guess again")
        elif user_guess>number_to_guess:
            user_guess=input("Too High. Guess again")
        else:
            print("You guessed it in",guess_count,"guesses!")
            correct_guess=True

main()