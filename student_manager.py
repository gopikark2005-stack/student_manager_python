students = {}

def add_student():
    name = input("Enter name: ")
    marks = input("Enter marks: ")
    students[name] = marks
    print("Student added!")

def view_students():
    if not students:
        print("No records found")
    else:
        for name, marks in students.items():
            print(name, ":", marks)

def delete_student():
    name = input("Enter name to delete: ")
    if name in students:
        del students[name]
        print("Deleted!")
    else:
        print("Not found")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        break
    else:
        print("Invalid choice")