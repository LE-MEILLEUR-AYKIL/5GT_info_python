print("Bienvenue dans notre restaurant!")

print("Pour un hamburger, tapez 1.")
print("Pour une pizza, tapez 2.")
print("Pour une salade, tapez 3.")

choix=input("Votre choix est")

choix=int(choix)

while choix not in (1,2,3):
  print("Veuillez choisir 1, 2, ou 3")
  choix=input("Votre choix est")
  choix=int(choix)

if choix==1:
  print("Vous avez choisi un hamburger")

elif choix==2:
  print("Vous avez choisi une pizza")

elif choix==3:
  print("Vous avez choisi une salade")

else:
  print("Choisis un des plats bouffon.")

print("Mange bien, j'espère que tu t'étouffes")