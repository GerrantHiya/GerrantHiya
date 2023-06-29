import itemManagement as m
import keyboard as k

k.add_hotkey('f5',m.refresh)
k.add_hotkey('enter',m.addPrice)
k.add_hotkey('shift+enter',m.editPrice)

m.screen.config(bg='lightgreen')
m.screen.resizable(False,False)

L_jdl = m.c.tk.Label(m.screen,text="PRICE SETTING")
L_jdl.grid(row=0,column=0,columnspan=8,pady=5)
L_jdl.config(fg='whitesmoke',bg='navy',font=('Arial-Bold',17))

L_a = m.c.tk.Label(m.screen, text="")
L_a.grid(row=1,column=0,pady=3)
L_a.config(bg='lightgreen')

L_barcode = m.c.tk.Label(m.screen,text="BARCODE")
L_barcodeA = m.c.tk.Label(m.screen,text=":")
E_barcode = m.c.tk.Entry(m.screen,textvariable=m.barcode)
L_barcode.grid(row=2,column=0,sticky='w',pady=3)
L_barcodeA.grid(row=2,column=1)
E_barcode.grid(row=2,column=2,sticky='we')
L_barcode.config(font=('Arial',12),bg='lightgreen')
L_barcodeA.config(font=('Arial',12),bg='lightgreen')
E_barcode.config(font=('Arial',12))

L_month = m.c.tk.Label(m.screen,text="MONTH")
L_monthA = m.c.tk.Label(m.screen,text=":")
E_mVal = ['January','February','March','April',
          'May','June','July','August','September',
          'October','November','December']
E_month = m.c.ttk.Combobox(m.screen, values=E_mVal, state='readonly', textvariable=m.month)
L_month.grid(row=3,column=0,sticky='w',pady=3)
L_monthA.grid(row=3,column=1)
E_month.grid(row=3,column=2,sticky='we')
L_month.config(font=('Arial',12),bg='lightgreen')
L_monthA.config(font=('Arial',12),bg='lightgreen')
E_month.config(font=('Arial',12))

L_hJ = m.c.tk.Label(m.screen,text="Harga Jual")
L_hJA = m.c.tk.Label(m.screen,text="Rp.")
E_hJ = m.c.tk.Entry(m.screen,textvariable=m.harga_jual)
L_hJ.grid(row=4,column=0,sticky='w',pady=3)
L_hJA.grid(row=4,column=1)
E_hJ.grid(row=4,column=2,sticky='we')
L_hJ.config(font=('Arial',12),bg='lightgreen')
L_hJA.config(font=('Arial',12),bg='lightgreen')
E_hJ.config(font=('Arial',12))

m.view['column'] = ("f_barcode","f_merk","f_nama","f_harga")
m.view.column("#0",width=40,stretch="NO")
m.view.column('f_barcode',width=120)
m.view.column('f_merk',width=120)
m.view.column('f_nama',width=120)
m.view.column('f_harga',width=120)
m.view.heading('#0',text="")
m.view.heading('f_barcode', text="barcode")
m.view.heading('f_merk',text="Merk Produk")
m.view.heading('f_nama',text="Nama Produk")
m.view.heading('f_harga', text="Harga Jual (Rp.)")
m.view.grid(row=5,column=0,columnspan=5,rowspan=10,pady=5)

B_addprice = m.c.tk.Button(m.screen,text="UPDATE PRICE\n[press ENTER]",command=m.addPrice)
B_updprice = m.c.tk.Button(m.screen,text="CHANGE PRICE\n[press Shift+ENTER]",command=m.editPrice)
B_addprice.config(bg='darkkhaki',fg='black',font=('Helvetica-Bold',15))
B_updprice.config(bg='darkkhaki',fg='black',font=('Helvetica-Bold',15))
B_addprice.grid(row=16,column=0,columnspan=5,rowspan=2,pady=5,sticky='ewns')
B_updprice.grid(row=18,column=0,columnspan=5,rowspan=2,pady=5,sticky='ewns')

m.screen.mainloop()