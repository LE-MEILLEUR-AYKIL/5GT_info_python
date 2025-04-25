def bonjour(nom):
  print("Bonjour")
  
  continuer=input("Est-ce que vous voulez continuer ?")

  valid=is_answer_valid(continuer)

  while not valid:
    print("Veuillez répondre par oui (o) ou non (n)")
    continuer=input("Est-ce que vous voulez continuer ?")
    valid=is_answer_valid(continuer)
  
  if continuer=="o":
    bonjour(nom)
  
  else:
    print("Au revoir")

def is_answer_valid(answer):
  if answer in ["o","n"]:
    valid= True
  else:
    valid= False
  return valid

bonjour("D'one")
  