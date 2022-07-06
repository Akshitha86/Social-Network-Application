from tkinter import *
import tkinter.messagebox as tmsg
from tkinter import ttk
from tkinter import filedialog

import os

def raise_frame(frame):
	frame.tkraise()

root = Tk()
root.title("Social Network")
root.geometry("550x400")

class users:
	def __init__(self,name):
		self.name=name
		self.frnds=[]
		self.grps=[]
		self.messages=[]
		self.senders=[]

	def add_friend(self,frnd):
		self.frnds.append(frnd)

	def add_grp(self,id):
		self.grps.append(id)

	def add_msg(self,msgs):
		self.messages.append(msgs)

	def add_sender(self,send):
		self.senders.append(send)

dirn=os.path.dirname(__file__)
file = os.path.join(dirn,'social_network.txt')
file1 = open(file, 'r')

u=0
g=0
list=[]

for line in file1.readlines():
	if "user" in line :
		u=1
		continue
	if "group" in line :
		g=1
		continue
	if(u==1 and g==0):
		line=line.strip().replace(": ",",")
		s=line.split(",")
		user=users(s[0].strip())
		list.append(user)
		for i in s[1:] :
			user.add_friend(i)
	if(g==1) :
		line=line.strip().replace(": ",",")
		s=line.split(",")
		for j in list :
			for i in s[1:] :
				if(i==j.name) :
					j.add_grp(s[0].strip())



file1.close()


title=Label(root,text="Social Network",font=("times new roman",18,"bold"),bg="steelblue")
title.pack(side=TOP,fill=X)

f1 = Frame(root, borderwidth=4, bg="light grey", relief=GROOVE)
f2 = Frame(root, borderwidth=4, bg="light grey", relief=GROOVE)
f3 = Frame(root, borderwidth=4, bg="light grey", relief=GROOVE)
f4 = Frame(root, borderwidth=4, bg="light grey", relief=GROOVE)
f5 = Frame(root, borderwidth=4, bg="light grey", relief=GROOVE)


for frame in (f1,f2, f3, f4,f5):
	frame.place(x=25,y=35,width=500,height=350)

Button(f1, text="Post Messages",bg="Pale Turquoise" ,command=lambda:raise_frame(f2)).pack(anchor="nw",padx=10,pady=10)
Button(f2, text="Back to home page",command=lambda:raise_frame(f1)).pack(anchor="se",padx=10,pady=10)

Button(f1, text="Friends",bg="Pale Turquoise", command=lambda:raise_frame(f3)).pack(anchor="w",padx=10,pady=10)
Button(f3, text='Back to home page', command=lambda:raise_frame(f1)).pack(anchor="se",padx=10,pady=10)
Button(f1, text="Groups",bg="Pale Turquoise", command=lambda:raise_frame(f4)).pack(anchor="w",padx=10,pady=10)
Button(f4, text='Back to home page', command=lambda:raise_frame(f1)).pack(anchor="se",padx=10,pady=10)
Button(f1, text="Notifications",bg="Pale Turquoise",command=lambda:raise_frame(f5)).pack(anchor="w",padx=10,pady=10)
Button(f5, text='Back to home page', command=lambda:raise_frame(f1)).pack(anchor="se",padx=10,pady=10)

def leave():
	a=tmsg.askyesno("Exit","Do you really want to leave?")
	if(a==True) :
		root.quit()
		root.destroy()
	else :
		msg="Thank You"
		tmsg.showinfo("Exit",msg)
		 

Button(f1, text="Exit",bg="Pale Turquoise", command=leave).pack(anchor="w",padx=10,pady=10)


lbl_user=Label(f1,text = "Select User",bg="light grey",fg="black",font=("times new roman",10,"bold"))
lbl_user.place(x=350,y=20)

Label(f3,text="List of friends :",font=("Times new roman",15,"bold"),bg="light grey").pack()
	

