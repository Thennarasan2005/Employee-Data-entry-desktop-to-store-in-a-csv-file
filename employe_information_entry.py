import pandas as pd
from tkinter import messagebox
import tkinter as tk

root=tk.Tk()
root.geometry('1000x1000')

l=tk.Label(root,text='Data Frame operation',font=('arial black',25,'italic','bold'),justify=tk.CENTER)
l.pack()

l2=tk.Label(root,text='name of the employee:',font=('arial black',25,'italic','bold'))
l2.place(x=50,y=300)

l3=tk.Label(root,text='experience:',font=('arial black',25,'italic'))
l3.place(x=50,y=400)

l4=tk.Label(root,text='limit:',font=('arial black',25,'italic','bold'))
l4.place(x=50,y=200)

lim=tk.IntVar();emp=tk.StringVar();exp=tk.IntVar()
e1=tk.Entry(root,textvariable=emp,font=('arial black',25,'italic',))
e1.place(x=550,y=300)
e2=tk.Entry(root,textvariable=exp,font=('arial black',25,'italic'))
e2.place(x=550,y=400)
e3=tk.Entry(root,textvariable=lim,font=('arial black',25,'italic'))
e3.place(x=550,y=200)

data={'employee name':[],'experience':[],'salary':[]}

def add():
    if lim.get()!=0:
        data['employee name'].append(emp.get())
        data['experience'].append(exp.get())
        salary=100000*(exp.get()/100)
        data['salary'].append(salary)

        messagebox.showinfo('added','successful')
        emp.set(' ')
        exp.set(0)
        lim.set(lim.get()-1)
    
    if lim.get()==0:
        df=pd.DataFrame(data)
        with open(r'C:\Users\thenn\OneDrive\Desktop\emp_info.csv','a') as f:
            df.to_csv(r'C:\Users\thenn\OneDrive\Desktop\emp_info.csv',index=False)
            messagebox.showinfo('done','program finished')
            root.quit()

b=tk.Button(root,text='add to file',font=('arial black',20,'italic',),command=add)
b.place(x=300,y=500)
root.mainloop()