import cashier as m
import keyboard as k
m.generate_invoiceNo()

k.add_hotkey('enter',m.enter_click)
k.add_hotkey('shift+enter',m.bayar)
k.add_hotkey('f5',m.refresh)
m.screen.config(bg="darkgrey")
m.screen.resizable(False,False)

L_jdl = m.c.tk.Label(m.screen, text="SISTEM PEMBAYARAN")
L_jdl.grid(row=0,column=0,columnspan=10,pady=8)
L_jdl.config(bg='darkgreen',font=('Batang-Bold',17),fg='whitesmoke')

L_tgl = m.c.tk.Label(m.screen, textvariable=m.transactionDate)
L_tgl.grid(row=1,column=0,pady=3,columnspan=5,sticky='ew')
L_tgl.config(bg='darkgrey')

L_invoiceNo = m.c.tk.Label(m.screen,text="INVOICE NO")
L_invoiceNoA = m.c.tk.Label(m.screen,text=":")
E_invoiceNo = m.c.tk.Entry(m.screen,textvariable=m.invoiceNo,state='disabled')
L_invoiceNo.grid(row=3,column=0,sticky='w',pady=3)
L_invoiceNoA.grid(row=3,column=1)
E_invoiceNo.grid(row=3,column=2,sticky='we')
L_invoiceNo.config(font=('Batang',12),bg='darkgrey')
L_invoiceNoA.config(font=('Batang',12),bg='darkgrey')
E_invoiceNo.config(font=('Batang',12))

L_barcode = m.c.tk.Label(m.screen,text="BARCODE")
L_barcodeA = m.c.tk.Label(m.screen,text=":")
E_barcode = m.c.tk.Entry(m.screen,textvariable=m.barcode)
L_barcode.grid(row=4,column=0,sticky='w',pady=3)
L_barcodeA.grid(row=4,column=1)
E_barcode.grid(row=4,column=2,sticky='we')
L_barcode.config(font=('Batang',12),bg='darkgrey')
L_barcodeA.config(font=('Batang',12),bg='darkgrey')
E_barcode.config(font=('Batang',12))

L_cust_ID = m.c.tk.Label(m.screen,text="CUSTOMER ID")
L_cust_IDA = m.c.tk.Label(m.screen,text=":")
E_cust_ID = m.c.tk.Entry(m.screen,textvariable=m.cust_ID)
L_cust_ID.grid(row=5,column=0,sticky='w',pady=3)
L_cust_IDA.grid(row=5,column=1)
E_cust_ID.grid(row=5,column=2,sticky='we')
L_cust_ID.config(font=('Batang',12),bg='darkgrey')
L_cust_IDA.config(font=('Batang',12),bg='darkgrey')
E_cust_ID.config(font=('Batang',12))

m.view['column'] = ("f_barcode","f_merk","f_nama","f_qty","f_hj","f_ktg")
m.view.column("#0",width=40,stretch="NO")
m.view.column('f_barcode',width=120)
m.view.column('f_merk',width=120)
m.view.column('f_nama',width=120)
m.view.column('f_qty',width=120)
m.view.column('f_hj',width=120)
m.view.column('f_ktg',width=120)
m.view.heading('#0',text="")
m.view.heading('f_barcode', text="Barcode")
m.view.heading('f_merk',text="Merk Produk")
m.view.heading('f_nama',text="Nama Produk")
m.view.heading('f_qty', text="Qty")
m.view.heading('f_hj', text="Harga /pcs (Rp.)")
m.view.heading('f_ktg', text="Keterangan")
m.view.grid(row=6,column=0,columnspan=5,rowspan=10,sticky='nsew',pady=3)

L_total = m.c.tk.Label(m.screen,text="TOTAL BELANJA")
L_totalA = m.c.tk.Label(m.screen,text="RP.")
E_total = m.c.tk.Entry(m.screen,textvariable=m.total)
L_total.grid(row=16,column=0,sticky='w',pady=3)
L_totalA.grid(row=16,column=1)
E_total.grid(row=16,column=2,sticky='we')
L_total.config(font=('Batang',12),bg='darkgrey')
L_totalA.config(font=('Batang',12),bg='darkgrey')
E_total.config(font=('Batang',12))

L_cash = m.c.tk.Label(m.screen,text="CASH")
L_cashA = m.c.tk.Label(m.screen,text="RP.")
E_cash = m.c.tk.Entry(m.screen,textvariable=m.cash)
L_cash.grid(row=17,column=0,sticky='w',pady=3)
L_cashA.grid(row=17,column=1)
E_cash.grid(row=17,column=2,sticky='we')
L_cash.config(font=('Batang',12),bg='darkgrey')
L_cashA.config(font=('Batang',12),bg='darkgrey')
E_cash.config(font=('Batang',12))

L_kmbln = m.c.tk.Label(m.screen,text="KEMBALIAN")
L_kmblnA = m.c.tk.Label(m.screen,text="RP.")
E_kmbln = m.c.tk.Entry(m.screen,textvariable=m.kmbln)
L_kmbln.grid(row=18,column=0,sticky='w',pady=3)
L_kmblnA.grid(row=18,column=1)
E_kmbln.grid(row=18,column=2,sticky='we')
L_kmbln.config(font=('Batang',12),bg='darkgrey')
L_kmblnA.config(font=('Batang',12),bg='darkgrey')
E_kmbln.config(font=('Batang',12))

B_enterClick = m.c.tk.Button(m.screen,text="TAMBAHKAN BARANG\n[press ENTER]",command=m.enter_click)
B_enterClick.config(bg='darkkhaki',fg='black',font=('Batang-Bold',15))
B_enterClick.grid(row=19,column=0,columnspan=5,rowspan=2,sticky='ewns')

B_bayar = m.c.tk.Button(m.screen,text="HITUNG KEMBALIAN\n[press SHIFT+ENTER]",command=m.bayar)
B_bayar.config(bg='darkkhaki',fg='black',font=('Batang-Bold',15))
B_bayar.grid(row=21,column=0,columnspan=5,rowspan=2,sticky='ewns')

B_refresh = m.c.tk.Button(m.screen,text="REFRESH\n[press F5]",command=m.refresh)
B_refresh.config(bg='darkkhaki',fg='black',font=('Batang-Bold',15))
B_refresh.grid(row=23,column=0,columnspan=5,rowspan=2,sticky='ewns')

m.screen.mainloop()