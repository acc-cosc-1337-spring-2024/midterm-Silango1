from question_d.main import get_sum_of_evens      
def main():
    while True:  # Main loop for user interaction
        user_input = input("Enter a number to sum its evens (or type 'quit' to exit): ")
        if user_input.lower() == 'quit':
            print("Program exited. Goodbye!")
            break
        
        try:
            num = int(user_input)
            sum_of_evens = get_sum_of_evens(num)
            print(f"The sum of even numbers up to and including {num} is: {sum_of_evens}")
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
