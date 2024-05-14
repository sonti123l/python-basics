user = input("Greetings: ").split(" ")
for i in user:
    if i == 'Hello' or i == 'Hello,':
        print("$0")
    elif i == 'Hey' or i == 'How' or i == "How's":
        print("$20")
    elif i == "What's":
        print("$100")
