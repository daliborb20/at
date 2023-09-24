import re

Poruka = 'pozovi me na broj telefona 444-442-4422 sutra ili na broj telefona 123-321-1234'
numRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')#takodje, postoji i method findall za sve brojeve
mo = numRegex.search(Poruka)
mo2 = numRegex.findall(Poruka)

print(mo.group())
print("###########################################")



for i in mo2:
    print(i)
