from msvcrt import getwch
import os
from colors import bcolors


os.system("cls")


print(bcolors.PURPLE+"hello world!"+bcolors.DEFAULT)
variable = getwch()

if variable == "q":
    print(bcolors.CYAN+"hello"+bcolors.DEFAULT)

print (bcolors.BLUE+"Hello"+bcolors.DEFAULT)

print (bcolors.PURPLE+"Hello"+bcolors.DEFAULT)

print (bcolors.GREEN+"Hello"+bcolors.DEFAULT)





