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


# Test
nachricht = "Hallo Welt"
schritt = 3

geheim = verschluesseln(nachricht, schritt)
klar = entschluesseln(geheim, schritt)

print("Geheim:", geheim)
print("Klartext:", klar)
