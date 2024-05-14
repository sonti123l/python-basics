user = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
if (user.strip() == "42") or (user == "forty-two") or (user.lower() == "forty two"):
    print("Yes")
else:
    print("No")
