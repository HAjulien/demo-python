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
nombre = 7
nombre = int(input("la table de multuplication que vous voulez voir: "))
print("Voici la table de multiplication de ", nombre)
for x in range(0,11):   #exclu le 11 mais inclu le 0
    print(x, "x ", nombre, "= ", x*nombre )
