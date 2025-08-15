from tkinter import *
import math

def prime_code():
    try:
        nm = int(e1.get())
    except ValueError:
        l2.config(text="invalid input! enter a number",fg="red",font="bold")
        return


    if nm <= 1  :
        l2.config(text="Not Prime",fg="red",font="bold")
    else:
        for i in range (2,int(math.sqrt(nm)) + 1):
            if nm % i == 0:
                l2.config(text="Not Prime",fg="red" , font="bold")
                break
                
        else:
            l2.config(text="Prime", fg="green" , font="bold" )


root = Tk()
root.title("prime numbers")
root.geometry("400x200")
root.configure(bg="yellow")

l1 = Label(root , text="prime number : "  , font="bold")
l1.configure(bg="yellow")
l1.grid(row=1,column=2)

l2 = Label(root, text="", bg="yellow")
l2.grid(row=2, column=3)

e1 = Entry(root)
e1.grid(row=1 , column= 3)

b1 = Button(root,text="Check",font="20",command=prime_code)
b1.grid(row=4,column=3)

root.mainloop()