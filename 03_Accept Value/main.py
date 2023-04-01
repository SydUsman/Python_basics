user_input = int(input("Enter your age\n"))


def Validate(age):
    if age < 0:
        print("Age cannot be 0, or a -ve number")


Validate(user_input)
print(type(user_input))
