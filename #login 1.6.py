    
    #login 1.5
import tkinter
from tkinter import * 
from tkinter import messagebox
import random
from tkinter import Label
from time import strftime
import tkinter as tk
from tkinter import filedialog
import ast


root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)



def signin():
    username = user.get()
    password = code.get()
    
    file= open('datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()
    
    print(r.keys())
    print(r.values())
    
    if username in r.keys() and password == r[username]:
        root = Tk()
        root.geometry('925x500+300+200')
        root.title("APP")
        root.resizable(False,False)
        root.configure(bg="green")
        
        def enter():
            root = tk.Tk()
            w = root.winfo_height
            root.geometry("925x500+300+200")
            root.resizable(False,False)
            
            lab1 = tk.Label(root,text="",font="Times 260")#deschidere lab
            def roll():
                dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
                lab1.configure(text=f'{random.choice(dice)}{random.choice(dice)}')
                lab1.pack()
   
            button = Button(root,text="lets roll....",width=40,height=5,font=10,bg="red",bd=2,command=roll)
            button.pack(padx=10,pady=10)

                
            lab1.pack()#inchidere lab
            root.mainloop    
        #CALCULATOR
        def calculator():
            root = Tk()
            root.title("Simple calculator")
            root.geometry("570x630+100+200")
            root.resizable(False,False)
            root.configure(bg="#17161b")

    
            global equation 
            equation = ""

            def show(value):
                        global equation
                        equation+=value
                        label_result.config(text=equation)   
            def clear():
                        global equation
                        equation = ""
                        label_result.config(text=equation)  

            def calculate():
                        global equation
                        result = ""
                        if equation != "":
                            try:
                                result = eval(equation)
                            except:
                                result = "error"
                                equation = ""
                        label_result.config(text=result)            

                
                
            label_result = Label(root,width=25,height=3,text="",font=("arial",30))
            label_result.pack()

                
            Button(root,text="C",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5", command=lambda: clear()).place(x=10,y=150)
            Button(root,text="/",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show("/")).place(x=150,y=150)
            Button(root,text="%",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show("%")).place(x=290,y=150)
            Button(root,text="*",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show("*")).place(x=430,y=150)


            Button(root,text="7",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show("7")).place(x=10,y=250)
            Button(root,text="8",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show("8")).place(x=150,y=250)
            Button(root,text="9",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show("9")).place(x=290,y=250)
            Button(root,text="-",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show("-")).place(x=430,y=250)

            Button(root,text="4",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show("4")).place(x=10,y=350)
            Button(root,text="5",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show("5")).place(x=150,y=350)
            Button(root,text="6",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show("6")).place(x=290,y=350)
            Button(root,text="+",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show("+")).place(x=430,y=350)

            Button(root,text="1",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show("1")).place(x=10,y=450)
            Button(root,text="2",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show("2")).place(x=150,y=450)
            Button(root,text="3",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show("3")).place(x=290,y=450)
            Button(root,text="0",width=11,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show("0")).place(x=10,y=550)

            Button(root,text=".",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show(".")).place(x=290,y=550)
            Button(root,text="=",width=5,height=3,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#fe9037",command=lambda: calculate()).place(x=430,y=455)


            mainloop()

        def digital_clock():
            top = Tk()
            top.title("Digital Clock")
            def none():
                text = strftime('%H:%M:%S %p')
                lbl.config(text=text)
                lbl.after(1000,none)
            lbl = Label(top,font=('digital-7',50,'bold'),
                        background = 'white',foreground = 'blue')
            lbl.pack(anchor='center')
            none()
            mainloop()

        def notepad():
            root = Tk()
            root.geometry("600x600")
            root.title("notepad")
            root.config(bg="lightblue")
            root.resizable(False,False)

            def save_file():
                        open_file = filedialog.asksaveasfile(mode="w",defaultextension=".txt")
                        if open_file is None:
                            return
                        text = str(entry.get(1.0,END))
                        open_file.write(text)
                        open_file.close()
        
            def open_file():
                        file=filedialog.askopenfiles(mode="r",filetypes=[("text files","*,txt")])
                        if file is not None:
                            content=file.read()
                        entry.insert(INSERT,content) 
        
            b1 = Button(root,width="20",height="2",bg="#fff",text="save",command=save_file,).place(x=100,y=5)    
            b2 = Button(root,width="20",height="2",bg="#fff",text="open",command=open_file,).place(x=300,y=5)       

            entry = Text(root,height="33",width="72",wrap=WORD)
            entry.place(x=10,y=60)

            root.mainloop()
            
        #Button(root,text="DIRD DADS",width=10,height=3,font=("arial",10,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: enter()).place(x=150,y=150)
        #Button(root,text="CALCULATOR",width=10,height=3,font=("arial",10,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: calculator ()).place(x=500,y=150)       
        Button(root,width=40,pady=40,text='GAME',bg='#57a1f8',fg='white',border=4,command=enter).place(x=35,y=300)        
        Button(root,width=40,pady=40,text='CALCULATOR',bg='#57a1f8',fg='white',border=4,command=calculator).place(x=500,y=300)            
        Button(root,width=40,pady=40,text='DIGITAL CLOCK',bg='#57a1f8',fg='white',border=4,command=digital_clock).place(x=35,y=70)
        Button(root,width=40,pady=40,text='NOTEPAD',bg='#57a1f8',fg='white',border=4,command=notepad).place(x=500,y=70)


        mainloop()    
       
        
        
        
    
    elif username in r.keys() and password != r[username]:
        messagebox.showerror("Invalid","Invalid username or password")
        
        mainloop()






#img = PhotoImage(file='login.png')
#Label(root,image=img,bg='white').place(x=50,y=50)


frame = Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading = Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=125,y=3)

#---------------------------------------------------------------------------------------------------------------------
#PENTRU USERNAME
def on_enter(e):
    user.delete(0,'end')

def on_Leave(e):
    name=user.get()
    if name == '':
        user.insert(0,'Username')
             

user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')

user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_Leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

#---------------------------------------------------------------------------------------------------------------------
#PENTRU PASSWORD
def on_enter(e):
    code.delete(0,'end')

def on_Leave(e):
    name=code.get()
    if name == '':
        code.insert(0,'Password')


code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'password')


code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_Leave)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

#---------------------------------------------------------------------------------------------------------------------
Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
Label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
Label.place(x=75,y=270)

sign_up = Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8')
sign_up.place(x=230,y=270)





root.mainloop()



















    
    
    
    
    
    
    