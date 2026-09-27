name = input("What name do u want to give your character? ")
gender = input("Sex male[m] or female[f]? ")


def romantic():
    if gender.lower() == "male" or "m":
        print("You are a 16 year old in high school, your name is ", name,
              " you like a girl in your maths class named Emily but she doesn't know. ")
        r_1 = input("Do you want to shoot your shot in class today? ")
        if r_1.lower() == "yes":
            r_2 = input("How do u want to do that?")
    if gender.lower() == "female" or "f":
        print("You are a 16 year old in high school, your name is ", name,
              " you like a boy in your maths class named Emily but she doesn't know. ")
        r_1 = input("Do you want to shoot your shot in class today? ")
        if r_1.lower() == "yes":
            r_2 = input("How do u want to do that?")

    return


def action():
    print("ok")
    return


def horror():
    return


def play():
    story_choice = input("What type of story do u want to live in, romantic[r], action[a], horror[h] ")

    if story_choice.lower() == "romantic" or "r":
        a = 2
    elif story_choice.lower() == "action" or "a":
        action()
    elif story_choice.lower == "horror" or "h":
        horror()
    else:
        play()


play()
