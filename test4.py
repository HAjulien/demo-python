#LA PORTER DES VARIABLES

a = 42
def affichage():
    print(a)

affichage()

def change(valeur):
    global a  #redeffinir variable au niveau global même en dehors de la fonction
    a = valeur

print(a)

change(10)

affichage()