from tkinter import*
import ttk
import pyodbc
from tkinter import messagebox
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\Haider\Downloads\lab15.accdb;')
cnxn=pyodbc.connect(conn_str)

def display():
 crsr1=cnxn.cursor()
 crsr1.execute(f"Select * from {tbl.get()} where {fld.get()}='{dlt.get()}'")
 tinfo=crsr1.fetchone()
 for i in range(len(tinfo)):
  Label(text=f"{tinfo[i]}",font=("Times",15),bg='#79CDCD',width=30,anchor="center").grid(row=i+14,columnspan=2,padx=5,pady=10)


def add():
 try:
  crsr1=cnxn.cursor()
  crsr1.execute(f"Insert into {tbl.get()}({fld.get()}) Values('{dlt.get()}')")
  crsr1.commit()
  crsr1.close()
  messagebox.showinfo('Success',f'{fld.get()} inserted into records successfully!')
 except pyodbc.Error:
  messagebox.showinfo('Error','Primary key field missing or repeated!')
  

def delete():
 crsr1=cnxn.cursor()
 crsr1.execute(f"Delete * from {tbl.get()} where {fld.get()}='{dlt.get()}'")
 crsr1.commit()
 messagebox.showinfo('Record Deleted!',f'{fld.get()} deleted from records successfully!')

def update():
   crsr1=cnxn.cursor()
   crsr1.execute(f"Update {tbl.get()} set {fld.get()}='{dlt.get()}' where {updfld.get()}='{updval.get()}'")
   crsr1.commit()
   messagebox.showinfo('Success',f'{fld.get()} records updated successfully!')

def getvalue():
    crsr1=cnxn.cursor()
    crsr1.execute(f"Select {updfld.get()} from {tbl.get()}")
    data=crsr1.fetchall()
    crsr1.close()
    lst=[]
    for i in range(len(data)):
     lst.append(data[i][0])
    Label(text='Select Value',bg="#528B8B",font=("Times",15),width=15,anchor="center").grid(row=15,padx=10,pady=10)
    ttk.Combobox(textvariable=updval,values=lst,font=("Times",15),width=15).grid(column=1,row=15,padx=10,pady=10)
    Button(text='Update',bg="#528B8B",font=("Times",15),width=15,anchor="center",command=update).grid(column=3,row=15,padx=10,pady=10)

def add_where():
    Label(text='Select Field',bg="#528B8B",font=("Times",15),width=15,anchor="center").grid(row=14,padx=10,pady=10)
    ttk.Combobox(textvariable=updfld,values=fields,font=("Times",15),width=15).grid(column=1,row=14,padx=10,pady=10)
    Button(text='Proceed',bg="#528B8B",font=("Times",15),width=15,anchor="center",command=getvalue).grid(column=3,row=14,padx=10,pady=10)
 
def ftch_data():
  crsr1=cnxn.cursor()
  crsr1.execute(f"Select {fld.get()} from {tbl.get()}")
  data=crsr1.fetchall()
  data2=[]
  for i in range(len(data)):
   data2.append(data[i][0])   
  ttk.Combobox(textvariable=dlt,values=data2,font=("Times",15),width=15).grid(column=1,row=12,padx=10,pady=10)
  Button(text='Delete',bg="#528B8B",font=("Times",15),width=15,anchor="center",command=delete).grid(column=1,row=13,padx=10,pady=10)
  Button(text='Show Details',bg="#528B8B",font=("Times",15),width=15,anchor="center",command=display).grid(row=13,padx=10,pady=10)
  Button(text='Insert',bg="#528B8B",font=("Times",15),width=15,anchor="center",command=add).grid(column=3,row=13,padx=10,pady=10)
  Button(text='Add where:',bg="#528B8B",font=("Times",15),width=15,anchor="center",command=add_where).grid(column=3,row=14,padx=10,pady=10)
  

root=Tk()
root.title("Database app")
root.config(bg="#708090")
root.geometry("800x900")
dlt=StringVar()
tbl=StringVar()
fld=StringVar()
updfld=StringVar()
updval=StringVar()
fields=['tID','name','designation','salary','deptID','deptID','dname','ccode','cname','credithrs','TiD']
tab=['Teacher','Courses','Dept']
Label(text="Management System",font=("Verdana",22),bg='#00FFFF',width=30,anchor="center").grid(row=0,columnspan=3,padx=10,pady=10)
Label(text="Select Field",font=("Times",15),bg='#00FFFF',width=20,anchor="center").grid(row=11,padx=10,pady=10)
Label(text="Select Table",font=("Times",15),bg='#00FFFF',width=20,anchor="center").grid(row=10,padx=10,pady=10)
ttk.Combobox(textvariable=tbl,values=tab,font=("Times",15),width=15).grid(column=1,row=10,padx=10,pady=10)
ttk.Combobox(textvariable=fld,values=fields,font=("Times",15),width=15).grid(column=1,row=11,padx=10,pady=10)
Button(text='Next',bg="#528B8B",font=("Times",15),width=15,anchor="center",command=ftch_data).grid(column=3,row=12,padx=10,pady=10)

root.mainloop()