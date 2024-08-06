import random


def game():
    global user_score, computer_score
    if user_input not in ['R', 'P', 'S']:
        print("INVALID INPUT")
    if user_input == computer_choice[0]:
        print("IT'S A TIE.")
    else:
        if user_input == 'R':
            if computer_choice == 'PAPER':
                print("YOU LOSS.")
                computer_score += 1
            else:
                print("YOU WON.")
                user_score += 1
        if user_input == 'P':
            if computer_choice == 'SCISSOR':
                print("YOU LOSS.")
                computer_score += 1
            else:
                print("YOU WON")
                user_score += 1
        if user_input == 'S':
            if computer_choice == 'ROCK':
                print("YOU LOSS.")
                computer_score += 1
            else:
                print("YOU WON")
                user_score += 1


print("WELCOME TO THE ROCK-PAPER-SCISSOR GAME: \nRULE:FOR EVERY WON YOU WILL BE AWARDED +1.NO NEGATIVE MARKING.")

user_score = 0
computer_score = 0
start = True
while start:
    choice = input("\nWANT TO PLAY THE GAME.TYPE YES:'Y' & NO:'N':\n").upper()
    if choice == 'Y':
        user_input = input("ENTER YOUR CHOICE.TYPE ROCK:'R',PAPER:'P'& SCISSOR:'S':\n").upper()
        computer_choice = random.choice(['ROCK', 'PAPER', 'SCISSOR'])
        print(f"THE COMPUTER CHOICE IS: {computer_choice}")
        game()
        print(f"YOUR FINAL SCORE IS: {user_score}")
        print(f"COMPUTER FINAL SCORE IS: {computer_score}")

    elif choice == 'N':
        feedback = input("ANY FEEDBACK REGARDING GAME:\n")
        print("\nNICE GAME WITH YOU.SEE YOU SOON!")
        start = False
    else:
        print("INVALID INPUT.TRY AGAIN.")
