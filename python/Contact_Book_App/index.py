exit = False

data = {}

while exit != True:
    print('''
          Contact Book App
          1. Create contact 
          2. View contact 
          3. Update Contact 
          4. Delete Contact 
          5. Search Contact
          6. Count contact 
          7. Exit
          ''')
    
    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        name = input("Enter your name: ").lower()
        age = int(input("Enter your age: "))
        email = input("Enter your email: ").lower()
        Mobile_Number = int(input("Enter your mobile number: "))
        data[name] = {
            'age':{age},
            'email':{email},
            "Mobile_Number":{Mobile_Number}
        }
        print(f"Contact {name} has been added Successfully")
        
    elif choice == 2:
        name = input("Enter name to view: ").lower()
        result = data[name]
        print(result)

    elif choice == 3:
        update_name = input("Enter name to update Contact: ").lower()
        update_age = int(input("Enter Updated Age: "))
        update_email = input("Enter Updated Email: ").lower()
        update_mob = int(input("Enter Updated Mobile Number: "))
        if update_name in data:
            data[update_name] = {'age':update_age,'email':update_email,'Mobile_Number':update_mob}
        else:
            print("User Not Found")
    elif choice == 4:
        name = input("Enter Contact name to delete: ").lower()
        if name in data:
            del data[name]
            print(f"Contact name {name} has been deleted successfully!")
        else:
            print("Contact not found!!")
    elif choice == 5:
        print(data)
    elif choice == 6:
        print(f"Total Contact in your book: {len(data)}")
    else:
        exit = True