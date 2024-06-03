from tkinter import *

# Create the root window
root = Tk()
root.geometry("400x600")
root.title("Calculator By Prabha")
# p1 = PhotoImage(file = "https://png.pngtree.com/png-vector/20190115/ourmid/pngtree-vector-calculator-icon-png-image_319747.jpg")
# root.iconphoto(False, p1)
# root.wm_iconbitmap("https://png.pngtree.com/png-vector/20190115/ourmid/pngtree-vector-calculator-icon-png-image_319747.jpg")

# Global variable for the screen value
scvalue = StringVar()
scvalue.set("")

# Function to handle button clicks 
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            value = eval(scvalue.get())
            scvalue.set(value)
        except Exception as e:
            scvalue.set("Error")
    elif text == "C":
        scvalue.set("")
    else:
        scvalue.set(scvalue.get() + text)
    screen.update()

# Configure the display screen
screen = Entry(root, textvariable=scvalue, font="Helvetica 30 bold", bg="#f0f0f0", bd=10, relief=SUNKEN, justify=RIGHT)
screen.pack(fill=BOTH, ipadx=8, pady=10, padx=10)

# Button configuration
button_font = "Helvetica 20 bold"
button_bg = "#8ddcf0"
button_active_bg = "#ffa07a"
button_fg = "#000000"
button_active_fg = "#ffffff"

# Function to create a frame with buttons
def create_frame(button_texts):
    frame = Frame(root, bg="#dcdcdc")
    for text in button_texts:
        button = Button(frame, text=text, font=button_font, bg=button_bg, activebackground=button_active_bg, fg=button_fg, activeforeground=button_active_fg, bd=5)
        button.pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=5)
        button.bind("<Button-1>", click)
    frame.pack(expand=True, fill=BOTH, padx=10, pady=5)
    return frame

# Create frames for calculator buttons
create_frame(["7", "8", "9", "+"])
create_frame(["4", "5", "6", "-"])
create_frame(["1", "2", "3", "*"])
create_frame(["0", "00", "%", "/"])
create_frame(["C", "=", "."])

# Start the Tkinter main loop
root.mainloop()
