import connector as c

screen = c.tk.Tk()
screen.title("ITEM MANAGEMENT")

# VARIABLES

kunci = False # untuk pengaman
qty = c.tk.IntVar() # state = 'disabled'
today = c.nowDate
sup_ID = c.tk.StringVar()
barcode = c.tk.StringVar()
modal_stn = c.tk.IntVar()

cursor = c.dbc.cursor()

temp_q = 0

# FUNCTION

## renew stock
def addStock():
    # kondisi untuk memasukkan data
    cond = barcode.get() != "" and (modal_stn.get() != 0 or modal_stn.get() != "") and sup_ID.get() != ""
    
    if cond:
        # memeriksa data barang
        check_q = "SELECT COUNT(BARCODE) FROM PRODUCT_MASTER WHERE BARCODE = %s"
        check_v = (barcode.get(),)
        cursor.execute(check_q,check_v)
        check_r = cursor.fetchone()[0]
        
        if check_r != 0:
            print(f"{c.logs} Item ditemukan")
            # cek apakah sudah ada data sebelumnya di tanggal yang sama
            date_q = "SELECT COUNT(BARCODE) FROM STOCK_MASTER WHERE ENTRYDATE = %s AND BARCODE = %s"
            date_v = (today,barcode.get())
            cursor.execute(date_q,date_v)
            date_r = cursor.fetchone()[0]
            
            if date_r == 0:
                ins_q = "INSERT INTO STOCK_MASTER VALUES (%s,%s,%s,1,%s)"
                ins_v = (today,sup_ID.get(),barcode.get(),modal_stn.get())
                cursor.execute(ins_q,ins_v)
                print(f"{c.logs} Stok ditambahkan")
                qty.set(temp_q + 1)
            elif date_r != 0:
                upd_q = "UPDATE STOCK_MASTER SET QTY = QTY + 1 WHERE BARCODE = %s AND ENTRYDATE = %s"
                upd_v = (barcode.get(),today)
                cursor.execute(upd_q,upd_v)
                print(f"{c.logs} Stok ditambahkan +1")
                
                sel_q = "SELECT QTY FROM STOCK_MASTER WHERE BARCODE = %s AND ENTRYDATE = %s"
                sel_v = (barcode.get(),today)
                cursor.execute(sel_q,sel_v)
                sel_r = cursor.fetchone()[0]
                
                qty.set(sel_r)
        else:
            print(f"{c.logs} Item tidak ditemukan/tidak terdaftar")
            c.messagebox.showerror("ERROR 404","ITEM TIDAK TERDAFTAR")
    else:
        print(f"{c.logs} -")
        c.messagebox.showerror("ERROR","Detail produk TIDAK LENGKAP")
    c.dbc.commit()

## buat harga (bukan diskon)
# VARIABLE

month = c.tk.StringVar()
month.set(c.now.strftime("%B"))
startDate = c.tk.StringVar()
endDate = c.tk.StringVar()
harga_jual = c.tk.IntVar()
view = c.ttk.Treeview()

# FUNCTION
def month_set():
    if month.get() == "January":
        startDate.set(f"{c.thn}-01-01")
        endDate.set(f"{c.thn}-01-31")
    elif month.get() == "February":
        if is_leap_year(c.thn):
            startDate.set(f"{c.thn}-02-01")
            endDate.set(f"{c.thn}-02-29")
        else:
            startDate.set(f"{c.thn}-02-01")
            endDate.set(f"{c.thn}-02-28")
    elif month.get() == "March":
        startDate.set(f"{c.thn}-03-01")
        endDate.set(f"{c.thn}-03-31")
    elif month.get() == "April":
        startDate.set(f"{c.thn}-04-01")
        endDate.set(f"{c.thn}-04-30")
    elif month.get() == "May":
        startDate.set(f"{c.thn}-05-01")
        endDate.set(f"{c.thn}-05-31")
    elif month.get() == "June":
        startDate.set(f"{c.thn}-06-01")
        endDate.set(f"{c.thn}-06-30")
    elif month.get() == "July":
        startDate.set(f"{c.thn}-07-01")
        endDate.set(f"{c.thn}-07-31")
    elif month.get() == "August":
        startDate.set(f"{c.thn}-08-01")
        endDate.set(f"{c.thn}-08-31")
    elif month.get() == "September":
        startDate.set(f"{c.thn}-09-01")
        endDate.set(f"{c.thn}-09-30")
    elif month.get() == "October":
        startDate.set(f"{c.thn}-10-01")
        endDate.set(f"{c.thn}-10-31")
    elif month.get() == "November":
        startDate.set(f"{c.thn}-11-01")
        endDate.set(f"{c.thn}-11-30")
    elif month.get() == "December":
        startDate.set(f"{c.thn}-12-01")
        endDate.set(f"{c.thn}-12-31")

