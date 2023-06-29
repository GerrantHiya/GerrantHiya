import connector as c

screen = c.tk.Tk()
screen.title("CASHIER")
screen.config(bg="lightblue")

# VARIABLES
## variabel yang akan muncul pada UI
invoiceNo = c.tk.StringVar()
transactionDate = c.tk.StringVar()
transactionDate.set(c.nowDate)
barcode = c.tk.StringVar()
harga_jual = c.tk.IntVar()
cust_ID = c.tk.StringVar()
## pembayaran
total = c.tk.IntVar()
cash = c.tk.IntVar()
kmbln = c.tk.IntVar()
## variabel tidak muncul di UI
qty = c.tk.IntVar()
modal = c.tk.IntVar()
harini = c.nowDate
ktg = c.tk.StringVar()
## Treeview
view = c.ttk.Treeview()
## cursor
cursor = c.dbc.cursor()
print(f"{c.logs} {c.nowtime} Aplikasi Kasir dimulai")

# FUNCTIONS
def generate_invoiceNo():
    sel_q = "SELECT COUNT(DISTINCT(INVOICENO)) FROM INVOICE WHERE TRANSACTION_DATE = %s"
    sel_v = (transactionDate.get(),)
    cursor.execute(sel_q,sel_v)
    sel_r = int(cursor.fetchone()[0]) + 1
    # format YYYY/INV-0000/DD-MM
    temp_invoiceNo = f"{c.thn}/INV-{sel_r}/{c.tgl}-{c.bln}"
    invoiceNo.set(temp_invoiceNo)
    print(f"{c.logs} invoice Number generated")

def generate_custID():
    cond = cust_ID.get() == ""
    if cond:
        sel_q = "SELECT COUNT(CUST_ID) FROM CUSTOMER_MASTER"
        cursor.execute(sel_q)
        sel_r = cursor.fetchone()[0]
        sel_r = sel_r + 1
        # mengisi 0 didepan angka
        if len(sel_r) == 1:
            sel_r = "000" + sel_r
        elif len(sel_r) == 2:
            sel_r = "00" + sel_r
        elif len(sel_r) == 3:
            sel_r = "0" + sel_r
        # format CYYYY000
        temp_custID = f"C{c.thn}{sel_r}"
        cust_ID.set(temp_custID)
    print(f"{c.logs} invoice Number generated")

def get_qty():
    # mengantisipasi nilai kosong (bukan NULL)
    cek_q = "SELECT COUNT(INVOICENO) FROM INVOICE WHERE INVOICENO = %s AND BARCODE = %s"
    cek_v = (invoiceNo.get(),barcode.get())
    cursor.execute(cek_q,cek_v)
    cek_r = cursor.fetchone()[0]
    
    if cek_r != 0:
        sel_q = "SELECT QTY FROM INVOICE WHERE INVOICENO = %s AND BARCODE = %s"
        sel_v = (invoiceNo.get(),barcode.get())
        cursor.execute(sel_q,sel_v)
        sel_r = cursor.fetchone()[0]
        qty.set(sel_r)
        print(f"{c.logs} get quantity = {qty.get()}")
    else:
        qty.set(0)

def get_modal():
    # cek apakah ada stok atau tidak di database
    cek_q = """
    SELECT COUNT(BARCODE) FROM STOCK_MASTER
    WHERE QTY > 0 AND BARCODE = %s
    """
    cek_v = (barcode.get(),)
    cursor.execute(cek_q,cek_v)
    cek_r = cursor.fetchone()[0]
    if cek_r != 0:
        sel_q = """
        SELECT MODAL_SATUAN FROM STOCK_MASTER
        WHERE BARCODE = %s AND QTY > 0
        ORDER BY ENTRYDATE DESC LIMIT 1
        """
        sel_v = (barcode.get(),)
        cursor.execute(sel_q,sel_v)
        sel_r = cursor.fetchone()[0]
        modal.set(sel_r)
        print(f"{c.logs} Modal di dapatkan {modal.get()//100}")
    elif cek_r == 0:
        c.messagebox.showwarning("Pemberitahuan","Tidak ada stock yang terdaftar")

def get_harga():
    sel_q = """
    SELECT HARGA_SATUAN,KETERANGAN FROM PRICE_MASTER
    WHERE BARCODE = %s AND (
        (STARTDATE <= %s AND ENDDATE >= %s) OR
        (STARTDATE <= %s AND ENDDATE IS NULL)
    ) ORDER BY STARTDATE DESC LIMIT 1
    """
    sel_v = (barcode.get(),harini,harini,harini)
    cursor.execute(sel_q,sel_v)
    sel_r = cursor.fetchone()
    if sel_r[1] == None:
        harga_jual.set(sel_r[0])
        ktg.set("normal")
    elif sel_r[1] != None:
        harga_jual.set(sel_r[0])
        ktg.set("diskon")
    print(f"{c.logs} harga jual didapatkan Rp.{harga_jual.get()}")

