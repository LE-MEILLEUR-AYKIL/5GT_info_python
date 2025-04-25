import random

nombre1=random.randint(-100000000000000,100000000000000000)
nombre2=random.randint(-100000000000000,100000000000000000)
somme= nombre1 + nombre2
question="Que vaut la somme de "+str(nombre1)+" et "+str(nombre2)+"?"
reponse= input(question)

valid=0

while valid==0:
  try:
    reponse=int(reponse)
    valid=1
  except:
   print("Votre réponse n'est pas un nombre entier.")
   reponse=input("Quelle est votre réponse")
  
reponse=int(reponse)

if reponse== somme:
   print("Vous êtes bon")
elif reponse!=somme:
   print("T'es con ou quoi on dirait Lilya")
   print("Recommence trdc")