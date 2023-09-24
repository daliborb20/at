sunka = "SSSSSSS"

if sunka.islower():
    print("malim slovima")
else:
    print("nije malim slovima")



####sve slova

if sunka.isalpha():
    print("Samo slova")

if sunka.isnumeric():
    print("Samo bojevi")


#########SPLITOVANJE

ime = "Moje ime je medvedic Lino, svakog dana donsem nesto fino"


print(ime.split())

novo = ime.ljust(200, "*")
print(novo)

####duga opcija je ljust
###treca opcija je center

novoNovo = ime.center(2, "-")

#####strip

####replace