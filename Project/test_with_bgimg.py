from turtle import bgcolor
import mysql.connector as myc
from tkinter import *
from PIL import Image, ImageTk
from numpy import size
import dbConnection as dbc
import main as mn



root = Tk()
root.geometry("620x663")
root.resizable(0,0)
# canvas holds bg img
cav = Canvas(root,width=663,height=620)
bg = ImageTk.PhotoImage(Image.open("img_dir with \\.png"))
cav.pack(fill="both",expand=True)
cav.create_image(0,0,image=bg,anchor="nw")





#e1.grid(row=2, column=3)
#e0 = cav.create_window(20,70 anchor="nw")
#widget = Label(cav, text='Spam', fg='white', bg='black')
#widget.pack()
#e0.grid(row=0, column=3)


database_name = "student_portfolio_database"

def getuser():

    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)

    lhost = "localhost"
    luser = "root"
    lpasswd = ""

    # database name can be changed below the import statements

    student_db_connection = myc.connect(
        host=lhost, user=luser, passwd=lpasswd, database=database_name
    )
    student_cursor = student_db_connection.cursor()

    id = int(e0.get())
    u1 = dbc.User(id, student_cursor)
    userdetails = u1.getDetails()

    e1.insert(0, userdetails["name"])
    e2.insert(0, userdetails["age"])
    e3.insert(0, userdetails["phoneno"])
    e4.insert(0, userdetails["emailid"])
    e5.insert(0, userdetails["address"])
    e6.insert(0, userdetails["githublink"])
    e7.insert(0, userdetails["linkedinlink"])
    e8.insert(0, userdetails["hackerrank"])

    student_db_connection.close()


def facerecognition():

    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)

    fr = mn.FaceRecognition(path=r"Project/ImageInfo")
    fr.extractClassNames()
    encodeList = fr.findEncodings()
    print("Encoding Complete")

    id = fr.captureAndRecognize(encodeList)
    print(f"Recognized Id {id}")

    e0.insert(0, id)
    getuser()

#Canvas has been used here so that a bg img can be set
# here the button labe;l and text syntax  is a bit different
#idlabel = Label(cav, text="RollNo:", font="Arial ",fg="white",bg="none")
#idlabel.pack()

# buttons



buttonTryFR = Button(root,text="Try Face Recognition",command=facerecognition,font=("Arial",20),width=17,fg="blue",bg="white")
buttonTryFR_window = cav.create_window(150,620,height=30,window=buttonTryFR)


buttonGetUser = Button(root,text="Get User",command=getuser,font=("Arial",20),width=17,fg="blue",bg="white")
buttonGetUser_window = cav.create_window(450,620,height=30,window=buttonGetUser)

# adding text in canvas and labels
cav.create_text(300, 70, text="Welcome Bitches!!", font=("Helvetica",30), fill="yellow")

cav.create_text(150, 570, text="Something:", font=("Arial",20), fill="white")
e0 = Entry(cav,width=20,fg="black")
e0_window = cav.create_window(280,570,height=30,window=e0)

cav.create_text(150, 130, text="RollNo:", font=("Arial",20), fill="white")
e1 = Entry(cav,width=20,fg="black")
e1_window = cav.create_window(280,130,height=30,window=e1)

cav.create_text(150, 170, text="Name:", font=("Arial",20), fill="white")
e2 = Entry(cav,width=20,fg="black")
e2_window = cav.create_window(280,170,height=30,window=e2)

cav.create_text(150, 220, text="Age:", font=("Arial",20), fill="white")
e2 = Entry(cav,width=20,fg="black")
e2_window = cav.create_window(280,220,height=30,window=e2)

cav.create_text(150, 270, text="Phone:", font=("Arial",20), fill="white")
e3 = Entry(cav,width=20,fg="black")
e3_window = cav.create_window(280,270,height=30,window=e3)

cav.create_text(150, 320, text="Email:", font=("Arial",20), fill="white")
e4 = Entry(cav,width=20,fg="black")
e4_window = cav.create_window(280,320,height=30,window=e4)

