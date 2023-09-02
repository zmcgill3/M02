#Zachary McGill 
#caseStudy.py
#Tests if students qualify for Dean's list or honor roll.
while(1):
    studentLastName = input("Plese enter your last name or ZZZ to quit: ")

    if studentLastName == "ZZZ" or studentLastName == "zzz":
        break

    studentFirstName = input("Plese enter your first name: ")
    studentGPA = input("Please enter your gpa: ")
    if "." in studentGPA:
        studentGPA = float(studentGPA)
    else:
        print("incorrect format for GPA please start over and enter a float")
        continue

    if studentGPA >= 3.5:
        print(studentFirstName, studentLastName, "has made the Dean's list.")
    elif studentGPA >= 3.25:
        print(studentFirstName, studentLastName, "has made the Honor Roll.")
