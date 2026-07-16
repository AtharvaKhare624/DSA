def age(age):
    if age<18:
        raise ValueError("age cannot be below 18")
    elif age>50:
        raise ValueError("age cannot be above 50")
    else:
        print(f"age is {age}")

s = int(input("enter age:"))
try:
    age(s)
except ValueError as e:
    print(e) 

class InvalidNameError(Exception):
    pass
def validate_name(name):
    if not name.isalpha():
        raise InvalidNameError("Name should contain only alphabets")
    else:
        print(f"Name is {name}")

q = input("Enter name: ")

try:
    validate_name(q)
except InvalidNameError as e:
    print(e)
