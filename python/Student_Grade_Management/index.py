'''
welcome to student grade management system
student grade management system 
1. add student 
2. update student 
3. delete student 
4. view students
5. exit 

enter your choice 
4 = view student list 
no student found/no student add

gopal : 100
laskshmi : 40

1 = enter student name 
enter student grade 
added {name} with a {grade}

2 = enter student name 
updated marks = ---
radha with marks are updated 

3 = enter student name 
{name} has been deleted 

'''

print("--Welcome to Student Grade Management System--")
print("Student Grade Management System")
print("1. Add Student\n2. Update student\n3. Delete Student\n4. View Student\n5. Exit")

working = True

dict = dict(())

while working != False:
    choice = int(input("Enter your Choice: "))

    if choice == 1:
        name = input("Enter Student Name: ").capitalize()
        grade = int(input("Enter Student Marks: "))
        dict[name] = grade
        print(f'Added {name} with a {grade}')
        working = True

    elif choice == 2:
        name = input("Enter Student name: ").capitalize()
        if name in dict:
            grade = int(input("Enter Updated Marks: "))
            dict[name] = grade
            print(f"{name} with Marks are Updated") 
        else:
            print("Student not Found")
        working = True

    elif choice == 3:
        name = input("Enter Student Name: ").capitalize()
        del dict[name] 
        print(f'{name} has been deleted ')
        working = True
    
    elif choice == 4:
        if not dict:
            print("No Element Added/Found")
        else:
            print(dict)
        working = True

    else:
        print("Thnkuuu!")
        working = False    
    
 