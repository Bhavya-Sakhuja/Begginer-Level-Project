import random as rd

ishappen = "y"

subject = ["Shahrukh Khan","Virat Kohli","Salman Khan","Ajay Devgan","A mumbai Cat","A group of Monkeys","A group of dogs"]

Actions = ['launches','cancels','dance with Ram','eats','declare war on']

Object = ['at red fort','in mumbai local train','a plate of samosas','inside parliament','at ganga ghat']

while(ishappen == 'y'):
    From_Sub = rd.choice(subject)
    From_Actions = rd.choice(Actions)
    From_Object = rd.choice(Object)

    print(f"BREAKING NEWS: {From_Sub} {From_Actions} {From_Object}")
   
    ishappen = input("Do You Want More News (y/n): ").strip().lower()
else:
    print("GoodBye")
