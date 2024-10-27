import tkinter

window = tkinter.Tk()
window.title("My GUI Program")
window.minsize(width=800,height=500)


#Label
label = tkinter.Label(text="This is a lebel")
label.pack()



window.mainloop()