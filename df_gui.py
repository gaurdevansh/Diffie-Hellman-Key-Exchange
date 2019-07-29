from tkinter import *
from tkinter import filedialog
from keygen import *
from encrypt_decrypt import *


private_file = ''
public_file = ''
file_name = ''

#Diaglog Box

def entry3_dialog():
	filename = filedialog.askopenfilename(title="Select File",filetypes = (("All files","**"),("text files","*.txt")))
	f = filename.split('/')
	entry3.insert(0,f[-1])
	global private_file
	private_file = f[-1]


def entry4_dialog():
	filename = filedialog.askopenfilename(title="Select File",filetypes = (("All files","**"),("text files","*.txt")))
	f = filename.split('/')
	entry4.insert(0,f[-1])
	global public_file
	public_file = f[-1]

def entry5_dialog():
	filename = filedialog.askopenfilename(title="Select File",filetypes = (("All files","**"),("text files","*.txt")))
	f = filename.split('/')
	entry5.insert(0,f[-1])
	global file_name 
	file_name = f[-1]

#Calling encryption and decryption from other module

def enc():
	secret = str(gensecret(private_file,public_file))
	encrypt(getKey(secret),file_name)


def dec():
	secret = str(gensecret(private_file,public_file))
	decrypt(getKey(secret),file_name)


#Calling Keys generating function

def gen_pri():
	filename=entry1.get()
	genprivate(filename)

def gen_pub():
	filename1=entry1.get()
	filename2=entry2.get()
	genpublic(filename1,filename2)



root = Tk()

#Keys

#labels
label1 = Label(root,text='Private Key : ')
label2 = Label(root,text='Public Key : ')
label1.grid(row=0)
label2.grid(row=1)

#entry
entry1 = Entry(root)
entry1.insert(END,'Enter Key Name')
entry2 = Entry(root)
entry2.insert(END,'Enter Key Name')
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

#buttons
button1 = Button(root,text='Generate',command=gen_pri)
button2 = Button(root,text='Generate',command=gen_pub)
button1.grid(row=0,column=2)
button2.grid(row=1,column=2)



#Encryption and Decryption

#labels
label3 = Label(root,text='Encryption/Decryption : ')
label4 = Label(root,text='Private key : ')
label5 = Label(root,text='Public key of other user : ')
label6 = Label(root,text='File : ')
label3.grid(row=2)
label4.grid(row=3)
label5.grid(row=4)
label6.grid(row=5)

#entry
entry3 = Entry(root)
entry4 = Entry(root)
entry5 = Entry(root)
entry3.grid(row=3,column=1)
entry4.grid(row=4,column=1)
entry5.grid(row=5,column=1)

#buttons
button3 = Button(root,text='Browse',command=entry3_dialog)
button4 = Button(root,text='Browse',command=entry4_dialog)
button5 = Button(root,text='Browse',command=entry5_dialog)
button6 = Button(root,text='Encrypt',command=enc)
button7 = Button(root,text='Decrypt',command=dec)
button3.grid(row=3,column=2)
button4.grid(row=4,column=2)
button5.grid(row=5,column=2)
button6.grid(row=6,column=1)
button7.grid(row=6,column=2)


root.title('Encryptor-Decryptor')
root.geometry('600x400')
root.resizable(height=False,width=False)

root.mainloop()
