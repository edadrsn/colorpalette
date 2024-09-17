import tkinter
from tkinter import colorchooser
from tkinter import messagebox

window=tkinter.Tk()
window.title("Color Palette")
window.geometry("600x400+400+200")
window.resizable(False,False)

def choose_color():
        my_color=colorchooser.askcolor()[1]
        result = messagebox.askyesno("Confirm", "Do you want to save these changes?")
        if result:
            if my_color:
                window.config(bg=my_color)
                label_color.config(text=f"Your Color: {my_color}")
                messagebox.showinfo("Success","Changes are saved.")
        else:
            messagebox.showinfo("Cancelled","Changes not saved")


label1=tkinter.Label(text="WELCOME TO COLOR PALETTE",bg="light blue",font="Times 20 italic bold")
label1.place(x=100,y=10)

label_color=tkinter.Label(text="Your color:",font="Times 20 italic bold",bg="light blue")
label_color.place(x=50,y=300)

color_button=tkinter.Button(text="Choose Your Color",bg="pink",font="Times 15 bold italic",command=choose_color)
color_button.place(x=200,y=100)


window.mainloop()