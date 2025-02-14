import datetime
now=datetime.datetime.now()
annee_now=now.year

print ("Bonjour")
nom1=input ("Comment t'appelles tu ?")
annee1=input ("Et en quelle année es-tu né(e)?")

nom2=input ("Quel est le nom de ta voisinne/ton voisin?")
annee2=input ("Et en quelle année est-elle (il) né(e)?")

annee1=int (annee1)
age1=now.year-annee1

annee2=int (annee2)
age2=now.year-annee2

print(nom1,"a",age1,"ans")
print(nom2,"a",age2,"ans")

if age1>age2:
  difference=age1-age2
  print(nom1,"est plus agé que",nom2)
  print(nom1,"a",difference,"années de plus que",nom2)
elif age1<age2:
   difference=age2-age1
  print(nom2,"est plus agé que",nom1)
  print(nom2,"a",difference,"années de plus que",nom1)
elif age1==age2:
  print(nom1,"et",nom2,"ont le même age.")
else:
  print("MAIS T BÊTE OU QUOI TU REFLECHIS COMME JOSUE")
