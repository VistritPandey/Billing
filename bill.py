from Tkinter import *


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#074463"
        title = Label(self.root, text="Billing Software", bd=12, relief=GROOVE,
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
        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="R1", font=(
            "times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F2.place(x=5, y=180, width=325, height=380)

        x1_lbl = Label(F2, text="X1", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        x1_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        x2_lbl = Label(F2, text="X2", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        x2_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        x3_lbl = Label(F2, text="X3", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        x3_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        x4_lbl = Label(F2, text="X4", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        x4_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        x5_lbl = Label(F2, text="X5", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        x5_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        x6_lbl = Label(F2, text="X6", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        x6_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # Frame2
        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="R2", font=(
            "times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F3.place(x=340, y=180, width=325, height=380)

        y1_lbl = Label(F3, text="Y1", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        y1_txt = Entry(F3, width=10, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        y2_lbl = Label(F3, text="Y2", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        y2_txt = Entry(F3, width=10, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        y3_lbl = Label(F3, text="Y3", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        y3_txt = Entry(F3, width=10, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        y4_lbl = Label(F3, text="Y4", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        y4_txt = Entry(F3, width=10, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        y5_lbl = Label(F3, text="Y5", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        y5_txt = Entry(F3, width=10, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        y6_lbl = Label(F3, text="Y6", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        y6_txt = Entry(F3, width=10, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # Frame3
        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="R3", font=(
            "times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F4.place(x=670, y=180, width=325, height=380)

        z1_lbl = Label(F4, text="Z1", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        z1_txt = Entry(F4, width=10, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        z2_lbl = Label(F4, text="Z2", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        z2_txt = Entry(F4, width=10, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        z3_lbl = Label(F4, text="Z3", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        z3_txt = Entry(F4, width=10, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        z4_lbl = Label(F4, text="Z4", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        z4_txt = Entry(F4, width=10, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        z5_lbl = Label(F4, text="Z5", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        z5_txt = Entry(F4, width=10, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        z6_lbl = Label(F4, text="Z6", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        z6_txt = Entry(F4, width=10, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # Frame 4

        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=340, height=380)
        bill_title = Label(
            F5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # Button Frame

        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=(
            "times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)


root = Tk()
obj = Bill_App(root)
root.mainloop()
