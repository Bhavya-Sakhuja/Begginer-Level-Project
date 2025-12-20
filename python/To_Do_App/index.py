'''
Welcome message 
how many task do you want to add?
today's task are --- write kiya hai vo show ho 
enter 1 - add
2 - update 
3 - delete 
4 - view 
5 - exit or stop krne ke liye 
--> add krne prr line show hogi 
   task book has been added 
---> update -- line show hogi kya update     krna chahte ho 
     updated message 
--->delete me bss ek element delete hoga 
    task gaming has been deleted
--->exit 
    closing the program 
--->view all the task written in the list 
'''

print("----Welcome to Task Management APP----")

total = int(input("How many task do you want to add? "))

To_Do = []

i = 1 
while i<=total:
    task = input(f'Enter Task {i}: ').capitalize()
    To_Do.append(task)
    i += 1

exit = False

while exit != True:
   print('Enter 1 -- Add\n2 -- Update\n3 -- Delete\n4 -- View\n5 -- Exit')

   Num = int(input("Enter What You Want to do Next:  "))

   if Num == 1:
      add = input("Enter task do you want to add: ").capitalize()
      print(f'Task {add} has been Added')
      To_Do.append(add)
      exit = False

   elif Num == 2:
      update = input("Enter Task Name do you want to update: ").capitalize()
     
      if update in To_Do:
         new_update = input("Enter New Task: ").capitalize()
         no = 0
         for i in To_Do:
            if update == i:
               index = no
            no += 1
         To_Do[index] = new_update
         print("Updated Task ",{new_update})

      else:
        print("Task not Found...")
      exit = False

   elif Num == 3:
      delete = input("Which task do you want to delete: ").capitalize()
      if delete in To_Do:
        To_Do.remove(delete)
        print(f'Task {delete} has been deleted')
      else:
        print("Element not Found...")
      exit = False

   elif Num == 4:
      print(To_Do)
      exit = False

   else:
      exit = True
