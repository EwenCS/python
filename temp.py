"""
mot= input ("entre le mot a crypte")
clef="e"

clef_int = ord(clef)

mot_chiffre = ""

for i in range(len (mot)):
    char_int = ord (mot[i])
    char_chiffre = char_int ^ clef_int
    mot_chiffre += chr(char_chiffre)

print("Le mot chiffré est:", mot_chiffre)
"""

"""
mot= input ("entre le mot a crypte")
clef="e"

def chiffrement (message, cle):
    nouv_message = ""
    for k in range(len(message)):
        x = ord(message[k])
        y = ord(cle[k % len(cle)])
        z = x ^ y
        nouv_message += chr(z)
    return nouv_message
print(chiffrement(mot,clef))
"""  
"""
def crypter(mot,cle):
    motcrypte=""
    for i in range(len(mot)):
        motcrypte+=chr(ord(mot[i])^cle)
    return motcrypte

def decrypter(motcrypte,cle):
    mot=""
    for i in range(len(motcrypte)):
        mot+=chr(ord(motcrypte[i])^cle)
    return mot
def brutforce(motcrypte):
    for i in range(256):
        print(i,":",decrypter(motcrypte,i))
         
"""

def lire(nomFichier):
    with open(nomFichier, "r", encoding="utf-8")as fichier:
        chaine = fichier.read()
    return chaine

chaine = lire("c:/texte.txt")

cpt_Car = [0]*256
for k in range(len(chaine)):
    if ord(chaine[k]) <256:
        cpt_Car[ord(chaine[k])]+=1
        
for k in range(256):
    if cpt_Car[k]!=0:
        print(chr(k),cpt_Car[k])


        
        
