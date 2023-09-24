import requests

odgovor = requests.get("https://automatetheboringstuff.com/files/rj.txt")
if odgovor.status_code == 200:
    print("Dokument je uspesno preuzet")
else:
    print("Dokument nije uspesno preuzet")
#otvaranje fajla za snimanje
fajlCuvanje = open('Romeo.txt', 'wb')

#snimanje koristeci iteracije
for i in odgovor.iter_content(100000):
    fajlCuvanje.write(i)
#zatvaranje fajla
fajlCuvanje.close()

