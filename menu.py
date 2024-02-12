from my_package_YB import find3

x = int(input("Menu: \n1. find1 \n2. find2 \n3. find3 \n4. Quitter \nVeuillez choisir une option (1-4) :"))

def start_find1():
    ...
def start_find2():
    ...
def start_find3():
    find3

if __name__ == "__main__":
    if x == 1:
        start_find1()
    elif x == 2:
        start_find2()
    elif x == 3 :
        start_find3()
    elif x == 4:
        exit()
    else:
        print("L'option choisie n'est pas valide, réessayez.")