choix="o"
while choix in ["o"]:
  print("Bonjour")
  choix=input("Voulez vous continuer ?")
  while choix not in ["o","n"]:
    print("Veuillez choisir entre oui (o) et non (n)")
    choix=input("Voulez vous continuer ?")
print("Au revoir")    