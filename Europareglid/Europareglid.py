from module1 import *
from tkinter import *
from tkinter.ttk import Radiobutton
from tkinter import messagebox
from tkinter.ttk import Checkbutton

stolica=[]
strana=[]
strana=loef('TextFile1.txt',strana)
stolica=loef('TextFile2.txt',stolica)


def kwindow(t:str):
    awindow=Toplevel()
    awindow.title(t)
    awindow.geometry("650x260")

       
    opisanie=Label(awindow,text="Окно для описания уроков\nИнформация ниже\n⮟",height=4,width=60,bg="#98FF98",font="Calibri 18",relief="groove")
    opisanie.pack(side=TOP)
    lbl_k=Label(awindow,text=tunni_plaan[t],font="Calibri 18",bg="#4169E1",height=2,relief="groove").pack(side=BOTTOM)


def clicked1():
    question=messagebox.askyesno('Adeptgod', 'Добавить новую страну или столицу')
    while question == True:
        strana=newWord("TextFile1.txt", input("Новая страна: "))
        stolica=newWord("TextFile2.txt", input("Новая столица: "))


def clicked2():
    question=messagebox.askyesno('Adeptgod','Увидеть список столиц и стран')
    while question==True:
        print(strana)
        print()
        print(stolica)
        break

    
def clicked3():
    question=messagebox.askyesno('Adeptgod','Просто столица и страна')
    while question==True:
        translate(strana,stolica)

def clicked4():
    question=messagebox.askyesno('Adeptgod','Нашел ошибку')
    while question==True:
         error(strana,"TextFile1.txt", stolica,"TextFile2.txt")

def clicked5():
    question=messagebox.showwarning('Adeptgod','Проговорить слово(в разработке)')

def clicked6():
    question=messagebox.askyesno('Adeptgod','Тест на знание слов')
    while question==True:
        test(strana, stolica)


def clicked7():
    question=messagebox.askyesno('Adeptgod','Закончить')
    while question==True:
        print('Head Aega!')
        break







window=Tk()
window.title("Страны и столицы")
window.geometry("250x50")




rad1 = Radiobutton(window, text='Y', value=1,command=clicked1)
rad2 = Radiobutton(window, text='N', value=2,command=clicked2)  
rad3 = Radiobutton(window, text='T', value=3,command=clicked3)
rad4 = Radiobutton(window, text='V', value=4,command=clicked4)  
rad5 = Radiobutton(window, text='R', value=5,command=clicked5)  
rad6 = Radiobutton(window, text='Z', value=6,command=clicked6)  
rad7 = Radiobutton(window, text='E', value=7,command=clicked7)
rad1.grid(column=0, row=0)  
rad2.grid(column=1, row=0)  
rad3.grid(column=2, row=0)
rad4.grid(column=3, row=0)  
rad5.grid(column=4, row=0)  
rad6.grid(column=5, row=0) 
rad7.grid(column=6, row=0)


window.mainloop()