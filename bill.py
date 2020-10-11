from Tkinter import *

# Prices
tax = 0.18
x1_price = 10
x2_price = 10
x3_price = 10
x4_price = 10
x5_price = 10
x6_price = 10

y1_price = 10
y2_price = 10
y3_price = 10
y4_price = 10
y5_price = 10
y6_price = 10

z1_price = 10
z2_price = 10
z3_price = 10
z4_price = 10
z5_price = 10
z6_price = 10


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#074463"
        title = Label(self.root, text="Billing Software", bd=12, relief=GROOVE,
                      bg=bg_color, fg="white", font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

        # Variables
        self.x1 = IntVar()
        self.x2 = IntVar()
        self.x3 = IntVar()
        self.x4 = IntVar()
        self.x5 = IntVar()
        self.x6 = IntVar()

        self.y1 = IntVar()
        self.y2 = IntVar()
        self.y3 = IntVar()
        self.y4 = IntVar()
        self.y5 = IntVar()
        self.y6 = IntVar()

        self.z1 = IntVar()
        self.z2 = IntVar()
        self.z3 = IntVar()
        self.z4 = IntVar()
        self.z5 = IntVar()
        self.z6 = IntVar()

        self.r1_total = StringVar()
        self.r2_total = StringVar()
        self.r3_total = StringVar()

        self.r1_tax = StringVar()
        self.r2_tax = StringVar()
        self.r3_tax = StringVar()

        self.c_name = StringVar()
        self.c_phon = StringVar()
        self.bill_no = StringVar()
        self.search_bill = StringVar()

        # Customer Detail
        F = LabelFrame(self.root, text="Customer Details", font=(
            "times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F, text="Customer Name", bg=bg_color, fg="white", font=(
            "times new roman", 15, "bold")).grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F, width=15, textvariable=self.c_name, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F, text="Phone Number", bg=bg_color, fg="white", font=(
            "times new roman", 15, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F, width=15, textvariable=self.c_phon, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F, text="Bill Number", bg=bg_color, fg="white", font=(
            "times new roman", 15, "bold")).grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F, width=15, textvariable=self.search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=5, pady=5, padx=10)

        bill_btn = Button(F, text="Search", width=10, bd=7,
                          font="arial 12 bold").grid(row=0, column=6, pady=10, padx=10)

        # Frame1
        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="R1", font=(
            "times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F2.place(x=5, y=180, width=325, height=380)

        x1_lbl = Label(F2, text="X1", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        x1_txt = Entry(F2, width=10, textvariable=self.x1, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        x2_lbl = Label(F2, text="X2", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        x2_txt = Entry(F2, width=10, textvariable=self.x2, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        x3_lbl = Label(F2, text="X3", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        x3_txt = Entry(F2, width=10, textvariable=self.x3, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        x4_lbl = Label(F2, text="X4", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        x4_txt = Entry(F2, width=10, textvariable=self.x4, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        x5_lbl = Label(F2, text="X5", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        x5_txt = Entry(F2, width=10, textvariable=self.x5, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        x6_lbl = Label(F2, text="X6", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        x6_txt = Entry(F2, width=10, textvariable=self.x6, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # Frame2
        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="R2", font=(
            "times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F3.place(x=340, y=180, width=325, height=380)

        y1_lbl = Label(F3, text="Y1", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        y1_txt = Entry(F3, width=10, textvariable=self.y1, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        y2_lbl = Label(F3, text="Y2", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        y2_txt = Entry(F3, width=10, textvariable=self.y2, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        y3_lbl = Label(F3, text="Y3", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        y3_txt = Entry(F3, width=10, textvariable=self.y3, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        y4_lbl = Label(F3, text="Y4", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        y4_txt = Entry(F3, width=10, textvariable=self.y4, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        y5_lbl = Label(F3, text="Y5", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        y5_txt = Entry(F3, width=10, textvariable=self.y5, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        y6_lbl = Label(F3, text="Y6", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        y6_txt = Entry(F3, width=10, textvariable=self.y6, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # Frame3
        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="R3", font=(
            "times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F4.place(x=670, y=180, width=325, height=380)

        z1_lbl = Label(F4, text="Z1", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        z1_txt = Entry(F4, width=10, textvariable=self.z1, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        z2_lbl = Label(F4, text="Z2", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        z2_txt = Entry(F4, width=10, textvariable=self.z2, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        z3_lbl = Label(F4, text="Z3", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        z3_txt = Entry(F4, width=10, textvariable=self.z3, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        z4_lbl = Label(F4, text="Z4", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        z4_txt = Entry(F4, width=10, textvariable=self.z4, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        z5_lbl = Label(F4, text="Z5", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        z5_txt = Entry(F4, width=10, textvariable=self.z5, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        z6_lbl = Label(F4, text="Z6", font=("times new roman", 16, "bold"), bg=bg_color,
                       fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        z6_txt = Entry(F4, width=10, textvariable=self.z6, font=("times new roman", 16, "bold"),
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
        m1_lbl = Label(F6, text="Total R1 price", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=0, column=0, padx=20, pady=1, sticky="w")
        m1_txt = Entry(F6, width=18, textvariable=self.r1_total, font="arial 10 bold", bd=7,
                       relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)

        m2_lbl = Label(F6, text="Total R2 price", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt = Entry(F6, width=18, textvariable=self.r2_total, font="arial 10 bold", bd=7,
                       relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(F6, text="Total R3 price", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=2, column=0, padx=20, pady=1, sticky="w")
        m3_txt = Entry(F6, width=18, textvariable=self.r3_total, font="arial 10 bold", bd=7,
                       relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        c1_lbl = Label(F6, text="R1 Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=0, column=2, padx=20, pady=1, sticky="w")
        c1_txt = Entry(F6, width=18, textvariable=self.r1_tax, font="arial 10 bold", bd=7,
                       relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        c2_lbl = Label(F6, text="R2 Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=1, column=2, padx=20, pady=1, sticky="w")
        c2_txt = Entry(F6, width=18, textvariable=self.r2_tax, font="arial 10 bold", bd=7,
                       relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        c3_lbl = Label(F6, text="R3 Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=2, column=2, padx=20, pady=1, sticky="w")
        c3_txt = Entry(F6, width=18, textvariable=self.r3_tax, font="arial 10 bold", bd=7,
                       relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        # Button F

        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=750, width=580, height=150)

        total_btn = Button(btn_f, command=self.total, text="Total", bg="cadetblue", fg="white", bd=2, pady=15, width=10, font="arial 15 bold").grid(
            row=0, column=0, padx=5, pady=5)
        GBill_btn = Button(btn_f, text="Generate Bill", bg="cadetblue", fg="white", bd=2, pady=15, width=10, font="arial 15 bold").grid(
            row=0, column=1, padx=5, pady=5)
        clear_btn = Button(btn_f, text="Clear", bg="cadetblue", fg="white", bd=2, pady=15, width=10, font="arial 15 bold").grid(
            row=0, column=2, padx=5, pady=5)
        exit_btn = Button(btn_f, text="Exit", bg="cadetblue", fg="white", bd=2, pady=15, width=10, font="arial 15 bold").grid(
            row=0, column=3, padx=5, pady=5)

    def total(self):
        self.total_r1_price = float(
            (self.x1.get()*x1_price) +
            (self.x2.get()*x2_price) +
            (self.x3.get()*x3_price) +
            (self.x4.get()*x4_price) +
            (self.x5.get()*x5_price) +
            (self.x6.get()*x6_price)
        )
        self.r1_total.set("Rs."+str(self.total_r1_price))
        self.r1_tax.set("Rs."+str(round((self.total_r1_price*tax), 2)))

        self.total_r2_price = float(
            (self.y1.get()*y1_price) +
            (self.y2.get()*y2_price) +
            (self.y3.get()*y3_price) +
            (self.y4.get()*y4_price) +
            (self.y5.get()*y5_price) +
            (self.y6.get()*y6_price)
        )
        self.r2_total.set("Rs."+str(self.total_r2_price))
        self.r2_tax.set("Rs."+str(round((self.total_r2_price*tax), 2)))

        self.total_r3_price = float(
            (self.z1.get()*z1_price) +
            (self.z2.get()*z2_price) +
            (self.z3.get()*z3_price) +
            (self.z4.get()*z4_price) +
            (self.z5.get()*z5_price) +
            (self.z6.get()*z6_price)
        )
        self.r3_total.set("Rs."+str(self.total_r3_price))
        self.r3_tax.set("Rs."+str(round((self.total_r3_price*tax), 2)))


root = Tk()
obj = Bill_App(root)
root.mainloop()
