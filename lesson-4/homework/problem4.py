import random

def play_game():
    random_number = random.randint(1, 100)  

    attempt = 0
    while attempt < 10:
        attempt += 1
        try:
            guess = int(input("Enter your guess (between 1 and 100): "))
        except ValueError:
            print("Please enter a valid integer.")
            continue  

        if guess == random_number:
            print(f"Congratulations! You found the number: {random_number}")
            break
        else:
            if guess > random_number:
                print("It is too high.")
            else:
                print("It is too low.")
    else:
        print(f"You've used all attempts. The number was {random_number}.")
    
    
    answer = input("Do you want to play again? (Y/N): ").strip()
    answerg = ['Y', 'YES', 'y', 'yes', 'ok']

    if answer in answerg:
        play_game()  
    else:
        print("Thanks for playing!")


play_game()

    