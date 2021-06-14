from calcart import logo

logo()

print("\nWelcome to PyCalc!\n")
print("Follow the prompts below to begin calculating.\n")

def first_prompt():
    new_calc = True
    while new_calc == True:
        num1 = int(input("Enter number: "))
        calc = input("Choose an operation. Type '+' to add, '-' to subtract,\n'*' to multiply, or '/' to divide: ")
        num2 = int(input("Enter number: "))

        if calc == '+':
            new_num = num1 + num2
        elif calc == '-':
            new_num = num1 - num2
        elif calc == '*':
            new_num = num1 * num2
        else:
            new_num = num1 / num2
        print(f"{num1} {calc} {num2}= {new_num}")
        return new_num

keep_or_start = input("To continue, type 'y'. Otherwise, type 'n' to start a new calculation: \n")

def second_prompt(new_num):
    


    
