from tkinter import*
import sys
import random

def rand_pass():
    x=''.join(random.choices('asdfghjklçzxcvbnmqwertyuiop0123456789!@#$%*()',k=int(sb.get())))
    y=e.get("1.0",END)

    with open("/home/loukis/D:/Desenvolvimento_de_sistemas/0/senhas.txt") as f:
        a=f.readlines()    
    b=e.get("1.0",END)[:-1]
    c=True

    for i in a:
        if b == i.rsplit(maxsplit=1)[0][:-1]:
            c=False
            d=i.rsplit(maxsplit=1)
            d[1]=x
            a[a.index(i)]=' '.join(d) +'\n'

    if c:
        ab=open("/home/loukis/D:/Desenvolvimento_de_sistemas/0/senhas.txt", 'a')
        ab.write(b+': '+x+'\n')
        ab.close()
    else:
        ab=open("/home/loukis/D:/Desenvolvimento_de_sistemas/0/senhas.txt", 'w')
        ab.writelines(a)
        ab.close()
    

    janela.clipboard_clear()
    janela.clipboard_append(x)
    janela.update()
    l['text']=x

janela = Tk()
janela.title("Gerador de senhas")
janela.geometry("350x120")

v0=Label(janela);v0.pack()
frame = Frame(janela);frame.pack()

e = Text(frame, height=1, width=35, borderwidth=2)
e.grid(row=0,column=0)

l=Label(frame, text="''")
l.grid(row=1,column=0)

bt= Button(frame, text="gerar", command=rand_pass)
bt.grid(row=2,column=0)

sb = Spinbox(frame, from_=0, to=40, width=3)
sb.delete(0,"end")
sb.insert(0,16)
sb.grid(row=2,column=0,sticky='e')

janela.mainloop()