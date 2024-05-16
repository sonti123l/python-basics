from fractions import Fraction
list = []
for i in range(2,99):
    list.append(i)

def check_fraction():
    fuel_input = Fraction(input("Fraction: "))
    percentage = 100 * fuel_input
    new_percentage = round(percentage)
    if new_percentage in list:
        print(f"{new_percentage}%")
    elif new_percentage == 0 or new_percentage == 1:
        print("E")
    elif new_percentage == 100 or new_percentage == 99:
        print("F")
    elif new_percentage not in list:
        check_fraction()

try:
    check_fraction()
except(ValueError,ZeroDivisionError):
    check_fraction()

