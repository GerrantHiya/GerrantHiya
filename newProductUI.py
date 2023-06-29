import newProduct as m
import keyboard as k

k.add_hotkey('enter',m.newProduct)
k.add_hotkey('f5',m.refresh)
m.screen.resizable(False,False)

L_jdl = m.c.tk.Label(m.screen, text="PRODUCT REGISTRATION")
L_jdl.grid(row=0,column=0,columnspan=10,pady=8)
L_jdl.config(bg='navy',font=('Helvetica-Bold',17),fg='whitesmoke')

L_a = m.c.tk.Label(m.screen, text="")
L_a.grid(row=1,column=0,pady=3)
L_a.config(bg='lightblue')

L_barcode = m.c.tk.Label(m.screen,text="BARCODE")
L_barcodeA = m.c.tk.Label(m.screen,text=":")
E_barcode = m.c.tk.Entry(m.screen,textvariable=m.barcode)
L_barcode.grid(row=2,column=0,sticky='w',pady=3)
L_barcodeA.grid(row=2,column=1)
E_barcode.grid(row=2,column=2,sticky='we')
L_barcode.config(font=('Helvetica',12),bg='lightblue')
L_barcodeA.config(font=('Helvetica',12),bg='lightblue')
E_barcode.config(font=('Helvetica',12))

L_merk = m.c.tk.Label(m.screen,text="MERK")
L_merkA = m.c.tk.Label(m.screen,text=":")
E_merk = m.c.tk.Entry(m.screen,textvariable=m.merk)
L_merk.grid(row=3,column=0,sticky='w',pady=3)
L_merkA.grid(row=3,column=1)
E_merk.grid(row=3,column=2,sticky='we')
L_merk.config(font=('Helvetica',12),bg='lightblue')
L_merkA.config(font=('Helvetica',12),bg='lightblue')
E_merk.config(font=('Helvetica',12))

L_nama = m.c.tk.Label(m.screen,text="NAMA PRODUK")
L_namaA = m.c.tk.Label(m.screen,text=":")
E_nama = m.c.tk.Entry(m.screen,textvariable=m.nama)
L_nama.grid(row=4,column=0,sticky='w',pady=3)
L_namaA.grid(row=4,column=1)
E_nama.grid(row=4,column=2,sticky='we')
L_nama.config(font=('Helvetica',12),bg='lightblue')
L_namaA.config(font=('Helvetica',12),bg='lightblue')
E_nama.config(font=('Helvetica',12))

B_addStock = m.c.tk.Button(m.screen, text="ADD PRODUCT\n[press ENTER]",command=m.newProduct)
B_addStock.grid(row=6,column=0,columnspan=8,rowspan=2,pady=3,sticky='nsew')
B_addStock.config(bg='darkkhaki',font=('Arial-Bold',12))

B_refresh = m.c.tk.Button(m.screen, text="REFRESH\n[press F5]",command=m.refresh)
B_refresh.grid(row=8,column=0,columnspan=8,rowspan=2,pady=3,sticky='nsew')
B_refresh.config(bg='darkkhaki',font=('Arial-Bold',12))

B_editProductDetails = m.c.tk.Button(m.screen, text="EDIT PRODUCT DETAILS\n",command=m.editProductDetails)
B_editProductDetails.grid(row=10,column=0,columnspan=8,rowspan=2,pady=3,sticky='nsew')
B_editProductDetails.config(bg='darkkhaki',font=('Arial-Bold',12))

m.screen.mainloop()