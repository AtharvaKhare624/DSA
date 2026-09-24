# class facory:
#     def __init__(self, name, breed, owner):
#         self.name = name
#         self.breed = breed
#         self.owner = owner

#     def dog_f(self):
#         name = self.name
#         breed = self.breed
#         own_name = self.owner.name
#         print(f"name:{name}, breed:{breed}, owner:{own_name}")

# class Owner:
#     def __init__(self, name, contact):
#         self.name = name
#         self.number = contact

# own1 = Owner("owner1", 234)
# own2 = Owner("owner2", 654)
# dog1 = facory("ral", 1, own1)
# dog2 = facory("sam", "rot", own2)

# dog2.dog_f()
# dog1.dog_f()

class Student:
    def __init__(self, name, first_sub, sec_sub, thr_sub, marks):
        self.first_sub = first_sub
        self.sec_sub = sec_sub
        self.thr_sub = thr_sub
        self.mark = marks
        self.name = name

    def display(self):
        print(f"{self.name}'s marks are-")
        for i in self.mark:
            print(f"marks:{i}")


    def avger(self):
        summ = 0
        for i in self.mark:
            summ+=i
        print(f"avg marks are:{summ/len(self.mark)}")

marks = [100,100,100]
stud1 = Student("ath", "science","maths","AI", marks)
if isinstance(stud1, Student):
    stud1.display()
    stud1.avger()