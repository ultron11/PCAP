unknown = int(input("Testez l'hypothese de Lothar Collatz avec : "))

if unknown > 1 : 

    c0 = unknown 

    while c0 > 1 :

        if c0 % 2 == 0 :

            c0 = (c0 / 2) 

            print(c0)

        elif c0 % 2 != 0 :

            c0 = 3 * c0 + 1

            print(c0)

else :

    print("La valeur est < 2")
