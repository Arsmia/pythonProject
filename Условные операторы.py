first_value=None
second_value=12
operator = "/"
if first_value is None or second_value is None:
    print("Can't divide None value")
else:
    if operator == "+":
            print(first_value + second_value)
    elif operator == "-":
        print (first_value - second_value)
    elif operator == "/":
        if second_value == 0:
            print("Can't divide by 0")
        else:
            print (first_value / second_value)
    elif operator == "*":
        print (first_value * second_value)
    else:
        print("Operator is wrong. Choose from given: + - / *")



