#create a student to perform the student registration where name and first installment of fees
#is mandatory for registration and providing addhar card address proof and income prooof are
#optional at the registration implemement using method overloading

class student:
    def __init__(self, name, first_installment):
        self.name = name
        self.first_installment = first_installment
    def register(self,aadhaar_card=None,address_proof=None,income_proof=None):

        print("Student Registered Successfully")
        print(f"Name: {self.name}")
        print(f"First Installment: {self.first_installment}")

        if aadhaar_card:
            print(f"Aadhaar Card: {aadhaar_card}")

        if address_proof:
            print(f"Address Proof: {address_proof}")

        if income_proof:
            print(f"Income Proof: {income_proof}")

s = student(name="raj", first_installment=12000)
s.register(aadhaar_card="Aadhaar1234")
s.register(aadhaar_card="asd", address_proof="qwe", income_proof="wed")

def my_method(*args):
    for arg in args:
        print(arg)
print(my_method(222,455,890,997))

def add(*args):
    print(args)
    return sum(args)
print(add(1, 2))
print(add(1, 2, 3, 4))
print(add(1, 2, 3, 4, 5))
print(add(1, 2, 3, 4, 5, 6))