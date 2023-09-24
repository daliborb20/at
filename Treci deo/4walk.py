import os as walk
fajl = open("folderi.txt", "w", encoding="utf-8" )

for folderName, subFolders, FileNames in walk.walk("c:\\users\\boogyman\\"):
    fajl.write(folderName)

fajl.close()
