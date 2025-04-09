import datetime
import os
import time

# os.system("cls")
# x = datetime.datetime.now()

# print(x)


# while True:
#     os.system("cls")  
#     x = datetime.datetime.now()
#     print(x)
#     time.sleep(1)


import os
import time


start_t = time.time()



while True:
    os.system('cls')
    current_t = time.time()

    elapsed_t = current_t - start_t

    if elapsed_t < 0:
        elapsed_t = 0
    
    elapsed_t_tuple = time.localtime(elapsed_t)

    elapsed_t_formatted = time.strftime("%M:%S", elapsed_t_tuple)
    
    print("Nuvarande tid", elapsed_t_formatted)
    
    time.sleep(1)


