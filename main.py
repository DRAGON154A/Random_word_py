import random
import os

#fonction qui prend  
Mots=["bonjour","mot","amene","cherche","prendre","reussir","joue","travaille","echec","travaille","moi"]
'''Ici nous utilison une liste pour que se soit plus facile au joueur de deviné 
pour norvions aussi utilisé les fichier pour que l'experiance soit plus aleatoi'''
choix_machine=random.choice(Mots) #choix du nombre par l'ordinateur
arg=list()#variable utilisé dans la boucle principale qui permet de stoché les informations saisit
tentative=10
#fonction affichage
def display(*args):
    tail=len(args) #variable pour stocké la taille 
    choix=str(args[0]) #variable qui contient la chaine choisit par l'ordinateur
    if (tail==0):
        return IndexError
    if (tail==1):
        for i in range(0,len(choix)):
            print("_ ",end="")
    if (tail>1):
        liste=[]
        for n in range(1,tail):
            liste.append(args[n])
        for i in range(0,len(choix)):
            if choix[i] in liste:
                print(choix[i],end="")
            else:
                print("_ ",end="")
            

#ecrivons une fonction qui vas nous permetre de savoir si l'utilisateur a gagné
def victoire(list1:list,list2):
    compt=0
    for i in list1:
        if i in set(list2):
            compt+=1
    if compt==len(list1):
        return True
    return False

#fonction pour déterminer si a trouve la lettre
def trouve(liste1,char):
    if char in liste1:
        return True
    return 0

arg.append(choix_machine)
display(choix_machine)

os.system("clear")
#Boucle principale
while victoire(choix_machine,set(arg))==False:
    lettre=str(input("\n Entre une lettre :"))#variable pour recupéré la saisit
    if trouve(choix_machine,lettre):
        arg.append(lettre)
    else:
        tentative-=1
    if tentative<=0:
        print("\n Le mot etais \""+choix_machine+"\"")
        break
    os.system("clear")
    display(*arg)

if victoire(choix_machine,set(arg)):
    print("\n$*************************** Felicitation **************************$")
else:
    print("\n$*************************** Echec ***************************$")