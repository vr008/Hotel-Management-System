from tkinter import *

import cx_Oracle

root = Tk()
root.geometry('300x400')
root.title('Register to access')


con=cx_Oracle.connect('xe/TSR@localhost:1521/xe')
cur = con.cursor()

'''cur.execute("create table reg(username varchar(20) primary key,password varchar(20))")'''
  
'''cur.execute("create table customer1(cu_id varchar(100) primary key,customer_name varchar(40),phone_no int,city varchar(100))")'''
'''cur.execute("create table room_details(no_of_pass int,room_type varchar(200),cu_id references customer1(cu_id),a_date varchar(20),d_date varchar(20),noofdays int)")'''
'''cur.execute("create table book_details1(b_id varchar(100) primary key,cost int,cu_id references customer1(cu_id))")'''
con.commit()
lb = Label(root, text="Username",font=('Times', 14))
lb.pack()
e = Entry(root)
e.pack()
lb2 = Label(root, text="Password",font=('Times', 14))
lb2.pack()
e2 = Entry(root)
e2.pack()


def insert():
    a = str(e.get())
    b = str(e2.get())
    con=cx_Oracle.connect('xe/TSR@localhost:1521/xe')
    cursor = con.cursor()
    cursor.execute(f"insert into reg values('{a}','{b}')")
    con.commit()


