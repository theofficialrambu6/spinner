from tkinter import *
import random
root = Tk()
root.title("Spinner")
root.geometry("200x300")
root.config(background="red")

answer = Entry(root)
answer.place(relx=0.5, rely= 0.2, anchor=CENTER)
fruitlist = Label(root)
randomnumber = Label(root)
luckyfruit = Label(root)
fruitlist.place(relx=0.5, rely=0.4, anchor=CENTER)
randomnumber.place(relx= 0.5, rely=0.6, anchor=CENTER)
luckyfruit.place(relx= 0.5, rely=0.7, anchor=CENTER)
list1= []
def add_fruit():
    fruitname = answer.get()
    list1.append(fruitname)
    fruitlist["text"] = "your list"+str(list1)

button1 = Button(root, text="add to list", command=add_fruit)
button1.place(relx=0.5, rely=0.3, anchor=CENTER)


def randomnum():
   length = len(list1)
   random_numb = random.randint(0, length-1)
   randomnumber["text"] = str(random_numb)
   random_num = list1[random_numb]
   luckyfruit["text"] = "the spinner picks... "+str(random_num)

button2 = Button(root, text="which is the lucky option?", command=randomnum)
button2.place(relx=0.5, rely= 0.5, anchor=CENTER)











root.mainloop()