def show_inv_record():
    view.delete(*view.get_children())
    sel_q = """
    SELECT I.BARCODE,P.MERK,P.NAMA,I.QTY,I.HARGA_JUAL
    FROM INVOICE I JOIN PRODUCT_MASTER P
    ON I.BARCODE = P.BARCODE
    WHERE I.INVOICENO = %s
    """
    sel_v = (invoiceNo.get(),)
    cursor.execute(sel_q,sel_v)
    sel_r = cursor.fetchall()
    # memasukkan pada view
    for item in sel_r:
        f_barcode = item[0]
        f_merk = item[1]
        f_nama = item[2]
        f_qty = item[3]
        f_hj = item[4]
        f_ktg = ktg.get()
        view.insert('','end',values=(f_barcode,f_merk,f_nama,f_qty,f_hj,f_ktg))

def upd_stock():
    cek_q = """
    SELECT COUNT(BARCODE) FROM STOCK_MASTER
    WHERE QTY > 0 AND BARCODE = %s
    """
    cek_v = (barcode.get(),)
    cursor.execute(cek_q,cek_v)
    cek_r = cursor.fetchone()[0]
    if cek_r != 0:
        upd_q = """
        UPDATE STOCK_MASTER SET QTY = QTY - 1
        WHERE QTY > 0 AND BARCODE = %s
        ORDER BY ENTRYDATE DESC LIMIT 1
        """
        upd_v = (barcode.get(),)
        cursor.execute(upd_q,upd_v)
        print(f"{c.logs} stock - 1")
        c.dbc.commit()    
    elif cek_r == 0:
        c.messagebox.showwarning("Pemberitahuan","Tidak ada stock yang terdaftar")

def sum_all():
    sel_q = """
    SELECT SUM(HARGA_JUAL) FROM INVOICE
    WHERE INVOICENO = %s
    """
    sel_v = (invoiceNo.get(),)
    cursor.execute(sel_q,sel_v)
    sel_r = cursor.fetchone()[0]
    # total
    total.set(sel_r)
    print(f"{c.logs} total dihitung Rp.{total.get()}")

def enter_click():
    # cek apakah barang terdaftar
    sel_q = "SELECT COUNT(BARCODE) FROM PRODUCT_MASTER WHERE BARCODE = %s"
    sel_v = (barcode.get(),)
    cursor.execute(sel_q,sel_v)
    sel_r = cursor.fetchone()[0]
    
    get_qty()
    if sel_r != 0:
        if qty.get() == 0:
            get_modal()
            get_harga()
            ins_q = "INSERT INTO INVOICE VALUES (%s,%s,%s,1,%s,%s,%s)"
            ins_v = (invoiceNo.get(),harini,barcode.get(),modal.get(),harga_jual.get(),cust_ID.get())
            cursor.execute(ins_q,ins_v)
            print(f"{c.logs} Invoice inserted")
            show_inv_record()
            # mengurangi jml stok
            upd_stock()
            print(f"{c.logs} view updated")
            c.dbc.commit()
            sum_all()
        elif qty.get() != 0:
            upd_q = """
            UPDATE INVOICE SET
            QTY = QTY + 1, HARGA_MODAL = HARGA_MODAL * QTY,
            HARGA_JUAL = HARGA_JUAL * QTY
            WHERE INVOICENO = %s AND BARCODE = %s
            """
            upd_v = (invoiceNo.get(),barcode.get())
            cursor.execute(upd_q,upd_v)
            show_inv_record()
            # mengurangi jml stok
            upd_stock()
            print(f"{c.logs} updated")
            c.dbc.commit()
            sum_all()
    else:
        c.messagebox.showerror("ERROR 404",f"{barcode} tidak terdaftar")
        print(f"{c.logs} gagal")

def bayar():
    if cash.get() != 0 or cash.get() != "":
        kembalian = cash.get() - total.get()
        kmbln.set(kembalian)
    else:
        c.messagebox.showinfo("Informasi","-")
        
def refresh():
    invoiceNo.set("")
    generate_invoiceNo()
    transactionDate.set(c.nowDate)
    barcode.set("")
    harga_jual.set(0)
    cust_ID.set("")
    total.set(0)
    cash.set(0)
    kmbln.set(0)
    qty.set(0)
    modal.set(0)
    view.delete(*view.get_children())