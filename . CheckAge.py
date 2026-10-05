age = int(input("Enter your age: "))

if age < 0 or age > 120:
    print("Invalid Age")
elif age >= 18:
    print("Age is Valid")
    print("Eligible for Voting")
else:
    print("Age is Valid")
    print("Not Eligible for Voting")