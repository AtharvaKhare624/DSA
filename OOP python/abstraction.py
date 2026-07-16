class car():
    def start_engine(self):
        pass
def stop_engine(self):
    pass

class Kia(car):
    def start_engine(self):
        return "Kia engine started"

    def stop_engine(self):
        return "kia engine stop"
    
class Honda(car):
    def start_engine(self):
        return "Honda engine started"

    def stop_engine(self):
        return "honda engine stop"

Kia = Kia()
honda = Honda()

print(Kia.start_engine())
print(Kia.stop_engine())
print(honda.start_engine())
print(honda.stop_engine())

class person():
    def __init__(self, name, address, dob):
        self.name = name
        self.address = address
        self.dot = dob
    
    def cal_age(self):
        birth_year = int(self.dob.split("-")[2])
        current_year = 2026
        return current_year - birth_year

per1 = person(name="as",address="asdf", dob=12-11-2011)
per1.cal_age()