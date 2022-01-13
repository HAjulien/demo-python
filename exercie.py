
print("Veuillez donner 3 nombres comprit entre 0 et 40 000.")


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
