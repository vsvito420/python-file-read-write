# Dateien lesen

with open('dateiname.txt', 'r', encoding='utf-8') as datei:
    inhalt = datei.read()
    print(inhalt)
