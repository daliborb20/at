import shutil as sh

sh.copy("..\\Prvi deo\\1.py", ".") #ukoliko treba da se kopira samo jedcan fajl
print("Uspesno kopirano!")


#sh.copytree(#PutanjaDoFajla, #Destinacija)#ukoliko treba da se kopira ceo direktorijum
#sh.move(#PutanjaDoFajla, #Destinacija)#ukoliko treba da se izmesti ceo direktorijum ili fajl. NE POSTOJI opcija za preimenovanje fajlova, vec se koristi MOVE()funkcija)

sh.copytree("C:\\users\\boogyman\\Desktop\\VBA\\", "C:\\NEWFOLDEREEE")
