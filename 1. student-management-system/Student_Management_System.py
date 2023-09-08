from prettytable import PrettyTable

students = {}
while True:
    print("1.Add Students")
    print("2.Search a Student")
    print("3.Remove a Student")
    print("4.Exit")
    Choose = int(input("Choose option:"))
    table = PrettyTable(["Roll No.", "Name", "Maths Marks", "English Marks"])
    if Choose == 1:
        No_of_students = int(input("Enter the no of Students to add:"))
        while No_of_students >= 1:
            roll = int(input("Enter Roll No:"))
            students[roll] = {}
            students[roll]["name"] = input("Enter the student name:")
            students[roll]["math-marks"] = int(input("Enter Maths Marks:"))
            students[roll]["english-marks"] = int(input("Enter English Marks:"))
            No_of_students = No_of_students - 1
            table.add_row(
                [
                    roll,
                    students[roll]["name"],
                    students[roll]["math-marks"],
                    students[roll]["english-marks"],
                ]
            )
        else:
            print("*" * 30)
            print(table)
            print("*" * 30)

    elif Choose == 2:
        student_roll = int(input("Enter the Roll no of Student:"))
        if student_roll in students:
            table1 = PrettyTable(["Roll", "Name", "Maths Marks", "English Marks"])
            table1.add_row(
                [
                    student_roll,
                    students[student_roll]["name"],
                    students[student_roll]["math-marks"],
                    students[student_roll]["english-marks"],
                ]
            )
            print("*" * 30)
            print(table1)
            print("*" * 30)
        else:
            print(student_roll, "Student not in database. Please Add!")

    elif Choose == 3:
        student_roll = int(input("Enter the student roll no to remove:"))
        if student_roll in students:
            table2 = PrettyTable(["Roll", "Name", "Maths Marks", "English Marks"])
            table2.add_row(
                [
                    student_roll,
                    students[student_roll]["name"],
                    students[student_roll]["math-marks"],
                    students[student_roll]["english-marks"],
                ]
            )
            print("*" * 30)
            print(table2, "\nRemoved")
            print("*" * 30)
            del students[student_roll]
        else:
            print(student_roll, "Student not present in Database. ")

    elif Choose == 4:
        print("*" * 30)
        print("Thank you for using our system!!")
        print("*" * 30)
        break
    else:
        print("Please enter a valid Choise!")
