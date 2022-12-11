print("Hello Deniel Di Marcello")#Задание 1
print("Koosta programm on öeldud tehte 3 + 8 / (4 - 2) * 4 vastuse?")#Задание2
a=4
b=2
c=3
d=8
e=c+d/(a-b)*a
print(e)
print("Ruudu sees asub ring. Ringi raadius on 3.Leia ja väljasta ekraanile ruudu pindala, ruudu ümbermõõt, ringi pindala, ringi ümbermõõt.")#Задание2.1
r=3
w=4#У квадрата 4 стороны
Sruudu=(r+r)*(r+r)#Сумма двух радиусов круга вписанного в квадрат равняется стороне квадрата. У квадрата все стороны равны.Sквадрата = a*a
Pruudu=(r+r)*w
import math
from tkinter import Y
f=math.pi
Sringi=f*(r*r)
Pringi=b*f*r#P=2pir
print("Sruudu=", Sruudu)
print("Pruudu=", Pruudu)
print("Sringi=", Sringi)
print("Pringi=", Pringi)
print("Koosta programm, mis arvutab välja Maa ümbermõõdu ekvaatori kohal 2-eurostes")#Задание2.2
print("Диаметр монеты в 2 евро равен 3мм")
print("Диаметр Земли над экватором равен 6378км или 6378000000мм")
print("сколько монет номиналом 2 евро нужно положить рядом друг с другом, чтобы линия прошла вокруг Земли.")
g=3
v=6378000000
k=v/g
print(k)
print("Eelnevaid teadmisi kasutades kirjuta programm, mis väljastaks:kill-koll kill-koll killadi-koll kill-koll kill-koll killadi-koll kill-koll kill-koll killkollkill-koll")#Задание3
name="kill-koll "
ame="killadi-koll "
me="killkoll "
print(name+name+ame+name+name+ame+name+name+me+name)
print("Koosta programm, mis väljastaks järgmised laulusõnad:")#Задание4
y="tsuh tsuh tsuh"
i="tuut tuut tuut"
z="rat tat taa"
l="tat tat taa"
h="kill koll koll"
m="kill koll kill"
print("Rong see sõitis "+y+",\
piilupart oli rongijuht.\
Rattad tegid "+z+" "+z+" ja "+l+".")
print("Rong see sõitis "+i+",\
piilupart oli rongijuht.\
Rattad tegid "+h+" "+h+" ja "+m+".")
print("Koosta programm, mis küsib kasutajalt ristküliku lähiskülgede pikkused ning väljastab ekraanile ristküliku ümbermõõdu ja pindala.")#Задание 5
what=input("Что делаем? (S,P): ")
sidea=float(input("Введите сторону а"))
sideb=float(input("Введите сторону b"))
if what=="S":
    s=sidea*sideb
    print(s)
if what=="P":
    p=sidea+sidea+sideb+sideb
    print(p)
else:
    print("Такого варианта ответа нет!")


