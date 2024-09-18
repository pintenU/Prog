import os
import math
import random
os.system("cls")

"""
baldur_online = True


while True:

    try:
        height = float(input("höjd: "))
        break
    except:
     print("skriv höjd i nummer")
     continue
    exit()

if baldur_online: #baldur_online == True
    
    if height >=  1.2 and height <= 1.99:
        print("Du får åka")
    if height < 1.2:
        print("Du får inte åka för att du är en dvärg, L bozo")
    elif height > 1.99:
        print("Du får inte åka för att du är för hög din lilla lyktstolpe")

else:
    print("Du kan inte åka pga Baldur är stängd")
"""




# 1) om baldur är (TRUE) och du är över 1,2 m kan du åka
# 2) man kan bara åka om man är mellan 1,2 och 1,99 m
# 3) se till att programmet är tydlig med att attraktionen är av och det är därför du inte får åka eller för att du är fel höjd


"""
name = input("Vad heter du?")

while True:   
    try:
        age = int(input("hur gammal är du?"))
        break 
    except:
        print("Write your age in numbers")
    continue 
    

print("Welcome", name, "you are", age,  "years old" )
"""




"""
while True:
    try:
        length = float(input("hur lång är du?"))
        break
    except:
        print("skriv längd i siffror som motsvarar meter")
    continue


while True:
    try:
        weight = float(input("hur mycket väger du?"))
        break
    except:
        print("skriv vikt i siffror som motsvarar kilo")
        continue

print("Ditt BMI är:", float(weight) / float(length)**2  )
"""

"""
r = float(input("Radie: "))


print(f"Din cirkels Area är: {math.pi * r ** 2:.3f}" )

"""

"""
print(random.randint(1, 6))

"""

"""
throws = int(input("How many throws do you wanna throw? "))

while throws > 0:
    print(random.randint (1, 6))
    throws -= 1
"""


