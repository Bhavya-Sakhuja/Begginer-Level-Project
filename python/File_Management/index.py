'''
File Management App
1: create file 
2: view all files
3: delete file 
4: Read file 
5: Edit File 
6: Exit 

Enter Your Choice(1-6) = 2 
2 -- all files in directory 
1 -- create file 
Enter the file-name to create = hello.java
File Name hello.java created successfully!
3 -- Enter the name of file you want to delete 
hello.java has been deleted successfully 
4 -- enter the file name to read 
content of {file_name} : 
5 - enter file name to edit 
enter data to edit 
content edit to filename successfully 
'''

import os 

Final_folder = os.getcwd()


next = True

while next != False:
  print("File Management App")
  print('''
  1: create file 
  2: view all files
  3: delete file 
  4: Read file 
  5: Edit File 
  6: Exit 
  ''')
  
  choice = int(input("Enter your Choice(1-6): "))

  if choice == 1:
    name = input("Enter the file name to create: ")
    file_path = os.path.join(Final_folder, name)
    with open(file_path, "w") as f:
      f.write("")
    print(f"File {name} is created successfully")
    next = True

  elif choice == 2:
    files = os.listdir(Final_folder)
    if not files:
       print("No files found.")
    else:
        print("Files in directory:")
        for file in files:
            print(file)
    next = True

  elif choice == 3:
    name = input("Enter the name of file you want to delete")
    for root,dirct,file_name in os.walk(Final_folder):
      file_path = os.path.join(root, name)
      if os.path.exists(file_path):
          for files in file_name:
              if name == files:
                os.remove(os.path.join(Final_folder, name))
                print(f"File {name} deleted successfully")
      else:
         print("File doesn't Found")  
    next = True

  elif choice == 4:
    name = input("Enter the file name to read: ")
    file_path = os.path.join(Final_folder, name)
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            print("\nContent of file:")
            print(f.read())
    else:
        print("File does not exist!")
    next = True

  elif choice == 5:
    name = input("Enter the file name to edit: ")
    file_path = os.path.join(Final_folder, name)
    if os.path.exists(file_path):
        data = input("Enter data to write: ")
        with open(file_path, "w") as f:
            f.write(data)
            print("File edited successfully!")
    else:
            print("File does not exist!")
    next = True

  else:
    next = False

