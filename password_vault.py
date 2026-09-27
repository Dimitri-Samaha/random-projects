 master_pwd = input("What is your master password? ")


def view():
    with open("file.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split(" ")
            print(f"User: {user} | Password: {passw}")


def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("file.txt", "a") as f:
        f.write(name + " " + pwd + "\n")


while True:
    mode = input("Do you want to add[a] a new password or view[v] existing ones?"
                 " \n\t press q to exit ").lower()
    if mode == "q":
        break
    elif mode == "v":
        view()
    elif mode == "a":
        add()
    else:
        continue
