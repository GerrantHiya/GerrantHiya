import connector as c

screen = c.tk.Tk()
screen.title("ITEM MANAGEMENT SYSTEM")
screen.configure(bg="lightblue")

# VARIABLES

barcode = c.tk.StringVar()
merk = c.tk.StringVar()
nama = c.tk.StringVar()
cursor = c.dbc.cursor()
# FUNCTION

def newProduct():
    check_q = "SELECT COUNT(BARCODE) FROM PRODUCT_MASTER WHERE BARCODE = %s"
    check_v = (barcode.get(),)
    cursor.execute(check_q,check_v)
    check_r = cursor.fetchone()[0]
    
    if check_r == 0:
        print(f"{c.logs} proses mendaftar barang ...")
        ins_q = "INSERT INTO PRODUCT_MASTER VALUES (%s,%s,%s)"
        ins_v = (barcode.get(),merk.get(),nama.get())
        cursor.execute(ins_q,ins_v)
        c.messagebox.showinfo("Informasi",f"Produk {nama.get()} sudah disimpan")
    else:
        print(f"{c.logs} Data sudah pernah disimpan")
        c.messagebox.showinfo("Informasi","GAGAL MENYIMPAN. CEK BARCODE")
    c.dbc.commit()

def editProductDetails():
    s_q = "SELECT COUNT(BARCODE) FROM PRODUCT_MASTER WHERE BARCODE = %s"
    s_v = (barcode.get(),)
    cursor.execute(s_q,s_v)
    s_r = cursor.fetchone()[0]
    condition = barcode.get() != ""
    
    if s_r != 0:
        if condition:
            if merk.get() != "":
                print(f"{c.logs} Proses mengubah Merk")
                upd_q = "UPDATE PRODUCT_MASTER SET MERK = %s WHERE BARCODE = %s"
                upd_v = (merk.get(),barcode.get())
                cursor.execute(upd_q,upd_v)
                print(f"{c.logs} Selesai mengubah Merk")
                c.messagebox.showinfo("Informasi","Merk diperbaharui")
            elif nama.get() != "":
                print(f"{c.logs} Proses mengubah nama produk")
                upd_q = "UPDATE PRODUCT_MASTER SET NAMA = %s WHERE BARCODE = %s"
                upd_v = (nama.get(),barcode.get())
                cursor.execute(upd_q,upd_v)
            else:
                print(f"{c.logs} Perintah tidak valid")
                c.messagebox.showerror("ERROR","Perintah tidak valid")
        else:
            c.messagebox.showinfo("Informasi","BARCODE WAJIB DIISI!")
    else:
        c.messagebox.showerror("ERROR 404","BARCODE TIDAK TERDAFTAR")
        
def refresh():
    barcode.set("")
    merk.set("")
    nama.set("")