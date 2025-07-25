# Dokumentation: Dateien lesen, schreiben und anhängen in Python

## dateien_lesen.py
Dieses Skript liest den gesamten Inhalt einer Datei (`dateiname.txt`) und gibt ihn auf der Konsole aus.
- Modus `'r'`: Datei wird zum Lesen geöffnet.
- Beispiel:
  ```python
  with open('dateiname.txt', 'r', encoding='utf-8') as datei:
      inhalt = datei.read()
      print(inhalt)
  ```

## dateien_schreiben.py
Dieses Skript schreibt Text in eine Datei (`dateiname.txt`). Existierende Inhalte werden überschrieben.
- Modus `'w'`: Datei wird zum Schreiben geöffnet, vorhandener Inhalt wird gelöscht.
- Beispiel:
  ```python
  with open('dateiname.txt', 'w', encoding='utf-8') as datei:
      datei.write('test\n')
      datei.write('Dies ist eine Testdatei.\n')
  ```

## dateien_hinzufuegen.py
Dieses Skript fügt eine weitere Zeile am Ende der Datei (`dateiname.txt`) hinzu.
> Hinweis `'a'` steht für "append" (englisch für "anhängen")
- Modus `'a'`: Datei wird zum Anhängen geöffnet, neuer Text wird am Ende hinzugefügt.
- Beispiel:
  ```python
  with open('dateiname.txt', 'a', encoding='utf-8') as datei:
      datei.write('Dies ist eine weitere Zeile.\n')
  ```

## Hinweise
- Der Dateiname kann beliebig angepasst werden.
- Die Kodierung `utf-8` sorgt für die richtige Darstellung von Umlauten und Sonderzeichen.
- Mit `with open(...)` wird die Datei nach der Bearbeitung automatisch geschlossen.
