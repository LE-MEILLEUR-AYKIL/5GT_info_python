from math import pi

def menu():
  print("Bienvenu dans ce programme de calcul d'aire")
  print("Pour calculer l'aire d'un triangle tapez 1")
  print("Pour calculer l'aire d'un carré tapez 2")
  print("Pour calculer l'aire d'un rectangle tapez 3")
  print("Pour calculer l'aire d'un cercle tapez 4")
  print("Pour quitter tapez 5")

  choix=input("Quel est votre choix ?")
  choix=int(choix)

  if choix==1:
    triangle()

  elif choix==2:
    carre()

  elif choix==3:
    rectangle()

  elif choix==4:
    cercle()

  elif choix==5:
    quit()

  else:
    print("Tu le fais exprès où quoi ?")

def triangle():
  base=input("Que vaut la base ?")
  base=float(base)
  hauteur=input("Que vaut la hauteur ?")
  hauteur=float(hauteur)
  aire=base*hauteur/2
  print("L'aire du triangle vaut :",round(aire,3))
  print()
  menu()

def carre():
  cote=input("Que vaut le coté ?")
  cote=float(cote)
  aire=cote**2
  print("L'aire du carre vaut:",round(aire,3))
  print()
  menu()

def cercle():
  rayon=input("Que vaut le rayon ?")
  rayon=float(rayon)
  aire=pi*rayon**2
  print("L'aire du cercle vaut:",round(aire,3))
  print()
  menu()

def quit():
  print("Au revoir !")


if __name__=="__main__":
  menu()
