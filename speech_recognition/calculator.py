# # import sys
# cnt = 0
# while True:
#   if cnt == 5:
#     print("That's enough for today, bye!")
#     # sys.exit()
#     break
#   print("What do you want to do?")
#   operation = input("Type '+' for addition,\n'-' for subtraction,\n'*' for multiplication,\nor '/' for division.\nType 'q' to quit.\n")
#   if operation == 'q':
#     print("Bye!!")
#     # sys.exit()
#     break
#   elif operation == '+' or operation == '-' or operation == '*' or operation == '/':
#     a = input("First number: ")
#     b = input("Second number: ")
#     while not (a.isnumeric() and b.isnumeric()):
#       print("Input must be two numbers")
#       a = input("First number: ")
#       b = input("Second number: ")
#     print(f"{a} {operation} {b} = {eval(str(a)+operation+str(b))}")
#     cnt += 1
#   else:
#     print("Please choose one of the given operations")

## imports/installs: pyaudio




### To do: check all possibilities and see what needs tidying

def tidy(eq):
    eq = eq.lower()
    ## Remove spaces
    return eq

def calculate(equation):
    eq = tidy(equation)
    try:
        res = eval(eq)
    except:
        res = None
    return eq, res