def ne():
    def search():
        c = str(e3.get())
        d = str(e4.get())
        con = cx_Oracle.connect('xe/TSR@localhost:1521/xe')
        cursor = con.cursor()
        cnt = 0
        for i in cursor.execute(f"select * from reg where username='{c}' and password='{d}'"):
            cnt += 1
        if cnt == 1:
            def newwindow():
                new = Toplevel(new1)
                new.geometry('500x300')
                new.title('Welcome to hotel royal meridian')

                def add():
                    add = Toplevel(new)
                    add.geometry('500x300')
                    add.title('Add customer details')
                    l2 = Label(add, text="Name")
                    l2.grid(row=2, column=2)
                    l3=Label(add,text="Phone no")
                    l3.grid(row=3,column=2)
                    l4=Label(add,text="city")
                    l4.grid(row=4,column=2)
                
                    a2 = Entry(add)
                    a2.grid(row=2, column=3)
                    a3=Entry(add)
                    a3.grid(row=3,column=3)
                    a4=Entry(add)
                    a4.grid(row=4,column=3)
                  
                
                    def insert():
                        def showcars():
                            show=Toplevel(add)
                            show.geometry('600x600')
                            show.title("List of rooms available")
                            lb1=Label(show,text="\tRoom Type  Seat Capacity    Rent For 1 Fay\n Single Bed\t1\t Rs:1000\n Double Bed\t2\t Rs:1400\n Triple Bed \t3\t Rs:2500\n Four Bed \t4\t Rs:3200")
                            lb1.grid(row=3,column=1)
                        
                            sc2=Label(show,text="No of people staying").grid(row=7,column=1)
                            sc3=Label(show,text="Date of arrival").grid(row=8,column=1)
                            sc4=Label(show,text="Date of departure").grid(row=9,column=1)
                            sc5=Label(show,text="no of days").grid(row=10,column=1)
                          
                            k2=Entry(show)
                            k2.grid(row=7,column=2)
                            k3=Entry(show)
                            k3.grid(row=8,column=2)
                            k4=Entry(show)
                            k4.grid(row=9,column=2)
                            k5=Entry(show)
                            k5.grid(row=10,column=2)
                            d={"single bed":1000,"double bed":1400,"triple bed":2500,"four bed":3200}
                            d1={"single bed":1,"double bed":2,"triple bed":3,"four bed":4}
                            d2={1:1000,2:1400,3:2500,4:3200}
                            d3={1:"single bed",2:"double bed",3:"triple bed",4:"four bed"}
                            def inp1():
                                ks2=int(k2.get())
                                ks3=str(k3.get())
                                ks4=str(k4.get())
                                ks5=int(k5.get())
                               
                                
                                
                                
                                if(ks2<=4):
                                    c=d2[ks2]*ks5
                                    ks="one"+d3[ks2]+"room"

                                elif(ks2>4 and ks2%4==0):
                                    a=ks2//4
                                    c=a*3200*ks5
                                    ks=str(a)+"-"+"four bed rooms"
                                elif(ks2>4 and ks2%4!=0):
                                    t=ks2%4
                                    a=ks2//4
                                    c=(a*3200+d2[t])*ks5
                                    ks=str(a)+"-"+"four bed and a "+d3[t]+"room"
                                b_id=cu_id+ks[0]+ks3[0]+str(ks2)
                                t1=Label(show,text="details of room and rent").grid(row=16,column=2)
                                t=Label(show,text=f"Your customer id={cu_id}").grid(row=15,column=2)
                                t3=Label(show,text=f"best room accomodation='{ks}'").grid(row=17,column=2)
                                t4=Label(show,text=f"rent ={c} and no of days={ks5}").grid(row=18,column=2)
                            def inp2():
                                show.destroy()
                            def inp():
                            
                                ks2=int(k2.get())
                                ks3=str(k3.get())
                                ks4=str(k4.get())
                                ks5=int(k5.get())
                                con = cx_Oracle.connect('xe/TSR@localhost:1521/xe')
                                cur = con.cursor()
                                
                                
                                
                                if(ks2<=4):
                                    c=d2[ks2]*ks5
                                    ks="one"+d3[ks2]+"room"
                                elif(ks2>4 and ks2%4==0):
                                    a=ks2//4
                                    c=a*3200*ks5
                                    ks=str(a)+"-"+"four bed rooms"
                                elif(ks2>4 and ks2%4!=0):
                                    t=ks2%4
                                    a=ks2//4
                                    c=(a*3200+d2[t])*ks5
                                    ks=str(a)+"-"+"four bed and a "+d3[t]+"rooms"
                                cur.execute(f"insert into room_details values({ks2},'{ks}','{cu_id}','{ks3}','{ks4}',{ks5})")
                                b_id=cu_id+ks[0]+ks3[0]+str(ks2)+str(ks5)
                              
                                
                                
                                cur.execute(f"insert into book_details1 values('{b_id}',{c},'{cu_id}')")
                                con.commit()
                                def last():
                                    final=Toplevel(show)
                                    final.geometry("400x400")
                                    final.title("Payment Successful")
                                    c=Label(final,text=f"            Congrats your payment is succesful\n\n        Your booking id={b_id}\n Kindly visit us again! ").grid(row=2,column=1)
                                last()
                            bt=Button(show,text="Click for payment",command=inp)
                            bt.grid(row=13,column=1)
                            bt1=Button(show,text="show details",command=inp1)
                            bt1.grid(row=13,column=2)
                            bt2=Button(show,text="abort",command=inp2)
                            bt2.grid(row=13,column=3)
                   
                        b=str(a2.get())
                        c=int(a3.get())
                        d=str(a4.get())
                        cu_id=b[0]+d[0]+d[1]+b[1]+str(c)
                        con=cx_Oracle.connect('xe/TSR@localhost:1521/xe')
                        cur = con.cursor()
                        
                        cur.execute(f"insert into customer1 values('{cu_id}','{b}',{c},'{d}')")
                        con.commit()
                        con.close()
                        showcars()


                       

                    b1 = Button(add, text="Add your details", command=insert)
                    b1.grid(row=10, column=10)
                   
                 

                    

                def search():
                    def search2():
                        v=str(se.get())
                        con = cx_Oracle.connect('xe/TSR@localhost:1521/xe')
                        cur = con.cursor()
                        global txt
                        txt=""
                        cnt=0
                        c=0
                        for i in cur.execute(f"select customer_name,room_type,a_date,d_date from room_details,customer1 where customer1.cu_id='{v}' and room_details.cu_id='{v}'"):

                             for j in i:
                                if cnt % 4 == 0:                      
                                    txt+="\n"
                                    txt += "customer name: "
                                elif cnt % 4 == 1:
                                    txt += "room type: "
                                elif cnt % 4 == 2:
                                    txt += "arrival date: "
                                elif cnt%4==3:
                                    txt+="departure date: "
                                for k in j:
                                    txt+=str(k)
                                cnt += 1
                                txt += "\n"
                                
                        for k in cur.execute(f"select noofdays from room_details where room_details.cu_id='{v}'"):
                            for h in k:
                                if c==0:
                                    txt+="no of days: "
                                    txt+=str(h)


                        if txt=="":
                            t=Label(search,text="Not found",font=("helvetica",17)).grid(row=5,column=3)
                        else:
                            t=Label(search,text=txt,font=("helvetica",17)).grid(row=5,column=3)
                        con.commit()
                        con.close()
                    search = Toplevel(new)
                    search.title("Search")
                    search.geometry("800x800")
                    sl=Label(search,text="Enter your customer id",font=("helvetica",17)).grid(row=2,column=2)
                    se=Entry(search,font=("helvetica",17))
                    se.grid(row=2,column=3)
                    bu=Button(search,text="Find details",font=("helvetica",17),command=search2)
                    bu.grid(row=3,column=3)
                

                def delete():
                    delete = Toplevel(new)
                    delete.geometry('500x300')
                    delete.title('Cancel booking')
                    l1 = Label(delete, text='Enter your book id ')
                    l1.grid(row=1, column=2)
                    e1 = Entry(delete)
                    e1.grid(row=1, column=3)
                    
                    def dell():
                        con = cx_Oracle.connect('xe/TSR@localhost:1521/xe')
                        cur = con.cursor()
                        c1=str(e1.get())
                        c=0
                        txt=""
                        for i in cur.execute(f"select cost from book_details1 where b_id='{c1}'"):
                           for h in c1:
                               if c==0:
                                   txt+="cost:"
                                   txt+=str(h)
                                   
                        
                        cur.execute(f"delete from book_details1 where b_id='{c1}'")
                        if(txt==""):
                            s1=Label(delete,text="id not found enter the correct id").grid(row=5,column=3)
                        else:
                            s1=Label(delete,text="Booking cancelled, amount will be refunded soon").grid(row=5,column=3)
                        
                        cur.close()
                        con.commit()
                        con.close()
                    deletebutton = Button(delete, text='Cancel Booking',command=dell)
                    deletebutton.grid(row=10, column=10)
                    
                        

                def update():
                    update = Toplevel(new)
                    update.geometry('500x300')
                    update.title('Update booking details')
                    l=Label(update,text="To Update The Booking Details Of The Customer")
                    l.grid(row=1,column=3)
                    l1 = Label(update, text='Enter  your customer id')
                    l1.grid(row=2, column=2)
                    e1 = Entry(update)
                    e1.grid(row=2, column=3)
                    l7=Label(update,text="Enter The Values need to be Modified")
                    l7.grid(row=3,column=3)
                    l2 = Label(update, text='Enter arrival date')
                    l2.grid(row=4, column=2)
                    l3 = Label(update, text='Enter departure date')
                    l3.grid(row=5, column=2)
                    l4 = Label(update, text='Enter no of days')
                    l4.grid(row=6, column=2)
                    l5 = Label(update, text='Enter no of passengers')
                    l5.grid(row=7, column=2)
                
                    e2 = Entry(update)
                    e2.grid(row=4, column=3)
                    e3 = Entry(update)
                    e3.grid(row=5, column=3)
                    e4 = Entry(update)
                    e4.grid(row=6, column=3)
                    e5 = Entry(update)
                    e5.grid(row=7, column=3)
                   
                    def update1():
                        con = cx_Oracle.connect('xe/TSR@localhost:1521/xe')
                        cur = con.cursor()
                        c1=str(e1.get())
                        c2=str(e2.get())
                        c3=str(e3.get())
                        c4=int(e4.get())
                        c5=int(e5.get())
                        d={"single bed":1000,"double bed":1400,"triple bed":2500,"four bed":3200}
                        d1={"single bed":1,"double bed":2,"triple bed":3,"four bed":4}
                        d2={1:1000,2:1400,3:2500,4:3200}
                        d3={1:"single bed",2:"double bed",3:"triple bed",4:"four bed"}
                        if(c5<=4):
                            c=d2[c5]*c4
                            ks="one"+d3[c5]+"room"
                        elif(c5>4 and c5%4!=0):
                            t=c5%4
                            a=c5//4
                            c=(a*3200+d2[t])*c4
                            ks=str(a)+"-"+"four bed and a "+d3[t]+"room"
                        elif(c5>4 and c5%4==0):
                            a=c5//4
                            c=a*3200*c4
                            ks=str(a)+"-"+"four bed rooms"
                        cur.execute(f"update room_details set a_date='{c2}',d_date='{c3}',noofdays={c4},no_of_pass={c5},room_type='{ks}' where cu_id='{c1}'")
                        cur.execute(f"update book_details1 set cost={c} where cu_id='{c1}'")
                        cur.close()
                        con.commit()
                        con.close()
                    def select12():
                        con = cx_Oracle.connect('xe/TSR@localhost:1521/xe')
                        cur = con.cursor()
                        c1=str(e1.get())
                        global txt
                        txt=""
                        cnt=0
                        c=0
                        d=0
                        e=0
                        for l in cur.execute(f"select a_date,d_date,room_type from room_details where cu_id='{c1}'"):
                            for j in l:
                                if cnt % 3 == 0:                      
                                    txt+="\n"
                                    txt += "date of arrival: "
                                elif cnt % 3 == 1:
                                    txt += "date of departure: "
                                elif cnt % 3 == 2:
                                    txt += "room type: "
                                for k in j:
                                    txt+=str(k)
                                cnt += 1
                                txt += "\n"
                                
                        for k in cur.execute(f"select noofdays from room_details where room_details.cu_id='{c1}'"):
                            for h in k:
                                if c==0:
                                    txt+="no of days: "
                                    txt+=str(h)
                        
                        for o in cur.execute(f"select no_of_pass from room_details where room_details.cu_id='{c1}'"):
                            for p in o:
                                if e==0:
                                    txt+="\nno of pass: "
                                    txt+=str(p)
                                
                        for g in cur.execute(f"select cost from book_details1 where book_details1.cu_id='{c1}'"):
                            for a in g:
                                if d==0:
                                    txt+="\ncost: "
                                    txt+=str(a)


                        if txt=="":
                            t=Label(update,text="Not found",font=("helvetica",17)).grid(row=17,column=3)
                        else:
                            t=Label(update,text="after updation",font=("helvetica",17)).grid(row=16,column=3)
                            t=Label(update,text=txt,font=("helvetica",17)).grid(row=17,column=3)
                
                        con.commit()
                    
                            
                    updatebutton = Button(update, text='Update booking date',command=update1)
                    updatebutton.grid(row=10, column=10)
                    show1=Button(update,text="Show changes",command=select12)
                    show1.grid(row=10,column=14)
                def exit1():
                    new.destroy()

                addb = Button(new, text="Book rooms", command=add)
                searchb = Button(new, text="Search booking details", command=search)
                updateb = Button(new, text="Update booking details", command=update)
                deleteb = Button(new, text="Cancel booking", command=delete)
                exit=Button(new,text='Exit',command=exit1)
                addb.grid(row=2, column=3)
                searchb.grid(row=5, column=6)
                updateb.grid(row=6, column=7)
                deleteb.grid(row=7, column=8)
                exit.grid(row=8,column=9)
            newwindow()

        elif cnt == 0:
            lbb = Label(new1, text="Invalid")
            lbb.pack()
        con.commit()

    new1 = Toplevel(root)
    new1.geometry("400x400")
    new1.title("Log in ")

    l = Label(new1, text="Username").pack()
    e3 = Entry(new1)
    e3.pack()
    l2 = Label(new1, text="Password").pack()
    e4 = Entry(new1,show='*')
    e4.pack()
    b = Button(new1, text="Log in", command=search).pack()


bt = Button(root, text="Register", command=insert,font=('Times', 14)).pack()
bt2 = Button(root, text="Already Signed up", command=ne,font=('Times', 14)).pack()

root.mainloop()
