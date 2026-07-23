def add(n1 , n2):
    return n1 + n2

def subtract(n1 , n2):
    return n1 - n2

def multiply(n1 , n2):
    return n1 * n2

def divide(n1 , n2):
    return n1 / n2

def calculate(n1 , n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    should_accumulate = True
    first_num = int(input("Enter first number:"))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Enter operation symbol:")
        next_number = int(input("What's the next number?: "))
        cal = operations[operation_symbol](first_num, next_number)
        print(f"{first_num} {operation_symbol} {next_number} = {cal}")
        cont_cal = input("Type 'YES' to continue calculating or 'NO' to exit:").lower()

        if cont_cal == "yes":
            first_num = cal

        else:
            should_accumulate = False
            print('\n' * 200)
            calculator()
calculator()



