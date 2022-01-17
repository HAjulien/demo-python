#   EXERCICE 1


print("Veuillez donner 3 nombres  entre 0 et 40 000.")


nombre1= int(input("a:"))
nombre2= int(input("b:"))
nombre3= int(input("c:"))
resultat= (nombre2 + nombre1 + nombre3)/3


if  nombre1 > 40000 or 0 > nombre1:
    print("le nombre 1 est incorrect.")
elif  nombre2 > 40000 or 0 > nombre1:
    print("le nombre 2 est incorrect.")
elif  nombre3 > 40000 or 0 > nombre1:
    print("le nombre 3 est incorrect.")

else :
    print("la moyenne de vos 3 nombres est : " + str(resultat))



# EXERCICE 2

print("Veuillez donner un nombre entier.")

nombre4= int(input("d:"))

if nombre4 >= 0:
    print("le nombre est positif ou nul.")
else :
    print("le nombre est négatif.")



# EXERCICE 3

print("Veuillez donner un nombre entier pour voir si on peut le diviser par 3.")

nombre5= int(input("e:"))
resultat2= nombre5 % 3

if resultat2 != 0:
    print("le nombre " +str(nombre5)+ " n'est pas divisible par 3.")
else :
    print( str(nombre5) + " est divisible par 3.")