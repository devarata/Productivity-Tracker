import tkinter as tk
from tkinter import StringVar
import os
import tkinter.messagebox as mb

def getTask(entry1,root):
    outF = open("output.txt","w")
    outF.write(entry1.get())
    outF.close()
    root.destroy()



def task_name(root,final_task):
    try:
        os.remove("output.txt")
    except OSError:
        pass
    canvas = tk.Canvas(root, width = 400, height = 300,  relief = 'raised',bg = "#92CCEB")
    canvas.pack()
    label1 = tk.Label(root, text='Task Tracker')
    label1.config(font=('helvetica', 14))
    label1.config(bg="#92CCEB")
    canvas.create_window(200, 25, window=label1)
    label2 = tk.Label(root, text='Type the task to track:')
    label2.config(font=('helvetica', 10))
    label2.config(bg = "#92CCEB")
    canvas.create_window(200, 100, window=label2)
    entry1 = tk.Entry(root)
    entry1.focus()
    canvas.create_window(200, 140, window=entry1)
    button1 = tk.Button(text='Track', command=lambda:getTask(entry1,root), bg='#0288D1', fg='white', font=('helvetica', 9, 'bold'))
    canvas.create_window(200, 180, window=button1)
    root.mainloop()



def task():
    root= tk.Tk()
    final_task = ""
    task_name(root,final_task)
    try:
        with open('output.txt','r') as f:
            final_task = f.readline()
    except FileNotFoundError:
            mb.showerror('Output','closed the box without entering anything')
    return final_task
