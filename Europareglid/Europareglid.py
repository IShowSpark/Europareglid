from module1 import *

stolica=[]
strana=[]
strana=loef('TextFile1.txt',strana)
print(strana)
stolica=loef('TextFile2.txt',stolica)
print(stolica)

print("--------------------------------------Добро пожаловаться в Python Clownsnap!--------------------------------------------")
while True:
    language=input("Добавить новую страну или столицу - Y\nУвидеть список столиц и стран - N\nПросто столица и страна - T\nНашел ошибку - V\nПроговорить слово - R\nТест на знание слов - Z\nЗакончить - E\nВыбери вариант: ")
    print()
    if language.upper()=="Y":
        strana=newWord("TextFile1.txt", input("Новое слово: "))
        stolica=newWord("TextFile2.txt", input("Перевод слова: "))
    elif language.upper()=="N":
        print(strana)
        print(stolica)
    elif language.upper()=="T":
        translate(strana,stolica)

    elif language.upper()=="V":
        error(strana,"TextFile1.txt", stolica,"TextFile2.txt")

    elif language.upper()=="R":
        lang=input("На каком языке проговорить?: ")
        word=input("Слово: ")
        heli(word,lang)
    elif language.upper()=="R":
        lang=input("На каком языке проговорить?: ")
        word=input("Слово: ")
        heli(word,lang)
    elif language.upper()=="Z":
        test(strana, stolica)
    elif language.upper()=="E":
        print('Head Aega!')
        break