from re import I
from tkinter import*
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
class Qr_Generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Generator | Developed By Jishnu Adhikary")
        self.root.resizable(False,False)

        title=Label(self.root,text="  QR Code Generator",font=("times new roman",40),bg='#053246',fg='white',anchor='w').place(x=0,y=0,relwidth=1)
        
        #====Student Details window==========
        #===variables=====
        self.var_emp_code=StringVar()
        self.var_name=StringVar()
        self.var_department=StringVar()
        self.var_stream=StringVar()
        
        emp_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        emp_frame.place(x=50,y=100,width=500,height=380)

        emp_title=Label(emp_frame,text="Student Details",font=("goudy old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)

        lbl_emp_code=Label(emp_frame,text="Student ID",font=("times new roman",15,'bold'),bg='white').place(x=20,y=60)
        lbl_name=Label(emp_frame,text="Name",font=("times new roman",15,'bold'),bg='white').place(x=20,y=100)
        lbl_department=Label(emp_frame,text="Departmemt",font=("times new roman",15,'bold'),bg='white').place(x=20,y=140)
        lbl_stream=Label(emp_frame,text="Stream",font=("times new roman",15,'bold'),bg='white').place(x=20,y=180)

        txt_emp_code=Entry(emp_frame,font=("times new roman",15),textvariable=self.var_emp_code,bg='lightyellow').place(x=200,y=60)
        txt_name=Entry(emp_frame,font=("times new roman",15),textvariable=self.var_name,bg='lightyellow').place(x=200,y=100)
        txt_department=Entry(emp_frame,font=("times new roman",15),textvariable=self.var_department,bg='lightyellow').place(x=200,y=140)
        txt_stream=Entry(emp_frame,font=("times new roman",15),textvariable=self.var_stream,bg='lightyellow').place(x=200,y=180)


        btn_generate=Button(emp_frame,text='QR Generate',command=self.generate,font=("times new roman",18,'bold'),bg='#2196f3',fg='white').place(x=90,y=250,width=180,height=30)
        btn_clear=Button(emp_frame,text='Clear',command=self.clear,font=("times new roman",18,'bold'),bg='#607d8b',fg='white').place(x=282,y=250,width=120,height=30)

        self.msg=''
        self.lbl_msg=Label(emp_frame,text=self.msg,font=("times new roman",20),bg='white',fg='green')
        self.lbl_msg.place(x=0,y=310,relwidth=1) 

        #====Student QR Code window==========
        qr_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_frame.place(x=600,y=100,width=250,height=380)

        emp_title=Label(qr_frame,text="Student QR Code",font=("goudy old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)

        self.qr_code=Label(qr_frame,text='No QR\nAvailable',font=('times new roman',15),bg='#3f51b5',fg='white',bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=180)  
    
    def clear(self):
        self.var_emp_code.set('')
        self.var_name.set('')
        self.var_department.set('')
        self.var_stream.set('')

        self.msg=''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')

    def generate(self):
        if (self.var_stream.get()=='' or self.var_emp_code.get()=='' or self.var_department.get()=='' or self.var_name.get()==''):
            self.msg='All Fields are Reqired!!!'
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f"Student ID: {self.var_emp_code.get()}\nStudent Name:{self.var_name.get()}\nDepartment: {self.var_department.get()}\nStream:{self.var_stream.get()}")
            qr_code=qrcode.make(qr_data)
            #print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("python_project_QRcode/Emp_"+str(self.var_emp_code.get())+'.png')
            #===========qrcode image update============
            self.im=ImageTk.PhotoImage(file="python_project_QRcode/Emp_"+str(self.var_emp_code.get())+'.png')
            self.qr_code.config(image=self.im)
            #==========updating Notification================
            self.msg='QR Generated Successfully!!!'
            self.lbl_msg.config(text=self.msg,fg='green')

        

    


root=Tk()
obj=Qr_Generator(root)
root.mainloop()

        