class rectangle:
    def __init__(self, width = 0, height = 0):
        if width and height:
            self.width = width
            self.height = height
        elif width:
            self.width = width
            self.height = width
        else:
            self.width = 0
            self.height = 0
    
    def area(self):
        return self.width * self.height
    
    def display(self):
        print(f"width {self.width}, height {self.height}, area {self.area}")

rec1 = rectangle(10,20)
rec2 = rectangle(30)
rec3 = rectangle()
rec1.display()
rec2.display()
rec3.display()

class employee():
    basic_pay = 10000
    def __init__(self, DA=None, TA=None, HRA=None):
        salary = self.basic_pay
        if DA:
            self.DA = (self.basic_pay/100) * 5
        if TA:
            
        if HRA and DA and TA:
            self.DA=DA
            self.TA= TA