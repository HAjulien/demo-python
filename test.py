a = 7

# print(a + 3)

b = 3

# print( a + b)

# a = b + 1

# print (a)

#a += b  # operateur equivalent a = a + b  a*= b a/=b 
#print (a)

c = a//b
d = a%b
print('La division de ' +str(a)+ ' par ' +str(b)+ ' est égale à ' +str(c)+'.Il reste ' +str(d)+ '.' )
print(d)

chaine= 'Et voilà du texte'
chaine= 'nous l\'avons'
chaine2= "\"réparé\""
# print(chaine +" "+ chaine2)

#reponse= input()    #12une ligne vide apparaît et attend que l'utilisateur entre une info

age = int(input("quel est votre âge? "))  #transforme string en integrer pour par exemple fonction if age > 16

print("Vous avez " +str(age)+ " ans.")

if age > 16 and age < 100:
    print("Vous avez plus de 16 ans.")
# elif age < 0:      #elif est un if else
#     print("tu te moquerais pas de moi? ")
elif age > 100 or age < 0:      #elif est un if else
    print("tu te moquerais pas de moi? ")
else :
    print("Tu es encore trop jeune")

a = 3
print(type(a))

b = 8.2
print(type(b))

chaine = "Au revoir"
print(type(chaine))
vrai= True
print(type(vrai))

print(7 > 11 < 9 !=10)  # != différent
