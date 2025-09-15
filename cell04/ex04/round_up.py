import math

user_input = input("Give me a number: ")

try:
    number = float(user_input)
    
    
    rounded_up_number = int(math.ceil(number))
    
    print(rounded_up_number)

except ValueError:
    
    print("That's not a valid number.")