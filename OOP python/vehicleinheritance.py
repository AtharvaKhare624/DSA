class vehicle:
    def __init__(self, brand):
        self.brand = brand
    def start_eng(self):
        print(f"{self.brand} engine started")
    
class car(vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def drive(self):
        print(f"the {self.brand}'s {self.model} is started")

class motor(vehicle):
    def __init__(self, brand, tyre_set):
        super().__init__(brand)
        self.tyre_set = tyre_set
    def rise(self):
        print(f"the {self.brand}'s {self.tyre_set} is rising on the wheel")

car1 = car(brand="Ford", model="cc")
bike1  = motor(brand="shine" , tyre_set=2)
car1.drive()
bike1.rise()

class book:
    def __init__(self, title):
        self.title = title
    
    def read(self):
        print(f"reading {self.title} book")

class notebook(book):
    def __init__(self, title):
        super().__init__(title)

    def write(self):
        print(f"writing in {self.title} notebook")

class digital(book, notebook):
    def __init__(self, title):
        super().__init__(title)
        
    
    def print(self):
        print(f"printing {self.title} book")

note1 = notebook(title="notebook1")
digi = digital(title="digital1")
note1.write()
note1.read()
digi.print()
digi.read()
digi.write()
        