def addPrice():
    month_set()
    cond = startDate.get() != "" and endDate.get() != "" and barcode.get() != "" and harga_jual.get() != 0
    
    if cond:
        # cek barcode terdaftar/tidak
        query = "SELECT COUNT(BARCODE) FROM PRODUCT_MASTER WHERE BARCODE = %s"
        value = (barcode.get(),)
        cursor.execute(query,value)
        print(f"{c.logs} memeriksa data item ...")
        result = cursor.fetchone()[0]
        
        if result != 0:
            # cek harga sudah di data atau belum
            cek_q = "SELECT COUNT(STARTDATE) FROM PRICE_MASTER WHERE STARTDATE = %s AND BARCODE = %s"
            cek_v = (startDate.get(),barcode.get())
            cursor.execute(cek_q,cek_v)
            print(f"{c.logs} memeriksa harga item ...")
            cek_r = cursor.fetchone()[0]
            
            if cek_r == 0:
                add_q = "INSERT INTO PRICE_MASTER VALUES (%s,%s,%s,%s,%s)"
                add_v = (startDate.get(),endDate.get(),barcode.get(),harga_jual.get(),None)
                cursor.execute(add_q,add_v)
                print(f"{c.logs} harga disimpan Rp.{harga_jual.get()}")
                view.delete(*view.get_children())
                show_productMaster()
            else:
                c.messagebox.showinfo("Informasi","Harga gagal disimpan, sudah pernah diinput sebelumnya")
                print(f"{c.logs} gagal menyimpan harga - 1062")
        
        else:
            print(f"{c.logs} Produk tidak terdaftar")
            c.messagebox.showinfo("Informasi","Produk tidak terdaftar di database")
    else:
        c.messagebox.showerror("ERROR","Data tidak valid/kurang")
        print(f"{c.logs} -")
    c.dbc.commit()

def editPrice():
    month_set()
    cond = startDate.get() != "" and barcode.get() != "" and (harga_jual.get() != 0 or harga_jual.get() != "")
    
    if cond:
        # memeriksa apakah harga sudah di daftarkan
        ch_q = "SELECT COUNT(STARTDATE) FROM PRICE_MASTER WHERE STARTDATE = %s AND BARCODE = %s"
        ch_v = (startDate.get(),barcode.get())
        cursor.execute(ch_q,ch_v)
        ch_r = cursor.fetchone()[0]
        print(f"{c.logs} price_master count {ch_r}")
        
        if ch_r != 0:
            upd_q = "UPDATE PRICE_MASTER SET HARGA_SATUAN = %s WHERE STARTDATE = %s AND BARCODE = %s"
            upd_v = (harga_jual.get(),startDate.get(),barcode.get())
            cursor.execute(upd_q,upd_v)
            print(f"{c.logs} harga diperbaharui")
            view.delete(*view.get_children())
            show_productMaster()
        else:
            c.messagebox.showerror("ERROR 404","Belum pernah menyimpan harga jual")
            print(f"{c.logs} gagal mengubah harga jual")
    c.dbc.commit()

## buat harga (diskon)
# VARIABLE

ket = c.tk.StringVar()
disc = c.tk.DoubleVar() # dalam persen (0.0-100.0)

# FUNCTIONS
def buatDiskon_all_item():
    kunci = lock()
    cond = startDate.get() != "" and endDate.get() != "" and (disc.get() != 0 or disc.get() != "") and ket.get() != "" and kunci == True
    
    if cond:
        # mengambil semua barang yang startDate berada dalam range tersebut
        s_all_q = """
        SELECT BARCODE,HARGA_SATUAN FROM PRICE_MASTER
        WHERE STARTDATE <= %s AND ENDDATE >= %s
        ORDER BY BARCODE DESC
        """
        s_all_v = (startDate.get(),endDate.get())
        cursor.execute(s_all_q,s_all_v)
        s_all_r = cursor.fetchall()
        print(f"{c.logs} mengambil semua harga dari tabel dan disimpan sementara dalam list ...")
        # looping untuk dimasukkan ke list
        for item in s_all_r:
            t_barcode = item[0]
            t_harga = item[1]
            # update harga tiap record
            harga_baru = t_harga - ((disc.get()/100)*t_harga)
            ins_q = "INSERT INTO PRICE_MASTER VALUES (%s,%s,%s,%s,%s)"
            ins_v = (startDate.get(),endDate.get(),t_barcode,harga_baru,ket.get())
            cursor.execute(ins_q,ins_v)
            print(f"{c.logs} barcode {t_barcode}, new price Rp.{harga_baru}")
        show_productMaster()
    else:
        c.messagebox.showinfo("Informasi","Detail tidak lengkap!")
        print(f"{c.logs} gagal")
    c.dbc.commit()

