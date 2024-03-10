from src.question_c.question_c import get_random_number
def main():
    while True:  # User continue loop
        random_number = get_random_number()  # Generate a new random number for each game iteration
        print("Guess the number between 1 and 5. Type 'quit' to exit.")
        
        while True:  # Game loop
            user_input = input("Your guess: ")
            if user_input.lower() == 'quit':
                print("Thanks for playing!")
                return  # Exit the main function, thereby ending the program
                
            try:
                user_guess = int(user_input)
                if 1 <= user_guess <= 5:  # Ensure guess is within the valid range
                    if user_guess == random_number:
                        print("Congratulations! You've guessed the number. Starting a new game...")
                        break  # Exit the game loop to start over
                    else:
                        print("Wrong guess, try again!")
                else:
                    print("Please guess a number between 1 and 5.")
            except ValueError:
                print("Please enter a valid number or type 'quit' to exit.")
                
if __name__ == "__main__":
    main()
