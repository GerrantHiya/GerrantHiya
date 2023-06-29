import connector as c

screen = c.tk.Tk()
screen.title("CUSTOMER REGISTRATION")
screen.configure(bg="lightblue")

# VARIABLES

cust_ID = c.tk.StringVar()
NamaDepan = c.tk.StringVar()
NamaBelakang = c.tk.StringVar()
city = c.tk.StringVar()
Phone_No = c.tk.StringVar()

cursor = c.dbc.cursor()

# FUNCTIONS

def search_cust_byPhoneNo():
    query = "SELECT * FROM customer_master WHERE PHONE_NO = %s"
    value = (Phone_No.get(),)
    cursor.execute(query,value)
    result = cursor.fetchone()
    
    if result is not None:
        print(f"{c.logs} data pelanggan ditemukan")
        cust_ID.set(result[0])
        NamaDepan.set(result[1])
        NamaBelakang.set(result[2])
        city.set(result[3])
        bonus.set(result[5])
        print(f"{c.logs} data pelanggan ditampilkan")
    else:
        print(f"{c.logs} data pelanggan tidak ditemukan")
        c.messagebox.showinfo(title="Informasi",message="Nomor Telepon tidak terdaftar")

def newCust():
    print(f"{c.logs} proses membuat customerID ...")
    # generate nomor customer bdsrkan pada jml customer total +1
    query = "SELECT COUNT(CUST_ID) FROM CUSTOMER_MASTER"
    cursor.execute(query)
    result = cursor.fetchone()[0]
    customerID = f"C{c.thn_b}{result}"
    cust_ID.set(customerID)
    print(f"{c.logs} customer ID dibuat")
    print(f"{c.logs} proses menyimpan")
    
    query = "INSERT INTO CUSTOMER_MASTER VALUES (%s,%s,%s,%s,%s,%s)"
    value = (cust_ID.get(),NamaDepan.get(),NamaBelakang.get(),city.get(),Phone_No.get(),None)
    cursor.execute(query,value)
    print(f"{c.logs} data customer berhasil disimpan")
    c.messagebox.showinfo(title="Informasi",message=f"Customer ID anda : {customerID}")
    c.dbc.commit()
    
def search_cust_byCustID():
    query = "SELECT * FROM customer_master WHERE CUST_ID = %s"
    value = (cust_ID.get(),)
    cursor.execute(query,value)
    result = cursor.fetchone()
    
    if result is not None:
        print(f"{c.logs} data pelanggan ditemukan")
        NamaDepan.set(result[1])
        NamaBelakang.set(result[2])
        city.set(result[3])
        Phone_No.set(result[4])
        bonus.set(result[5])
        print(f"{c.logs} data pelanggan ditampilkan")
    else:
        print(f"{c.logs} data pelanggan tidak ditemukan")
        c.messagebox.showinfo(title="Informasi",message="Nomor Telepon tidak terdaftar")
        
def updateCust():
    s_query = "SELECT COUNT(CUST_ID) FROM CUSTOMER_MASTER WHERE CUST_ID = %s"
    s_value = (cust_ID.get(),)
    cursor.execute(s_query,s_value)
    s_result = cursor.fetchone()[0]
    
    main_condition = cust_ID.get() != ""
    
    if s_result != 0:
        print(f"{c.logs} Customer ID ditemukan")
        if main_condition:
            if NamaDepan.get() != "":
                query = "UPDATE CUSTOMER_MASTER SET NAMADEPAN = %s"
                value = (NamaDepan.get(),)
                cursor.execute(query,value)
                print(f"{c.logs} Nama Depan diperbaharui")
                c.messagebox.showinfo("Informasi","Nama Depan sudah diperbaharui")
            elif NamaBelakang.get() != "":
                query = "UPDATE CUSTOMER_MASTER SET NAMABELAKANG = %s"
                value = (NamaBelakang.get(),)
                cursor.execute(query,value)
                print(f"{c.logs} Nama Belakang diperbaharui")
                c.messagebox.showinfo("Informasi","Nama Belakang sudah diperbaharui")
            elif city.get() != "":
                query = "UPDATE CUSTOMER_MASTER SET CITY = %s"
                value = (city.get(),)
                cursor.execute(query,value)
                print(f"{c.logs} Kota diperbaharui")
                c.messagebox.showinfo("Informasi","Kota sudah diperbaharui")
            elif Phone_No.get() != "":
                query = "UPDATE CUSTOMER_MASTER SET PHONE_NO = %s"
                value = (Phone_No.get(),)
                cursor.execute(query,value)
                print(f"{c.logs} Nomor Telepon diperbaharui")
                c.messagebox.showinfo("Informasi","Nomor Telepon sudah diperbaharui")
        else:
            c.messagebox.showinfo("Informasi","CUSTOMER ID harus TIDAK BOLEH kosong")
    else:
        c.messagebox.showerror("ERROR 404",f"{cust_ID.get()} Tidak terdaftar di database")
        
def refresh():
    cust_ID.set("")
    NamaDepan.set("")
    NamaBelakang.set("")
    city.set("")
    Phone_No.set("")