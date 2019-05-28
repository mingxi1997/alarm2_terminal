#!/usr/bin/python3
# coding: utf-8
from tkinter import *





def show_text():
    with open('event_come.txt','r')as f:
        event=f.read()
    with open('affirm.txt','r')as f:
        affirm=f.read()
    with open('affirm_add.txt','r')as f:
        affirm_add=f.read()
  
    if event=='1':
        with open('text.txt','r')as f:
            text=eval(f.read())
             
        panel1= Label(root,text=text[1],width =25,height = 1,font=('Timesnewroman','22')).place(x=285,y=170)
        panel2= Label(root,text=text[0],width =25,height = 1,font=('Timesnewroman','22')).place(x=834,y=170)
        if len(text[2][5:])>0:
            panel3= Label(root,text=text[2][5:],width =45,height = 9,font=('song','29'),justify = 'left',wraplength = 1050 ).place(x=77,y=238)
        else:
            panel3= Label(root,image=photo4).place(x=72,y=238)
        with open('event_come.txt','w')as f:
            f.write('0')
    
    
    if affirm_add!=affirm:
        with open('affirm_add.txt','w')as f:
            f.write(affirm)
        if affirm=='1':
            panel4= Label(root,image=photo2,width =585,height = 92).place(x=350,y=710)
        else:
            panel4= Label(root,image=photo3,width =585,height = 92).place(x=350,y=710)
    root.after(1000,show_text)

        
        
    



with open('event_come.txt','w')as f:
    f.write('1')


with open('affirm.txt','r')as f:
    affirm=f.read() 
with open('affirm_add.txt','w')as f:
    f.write(affirm)

root=Tk()
root.geometry('1280x800')
root.resizable(0,0)

#root.attributes('-fullscreen',1)
#root.overrideredirect(True)
photo=PhotoImage(file="bg.png")



img= Label(root,image=photo)
img.grid(row=0,column=0,rowspan=1000,columnspan=1000)


photo2=PhotoImage(file="confirm.png")
photo3=PhotoImage(file="nothing.png")
photo4=PhotoImage(file="no_message.png")

show_text()
root.update_idletasks()
root.mainloop()
