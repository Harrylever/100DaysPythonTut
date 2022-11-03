year_ = int(input("Which year do you want to check?: "))

if year_ % 4 == 0:
    if year_ % 100 == 0:
        if year_ % 400 == 0:
            print("leap year")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
    print("not leap year")
