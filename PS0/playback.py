user = input()
string_1 = ""
for i in user:
    if i == " ":
        string_1 += "..."
    else:
        string_1 += i
print(string_1)
