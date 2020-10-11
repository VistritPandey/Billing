from Tkinter import *


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#074463"
        title = Label(self.root, text="Jaysurya Billing", bd=12, relief=GROOVE,
                      bg=bg_color, fg="white", font=("times new roman", 30, "bold"), pady=2).pack(fill=X)
        F = LabelFrame(self.root, text="Customer Details", font=(
            "times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F.place(x=0, y=80, relwidth=1)


root = Tk()
obj = Bill_App(root)
root.mainloop()