scrollbar=Scrollbar(f3)
scrollbar.pack(side=RIGHT, fill=Y)
listbox = Listbox(f3, yscrollcommand = scrollbar.set,height=15)
listbox.delete(0,END)
listbox.pack(fill="both",padx=22,pady=20)
scrollbar.config(command=listbox.yview)


Label(f4,text="List in Groups :",font=("Times new roman",15,"bold"),bg="light grey").pack()
scrollbar1=Scrollbar(f4)
scrollbar1.pack(side=RIGHT, fill=Y)
listbox1 = Listbox(f4, yscrollcommand = scrollbar1.set,height=15,font=("Times new roman",13," "))
listbox1.pack(fill="both",padx=22,pady=20)
scrollbar1.config(command=listbox1.yview)

Label(f5,text="New posts of your freinds/groups",font=("Times new roman",16,"bold"),bg="light grey").pack()

scrollbar2=Scrollbar(f5)
scrollbar2.pack(side=RIGHT, fill=Y)
listbox2 = Listbox(f5, yscrollcommand = scrollbar2.set,height=15,width=40)

listbox2.pack(fill="both",padx=22,pady=20)
scrollbar2.config(command=listbox2.yview)   


users=[""]

for i in list :
	users.append(i.name)
file = os.path.join(dirn,'messeges.txt')
def pick_user(event):
	a=my_dd.get()
	def post_msg(event):
		for i in list :
			 if(i.name==a):
						
						str3="To-"+str (my_dd1.get())+" From:"+i.name +", "
						str4= "Msg:" +str(T.get("1.0","end-1c"))
						file2=open(file,"a")
						file2.write(str3)
						file2.write(str4)
						file2.write("\n")
						i.add_msg(T.get("1.0","end-1c"))
						i.add_sender(my_dd1.get())
						file2.close()
				  
		
	
	def open_image():
		global image
		file=filedialog.askopenfilename()
		image=PhotoImage(file=file)
		position=T.index(INSERT)
		T.image_create(position,image=image)

	T=Text(f2,width=30,bg="white",height=15)
	T.pack(anchor="w",padx=10,pady=5)

	def clear_text():
		T.delete("1.0","end")
	
	for i in list :
		if(i.name==a):
			my_dd1=ttk.Combobox(f2,value=(i.frnds+i.grps))
			my_dd1.current(0)
			my_dd1.place(x=310,y=80,width=150)
			my_dd1.bind("<<ComboboxSelected>>",post_msg)

	lbl_user=Label(f2,text = "Send to",bg="light grey",fg="black",font=("times new roman",10,"bold"))
	lbl_user.place(x=350,y=50)

	Button(f2, text="Post",bg="lightblue",command=clear_text).place(x=360,y=200)
	Button(f2, text="Add Image",bg="lightblue", command=open_image).place(x=345,y=240)
#Label(f3, text='FRAME 3').pack(side='left')
	for i in list:
		if(i.name==my_dd.get()):
			listbox.delete(0,END)
			for j in i.frnds:
				listbox.insert(END,f"{j}")

	

 
	#Label(f4, text='FRAME 4').pack()   
	for i in list:
		if(i.name==a):
			listbox1.delete(0,END)
			for j in i.grps:
				listbox1.insert(END, j)
	
	
	#Label(f5, text='FRAME 4').pack()

	file3=open(file,"r")
	f=0
	count=0
	listbox2.delete(0,END)
	for line in file3.readlines():
		if(line.count("To-")>0):
			f=0
		if(line.count("To-"+my_dd.get())>0):
			f=1
			s=line.split(":")[1].split(",")[0]
			ms=line.split(":")
			listbox2.insert(END, f"From : {s}")
			ms1=ms[len(ms)-1]
			listbox2.insert(END, f"Msg: {ms1}")
			continue
		if(f==1):
			listbox2.insert(END, f"        {line}")
		

	file3.close()
 

my_dd=ttk.Combobox(f1,values=users)
my_dd.current(0)
my_dd.place(x=310,y=50,width=150)
my_dd.bind("<<ComboboxSelected>>",pick_user)



raise_frame(f1)

root.mainloop()