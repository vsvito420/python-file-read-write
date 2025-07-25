def verschluesseln(text, schritt):
    geheimtext = ""
    for buchstabe in text:
        if buchstabe.isalpha():
            verschoben = ord(buchstabe) + schritt
            if buchstabe.islower():
                if verschoben > ord('z'):
                    verschoben -= 26
                geheimtext += chr(verschoben)
            elif buchstabe.isupper():
                if verschoben > ord('Z'):
                    verschoben -= 26
                geheimtext += chr(verschoben)
        else:
            geheimtext += buchstabe
    return geheimtext


def entschluesseln(text, schritt):
    return verschluesseln(text, -schritt)


# Schritt für die Caesar-Verschlüsselung
schritt = 3

# Klartext aus Datei lesen
with open('klartext.txt', 'r', encoding='utf-8') as datei:
    nachricht = datei.read()

# Verschlüsseln und in Datei schreiben
geheim = verschluesseln(nachricht, schritt)
with open('geheimtext.txt', 'w', encoding='utf-8') as datei:
    datei.write(geheim)

# Geheimtext aus Datei lesen
with open('geheimtext.txt', 'r', encoding='utf-8') as datei:
    geheimtext = datei.read()

# Entschlüsseln und in Datei schreiben
klar = entschluesseln(geheimtext, schritt)
with open('entschluesselt.txt', 'w', encoding='utf-8') as datei:
    datei.write(klar)

# Optional: Ausgabe zur Kontrolle
print("Geheim:", geheim)
print("Klartext:", klar)
