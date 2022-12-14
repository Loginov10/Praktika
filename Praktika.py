from math import *
from random import *
a=int(input("sissesta arv: "))







try:
    a=int(input("sissesta arv: "))
    if a>0:
        print("Positiivne")
        if a%2==0:
            print(f"{a} on paaris")
        else:
            print(f"{a} on paaritu")
    else:
        print("Negatiivne")
except:
    print("Vale andmetüüp")

    