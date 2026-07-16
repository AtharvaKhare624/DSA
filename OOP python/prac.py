class person():
    def __init__(self, name, address, dob):
        self.name = name
        self.address = address
        self.dob = dob
    
    def cal_age(self):
        birth_year = int(self.dob.split("-")[2])
        day = int(self.dob.split("-")[0])
        month = int(self.dob.split("-")[1])
        current_year = 2026
        cur_day = 5
        cur_month = 2
        print(current_year - birth_year)
        print(cur_day - day)
        print(cur_month - month)

per1 = person(name="as",address="asdf", dob="12-11-2011")
per2 = person(name="as",address="asdf", dob="1-11-2006")
per2.cal_age()

# accept year and month from the user and date 13 and find out the given day is a black friday or not. 
# if it is black friday then print "black friday" otherwise print "not black friday".

#accept a date that is year and month ,from the user and date is 13 and find out the given date is 
# black friday or not

from datetime import date

year = int(input("Enter year = "))
month = int(input("Enter month = "))
def check_friday(dt):
    week_day = dt.strftime('%A')
    if week_day == "Friday":
        print("the entered date is black friday")
    else:
        print("the entered date is not black friday")

check_friday(date(year,month,13))