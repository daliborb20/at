import traceback
import logging #modul za log -> umesto print funkcije


logging.basicConfig(filename='logging.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def boxPrint(simbol, sirina, visina):
    if len(simbol)!= 1:
        raise Exception('Simbol mora biti jedank 1 karakteru') #Prekida izvrsenje programa u slucaju da je unet vise od jednog karaktera
    print(simbol * sirina )
    for i in range(visina - 2):
        print(simbol + (' ' * (sirina-2)) + simbol)

    print(simbol * sirina)

boxPrint("#", 15,4)


try:
    raise Exception("Ovo je poruka")
except:
    errorFile = open('errorLog.txt', 'a', )
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print("Podaci o gresci su upisani u log fajl")


######################################logging
logging.debug('Pocetak programa')



def factorial(n):
    logging.debug('Pocetak fakorijala (%s)'%  (n))
    total = 1
    for i in range(n + 1):
        total *=1
        logging.debug('i is  %s, total is  %s' %(i, total))
        return total


logging.debug("Kraj programa")

print(factorial(5))
