import logo
# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# multiply
def multiply(n1, n2):
    return n1 * n2


# divide
def division(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division
}


def calculator():
    print(logo.logo)
    num1 = float(input("Enter first number: "))
    for operand in operations:
        print(operand)
    go_again = 'y'

    while go_again == 'y':
        operation_symbol = input("Enter any symbol: ")
        num2 = float(input("Enter next number: "))
        answer = operations[operation_symbol](n1=num1, n2=num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        go_again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation: ")
        if go_again == 'y':
            num1 = answer
        else:
            calculator()


calculator()
