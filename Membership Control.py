admins = ["Khaled", "Ali", "Omar", "Amr", "Saleh"]
name = input("What's Your Name ? ").strip().capitalize()
if name in admins:
    print(F"Hello {name}, weclcome back")
    option = input(
        "Delete or Update \n-- chose D for Delete & U for Update ").strip().capitalize()
    if option == "U" or option == "Update":
        newname = input("What's your New Name ? ").strip().capitalize()
        admins[admins.index(name)] = newname
        print("change Name are scsesfull")
        print(admins)
    elif option == "D" or option == "Delete":
        admins.remove(name)
        print("Deleted")
        print(admins)
    else:
        print("Wrong choise")
else:
    print("You Are Not Admin")
    option2 = input("Are You Want To Be Admin Y, N ").strip().capitalize()
    if option2 == "Y":
        admins.append(name)
        print("You Are Added As Admin")
        print(admins)
    elif option2 == "N":
        print("Ok Thank you :)")
