# Global variable declaration
global_var = 10

def use_global():
    global global_var  # Declare the use of the global variable
    global_var = 20  # Modify the global variable

def main():
    print("Before calling use_global():", global_var)  # Display value before modification
    use_global()  # Call the function to modify the global variable
    print("After calling use_global():", global_var)  # Display value after modification

# Entry point of the program
if __name__ == "__main__":
    main()
#add import