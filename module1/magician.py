secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

user_word = int(input())

test = "Entrer" 

while test == "Entrer" :

    if user_word != secret_number :

        print("Ha ha! Vous êtes coincé dans ma boucle!")
        
        user_word = int(input())

        continue

    else :

        print(user_word)
        print("Bien joué, moldu! Vous êtes libre maintenant.")
        
        break


