import tkinter as tk 
from tkinter import ttk
import numpy as np
from tkinter import messagebox

window = tk.Tk()

window.title("Tic-Tac-Toe")
window.geometry('300x240')
window.configure(bg="#f0f0f0")

btn = "0"
# def toggle_cond():
    
win_cond = [[0,3,6],[1,4,7],[2,5,8],[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6]]

def handle_click(r,c):
    global btn 
    if btn == 'X':
        button1[r][c].configure(text=btn)
        button1[r][c].configure(state='disabled')
        btn = "0"
    else:
        button1[r][c].configure(text=btn)
        button1[r][c].configure(state='disabled')
        btn = "X"
        
    change_text.set(f"User {btn} turn")
    for check in win_cond:
           i,j,k = check
           if button1[i//3][i%3]['text'] == button1[j//3][j%3]['text'] == button1[k//3][k%3]['text'] != "":
               messagebox.showinfo(message=f"user {button1[i//3][i%3]['text']} wins")
               window.quit()
    return
    
button1 = [[None]*3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        button = tk.Button(master=window,width=13,height=4,text="",command= lambda c=j , r=i: handle_click(r,c))
        # button.config(style="TButton") 
        button1[i][j] = button
        button.grid(row=i,column=j)

change_text = tk.StringVar()
show = tk.Label(window,text=f"User {btn} turn",textvariable=change_text)
show.grid(row=3,columnspan=10)

window.mainloop()