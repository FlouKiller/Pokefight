from classes import Pokemon
from random import randint

#Fonction qui va tirer au sort 10 pokémons et les proposer aux joueurs 
def pokemons_dispos():

  #On stockera ici les pokémons disponibles après les avoir crées
  pokemons_dispos = []

  florizarre = Pokemon("Florizarre", "plante", 100, 80, 20)
  dracaufeu = Pokemon("Dracaufeu", "feu", 100, 80, 20)
  tortank = Pokemon("Tortank", "eau", 100, 80, 20)
  papilusion = Pokemon("Papilusion", "insecte", 100, 80, 20)
  dardargnan = Pokemon("Dardargnan", "insecte", 100, 80, 20)
  roucarnage = Pokemon("Roucarnage", "normal", 100, 80, 20)
  rattatac = Pokemon("Rattatac", "normal", 100, 80, 20)
  rapasdepic = Pokemon("Rapasdepic", "normal", 100, 80, 20)
  arbok = Pokemon("Arbok", "poison", 100, 80, 20)
  raichu = Pokemon("Raichu", "electrique", 100, 80, 20)
  sablaireau = Pokemon("Sablaireau", "sol", 100, 80, 20)
  nidoqueen = Pokemon("Nidoqueen", "poison", 100, 80, 20)
  nidoking = Pokemon("Nidoking", "poison", 100, 80, 20)
  feunard = Pokemon("Feunard", "feu", 100, 80, 20)
  grodoudou = Pokemon("Grodoudou", "normal", 100, 80, 20)
  nosferalto = Pokemon("Nosferalto", "poison", 100, 80, 20)
  rafflesia = Pokemon("Rafflesia", "plante", 100, 80, 20)
  aeromite = Pokemon("Aéromite", "insecte", 100, 80, 20)
  triopikeur = Pokemon("Triopikeur", "sol", 100, 80, 20)
  persian = Pokemon("Persian", "normal", 100, 80, 20)

  #Ajoute des pokémons crées aux pokémon disponibles
  pokemons_dispos.append(florizarre)
  pokemons_dispos.append(dracaufeu)
  pokemons_dispos.append(tortank)
  pokemons_dispos.append(papilusion)
  pokemons_dispos.append(dardargnan)
  pokemons_dispos.append(roucarnage)
  pokemons_dispos.append(rattatac)
  pokemons_dispos.append(rapasdepic)
  pokemons_dispos.append(arbok)
  pokemons_dispos.append(raichu)
  pokemons_dispos.append(sablaireau)
  pokemons_dispos.append(nidoqueen)
  pokemons_dispos.append(nidoking)
  pokemons_dispos.append(feunard)
  pokemons_dispos.append(grodoudou)
  pokemons_dispos.append(nosferalto)
  pokemons_dispos.append(rafflesia)
  pokemons_dispos.append(aeromite)
  pokemons_dispos.append(triopikeur)
  pokemons_dispos.append(persian)

  #On stockera ici les pokémons qui seront retenus par le jeu pour être proposés aux joueurs
  pokemons_proposes = []

  #Choisis aléatoirement 10 pokémons et les renvoie au programme principal
  for i in range(10):
    random = randint(0, len(pokemons_dispos)-1)
    pokemons_proposes.append(pokemons_dispos[random])
    del pokemons_dispos[random]

  return pokemons_proposes