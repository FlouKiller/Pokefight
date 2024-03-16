from classes import Dresseur
from pokemons import pokemons_dispos
from random import randint

#Print du vide pour "nettoyer" l'écran et y voir plus clair entre chaque tours
def clear():
  for i in range(50):
    print()

#Affichage des noms et des pv dans un rectangle
def namesAndHP(pok1, pok2):
  result = "   Vous " + str(len(pok1.dresseur.listePokemon)) + "/3"
  result += "      Adversaire " + str(len(pok2.dresseur.listePokemon)) + "/3\n"
  result += "+=============+  +=============+\n"
  result += "| " + pok1.nom + ((11-len(pok1.nom))*" ") + " |  | " + pok2.nom + ((11-len(pok2.nom))*" ") + " |\n" 
  result += "| " + str(pok1.pv) + "/" + str(pok1.pvmax) + "       |  | " + str(pok2.pv) + "/" + str(pok2.pvmax) + "       |\n"
  result += "+=============+  +=============+"

  return result

#Création des dresseurs joueur et ordinateur
joueur = Dresseur("Joueur")
ordinateur = Dresseur("Odrinateur")

#Récupération des pokémons qui vont être proposés aux joueurs
pokemons_dispos = pokemons_dispos()

#Le joueur et l'odinateur choisissent tour à tour 3 pokémon chacun
choix_possibles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(3):
  clear()#Nettoyage de l'écran

  print("Pokémon disponibes :\n")

  for i in range(len(pokemons_dispos)):
    print(i+1, ":", pokemons_dispos[i].nom)
  
  #On demande un nombre à l'utilisateur et on vérifie qu'il est bien dans les choix proposés
  choix = int(input("\nSéléctionnez en un > "))
  #Si ce n'est pas le cas, on lui redemande jusqu'a ce que sa demande soit conforme
  while not choix in choix_possibles:
    choix = int(input("\nSéléctionnez en un > "))
  
  #On lui affiche le pokémon qu'il à choisit
  print("\nVous avez choisi", pokemons_dispos[choix-1].nom)
  joueur.addPokemon(pokemons_dispos[choix-1])
  del pokemons_dispos[choix-1]
  del choix_possibles[-1]

  #On simule un choix de l'ordinateur (qui est en réalité aléatoire)
  choix_ordi = randint(0, len(pokemons_dispos)-1)
  print("L'ordinateur choisit", pokemons_dispos[choix_ordi].nom, "\n")
  ordinateur.addPokemon(pokemons_dispos[choix_ordi])
  del pokemons_dispos[choix_ordi]
  del choix_possibles[-1]
  
  input("Appuyez sur entré pour continuer...")

