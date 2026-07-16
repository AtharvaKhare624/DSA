class InvalidNameError(Exception):
    pass

class InvalidMarksError(Exception):
    pass


def calculate_grade(percentage):
    if percentage > 100:
        raise InvalidMarksError("Percentage cannot be greater than 100")
    elif 80 <= percentage <= 100:
        return "A"
    elif 50 <= percentage < 80:
        return "B"
    elif 35 <= percentage < 50:
        return "C"
    else:
        return "Fail"


def is_valid_name(name):
    return name.isalpha()


try:
    while True:
        print("\n------ MENU ------")
        print("1. Insert student record")
        print("2. Display records")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            roll_no = int(input("Enter Roll No: "))
            name = input("Enter Name: ")

            if not is_valid_name(name):
                raise InvalidNameError("Name should not contain symbols or numbers")

            marks = []
            for i in range(1, 6):
                m = float(input(f"Enter marks for subject {i}: "))
                if m < 0:
                    raise InvalidMarksError("Marks cannot be negative")
                marks.append(m)

            total = sum(marks)
            percentage = total / 5

            grade = calculate_grade(percentage)

            with open("student.csv", "a") as f:
                f.write(f"Roll No: {roll_no}\n")
                f.write(f"Name: {name}\n")
                f.write(f"Marks: {marks}\n")
                f.write(f"Percentage: {percentage}\n")
                f.write(f"Grade: {grade}\n")
                f.write("-------------------------\n")

            print("Student record saved successfully ")

        elif choice == 2:
            try:
                with open("student.csv", "r") as f:
                    print("\n--- Student Records ---")
                    print(f.read())
            except FileNotFoundError:
                print("No records found.")

        elif choice == 3:
            print("Exiting program ")
            break

        else:
            print("Invalid choice")

except InvalidNameError as e:
    print("Name Error:", e)

except InvalidMarksError as e:
    print("Marks Error:", e)

except Exception as e:
    print("Error:", e)
