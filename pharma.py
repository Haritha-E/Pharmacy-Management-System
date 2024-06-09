from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class PharmacyManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")
        
        
        #******************************addMed variable**********************
        self.refMed_var=StringVar()
        self.addmed_var=StringVar()
        self.addprice_var=StringVar()
        self.addquant_var=StringVar()
        
        #*****************************main variable**************************
        self.ref_var=StringVar()
        self.cmpName_var=StringVar()
        self.typeMed_var=StringVar()
        self.medName_var=StringVar()
        self.lot_var=StringVar()
        self.issuedate_var=StringVar()
        self.expdate_var=StringVar()
        self.uses_var=StringVar()
        self.sideEffect_var=StringVar()
        self.warning_var=StringVar()
        self.dosage_var=StringVar()
        self.price_var=StringVar()
        self.product_var=StringVar()
        
        
        lbltitle=Label(self.root,text="PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE,
                       bg='white',fg="dark green",font=("times new roman",50,"bold"),padx=2,pady=4)
        lbltitle.pack(side=TOP,fill=X)
        
        img1=Image.open("logo1.png")
        img1=img1.resize((80,80),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=60, y=15)
        
        
        #******************************DataFrame******************************
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1530,height=400)
        
        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",
                                 fg="dark green",font=("arial",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)
    
        
        
        #*******************************Button Frame*********************
        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=520,width=1530,height=65)
        
        
        #********************************Main Button***********************
        btnAddData=Button(ButtonFrame,command=self.add_data,text="Medicine Add",font=("arial",12,"bold"),bg="darkgreen",fg="white")
        btnAddData.grid(row=0,column=0)
        
        btnUpdateMed=Button(ButtonFrame,command=self.Update,text="UPDATE",font=("arial",13,"bold"),width=14,bg="darkgreen",fg="white")
        btnUpdateMed.grid(row=0,column=1)
        
        btnDeleteMed=Button(ButtonFrame,command=self.delete,text="DELETE",font=("arial",13,"bold"),width=14,bg="red",fg="white")
        btnDeleteMed.grid(row=0,column=2)
        
        btnResetMed=Button(ButtonFrame,command=self.reset,text="RESET",font=("arial",13,"bold"),width=14,bg="darkgreen",fg="white")
        btnResetMed.grid(row=0,column=3)
        
        btnExitMed=Button(ButtonFrame,command=self.exit_application,text="EXIT",font=("arial",13,"bold"),width=14,bg="red",fg="white")
        btnExitMed.grid(row=0,column=4)
        
        
        #******************Search By************************
        lblSearch=Label(ButtonFrame,font=("arial",15,"bold"),text="Search By",padx=2,bg="red",fg="white")
        lblSearch.grid(row=0,column=5,sticky=W)
        
        
        # Variable
        self.search_var=StringVar()
        search_combo=ttk.Combobox(ButtonFrame,textvariable=self.search_var,width=12,font=("arial",15,"bold"),state="readonly")
        search_combo["values"]=("Ref_no","medname","lot")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)
        
        self.searchTxt_var=StringVar()
        txtSearch=Entry(ButtonFrame,textvariable=self.searchTxt_var,bd=3,relief=RIDGE,width=12,font=("arial",17,"bold"))
        txtSearch.grid(row=0,column=7)
        
        searchBtn=Button(ButtonFrame,command=self.search_data,text="SEARCH",font=("arial",13,"bold"),width=13,bg="darkgreen",fg="white")
        searchBtn.grid(row=0,column=8)
        
        showAll=Button(ButtonFrame,command=self.show_all_data,text="SHOW ALL",font=("arial",13,"bold"),width=13,bg="red",fg="white")
        showAll.grid(row=0,column=9)
        
        
        #***********************label and entry*********************
        
        
        lblrefno=Label(DataFrameLeft,font=("arial",12,"bold"),text="Reference No",padx=2,pady=6)
        lblrefno.grid(row=0,column=0,sticky=W)
        
        self.comrefno=Entry(DataFrameLeft,textvariable=self.ref_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        self.comrefno.grid(row=0,column=1)

        
        lblCmpName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Company Name: ",padx=2,pady=6)
        lblCmpName.grid(row=1,column=0,sticky=W)
        txtCmpName=Entry(DataFrameLeft,textvariable=self.cmpName_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtCmpName.grid(row=1,column=1)
        
        lblTypeofMedicine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Type of Medicine",padx=2,pady=6)
        lblTypeofMedicine.grid(row=2,column=0,sticky=W)
        
        comTypeofMedicine=ttk.Combobox(DataFrameLeft,textvariable=self.typeMed_var,width=27,font=("arial",12,"bold"),state="readonly")
        comTypeofMedicine["values"]=("Tablet","Liquid","Capsules","Topical Medicines","Drops","Inhales","Injection")
        comTypeofMedicine.current(0)
        comTypeofMedicine.grid(row=2,column=1)
        
        
        #********************Add Medicine**********************
        
        
        lblMedicineName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medicine Name",padx=2,pady=6)
        lblMedicineName.grid(row=3,column=0,sticky=W)
        
        
        self.comMedicineName=Entry(DataFrameLeft,textvariable=self.medName_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        self.comMedicineName.grid(row=3,column=1)
        
        
        lblLotNo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot No: ",padx=2,pady=6)
        lblLotNo.grid(row=4,column=0,sticky=W)
        txtLotNo=Entry(DataFrameLeft,textvariable=self.lot_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtLotNo.grid(row=4,column=1)
        
        lblIssueDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date: ",padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataFrameLeft,textvariable=self.issuedate_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtIssueDate.grid(row=5,column=1)
        
        lblExDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Expiry Date: ",padx=2,pady=6)
        lblExDate.grid(row=6,column=0,sticky=W)
        txtExDate=Entry(DataFrameLeft,textvariable=self.expdate_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtExDate.grid(row=6,column=1)
        
        lblUses=Label(DataFrameLeft,font=("arial",12,"bold"),text="Uses: ",padx=2,pady=4)
        lblUses.grid(row=7,column=0,sticky=W)
        txtUses=Entry(DataFrameLeft,textvariable=self.uses_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtUses.grid(row=7,column=1)
        
        lblSideEffect=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effect: ",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataFrameLeft,textvariable=self.sideEffect_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtSideEffect.grid(row=8,column=1)
        
        lblPrecWarning=Label(DataFrameLeft,font=("arial",12,"bold"),text="Precaution/Warning: ",padx=15)
        lblPrecWarning.grid(row=0,column=2,sticky=W)
        txtPrecWarning=Entry(DataFrameLeft,textvariable=self.warning_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=27)
        txtPrecWarning.grid(row=0,column=3)
        
        lblDosage=Label(DataFrameLeft,font=("arial",12,"bold"),text="Dosage: ",padx=15,pady=6)
        lblDosage.grid(row=1,column=2,sticky=W)
        txtDosage=Entry(DataFrameLeft,textvariable=self.dosage_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=27)
        txtDosage.grid(row=1,column=3)
        
        lblPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Tablets Price: ",padx=15,pady=6)
        lblPrice.grid(row=2,column=2,sticky=W)
        txtPrice=Entry(DataFrameLeft,textvariable=self.price_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=27)
        txtPrice.grid(row=2,column=3)
        
        lblProductQt=Label(DataFrameLeft,font=("arial",12,"bold"),text="Product Quantity: ",padx=15,pady=6)
        lblProductQt.grid(row=3,column=2,sticky=W)
        txtProductQt=Entry(DataFrameLeft,textvariable=self.product_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=27)
        txtProductQt.grid(row=3,column=3,sticky=W)
        
        
        
        #*********************************Images**********************************
        lblhome=Label(DataFrameLeft,font=("arial",15,"bold"),text="Stay Home Stay Safe",padx=2,pady=6,bg="white",fg="red",width=37)
        lblhome.place(x=410, y=140)
        
        img2=Image.open("logo.jpeg")
        img2=img2.resize((200,135),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(self.root,image=self.photoimg2,borderwidth=0)
        b1.place(x=490, y=340)
        
        img3=Image.open("img3.jpg")
        img3=img3.resize((200,135),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b1=Button(self.root,image=self.photoimg3,borderwidth=0)
        b1.place(x=710, y=340)
        
        
        
        #***************************** dataFrame Right ********************
        
        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Department",
                                 fg="dark green",font=("arial",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)
                
        
        lblrefno=Label(DataFrameRight,font=("arial",12,"bold"),text="Reference No:",padx=15,pady=6)
        lblrefno.place(x=0,y=5)
        self.txtrefno=ttk.Combobox(DataFrameRight,textvariable=self.refMed_var,width=27,font=("arial",12,"bold"),state="readonly")
        self.txtrefno.place(x=135,y=5)
        self.txtrefno.bind("<<ComboboxSelected>>", self.update_medname)

        
        lblmedName=Label(DataFrameRight,font=("arial",12,"bold"),text="Medicine Name:",padx=15,pady=6)
        lblmedName.place(x=0,y=35)
        self.txtmedName=ttk.Combobox(DataFrameRight,textvariable=self.addmed_var,width=27,font=("arial",12,"bold"),state="readonly")
        self.txtmedName.place(x=135,y=35)
        self.update_comboboxes()
        
                
        lblquant=Label(DataFrameRight,font=("arial",12,"bold"),text="Quantity:",padx=15,pady=6)
        lblquant.place(x=0,y=65)
        self.txtquant=Entry(DataFrameRight,textvariable=self.addquant_var,width=29,font=("arial",12,"bold"))
        self.txtquant.place(x=135,y=65)
        
        lblprice=Label(DataFrameRight,font=("arial",12,"bold"),text="Price:",padx=15,pady=6)
        lblprice.place(x=0,y=95)
        self.txtprice=Entry(DataFrameRight,textvariable=self.addprice_var,width=29,font=("arial",12,"bold"))
        self.txtprice.place(x=135,y=95)
        #*******************************side frame**************************
        side_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=130,width=290,height=180)
        
        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)
        
        self.medicine_table=ttk.Treeview(side_frame,column=("ref","medname","quantity","price"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)
        
        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)
        
        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname",text="Medicine Name")
        self.medicine_table.heading("quantity",text="Quantity")
        self.medicine_table.heading("price",text="Price")

        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)
        
        self.medicine_table.column("ref",width=20)
        self.medicine_table.column("medname",width=80)
        self.medicine_table.column("quantity",width=50)
        self.medicine_table.column("price",width=50)
        
        self.medicine_table.bind("<ButtonRelease-1>",self.Medget_cursor)
        
        
        #************************************ Medicine Add Button ********************************************
        down_frame=Frame(DataFrameRight,bd=3,relief=RIDGE,bg="darkgreen")
        down_frame.place(x=330,y=130,width=135,height=180)
        
        btnAddmed=Button(down_frame,command=self.AddMed,text="ADD",font=("arial",12,"bold"),width=12,bg="lime",fg="white",pady=2)
        btnAddmed.grid(row=0,column=0)

        btnUpdatemed=Button(down_frame,command=self.UpdateMed,text="UPDATE",font=("arial",12,"bold"),width=12,bg="purple",fg="white",pady=2)
        btnUpdatemed.grid(row=1,column=0)

        btnDeletemed=Button(down_frame,command=self.DeleteMed,text="DELETE",font=("arial",12,"bold"),width=12,bg="red",fg="white",pady=2)
        btnDeletemed.grid(row=2,column=0)

        btnClearmed=Button(down_frame,command=self.ClearMed,text="CLEAR",font=("arial",12,"bold"),width=12,bg="orange",fg="white",pady=2)
        btnClearmed.grid(row=3,column=0)
        
        btnBill=Button(down_frame,command=self.generate_bill,text="GENERATE BILL",font=("arial",12,"bold"),width=12,bg="lime",fg="white",pady=2)
        btnBill.grid(row=4,column=0)
        
        
        #*******************************Frame Details*********************************
        Framedetails=Frame(self.root,bd=15,relief=RIDGE)
        Framedetails.place(x=0,y=580,width=1530,height=210)
        
        
        #******************************Main table & scrollbar*************************
        Table_frame=Frame(Framedetails,bd=15,relief=RIDGE)
        Table_frame.place(x=0,y=1,width=1500,height=180)
        
        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        self.pharmacy_table=ttk.Treeview(Table_frame,column=("ref","companyname","type","tabletname","lotno","issuedate",
                                                             "expdate","uses","sideeffect","warning","dosage","price","productqt"),
                                         xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)
        
        self.pharmacy_table["show"]="headings"
        
        self.pharmacy_table.heading("ref",text="Reference No")
        self.pharmacy_table.heading("companyname",text="Company Name")
        self.pharmacy_table.heading("type",text="Type of Medicine")
        self.pharmacy_table.heading("tabletname",text="Tablet Name")
        self.pharmacy_table.heading("lotno",text="Lot No")
        self.pharmacy_table.heading("issuedate",text="Issue Date")
        self.pharmacy_table.heading("expdate",text="Expiry Date")
        self.pharmacy_table.heading("uses",text="Uses")
        self.pharmacy_table.heading("sideeffect",text="Side Effect")
        self.pharmacy_table.heading("warning",text="Precaution/Warning")
        self.pharmacy_table.heading("dosage",text="Dosage")
        self.pharmacy_table.heading("price",text="Price")
        self.pharmacy_table.heading("productqt",text="Quantity")
        self.pharmacy_table.pack(fill=BOTH,expand=1)
        
        self.pharmacy_table.column("ref",width=100)
        self.pharmacy_table.column("companyname",width=100)
        self.pharmacy_table.column("type",width=100)
        self.pharmacy_table.column("tabletname",width=100)
        self.pharmacy_table.column("lotno",width=100)
        self.pharmacy_table.column("issuedate",width=100)
        self.pharmacy_table.column("expdate",width=100)
        self.pharmacy_table.column("uses",width=100)
        self.pharmacy_table.column("sideeffect",width=100)
        self.pharmacy_table.column("warning",width=100)
        self.pharmacy_table.column("dosage",width=100)
        self.pharmacy_table.column("price",width=100)
        self.pharmacy_table.column("productqt",width=100)
        self.fetch_dataMed()
        self.fetch_data()
        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        
        
        #***********************Add Medicine Functionality Declaration********************************
        
    def AddMed(self):
        if not self.refMed_var.get():
            messagebox.showerror("Error", "Please select a medicine.")
            return
    
        selected_ref = self.refMed_var.get()
        selected_quantity = int(self.addquant_var.get())
        
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="pharmacy")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT product FROM pharmacy WHERE Ref_no = %s", (selected_ref,))
        available_quantity = my_cursor.fetchone()[0]
        conn.close()
        
        if selected_quantity > available_quantity:
            messagebox.showerror("Error", "Insufficient stock.")
            return
        
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="pharmacy")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into cart(Ref,MedName,Quantity,Price) values(%s,%s,%s,%s)",(
            self.refMed_var.get(),
            self.addmed_var.get(),
            self.addquant_var.get(),
            self.addprice_var.get(),
        ))
        conn.commit()
        self.fetch_dataMed()
        self.ClearMed()
        conn.close()
        messagebox.showinfo("Success","Medicine Added")
        
        
    def fetch_dataMed(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="pharmacy")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM cart")
        rows = my_cursor.fetchall()

        self.medicine_table.delete(*self.medicine_table.get_children())
        for i in rows:
            self.medicine_table.insert("", END, values=i)
        conn.commit()
        conn.close()
        
    def update_comboboxes(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="pharmacy")
        my_cursor = conn.cursor()

        my_cursor.execute("SELECT Ref_no FROM pharmacy")
        ref_values = [row[0] for row in my_cursor.fetchall()]

        my_cursor.execute("SELECT medname FROM pharmacy")
        medname_values = [row[0] for row in my_cursor.fetchall()]

        self.txtrefno['values'] = ref_values
        self.txtmedName['values'] = medname_values

        conn.close()
        
    def update_medname(self, event):
        selected_ref = self.txtrefno.get()  
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="pharmacy")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT medname FROM pharmacy WHERE Ref_no=%s", (selected_ref,))
        medname = my_cursor.fetchone()  
        if medname:  
            self.addmed_var.set(medname[0]) 
        my_cursor.execute("SELECT price FROM pharmacy WHERE Ref_no=%s", (selected_ref,))
        medprice = my_cursor.fetchone()  
        if medprice:  
            self.addprice_var.set(medprice[0]) 
        conn.close()
        
        
        
    #****************************************Med GetCursor************************************************
    def Medget_cursor(self,event=""):
        cursor_row=self.medicine_table.focus()
        content=self.medicine_table.item(cursor_row)
        row=content["values"]
        self.refMed_var.set(row[0])
        self.addmed_var.set(row[1])
        self.addquant_var.set(row[2])
        self.addprice_var.set(row[3])
        
    def UpdateMed(self):
        if not self.refMed_var.get():
            messagebox.showerror("Error", "Please select a medicine.")
            return
    
        selected_ref = self.refMed_var.get()
        selected_quantity = int(self.addquant_var.get())
        
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="pharmacy")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT product FROM pharmacy WHERE Ref_no = %s", (selected_ref,))
        available_quantity = my_cursor.fetchone()[0]
        conn.close()
        
        if selected_quantity > available_quantity:
            messagebox.showerror("Error", "Insufficient stock.")
            return
        
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="pharmacy")
        my_cursor=conn.cursor()
        my_cursor.execute("update cart set MedName=%s,Quantity=%s,Price=%s where Ref=%s",(
            self.addmed_var.get(),
            self.addprice_var.get(),
            self.addquant_var.get(),
            self.refMed_var.get(),
        ))
        conn.commit()
        self.fetch_dataMed()
        self.ClearMed()
        conn.close()
            
        messagebox.showinfo("Success","Medicine has been updated")    
    
            
            
    
    def DeleteMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="pharmacy")
        my_cursor=conn.cursor()
        
        sql="delete from cart where  Ref=%s"
        val=(self.refMed_var.get(),)
        my_cursor.execute(sql,val)
        
        conn.commit()
        self.fetch_dataMed()
        self.ClearMed()
        conn.close()
        messagebox.showinfo("Success","Medicine has been deleted")

        
        
    def ClearMed(self):
        self.refMed_var.set("")
        self.addmed_var.set("")
        self.addprice_var.set("")
        self.addquant_var.set("")
        

    def generate_bill(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="pharmacy")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM cart")
        cart_items = my_cursor.fetchall()

        if not cart_items:
            messagebox.showinfo("Empty Cart", "The cart is empty.")
            conn.close()
            return

        total_amount = 0
        bill_details = "------------------------------------------------------------\n"
        bill_details += "                      Generated Bill\n"
        bill_details += "------------------------------------------------------------\n"
        bill_details += "{:<25} {:<10} {:<10} {:<10}\n".format("Medicine Name", "Quantity", "Price", "Total")
        bill_details += "------------------------------------------------------------\n"

        for item in cart_items:
            ref_no, med_name, quantity, price = item
            item_total = quantity * price
            total_amount += item_total
            bill_details += "{:<25} {:<10} ₹{:<10} ₹{:<10}\n".format(med_name, quantity, price, item_total)

        bill_details += "------------------------------------------------------------\n"
        bill_details += "Total Amount: ₹{}\n".format(total_amount)
        bill_details += "------------------------------------------------------------\n"

        bill_window = Toplevel(self.root)
        bill_window.title("Bill")
        bill_window.geometry("500x400")

        bill_text = Text(bill_window, wrap="word", width=60, height=20)
        bill_text.insert("end", bill_details)
        bill_text.config(state="disabled")
        bill_text.pack()

        close_button = Button(bill_window, text="Close", command=bill_window.destroy)
        close_button.pack()

        conn.close()
        
        
        
    #*****************************************************Main Table****************************************************************
    def add_data(self):
        if self.ref_var.get()=="" or self.lot_var.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="pharmacy")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into pharmacy values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.ref_var.get(),
                self.cmpName_var.get(),
                self.typeMed_var.get(),
                self.medName_var.get(),
                self.lot_var.get(),
                self.issuedate_var.get(),
                self.expdate_var.get(),
                self.uses_var.get(),
                self.sideEffect_var.get(),
                self.warning_var.get(),
                self.dosage_var.get(),
                self.price_var.get(),
                self.product_var.get(),
            ))
            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()
            messagebox.showinfo("Success","Data has been inserted")
            
            
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="pharmacy")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM pharmacy")
        rows = my_cursor.fetchall()
        
        self.pharmacy_table.delete(*self.pharmacy_table.get_children())
        for i in rows:
            self.pharmacy_table.insert("", END, values=i)
        self.update_comboboxes()
        conn.commit()
        conn.close()

        
        
    def get_cursor(self, event=""):
        cursor_row = self.pharmacy_table.focus()
        content = self.pharmacy_table.item(cursor_row)
        row = content["values"]
        
        if row:
            self.ref_var.set(row[0])
            self.cmpName_var.set(row[1])
            self.typeMed_var.set(row[2])
            self.medName_var.set(row[3])
            self.lot_var.set(row[4])
            self.issuedate_var.set(row[5])
            self.expdate_var.set(row[6])
            self.uses_var.set(row[7])
            self.sideEffect_var.set(row[8])
            self.warning_var.set(row[9])
            self.dosage_var.set(row[10])
            self.price_var.set(row[11])
            self.product_var.set(row[12])
        else:
            print("No values found in the row.")

        
        
    def Update(self):
        if self.ref_var.get()=="" or self.lot_var.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="pharmacy")
            my_cursor=conn.cursor()
            my_cursor.execute("update pharmacy set cmpName=%s,Type=%s,medname=%s,lot=%s,Issuedate=%s,expdate=%s,uses=%s,sideeffect=%s,warning=%s,dosage=%s,price=%s,product=%s where Ref_no=%s",(
                self.cmpName_var.get(),
                self.typeMed_var.get(),
                self.medName_var.get(),
                self.lot_var.get(),
                self.issuedate_var.get(),
                self.expdate_var.get(),
                self.uses_var.get(),
                self.sideEffect_var.get(),
                self.warning_var.get(),
                self.dosage_var.get(),
                self.price_var.get(),
                self.product_var.get(),
                self.ref_var.get(),

            ))
            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()  
            messagebox.showinfo("UPDATE","Record has been updated successfully")
            
            
    def delete(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="pharmacy")
        my_cursor = conn.cursor()
        ref_no = self.ref_var.get()

        sql_delete_pharmacy = "DELETE FROM pharmacy WHERE Ref_no = %s"
        val = (ref_no,)
        my_cursor.execute(sql_delete_pharmacy, val)
        
        sql_check_cart = "SELECT * FROM cart WHERE Ref = %s"
        my_cursor.execute(sql_check_cart, val)
        cart_entry = my_cursor.fetchone()
        
        if cart_entry:
            sql_delete_cart = "DELETE FROM cart WHERE Ref = %s"
            my_cursor.execute(sql_delete_cart, val)

        conn.commit()
        self.fetch_data() 
        self.fetch_dataMed()
        self.reset() 
        conn.close()
        messagebox.showinfo("Delete", "Info deleted successfully")

        
        
    def reset(self):
        self.ref_var.set(""),
        self.cmpName_var.set(""),
        self.typeMed_var.set(""),
        self.medName_var.set(""),
        self.lot_var.set(""),
        self.issuedate_var.set(""),
        self.expdate_var.set(""),
        self.uses_var.set(""),
        self.sideEffect_var.set(""),
        self.warning_var.set(""),
        self.dosage_var.set(""),
        self.price_var.set(""),
        self.product_var.set("")
        
        
        
    def search_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="pharmacy")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM pharmacy WHERE " + str(self.search_var.get()) + " LIKE '%" + str(self.searchTxt_var.get()) + "%'")

        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rows:
                self.pharmacy_table.insert("", END, values=i)
            conn.commit()
        else:
            messagebox.showinfo("No Results", "No results found.")

        conn.close()

        
        
    def show_all_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="pharmacy")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM pharmacy")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rows:
                self.pharmacy_table.insert("", END, values=i)
            conn.commit()
        conn.close()
        
        
    def exit_application(self):
        self.root.destroy()




if __name__ == "__main__":
    root=Tk()
    obj=PharmacyManagementSystem(root)
    root.mainloop()