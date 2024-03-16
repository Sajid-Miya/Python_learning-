Number_1 = int(input("Enter number: "))
Number_2 = int(input("Enter number: "))
operator = input("Enter '+', '-', '*', '/' ")

if operator == '+':
    print(f"The addition of Number_1 and Number_2 is {Number_1 + Number_2}")
elif operator == '-':
    print(f"The subtraction of Number_1 and Number_2 is {Number_1 - Number_2}")
elif operator == '*':
    print(f"The multiplication of Number_1 and Number_2 is {Number_1 * Number_2}")
elif operator == '/':
    if Number_2 == 0:
        print("Division by Zero is not allowed")
    else:
        print(f"The division of Number_1 and Number_2 is {Number_1 / Number_2}")
else:
    print("Enter a valid operator")
