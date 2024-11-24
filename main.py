# Code with Harry 100 days of programming 
#Making of Calculator which will produce result in readable manner


a = int(input("Please enter valid number : "))
b = int(input("Please enter valid number : "))
c = input('Please choose valid operators: "+", "-", "/", "*", "//", "%": \n')

add = a + b
subtract = a - b
multiply = a * b
divide = a / b
floor_division = a // b
remainder = a % b

if c == "+":
    print(f"The sum of two numbers is {add}")
elif c == "-":
    print(f">The difference of two numbers is {subtract}")
elif c == "/":
    print(f"You can divide the number {divide} times")
elif c == "*":
    print(f"The result is {multiply}")
elif c == "//":
    print(f"The result is {floor_division}")
elif c == "%":
    print(f"The result is {remainder}")
else:
    print("Please enter a valid operator and Try again !")
