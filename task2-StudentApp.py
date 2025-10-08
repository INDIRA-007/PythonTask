# create student database System
# 1. create object (studentname, rollnumber, any 2 subject marks)
# 2. create methods(add, update, search, delete) (add student, update student, display student, delete student data)
# 3. 

#how to perform this 
#1. create a class
#2. create methods
#3. create a list to store student objects
#4. create a menu to perform operations
#5. create a loop to perform operations until user wants to exit
#6. create a function to display menu
#7. create a function to get user input
#8. create a function to perform operations based on user input
#9. create a function to display student data
#10. create a function to update student data
#11. create a function to delete student data
#12. create a function to search student data
#13. create a function to add student data
#14. create a function to exit the program
#15. create a function to display all student data
#16. create a function to display student data based on roll number
#17. create a function to display student data based on name
#18. create a function to display student data based on subject marks
#19. create a function to display student data based on age

#now show me how to do this
#1. create a class
#2. create methods
#3. create a list to store student objects

class Student:
    def __init__(self, name, rollnumber, subject1, subject2):
        self.name = name
        self.rollnumber = rollnumber
        self.subject1 = subject1
        self.subject2 = subject2

    def displayStudent(self):
        return f"Name: {self.name}, Roll Number:{self.rollnumber}, Subject1:{self.subject1}, Subject2:{self.subject2}"
    
student_list = []
def display_menu():
    print("1. Add Student")
    print("2. Update Student")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")

def get_user_input():
    return int(input("Enter your choice: "))
def add_student():
    name = input("Enter student name: ")
    rollnumber = int(input("Enter roll number: "))
    subject1 = int(input("Enter subject 1 marks: "))
    subject2 = int(input("Enter subject 2 marks: "))
    student = Student(name, rollnumber, subject1, subject2)
    student_list.append(student)
    print("Student added successfully")
def display_all_students():
    for student in student_list:
        print(student.displayStudent())
def main():
    while True:
        display_menu()
        choice = get_user_input()
        if choice == 1:
            add_student()
        elif choice == 5:
            display_all_students()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice")