def buatDiskon_obo(): # obo = one-by-one
    cond = startDate.get() != "" and endDate.get() != "" and (harga_jual.get() != 0 or harga_jual.get() != "") and barcode.get() != "" and (disc.get() != 0 or disc.get() != "")
    
    if cond:
        # mencari data barang
        s_q = "SELECT COUNT(BARCODE) FROM PRICE_MASTER WHERE STARTDATE <= %s AND ENDDATE >= %s AND BARCODE = %s"
        s_v = (startDate.get(),endDate.get(),barcode.get())
        cursor.execute(s_q,s_v)
        s_r = cursor.fetchone()[0]
        
        if s_r == 0:
            c.messagebox.showerror("ERROR 404","Silahkan buat harga terlebih dahulu; Harga awal tidak terdaftar")
            print(f"{c.logs} tidak ada dalam harga awal")
        else:
            # mendapatkan harga awal
            sel_q = "SELECT HARGA_SATUAN FROM PRICE_MASTER WHERE BARCODE = %s AND STARTDATE <= %s AND ENDDATE >= %s"
            sel_v = (barcode.get(),startDate.get(),endDate.get())
            cursor.execute(sel_q,sel_v)
            sel_r = cursor.fetchone()[0]
            
            harga_baru = sel_r - ((disc.get()/100)*sel_r)
            
            ins_q = "INSERT INTO PRICE_MASTER VALUES (%s,%s,%s,%s,%s)"
            ins_v = (startDate.get(),endDate.get(),barcode.get(),harga_baru,ket.get())
            cursor.execute(ins_q,ins_v)
            print(f"{c.logs} produk {barcode.get()}, harga baru Rp.{harga_baru}")
            view.delete(*view.get_children())
            show_productMaster()
    else:
        c.messagebox.showerror("ERROR","Detail Diskon Produk tidak lengkap; Mohon Dilengkapi!")
        print(f"{c.logs} gagal")
    c.dbc.commit()

# refresh button
def refresh():
    qty.set(0)
    temp_q = 0
    today = c.nowDate
    sup_ID.set("")
    barcode.set("")
    modal_stn.set(0)
    month.set(c.now.strftime("%B"))
    startDate.set("")
    endDate.set("")
    harga_jual.set(0)
    ket.set("")
    disc.set(0)
    view.delete(*view.get_children())
    show_productMaster()
    print(f"{c.logs} form dibersihkan")

def show_productMaster():
    sel_q = """
    SELECT P.BARCODE,P.MERK,P.NAMA,H.HARGA_SATUAN
    FROM PRODUCT_MASTER P LEFT JOIN PRICE_MASTER H ON P.BARCODE = H.BARCODE
    WHERE (STARTDATE <= %s AND ENDDATE >= %s) OR (STARTDATE <= %s AND ENDDATE IS NULL)
    ORDER BY STARTDATE DESC"""
    sel_v = (today,today,today)
    cursor.execute(sel_q,sel_v)
    sel_r = cursor.fetchall()
    
    for item in sel_r:
        f_barcode = item[0]
        f_merk = item[1]
        f_nama = item[2]
        f_harga = item[3]
        view.insert('','end',values=(f_barcode,f_merk,f_nama,f_harga))

# pengamanan sebelum melakukan aksi besar
def lock():
    supID = c.askinteger("Require Supervisor","Masukkan Supervisor ID Anda:")
    id_q = "SELECT COUNT(SUPERVISOR_ID) FROM SUPERVISOR WHERE SUPERVISOR_ID = %s"
    id_v = (supID,)
    cursor.execute(id_q,id_v)
    id_r = cursor.fetchone()[0]
    # memeriksa kecocokan supervisor ID
    if id_r != 0:
        supPIN = c.askinteger("Require Supervisor","Masukkan PIN Anda:")
        pin_q = "SELECT PIN FROM SUPERVISOR WHERE SUPERVISOR_ID = %s"
        pin_v = (supID,)
        cursor.execute(pin_q,pin_v)
        pin_r = cursor.fetchone()[0]
        # memeriksa kecocockan PIN dan supervisor ID
        if str(pin_r) == str(supPIN):
            kunci = True
        else:
            kunci = False
            c.messagebox.showerror("ERROR","PIN Tidak Sesuai")
    else:
        c.messagebox.showerror("ERROR 404","SUPERVISOR ID tidak dikenal!")
    return kunci