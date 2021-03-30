a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a :

    message = " C'est un triangle" 

    if a > b and a > c and a**2 == b**2 + c**2 :  

        print(message +" rectangle")

    elif b > c and b > a and b**2 == a**2 + c**2 :

        print(message +" rectangle")

    elif c > a and c > b and c**2 == a**2 + b**2 :

        print(message +" rectangle")

    else : 

        print(message +" non connu") 





