def loef(f:str,l:list):
    fail=open(f,"r",encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        l.append(rida.strip())
    fail.close()
    return l

def fileSave(f:str,l:list):
    fail=open(f,'w',encoding="utf-8-sig")
    for el in l:
        fail.write(el+'\n')
    fail.close()

def newWord(f:str, rida:str)->list:
    l=[]
    with open(f,"a",encoding="utf-8-sig") as fail:
        fail.write(rida+"\n")
    l=loef(f,l)
    return l


def translate(r:list,a:list):
    word=input("Введите страну или столицу: ")
    if word in r:
        transl=a[r.index(word)]
        print(word+"-"+transl)
    elif word in a:
        transl=r[a.index(word)]
        print(word+"-"+transl)
    else:
        print("Страна или столица отсутствует в словаре")

def error(l1:list,l1a:str,l2:list,l2a:str):
    word=input("В какой стране или столице ошибка?: ")
    if word not in l1 and word not in l2:
        print("Такого нет :(")
    else:
        if word in l1:
            transl=l2[l1.index(word)]
            l1.remove(word)
            l2.remove(transl)
            print(l2, l1)
        elif word in l2:
            transl=l1[l2.index(word)]
            l2.remove(word)
            l1.remove(transl)
            print(l2, l1)
        l1.append(input("Введи новую страну "))
        l2.append(input("Введи новую столицу: "))
        fileSave(l1a,l1)
        fileSave(l2a,l2)
import random
def test(l1:list,l2:list):
    result=0
    bothLists=[]
    bothLists.extend(l1)
    bothLists.extend(l2)
    random.shuffle(bothLists)
    print('random list ',bothLists)
    for i in range(len(l1)):
        print('l1 ',l1)
        print('l2 ',l2)
        otvet=input(f"Какая это страна или столица - '{bothLists[i]}': ")
        if otvet in l1 or otvet in l2:
            if bothLists[i] in l1:
               if l1.index(bothLists[i])==l2.index(otvet):
                    result+=1
                    print('правильно!')
                    print()
            elif bothLists[i] in l2:
                if l2.index(bothLists[i])==l1.index(otvet):
                    result+=1
                    print('правильно!')
                    print()
        else:
            print('Неправильно!')
            print()
    resultPer=(result/len(l1))*100
    print(f"Ваш результат: {resultPer}%")


#def readFile(f:str,d:dict):
#    file=open(f)
#    d=file.read().split("\n")[:-1]
#    for item in di:
#        country=item.split("-")[0]
#        capital=item.split("-")[1:]
#        d[country]=capital
#    file.close()
#    return d
