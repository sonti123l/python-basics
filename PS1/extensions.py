user = input("File name: ").split(".")
if len(user) > 1:
    if user[1] == "gif":
        print("image/gif")
    elif (user[1] == "jpg" or user[1] == 'jpeg'):
        print("image/jpeg")
    elif user[1] == "txt":
        if len(user) >2 and user[2] == "pdf":
            print("application/pdf")
        else:
            print("text/plain")
    elif user[1] == "png":
        print("image/png")
    elif user[1] == "pdf" or user[1] == "PDF" or user[1].strip() == "PDF":
        print("application/pdf")
    elif user[1] == "zip":
        print("application/zip")
    elif user[1] == "bin":
        print("application/octet-stream")
else:
    print("application/octet-stream")