#Boucle du jeu, s'arrête une fois que l'un des deux dresseurs n'ait plus aucun pokémon dans son équipe (lorsqu'un pokémon est vaincu, on le retire de l'équipe du dresseur)
while len(joueur.listePokemon) != 0 and len(ordinateur.listePokemon) != 0:
  clear()# Nettoyage de l'écran
  #On stocke le pokémon actuellement en combat des deux joueurs
  poke_actuel_joueur = joueur.listePokemon[0]
  poke_actuel_ordi = ordinateur.listePokemon[0]

  #On demande au joueur soit d'attaquer, soit d'utiliser une potion
  choix_possible = [1, 2, 3]
  print("C'est votre tour.\n")
  print(namesAndHP(poke_actuel_joueur, poke_actuel_ordi) + "\n")
  print("1 : Attaquer")
  #Proposer le choix numéro 2 (changer de pokémon) seulement si le joueur possède toujours + de 1 pokémon 
  if len(joueur.listePokemon) > 1:
    print("2 : Changer de Pokémon")
  else:
    #Sinon, ne pas proposer l'option et la supprimer des choix possibles
    choix_possible.remove(2)
  #Proposer le choix numéro 3 (utiliser potion) seulement s'il reste des potions au joueur
  if joueur.potions > 0:
    print("3 : Utiliser potion", str(joueur.potions) + "/" + str(joueur.potionsmax))
  else:
    #Sinon, ne pas proposer l'option et la supprimer des choix possibles
    choix_possible.remove(3)
  choix = int(input("\nQue voulez vous faire > "))
  while choix not in choix_possible:
    choix = int(input("\nQue voulez vous faire > "))

  #S'il choisit d'attaquer, on execute les instructions necessaires
  if choix == 1:
    clear() #Nettoyage de l'écran
    pv_avant_attaque = poke_actuel_ordi.pv
    #Lancement de l'attaque avec la méthode prévue à cet effet
    poke_actuel_joueur.attack(poke_actuel_ordi)
    print(namesAndHP(poke_actuel_joueur, poke_actuel_ordi))
    print("\nVous avez attaqué", poke_actuel_ordi.nom, "en lui infligeant", pv_avant_attaque - poke_actuel_ordi.pv, "dégats\n")

    #Si le pokemon de l'adversaire n'a plus de vie, il est éliminé et est retiré de la liste de pokémon du dresseur
    if not poke_actuel_ordi.isAlive():
      print(poke_actuel_ordi.nom, "a été vaincu.\n")
      ordinateur.removePokemon(poke_actuel_ordi)
      #Si le dresseur ennemi n'a plus aucun pokémon, inutile de continuer
      if len(ordinateur.listePokemon) != 0:
        poke_actuel_ordi = ordinateur.listePokemon[0]
      else:
        #On met donc fin à la boucle sans se préoccuper de la suite
        break
  
  #Si le joueur choisit l'échange de pokémon, on lui demande contre lequel il veut faire son échange
  elif choix == 2:
    sous_choix_possibles = []
    clear() #Nettoyage de l'écran
    print("Changement de Pokémon\n")
    #Afficher les pokémons contre lesquels il peut faire l'échange (il s'agit des autres pokémons de son équipe)
    print("Échanger", poke_actuel_joueur.nom, "(" + str(poke_actuel_joueur.pv) + "/" + str(poke_actuel_joueur.pvmax) + ") contre :\n")
    pokemons = []
    for i in range(1, len(joueur.listePokemon)):
      pok = joueur.listePokemon[i]
      pokemons.append(pok)
      sous_choix_possibles.append(i)
      print(str(i) + " : " + pok.nom + " (" + str(pok.pv) + "/" + str(pok.pvmax) + ")")
    print()
    sous_choix = int(input("Que voulez vous faire > "))
    while sous_choix not in sous_choix_possibles:
      sous_choix = int(input("Que voulez vous faire > "))
    #Faire le swap dans la liste
    joueur.listePokemon[0], joueur.listePokemon[sous_choix] = joueur.listePokemon[sous_choix], joueur.listePokemon[0]
    print("\nVous avez échangé", poke_actuel_joueur.nom, "contre", joueur.listePokemon[0].nom + "\n")
    poke_actuel_joueur = joueur.listePokemon[0]
    
  #Si le joueur choisit d'utiliser une potion, on soigne son pokémon actuel
  elif choix == 3:
    clear() #Nettoyage de l'écran
    
    #(cette condition de devrait normalement pas s'éxécuter grâce à la protection juste en haut)
    if joueur.potions == 0:
      print("\nVous n'avez plus de potions.")
    else:
      #On retire une potion au dresseur qui l'utilise
      joueur.setPotion(joueur.potions - 1)
      #Et on rajoute 20 pv au pokémon courant
      poke_actuel_joueur.setPv(poke_actuel_joueur.pv + 20)
      print(namesAndHP(poke_actuel_joueur, poke_actuel_ordi))
      print("\nVous avez utilisé 1 potion pour soigner", poke_actuel_joueur.nom)
      print(poke_actuel_joueur.nom, "a maintenant", poke_actuel_joueur.pv, "points de vie et il vous reste", joueur.potions, "potions.\n")
  
  #Mettre une "pause" à la boucle
  input("Appuyez sur entré pour continuer...")
  clear() #Nettoyage de l'écran

  print("C'est le tour de l'adversaire.\n")
  #Si l'ordinateur n'a plus de potions, alors son choix sera forcément l'attaque
  if ordinateur.potions == 0:
    choix_adversaire = 1
  #Si le pokémon adverse à ses pv max, alors son choix sera forcément l'attaque
  elif poke_actuel_ordi.pv == poke_actuel_ordi.pvmax:
    choix_adversaire = 1
  else:
    #Sinon, son choix sera fait aléatoirement
    choix_adversaire = randint(1, 100)

  #70% de chances d'attaquer et 30% de chances d'utiliser une potion
  if choix_adversaire <= 70:
    #Ici, l'attaque
    pv_avant_attaque = poke_actuel_joueur.pv
    poke_actuel_ordi.attack(poke_actuel_joueur)
    print(namesAndHP(poke_actuel_joueur, poke_actuel_ordi) + "\n")
    print("L'adversaire vous a attaqué avec", poke_actuel_ordi.nom, "en infligeant", pv_avant_attaque - poke_actuel_joueur.pv, "dégats à votre", poke_actuel_joueur.nom, "\n")

    if not poke_actuel_joueur.isAlive():
      print(poke_actuel_joueur.nom, "a été vaincu.\n")
      joueur.removePokemon(poke_actuel_joueur)
      if len(joueur.listePokemon) != 0:
        poke_actuel_joueur = joueur.listePokemon[0]
      else:
        break

  else:
    #Ici l'utilisation de potion
    ordinateur.setPotion(ordinateur.potions - 1)
    poke_actuel_ordi.setPv(poke_actuel_ordi.pv + 20)
    print(namesAndHP(poke_actuel_joueur, poke_actuel_ordi))
    print("\nL'adversaire à utilisé 1 potion pour soigner", poke_actuel_ordi.nom)
    print(poke_actuel_ordi.nom, "a maintenant", poke_actuel_ordi.pv, "points de vie et il reste", ordinateur.potions, "potions à l'adversaire.\n")
  
  #Mettre "pause" à la boucle
  input("Appuyez sur une entré pour continuer...")

#Vérifier qui a gagné en regardant qui a une liste de pokémon vide
if len(joueur.listePokemon) == 0:
  print("Vous avez perdu")
else:
  print("Vous avez gagné")

input("Appuyez sur entré pour quitter")