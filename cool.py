import random
def game():
    num = random.randint(1, 10)
    guess_history = []
    numguess = 0

    while True:
        inputted = input("guess the number, 1-10")
        integer = int(inputted.replace(" ""/", ""))
        if integer == num:
            print(f"you got it bud, here are your {numguess} previous guesses")
            for a in range(len(guess_history)):
                print(f"{a+1}.{guess_history[a]}")
            break
        elif integer > num:
            print("the number is smaller")
            guess_history.append(integer)
            numguess +=1
        elif integer < num:
            print("the number is bigger")
            guess_history.append(integer)
            numguess +=1

game()