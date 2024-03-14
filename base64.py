def InitTableBase64():
    tableBase64=[]
    for i in range(26):
        tableBase64.append(chr(65+i))#A à Z
    for i in range(26):
        tableBase64.append(chr(97+i))#a à z
    for i in range(10):
        tableBase64.append(chr(48+i))#0 à 9
    tableBase64.append('+')
    tableBase64.append('/')
    return tableBase64

def AfficherTableBase64(tableBase64):
    for i in range(64):
        print(i,":",tableBase64[i])
        
def Coder3octets(entree,tableBase64):
    sortie=""
    sortie+=tableBase64[entree[0]>>2]
    sortie+=tableBase64[((entree[0]&0x03)<<4)+(entree[1]>>4)]
    sortie+=tableBase64[((entree[1]&0x0F)<<2)+((entree[2]>>6)&0x03)]
    sortie+=tableBase64[entree[2]&0x3F]
    return sortie

def CoderBase64(liste,tableBase64):
    sortie=""
    reste=len(liste)%3
    i=0
    while i<len(liste)-reste:
        entree=[liste[i],liste[i+1],liste[i+2]]
        sortie+=Coder3octets(entree,tableBase64)
        i+=3
    if reste==1:
        entree=[liste[i],0,0]
        sortie+=Coder3octets(entree,tableBase64)
        sortie=sortie[:-2] 
        sortie+="=="
    if reste==2:
        entree=[liste[i],liste[i+1],0]
        sortie+=Coder3octets(entree,tableBase64)
        sortie=sortie[:-1]
        sortie+="="
    return sortie

def TexteVersHex(leTexte):
    leTableau=[]
    for i in range(len(leTexte)):
        leTableau.append(ord(leTexte[i]))
        return leTableau
with open("pot_fleur.jpg","rb") as f:
    contenu= f.read()
    
tableBase64 = InitTableBase64()
Vraihome=CoderBase64(contenu, tableBase64)
#print(Vraihome)
with open("text.txt","w") as my_file:
    my_file.write(Vraihome)
        