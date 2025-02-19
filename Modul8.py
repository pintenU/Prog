
import os
os.system("cls")


# def number(x,y):
#     return x + y


# print(number(3,7))


# def my_name(fname):
#     print(fname + " " + "Pintér")


# my_name("Alexander")


# def multiply(x,y):
#     print (x*y)


# for i in range(10):
#     multiply(i,2)



# names_list = []

# def main():
#     while True:
#         print("\nNuvarande namn:", names_list)
#         print("1. Lägg till namn")
#         print("2. Ändra namn")
#         print("3. Ta bort namn")
        
#         choice = input("Välj vad du vill göra (1-3): ")

#         if choice == '1':
#             name = input("Skriv namnet du vill lägga till: ")
#             names_list.append(name)

#         elif choice == '2':
#             index = int(input("Skriv positionen av namnet du vill ändra (Börjar från 0): "))
#             if 0 <= index < len(names_list):
#                 new_name = input("Skriv det nya namnet: ")
#                 names_list[index] = new_name
#             else:
#                 print("Finns inget namn vid den positionen.")

#         elif choice == '3':
#             index = int(input("Skriv positionen på namnet du vill ta bort (Börjar från 0): "))
#             if 0 <= index < len(names_list):
#                 names_list.pop(index)
#             else:
#                 print("Finns inget namn vid den positionen.")

# if __name__ == "__main__":
#     main()




def main():
    while True:
        print("1. Addition")
        print("2. Subtraktion")
        print("3. Multiplikation")
        print("4. Division")

        def addition(x,y):
            return x+y
        
        def subtraktion(x,y):
            return x-y
        
        def multiplikation(x,y):
            return x*y
        
        def division(x,y):
            return x/y
        
        choice = input("Välj vad du vill göra (1-4): ")

        if choice == '1':
            x = float(input("Vilket är det första nummret du vill använda? "))
            y = float(input("Vilket är det andra nummret du vill använda? "))
            print(addition(x,y))
            try:
                break
            except:
                print("SKriv bara med tal")
                break

        elif choice == '2':
            x = float(input("Vilket är det första nummret du vill använda? "))
            y = float(input("Vilket är det andra nummret du vill använda? "))
            print(subtraktion(x,y))
            try:
                break
            except:
                print("SKriv bara med tal")
                break

        elif choice == '3':
            x = float(input("Vilket är det första nummret du vill använda? "))
            y = float(input("Vilket är det andra nummret du vill använda? "))
            print(multiplikation(x,y))
            try:
                break
            except:
                print("SKriv bara med tal")
                break
        
        elif choice == '4':
            x = float(input("Vilket är det första nummret du vill använda? "))
            y = float(input("Vilket är det andra nummret du vill använda? "))
            print(division(x,y))
            try:
                break
            except:
                print("SKriv bara med tal")
                break
        

if __name__ == "__main__":
    main()


