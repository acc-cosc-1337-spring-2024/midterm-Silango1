from src.question_b.question_b import is_prime
def main():
    while True:
        user_input = input("Enter a number (or type 'quit' to exit): ")
        if user_input.lower() == 'quit':
            print("Program exited.")
            break
        try:
            num = int(user_input)
            if is_prime(num):
                print(f"{num} is a prime number.")
            else:
                print(f"{num} is not a prime number.")
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()