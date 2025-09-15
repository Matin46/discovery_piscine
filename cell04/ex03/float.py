user_input = input("Give me a number: ")

try:
    number = float(user_input)
    
    
    if number % 1 == 0:
        print("This number is an integer.")
    else:
        print("This number is a decimal.")

except ValueError:
    print("That's not a valid number.")