firstName = input(" Please enter your name : ")
lastName = input(" Please enter your surname : ")
age = int(input(" Please enter your age : "))
dateOfBirth = int(input(" Please enter your date of birth : "))

userInfo = [firstName, lastName, age, dateOfBirth]

for allUserInformation in userInfo:
    print(allUserInformation)

if age < 18:
    print("You can't go out because it's too dangerous")
else:
    print("You can go out to the street")