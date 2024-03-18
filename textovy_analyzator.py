"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Martina Volrábová
email: Martina.volrabova@seznam.cz
discord: Martina Volrabova#!pdb1714

"""
text1 = '''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.'''

text2 = '''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.'''

text3 = '''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''


uzivatelskeJmenoHeslo = dict(bob='123', ann='pass123', mike='password123', liz='pass123')
texts = dict(t1 = text1, t2 = text2, t3 = text3)
oddelovac = "--------------------------------------------------------------------------------"

zadaneJmeno = input("Zadej uživatelské jméno: ")
zadaneHeslo = input("Zadej uživatelské heslo: ")

print(oddelovac)

# Kontrola, zda uživatel (jmeno + heslo) existuje v proměnné uzivatelskeJmenoHeslo
if zadaneJmeno in uzivatelskeJmenoHeslo and uzivatelskeJmenoHeslo[zadaneJmeno] == zadaneHeslo:
    # Pokud se jmeno a heslo shodují, nech uživatele analyzovat text
    print("Welcome to the app,bob. We have 3 texts to be analyzed. ")
    print(oddelovac)
# Pokud se jmeno a heslo neshodují, ukonči program
else:
    print("unregistered user, terminating the program..")
    exit()

# Zobraz uživateli nabízené texty:
print("Vyberte si z následujících variant textů určených k analýze:")
print(oddelovac)
print(f"Varianta 1: {texts['t1']}")
print(oddelovac)
print(f"Varianta 2: {texts['t2']}")
print(oddelovac)
print(f"Varianta 3: {texts['t3']}")
print(oddelovac)
# Uživatel si vybere jeden z textů, očekávaný vstup je int 1,2,3

vyberText = input("Zadejte variantu textu, kterou chcete analyzovat (1 ,2 ,3):")
if vyberText.isdigit() and vyberText == '1':
    print(f"Vybrali jste Variantu: {vyberText}")
    i = 't1'

elif vyberText.isdigit() and vyberText == '2':
    print(f"Vybrali jste Variantu: {vyberText}")
    i = 't2'

elif vyberText.isdigit() and vyberText == '3':
    print(f"Vybrali jste Variantu: {vyberText}")
    i = 't3'

else:
    print("Nebylo nebyla zadána správná varianta, ukončuji program.")
    exit ()


print(oddelovac)

# Počet slov
pocet_slov = len(texts[i].split())

# Počet slov začínajících velkým písmenem
pocet_slov_velka = sum(1 for word in texts[i].split() if word.istitle())

# Počet slov psaných velkými písmeny
pocet_slov_velkymi_pismeny = sum(1 for word in texts[i].split() if word.isupper() and word.isalpha())

# Počet slov psaných malými písmeny
pocet_slov_malymi_pismeny = sum(1 for word in texts[i].split() if word.islower())

# Počet čísel
pocet_cisel = sum(1 for word in texts[i].split() if word.isdigit())

# Suma všech čísel v textu
suma_cisel = sum(int(word) for word in texts[i].split() if word.isdigit())


print("Zde jsou statistiky vámi vybraného textu:")
print(f"Počet slov: {pocet_slov}")
print(f"Počet slov začínajících velkým písmenem: {pocet_slov_velka}")
print(f"Počet slov psaných velkými písmeny: {pocet_slov_velkymi_pismeny}")
print(f"Počet slov psaných malými písmeny: {pocet_slov_malymi_pismeny}")
print(f"Počet čísel: {pocet_cisel}")
print(f"Suma všech čísel v textu: {suma_cisel}")


# Rozdělíme text na slova a odstraníme nealfanumerické znaky
words = [word.strip(".,") for word in texts[i].split()]

# Vytvoříme slovník pro sledování četnosti délky slov
length_frequency = {}

# Projdeme slova a spočítáme délky
for word in words:
    length = len(word)
    if length in length_frequency:
        length_frequency[length] += 1
    else:
        length_frequency[length] = 1

# Seřadíme délky slov a vytiskneme graf
sorted_lengths = sorted(length_frequency.keys())
print("LEN | OCCURENCES | NR.")
for length in sorted_lengths:
    print(f"{length:3}| {'*' * length_frequency[length]} | {length_frequency[length]}")
