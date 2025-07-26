def caesar_encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - start + key) % 26 + start)
        else:
            result += char
    return result


def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)


def save_to_file(filename, text, key):
    encrypted = caesar_encrypt(text, key)
    with open(filename, "a", encoding="utf-8") as file:
        file.write(encrypted + "\n")


def read_from_file(filename, key):
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
    for line in lines:
        decrypted = caesar_decrypt(line.strip(), key)
        print("Entschlüsselt:", decrypted)

# 🔁 Hauptprogramm


def main():
    key = 3
    filename = "geheim.log"

    print("Willkommen zum Caesar-Tool!\n")
    while True:
        action = input(
            "Möchtest du etwas (s)peichern, (l)esen oder (e)xit? ").lower()

        if action == "s":
            text = input("Gib einen geheimen Text ein: ")
            save_to_file(filename, text, key)
            print("Gespeichert!\n")
        elif action == "l":
            print("\nInhalt von geheim.log:")
            read_from_file(filename, key)
            print()
        elif action == "e":
            print("Tschüss!")
            break
        else:
            print("Ungültige Eingabe.\n")


# Start
main()
