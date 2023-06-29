import connector as c

screen = c.tk.Tk()
screen.title("Supervisor Registration")
screen.resizable(False,False)

# Variable
staff_ID = c.tk.StringVar()
supPIN = c.tk.StringVar()
cursor = c.dbc.cursor()
supID = c.tk.StringVar()

# function
def refresh():
    staff_ID.set("")
    supPIN.set("")
    supID = ""
    print(f"{c.logs} form dibersihkan")

def supID_generator():
    sel_q = "SELECT COUNT(STAFF_ID) FROM SUPERVISOR"
    cursor.execute(sel_q)
    sel_r = cursor.fetchone()[0]
    supID.set(f"33{sel_r+1}")
    c.messagebox.showinfo("Informasi Penting!",f"Supervisor ID : {supID.get()}")
    print(f"{c.logs} supplier ID berhasil dibuat {supID.get()}")
    
def new_supervisor():
    # memeriksa keberadaan staff
    supID_generator()
    sel_q = "SELECT COUNT(STAFF_ID) FROM STAFF_MASTER WHERE STAFF_ID = %s"
    sel_v = (staff_ID.get(),)
    cursor.execute(sel_q,sel_v)
    sel_r = cursor.fetchone()[0]
    if sel_r != 0:
        ins_q = "INSERT INTO SUPERVISOR VALUES (%s,%s,%s)"
        ins_v = (staff_ID.get(),supID.get(),supPIN.get())
        cursor.execute(ins_q,ins_v)
        print(f"{c.logs} Supervisor berhasil didaftarkan")
        c.dbc.commit()
    else:
        c.messagebox.showerror("ERROR 404","Staff ID tidak ditemukan!")
        print(f"{c.logs} gagal menambahkan supervisor")