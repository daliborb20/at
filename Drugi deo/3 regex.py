import re

phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')#zagrade za odvajanje grupa
rezultat  = phoneRegex.search('Moj broj telefona je 354-545-5465, a poslovni 635-546-6879')
print(rezultat)
for i in rezultat.group(1):
    print(i)


    #####pipe||||

regexIzraz = re.compile(r'Bat(man|mobile|copter|bat)')

rezultatPipe = regexIzraz.search('Batmobile lost a wheel')
print(rezultatPipe.group())

