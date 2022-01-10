# i = 0
# while i < 10:
#     i += 1
#     if i%2 == 0:   # si i est paire
#         continue
#     print(i)

a = int(input("a:"))   #reponse utilisateur toujours en chaine caractere
b = int(input("b:"))

# a, b = b, a

while b !=0:
    a, b=b, a%b
print(a)
print(b)

