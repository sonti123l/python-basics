user = input("Expression: ").split(" ")
value1 = int(user[0])
value2 = int(user[-1])
for i in user:
    if i == "+":
        sum = value1+value2
        print(round(float(sum),1))
    elif i == "-":
        sum = value1-value2
        print(round(float(sum),1))
    elif i == "*":
        sum = value1*value2
        print(round(float(sum),1))
    elif i == "/":
        sum = value1/value2
        print(round(float(sum),1))
        
