#George West
#vote and retire

age= int(input("PLease enter your age: "))
if age >= 18:
    print("You can vote")
elif age <18:
    print("You cant vote")
if age >= 65:
    print("You can retire")
elif age < 65:
    year = 65-age
    print("you have {0} years until you can retire.".format(year))
    
