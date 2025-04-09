from time import sleep
import os

timer = 5


while timer > 0:
    os.system("cls")
    print(f"{timer}")
    timer -= 1
    sleep(1)
    if timer == 0:
        print("tiden är ute")








