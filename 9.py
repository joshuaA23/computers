import tkinter
import tkinter.messagebox as box

top = tkinter.Tk()

def helloCallBack():
   box.showinfo( "Hello Python", "Hello World")

B = tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()
