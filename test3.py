def affiche_menu():   #mot clé def est fonction
    print("Menu : ")
    print("*Action 1 : ")
    print("*Action 2 : ")

affiche_menu()

affiche_menu()

affiche_menu()  #appelle à la fonction

def dire(texte):   #argument decrit précisement pour clarté
    print('# ' +texte)

dire("Bonjour")  #affecte fonction dire grâce paramètre
dire("Au revoir")   #peut dire plusieurs chose en fonction argument
dire("A demain")

def addition(a, b):
    return a + b   #addition grâce return et +

somme = addition(4, 1)
print(somme)

def saluer(nom = 'visiteur'):  #valeur par defaut
    print("Bonjour " + nom)

saluer('Clem')
saluer()
