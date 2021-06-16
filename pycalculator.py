from calcart import logo

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

operations = {
    '+': add, 
    '-': sub, 
    '*': mult, 
    '/': div
}

def calculate():
    
    print(logo)
    print("\nWelcome to PyCalc!\n")
    print("Follow the prompts below to begin calculating.\n")
    
    num1 = float(input("Enter number: "))

    user_continue = True

    while user_continue:
        calc = print("Choose an operation:")
        for i in operations:
            print(i)

        user_operation = input("\n>> ")
        num2 = float(input("\nEnter number: "))
        calc_function = operations[user_operation]
        answer = calc_function(num1, num2)

        print(f"\n{num1} {user_operation} {num2} = {answer}\n")
    
        if input(f"\nTo continue calculating with {answer}, type 'y'. To exit, type 'n': ") == 'y':
            num1 = answer
        else:
            user_continue = False
            calculate()
        
calculate()
        
