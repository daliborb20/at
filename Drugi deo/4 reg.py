########prvi deo ? znaci 1 pojavljivanje ili nijedno
import re

regex = re.compile(r'Bat(wo)?man')

mo = regex.search("The adventures of Batman")
print(mo.group())

#################drugi deo => primena na brojeve telefona
egex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
wo = egex.search("Moj broj telefona jeste 454-3544 i nalazi se zapisan u prilogu. Drugi broj telefona jeste 454-3545")
print("##################################################")
print(wo)

####################treci deo * znaci pojavljuje se nijednom ili vise puta
regex = re.compile(r'Bat(wo)*man')

mo = regex.search("The adventures of Batwowowoman")
print(mo.group())

####################cetvrti deo + znaci pojavljuje se jednom ili vise puta
regex = re.compile(r'Bat(wo)+man')
rezultat = regex.search("The adventures of Batwowoman and the adventures of Batwoman")
print(rezultat)

###############peti deo {} viticaste zagrade => tacan broj ponavaljanja
print("########################")
patern = re.compile(r'\d\d\d-\d\d\d\d{3}')
mo = patern.findall("354-3254 354-3594 346-2354")

for i in mo:
    print(i)

###################sesti deo  => zadatak

imenik = """ Billing and Collections	
 126 Harvey Street
Punta Gorda, FL 33950

 (941) 639-2528	 pgcollections@pgorda.us
 Building	326 W Marion Ave
Punta Gorda, FL 33950	
 (941) 575-3324

 buildingdept@pgorda.us
 Canal Maintenance	 3130 Cooper St
Punta Gorda, FL 33950	 (941) 575-5050	 pubworks@pgorda.us
 CHNEP	 326 W Marion Ave
Punta Gorda, FL 33950	 (941) 575-5090	 chnep@pgorda.us
 City Clerk	 326 W Marion Ave
Punta Gorda, FL 33950	 (941) 575-3369	 cityclerk@pgorda.us
 City Manager	 326 W Marion Ave
Punta Gorda, FL 33950	 (941) 575-3302	 cmadmin@pgorda.us
 Code Compliance	 326 W Marion Ave
Punta Gorda, FL 33950	 (941) 575-3352	 code@pgorda.us
 Engineering	 3130 Cooper St
Punta Gorda, FL 33950	 (941) 575-5050	 pubworks@pgorda.us
 Finance	 326 W Marion Ave
Punta Gorda, FL 33950	 (941) 575-3318	 financedept@pgorda.us
 Fire	 1410 Tamiami Trail
Punta Gorda, FL 33950	 (941) 575-5529	 fireadministrators@pgorda.us
 Human Resources	 326 W Marion Ave
Punta Gorda, FL 33950	 (941) 575-3308	 humanresources@pgorda.us
 Information Technology	 326 W Marion Ave
Punta Gorda, FL 33950	 (941) 575-3333	 it@pgorda.us
 Legal	 326 W Marion Ave
Punta Gorda, FL 33950	 (941) 575-3307	 legal@pgorda.us
 Parks and Grounds	 3130 Cooper St
Punta Gorda, FL 33950	 (941) 575-5050	 pubworks@pgorda.us
 Police	 1410 Tamiami Trail
Punta Gorda, FL 33950	 (941) 639-4111	 policeadmins@pgorda.us
 Procurement	 326 W Marion Ave
Punta Gorda, FL 33950	 (941) 575-3366	 pgpurch@pgorda.us
 Public Works	 3130 Cooper St
Punta Gorda, FL 33950	 (941) 575-5050	 pubworks@pgorda.us
 Right of Way	 3130 Cooper St
Punta Gorda, FL 33950	 (941) 575-5050	 pubworks@pgorda.us
 Sanitation	 3130 Cooper St
Punta Gorda, FL 33950	 (941) 575-5050	 pubworks@pgorda.us
 Urban Design	 326 W Marion Ave
Punta Gorda, FL 33950	 (941) 575-3372	 urbandesign@pgorda.us
 Utilities	 3130 Cooper St
Punta Gorda, FL 33950	 (941) 575-3339	 utility@pgorda.us
 Zoning	 326 W Marion Ave
Punta Gorda, FL 33950	 (941) 575-3314	 zoning@pgorda.us"""



regexObrazac = re.compile(r'(\d\d\d-\d\d\d\d)+')

pretraga = regexObrazac.findall(imenik)
brojac = 1
for i in pretraga:
    print(str(brojac) + ". broj telefona: " + i)
    brojac=brojac +1

#####sedmi deo kreiranje proizvoljnih klasa koristeci uglaste zagrade

vowelRegex = re.compile(r'[self]')#sargarepa ispred ^ oznacava negaciju  [^self]' 

rec = """Obie Trice, real name no gimmicks
Two trailer park girls go round the outside
Round the outside, round the outside
Two trailer park girls go round the outside
Round the outside, round the outsid'Cause it feels so empty without me
Kids!"""

rezz = vowelRegex.findall(rec)
print(rezz)


####################################
#osmi deo dolar znak na kraju
####################################

dolar = re.compile(r'world!$')
dolar = dolar.search('The end of world!')
print(dolar)

#################################
#deveti deo ^obaznaka$ dolar i sargarepa, znaci da trazi tacno tu rec
################################
obaZnaka = re.compile(r'^John$')
obaZnaka = obaZnaka.search("John is the best name in all the USA, John")#nece pronaci nista
print(obaZnaka)

#################################
#Tacka ispred znaci bilo koji karakter osim nove novog reda
###############################
biloKoji = re.compile(r'.bilokoji')
#biloKoji = biloKoji.search("skkdlslssl sssss bilokoji")
biloKoji = biloKoji.findall("slslslsls bilokoji skdflsdfjdsf sd bilokoji")
print(biloKoji)
for i in biloKoji:
    print("Karakter je: " + i)
#################################
#PRonalazenje imena
###############################
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
rezultatIme = nameRegex.findall("First Name: Dalibor, Last Name: Bogicevic skskslsllsls")######### Zvezda* uvek koristi "Greedy mode", tako da ce uvek vratiti sto vise teksta moze, osim novog reda \n
print(rezultatIme)
#####################moze se koristiti re.I, sa ignorisanje kapitalizacije.

#########################################
#ZAMENA KARAKTERA
#########################################
recZamena = re.compile(r'Agent \w+')
recenica = ('Agent Alice gave the secret documents to Agent BOB')
recenica = recZamena.sub("Zamenjeno", recenica)
print(recenica)

#########################################
#ZAMENA KARAKTERA - verobse mode
#########################################
re.compile(r'''
(\d\d\d\-) | #area code
(\(d\d\d\d)) # - or area code with aprents and no dash
\d\d\d\d  #last 4 digits



        ''', re.IGNORECASE | re.DOTALL | re.VERBOSE)


