message = "Jednoga dana pre sedam dana"


count= {

}

for i in message:
    count.setdefault(i, 0)
    count[i] = count[i]+1
    


print(count)