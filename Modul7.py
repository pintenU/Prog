
import os
os.system("cls")


# car = {
#     "brand": "Porsche",
#     "model": "Taycan",
#     "year": 2023
# }




cars = [                #car-list
{
    "brand" : "Porsche",
    "model" : "911",
    "year" : 2023
},
{
    "brand" : "Dodge",
    "model" : "Charger",
    "year" : 2007
},
{
    "brand" : "LAmbo",
    "model" : "Revvan",
    "year" : 2024
}
]

while True:
    for car in cars:
        brand = car["brand"]
        model = car["model"]
        year = car["year"]
        print(f"{brand}, {model}, {year}")

    brand = input("Vilket märke? ")
    model = input("Vilken modell? ")
    year = input("vilket år? ")

    cars.append(
        {
        "brand" : brand,
        "model" : model,
        "year" : year
}) 
    while True:
        totalcars = {len(cars) + 1}
        try:
            remove = int(input((f"Vill du ta bort en bil? du kan ta bort 1 till {totalcars}: ")))
            if remove != 0:
                cars.pop(remove - 1)
                break
            if remove == 0:
                break
        except:
            print(f"snälla använd nummer mellan 1 0ch {totalcars} ifall du vill ta bort någon eller 0 ifall du inte vill ta bort något")
    pos = (cars)
    while True:
        try:
            change = int(input((f"Vill du ändra en bil? du kan ändra bilarna mellan 1 och {totalcars}: ")))
            if change != 0:
                brand = input("Vilket märke? ")
                model = input("Vilken modell? ")
                year = input("vilket år? ")

                cars[change] = (
        {
                "brand" : brand,
                "model" : model,
                "year" : year
})
            
                break
            if change == 0:
                break
        except:
            print(f"snälla använd nummer mellan 1 0ch {totalcars} ifall du vill ändra någon bil eller 0 ifall du inte vill ändra något")
