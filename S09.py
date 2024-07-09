
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide (n1, n2):
    return n1/n2

operations = {
    "+": add,
    "-":subtract,
    "*": multiply,
    "/": divide





}


def calculator():
    num1 = float((input("What's the first number?: ")))
    for symbol in operations:
        print(symbol)


    calc = True
    while calc:
        operation_symbol = input("Pick an operation: ")
        num2 =  float(input("Pick the next number: "))
        function = operations[operation_symbol]
        answer = function(num1, num2)
        print(f"{num1}{operation_symbol}{num2} = {answer}")
        should_continue = input('Type "y" to continue with operations on {answer} or "n" to start a new calculation ')
        if should_continue == "y":
            num1 = answer
        else:
            calc = False
            calculator()


    
calculator()





    
    




