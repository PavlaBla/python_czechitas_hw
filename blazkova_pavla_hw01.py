# Zadani:Napište skript, který přečte obsah souboru alice.txt a pomocí slovníku v něm 
# spočítá četnost jednotlivých znaků. 
# Tento slovník poté uloží do JSON souboru hw01_output.json.

import json

with open("alice.txt", encoding="utf-8") as file:
    text = file.read()

# nacte soubor do promenne text

text = text.lower()
text = text.replace(' ', '')
text = text.replace('\n', '')

# zmensi velka pismena a zbavi nas nepotrebnych znaku

frekvence_znaku = {}

for znak in text:
    if znak in frekvence_znaku:
        frekvence_znaku[znak] += 1
    else:
        frekvence_znaku[znak] = 1

# vytvori seznam znaku a spocita jejich cetnost

serazene_polozky = sorted(frekvence_znaku.items())

# seradi polozky podle klice (znak), vytvori seznam n-tic

serazene_polozky = dict(serazene_polozky)

# seznam prevede na slovnik

with open('hw01_output.json.', mode='w', encoding='utf-8') as file:
    json.dump(serazene_polozky, file, ensure_ascii=False, indent=4)

# vysledny slovnik prevede do JSON souboru