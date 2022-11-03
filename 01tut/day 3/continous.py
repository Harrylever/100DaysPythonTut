user_name = input("Welcome User,\nWhat is your name?\n'")

user_age = int(input("How old are you " + user_name + "?\n'"))
old_man_age = 95

if 2 < user_age < 14:
    print("Wow. Your pretty young. Don't take me for being weird I'm just a bit old myself\nI'm 95 years old")
    print("Don't you think it's a old age?")
    test01 = input('''"Y", Yeah that's pretty old,\n"N", Nope, Sure your old but not that old =>\n' ''')
    if test01 == "Y" or test01 == "y":
        print("Yeah I know, all I ever do these days is just sit down and remember all my young days")
    elif test01 == "N" or test01 == "n":
        suppose_age_test = input("Wow.. that's funny. So what age would you consider me an old man? ")
        if suppose_age_test is int:
            if suppose_age_test == old_man_age:
                print("Well isn't that my age!")
                print(f"It was nice to meet you {user_name}, I wish to go inside and have my rest good bye")
            elif suppose_age_test != old_man_age and (95 < suppose_age_test <= 100):
                print(f"{suppose_age_test}!\n That does not seem too far from my own very age.")
                print("Not that it even matters I could be dying whenever when you've lived as long as me")
