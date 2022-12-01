import tkinter as tk
import os
import hashlib
from tkinter import *
from tkinter import messagebox

main = Tk(className='Hasher')
main.geometry('300x250+450+250')
main.minsize(300,220)
main.maxsize(300,220)
msg = Message(main,text='Choose Hash Algorithm!',background='#8787CE',aspect=200,width=1000,font='Tahoma 16')
msg.pack()

dir=os.path.abspath( os.path.dirname( __file__ ) )
os.chdir(dir)

def logic_sha():
    try:
        main_method('s')
    except:
        alert_box()

def logic_md():
    try:
        main_method('m')
    except:
        alert_box()
        
def alert_box():
    messagebox.showerror('Duplicate File','File already exit!!')

def main_method(hash_logic):
    lbl.configure(text='SHA256 selected' if hash_logic=='s' else 'MD5 selected' )
    folder_name='SHA256' if hash_logic=='s' else 'MD5'
    folder = os.path.join(dir,folder_name)
    file_name='{}.txt'.format(folder_name)
    result_file=os.path.join(folder,file_name)

    hash_list=[]
    Buff_size=65535
    for file in os.listdir():
        if not file.endswith('.py') and os.path.isfile(file):
            if hash_logic=='s':
                hash=hashlib.sha256()
            else:
                hash=hashlib.md5()
            with open(file,'rb')as f:
                fb=f.read(Buff_size)
                while len(fb)>0:
                    hash.update(fb)
                    fb=f.read(Buff_size)
                result=file+"   :  "+hash.hexdigest()
            hash_list.append(result)
            print('loading.....')

    os.mkdir(folder)
    with open(result_file,'w')as f:
        f.write('Used Hash_Logic : ')
        f.write('SHA256\n\n'if hash_logic=='s'else 'MD5\n\n')
        for i in hash_list:    
            f.write(i+'\n')
    print('done!!!')

btn1 = Button(main,text='SHA256',font='david 10 bold',background='#696969',foreground='white',relief='raised',bd=3,highlightcolor='red',command=logic_sha)
btn2 = Button(main,text='MD5',font='david 10 bold',background='#696969',foreground='white',relief='raised',bd=3,command=logic_md)
btn1.pack(fill=tk.X,padx=100,pady=20)
btn2.pack(fill=tk.X,padx=100)
lbl = Label(main,text='Not yet selected',bg='lightgreen',fg='black',font='ubuntu 12 italic')
lbl2 = Label(main,text='Created by SI_WaiYan',fg='black',font='elephant 8 italic')
lbl.pack(pady=20)
lbl2.pack(anchor=SE,padx=5)
main.mainloop()
