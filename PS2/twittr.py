list = ['a','e','i','o','u','A','E','I','O','U']
user = input("Input: ")
list1 = []
full_string = ""
for i in user:
    list1.append(i)
for j in list1:
    for k in list:
        if j == k:
            list1.remove(j)
        else:
            pass
for j in list1:
    for k in list:
        if j == k:
            list1.remove(j)
        else:
            pass
for i in list1:
    full_string += i
print(f"Output: {full_string}")

