choice = input("Choose a number, '1', '2' or '3'")
while choice not in("1", "2", "3"):
    print("That isn't a valid choice")
    choice = input("Choose a number")
print(choice, "is a good number")

