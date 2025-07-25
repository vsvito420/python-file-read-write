# Dateien bearbeiten: Anhängen oder Überschreiben
# 'a' fuer Anhängen, 'w' zum Überschreiben

with open('dateiname.txt', 'a', encoding='utf-8') as datei:
    datei.write('Dies ist eine weitere Zeile.\n')
    datei.write('Dies ist noch eine weitere Zeile.\n')
