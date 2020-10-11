from Tkinter import *


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#074463"
        title = Label(self.root, text="Jaysurya Billing", bd=12, relief=GROOVE,
                      bg=bg_color, fg="white", font=("times new roman", 30, "bold"), pady=2).pack(fill=X)
        # Customer Detail
        F = LabelFrame(self.root, text="Customer Details", font=(
            "times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F, text="Customer Name", bg=bg_color, fg="white", font=(
            "times new roman", 15, "bold")).grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F, width=15, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F, text="Phone Number", bg=bg_color, fg="white", font=(
            "times new roman", 15, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F, width=15, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F, text="Bill Number", bg=bg_color, fg="white", font=(
            "times new roman", 15, "bold")).grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F, width=15, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=5, pady=5, padx=10)

        bill_btn = Button(F, text="Search", width=10, bd=7,
                          font="arial 12 bold").grid(row=0, column=6, pady=10, padx=10)

        # Frame1
        F2 = LabelFrame(self.root, bd=10, text="R1", font=(
            "times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F2.place(x=5, y=180, width=325, height=380)

        item1_lbl = Label(F2, text="X1", font=("times new roman", 16, "bold"), bg=bg_color,
                          fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        item1_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"),
                          bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        item2_lbl = Label(F2, text="X2", font=("times new roman", 16, "bold"), bg=bg_color,
                          fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        item2_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"),
                          bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        item3_lbl = Label(F2, text="X3", font=("times new roman", 16, "bold"), bg=bg_color,
                          fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        item3_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"),
                          bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        item4_lbl = Label(F2, text="X4", font=("times new roman", 16, "bold"), bg=bg_color,
                          fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        item4_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"),
                          bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        item5_lbl = Label(F2, text="X5", font=("times new roman", 16, "bold"), bg=bg_color,
                          fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        item5_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"),
                          bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)
        item6_lbl = Label(F2, text="X6", font=("times new roman", 16, "bold"), bg=bg_color,
                          fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        item6_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"),
                          bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)


root = Tk()
obj = Bill_App(root)
root.mainloop()
