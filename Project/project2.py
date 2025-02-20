'''
FILNAMN.PY: Bästa bilmärken

__author__  = "Alexander Pintér"
__version__ = "1.0.0"
__email__   = "Alexander.pinter@elev.ga.ntig.se"
'''


import os 

cars = []  # Tom lista

def add(x): # Definierar funktionen add
    cars.append(x) # sätter in ditt värde i listan

def change():
    try:
        index = int(input(f"Vilken vill du ändra? Börjar från 1 - {len(cars)}: ")) # välj vilket index du vill ändra
        newcar = input("Vad vill du ändra det till? ") # ger newcar ett nytt värde
        cars[index - 1] = newcar  # Uppdaterar listan med det nya bilmärket
    except: 
        print("Skriv med siffror när du väljer position, och med bokstäver när du byter namn") #medelandet den ger när du skrivit fel

def remove(): # Definierar funktionen remove
    try:
        index = int(input(f"Vilken vill du ta bort? Börjar från 1 - {len(cars)}: ")) # välj vilket index du vill ta bort
        cars.pop(index - 1) # tar bort bilmärket på indexen du valt
    except:
        print("Svara med siffror") # medelandet den ger när du skrivit fel

while True: #öppnar huvudlopen
    os.system("cls")  # rensar skärmnen varje gån loopen loopar
    print("-" * 40)
    print("-" * 9, "BÄSTA BILMÄRKERNA", "-" * 12) #titl
    print("-" * 40, "\n")

    if cars: #startar if loopen för att numrera listan
        i = 1 #gör att den börjar på 1
        for car in cars: #kallar på värdet
            print(f"{i}). {car}") # det är såhär den printar ut
            i += 1 #så att den ökar nummret med 1 för varje värde i listan
    else:
        print("Listan är tom.") # skriver att listan är tom om det inte fimms ett värde i den

    print("\n""1. Lägg till en bil")      #den skriver ut olika valen man har
    print("2. Ändra en existerande bil")   #den skriver ut olika valen man har
    print("3. Ta bort en existerande bil")  #den skriver ut olika valen man har
    print("Ifall du vill avsluta tryck på 'q'")   #den skriver ut olika valen man har
    choice = input("Vad vill du göra 1-3? ") #deklarerar choice som en variabel och ber var du vill göra

    if choice == '1': #aktiverar detta om du har valt 1
        x = input("Vilket bilmärke är det du vill lägga till? ") # ber om vad du vill lägga in i listan
        add(x) #tillkallar funktionen igen och lägger in värdet i den.
    elif choice == '2': #aktiverar detta om du har valt 2
        change() #tillkallar change funktionen och sedan tar den över och ser till att det görs
    elif choice == '3': #aktiverar detta om du har valt 3
        remove() #tillkallar remove funktionen och sedan tar den över och ser till att det görs
    elif choice.lower() == 'q': #aktiverar detta om du har valt q
        break #lämnar programmet
    else:
        print("Det är mellan 1-3 eller 'q' om du vill lämna") #skriver ut det här om du skrivit något annat.