cav.create_text(150, 370, text="Class:", font=("Arial",20), fill="white")
e5 = Entry(cav,width=20,fg="black")
e5_window = cav.create_window(280,370,height=30,window=e5)

cav.create_text(150, 420, text="Time:", font=("Arial",20), fill="white")
e6 = Entry(cav,width=20,fg="black")
e6_window = cav.create_window(280,420,height=30,window=e6)

cav.create_text(150, 470, text="Status:", font=("Arial",20), fill="white")
e7 = Entry(cav,width=20,fg="black")
e7_window = cav.create_window(280,470,height=30,window=e7)

cav.create_text(150, 520, text="Date:", font=("Arial",20), fill="white")
e8 = Entry(cav,width=20,fg="black")
e8_window = cav.create_window(280,520,height=30,window=e8)
# label1 = Label(root,text = 'Hello There').grid(row = 0,column = 0 )
# button1 = Button(root,text = 'Click Here',command = func1, width= 20 ).grid(row = 1,column = 0 )

# buttonAddUser = Button(root,text = 'Add User' , command = useradd ).grid(row = 9,column = 0 , columnspan=2 )
# buttonDeleteUser = Button(root , text = 'Delete User' , command = deluser).grid(row = 10 , column = 0, columnspan = 2)
'''
new_frame=Frame(root , bg='#24AAC9')
new_frame.pack(pady=190)
buttonTryFR = Button(new_frame, text="Try Face Recognition", command=facerecognition,width=20,font="Arial ",fg='#24AAC9',bg="white").grid(
    row=24, column=0, columnspan=1
)
buttonGetUser = Button(new_frame, text="Get User", command=getuser,width=20,font="Arial ",fg='#24AAC9',bg="white").grid(
    row=24, column=3, columnspan=2
)

idlabel = Label(new_frame, text="RollNo:", width=20,font="Arial ",fg="white",bg='#24AAC9').grid(row=0, column=0)
e0 = Entry(new_frame, width=30)
e0.grid(row=0, column=3)

#a_canvas.create_text(400,200, text="Welcome",font=("Arial", 50))

namelabel = Label(new_frame, text="Name", width=30,font="Arial ",fg="white",bg='#24AAC9').grid(row=2, column=0)
e1 = Entry(new_frame, width=30)
e1.grid(row=2, column=3)

agelabel = Label(new_frame, text="Age", width=30,font="Arial ",fg="white",bg='#24AAC9').grid(row=4, column=0)
e2 = Entry(new_frame, width=30)
e2.grid(row=4, column=3)

phonelabel = Label(new_frame, text="Phone No ", width=30,font="Arial ",fg="white",bg='#24AAC9').grid(row=6, column=0)
e3 = Entry(new_frame, width=30)
e3.grid(row=6, column=3)

emaillabel = Label(new_frame, text="Email Id", width=30,font="Arial ",fg="white",bg='#24AAC9').grid(row=8, column=0)
e4 = Entry(new_frame, width=30)
e4.grid(row=8, column=3)

addresslabel = Label(new_frame, text="Class", width=30,font="Arial ",fg="white",bg='#24AAC9').grid(row=10, column=0)
e5 = Entry(new_frame, width=30)
e5.grid(row=10, column=3)

githublabel = Label(new_frame, text="Time", width=30,font="Arial ",fg="white",bg='#24AAC9').grid(row=12, column=0)
e6 = Entry(new_frame, width=30)
e6.grid(row=12, column=3)

linkedinlabel = Label(new_frame, text="Status", width=30,font="Arial ",fg="white",bg='#24AAC9').grid(row=14, column=0)
e7 = Entry(new_frame, width=30)
e7.grid(row=14, column=3)

hrlabel = Label(new_frame, text="Date",width=30,font="Arial ",fg="white",bg='#24AAC9').grid(row=16, column=0)
e8 = Entry(new_frame, width=30)
e8.grid(row=16, column=3)
'''
root.mainloop()