import addSupervisor as m
import keyboard as k

k.add_hotkey('ctrl+enter',m.new_supervisor)
k.add_hotkey('f5',m.refresh)
m.screen.config(bg="lightyellow")
m.screen.resizable(False,False)

L_jdl = m.c.tk.Label(m.screen, text="SUPERVISOR REGISTRATION")
L_jdl.grid(row=0,column=0,columnspan=3,pady=8)
L_jdl.config(bg='lightgreen',font=('Arial-Bold',17),fg='black')

L_a = m.c.tk.Label(m.screen, text="")
L_a.grid(row=1,column=0,pady=3)
L_a.config(bg='lightyellow')

L_staff_ID = m.c.tk.Label(m.screen,text="STAFF ID")
L_staff_IDA = m.c.tk.Label(m.screen,text=":")
E_staff_ID = m.c.tk.Entry(m.screen,textvariable=m.staff_ID)
L_staff_ID.grid(row=2,column=0,sticky='w',pady=3)
L_staff_IDA.grid(row=2,column=1)
E_staff_ID.grid(row=2,column=2,sticky='we')
L_staff_ID.config(font=('Arial',12),bg='lightyellow')
L_staff_IDA.config(font=('Arial',12),bg='lightyellow')
E_staff_ID.config(font=('Arial',12))

L_supPIN = m.c.tk.Label(m.screen,text="new PIN")
L_supPINA = m.c.tk.Label(m.screen,text=":")
E_supPIN = m.c.tk.Entry(m.screen,textvariable=m.supPIN,show="*")
L_supPIN.grid(row=(2+1),column=0,sticky='w',pady=3)
L_supPINA.grid(row=(2+1),column=1)
E_supPIN.grid(row=(2+1),column=2,sticky='we')
L_supPIN.config(font=('Arial',12),bg='lightyellow')
L_supPINA.config(font=('Arial',12),bg='lightyellow')
E_supPIN.config(font=('Arial',12))

B_new_supervisor = m.c.tk.Button(m.screen,text="SAVE\n[press CTRL+ENTER]",command=m.new_supervisor)
B_new_supervisor.grid(row=(3+1),column=0,columnspan=3,rowspan=2,sticky='ewns',pady=5)
B_new_supervisor.config(bg='darkkhaki',fg='black',font=('Helvetica-Bold',12))

B_refresh = m.c.tk.Button(m.screen,text="CLEAR\n[press F5]",command=m.refresh)
B_refresh.grid(row=(4+1+2),column=0,columnspan=3,rowspan=2,sticky='ewns',pady=5)
B_refresh.config(bg='darkkhaki',fg='black',font=('Helvetica-Bold',12))

m.screen.mainloop()