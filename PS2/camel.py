user = input("camelCase: ")
string_1 = ""
for i in user:
    if i.isupper():
        new_value = i.lower()
        string_1 += ("_" + new_value)
    else:
        string_1 += i

print(f"snake_case: {string_1}")
