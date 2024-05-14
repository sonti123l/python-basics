user = input().split()
string = ""
for i in user:
    if i == ":)":
        index = user.index(i)
        user[index] = "🙂"
    elif i == ":(":
        index = user.index(i)
        user[index] = "🙁"

for j in user:
    string += (j+" ")

print(string)
