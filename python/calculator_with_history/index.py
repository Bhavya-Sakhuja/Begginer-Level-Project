Continue = True

while(Continue):
    print("Enter calculation (+, -, *, /, %) or command (history, clear, exit): ")
    
    value = input()

    if(value == 'history'):
       with open("Storage.txt",'r') as f:
          result = f.read()
          print(result)

    elif(value == 'clear'):
       with open("storage.txt",'w') as f:
          f.write(" ")
       print("History cleared.")

    elif(value == 'exit'):
       print("GoodBye!")
       break

    else:
       result = eval(value)
       ans = f"{value} = {result}"
       print(f'Result: ',result)

       with open("storage.txt",'a') as f:
          f.write(ans)
          f.write('\n')
    
    
    




