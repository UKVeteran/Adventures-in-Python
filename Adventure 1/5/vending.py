print ("a: Cake")
print ("b: Carrot")
print ("c: Fish")
print ("d: Soup")
choice = input("Select an option (a, b, c or d): ")
if choice == ("a"):
    print ("Here is your cake. Yum!")
elif choice == ("b"):
    print ("Carrots are orange. Have some.")
elif choice == ("c"):
    print ("Fish live in water. Enjoy!")
elif choice == ("d"):
    print ("Today's soup is tomato. Spoons are located behind you.")
else:
    print (choice) + (" is not a valid option. Have some air.")
