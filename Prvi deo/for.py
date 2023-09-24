lista = list(range(0,1000))
print(lista)



list2 = ['jedan', 'dva', 'tri', 'cetiri', 'pet', ]

for i in range(len(list2)):
    print(str(i) + " clan je " + list2[i])



print("Vrednost se nalazi na poziciji: " + str(list2.index("tri")))


list2.append("kokoska ")
print(list2)

list2.remove(list2[0])
print(list2)


string = "Jednoga dana pre sedam dana, srelo se sedam gotovana"
print(string[5:])