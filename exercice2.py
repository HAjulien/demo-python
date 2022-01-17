
# n = int(input("quel est la racine carré de ce nombre: "))
# nMin = n - 0.001
# nMax = n + 0.001
# a= n/2
# resultat= a*a

# #Ne marche pas
# while nMin > resultat or resultat > nMax:
#     if resultat > nMax:
#         a = (a/2)
#         resultat= a*a
#     elif resultat < nMin:
#         a= ((a + (a/2))/2)
#         resultat= a*a
# else:
#     print("le resultat est " + str(resultat))




# 

n = int(input('Entrez un nombre entier : '))

intervalle = .001
NBas = 0
NHaut = n

while NHaut - NBas > intervalle:
    valeur = (NHaut + NBas)/2
    print("On test la valeur", valeur)
    Nombre = valeur * valeur
    if Nombre > n :
        print(valeur, "x", valeur, "=", Nombre, ".Le résultat est", Nombre, " est supérieux à ", n)
        NHaut = valeur
    else :
        print(valeur, "x", valeur, "=", Nombre, ".Le résultat est", Nombre, " est inférieur à ", n)
        NBas = valeur

print("Donc le nombre recherché est donc compris entre ", NBas, "et ", NHaut)