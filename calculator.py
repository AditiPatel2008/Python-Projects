a = float(input("Enter the 1st num :"))
b = float(input("Enter the 2nd num :"))
operator = input("Enter Operator (+ , - , * , / , % , **) :")

if operator == "+":
    print(a+b)
elif operator == '-':
    print(a-b)
elif operator == '*':
    print(a*b)
elif operator == '/':
    print(a/b)
elif operator == '%':
    print(a%b)
elif operator == '**':
    print(a**b)
else:
    print("Invalid Operation")

