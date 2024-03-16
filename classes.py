from random import randint

class Dresseur:
  """
  Class Dresseur
  Attributs : nom (str)
  Sert a créer un dresseur et à stocker des potiosn et ses Pokémon
  Lui ajouter/Supprimer des Pokémon
  """

  def __init__(self, nom):
    self.nom = nom
    self.listePokemon = []
    #Chaque dresseurs possèdent un nombre de potions aléatoire (entre 3 et 5)
    pot = randint(3, 5)
    self.potions = pot
    #Nombre de potions maximum possédés par le dresseur
    #sert à faire un affichage du style : x/y ou x est le nombre de potions actuellement possédés par le dresseur et y est le nombre de potions que le dresseur avait lors de sa création
    self.potionsmax = pot
  
  #Ajouter un pokémon a l'équipe du dresseur
  def addPokemon(self, pokemon):
    self.listePokemon.append(pokemon)
    pokemon.dresseur = self

  #Retirer un pokémon de l'équipe du dresseur
  def removePokemon(self, pokemon):
    self.listePokemon.remove(pokemon)
    #Définir le dresseur du Pokémon sur None (car il n'en a plus)
    pokemon.dresseur = None
  
  #Changer le nombre de potion d'un dresseur
  def setPotion(self, amount):
    self.potions = amount


class Pokemon:
  """
  Class Pokemon
  Attributs : nom (str), type (str), niveau (int), pv (int), pa (int)
  Sert a créer un Pokémon avec un nom, un type, un niveau, des points de vie et des points d'attaque
  Contient une méthode permettant d'attaquer un autre Pokémon
  """

  def __init__(self, nom, type, niveau, pv, pa):
    self.nom = nom
    self.type = type
    self.niveau = niveau
    self.pv = pv
    self.pa = pa
    
    #Les forces et les faiblesses dépendent du type du Pokémon
    self.forces = []
    self.faiblesses = []
    #caracteristiques() définissent les forces et faiblesses en fonction du type
    self.caracteristiques()
    #Par défaut, le pokémon n'appartient à personne
    self.dresseur = None
    self.pvmax = pv
  

  #Changer le nombre de pv d'un pokemon
  def setPv(self, pv):
    self.pv = pv
    if self.pv >= self.pvmax:
      self.pv = self.pvmax
    #Si jamais le nombre de pv est inférieur à 0, on le définit sur 0 pour éviter qu'il soit négatif
    if self.pv < 0:
      self.pv = 0
  

  #Vérifier si un pokémon est vivant ou non
  def isAlive(self):
    return self.pv > 0
  

  #Récupérer les pv max d'un pokemon
  def pvMax(self):
    return self.pv == self.pvmax
  

  #Attaquer un autre Pokémon
  def attack(self, target):
    degats = self.pa
    #Dégats x2 si le pokémon est fort contre sa cible
    if target.type in self.forces:
      degats = degats*2
      #Dégats /2 si le pokémon est faible contre sa cible
    elif target.type in self.faiblesses:
      degats = degats/2
    
    #Multiplier le nobmre de dégats par un nombre aléatoire entre 0.85 et 1 pour rajouter un caractère aléatoire au jeu
    target.setPv(target.pv - int(degats * (randint(85, 100)/100)))


  #Définir les caractéristiques (forces et faiblesses en fonction du type)
  def caracteristiques(self):
    if self.type == "normal":
      self.faiblesses.append("roche")

    elif self.type == "feu":
      self.forces.append("plante")
      self.forces.append("glace")
      self.forces.append("insecte")
      self.faiblesses.append("feu")
      self.faiblesses.append("eau")
      self.faiblesses.append("roche")

    elif self.type == "eau":
      self.forces.append("feu")
      self.forces.append("sol")
      self.forces.append("roche")
      self.faiblesses.append("eau")
      self.faiblesses.append("plante")
      self.faiblesses.append("dragon")

    elif self.type == "plante":
      self.forces.append("eau")
      self.forces.append("sol")
      self.forces.append("roche")
      self.faiblesses.append("feu")
      self.faiblesses.append("plante")
      self.faiblesses.append("poison")
      self.faiblesses.append("vol")
      self.faiblesses.append("insecte")
      self.faiblesses.append("dragon")

    elif self.type == "electrique":
      self.forces.append("eau")
      self.forces.append("vol")
      self.faiblesses.append("plante")
      self.faiblesses.append("electrique")
      self.faiblesses.append("dragon")

    elif self.type == "glace":
      self.forces.append("plante")
      self.forces.append("sol")
      self.forces.append("vol")
      self.forces.append("dragon")
      self.faiblesses.append("eau")
      self.faiblesses.append("glace")

    elif self.type == "combat":
      self.forces.append("normal")
      self.forces.append("glace")
      self.forces.append("roche")
      self.faiblesses.append("poison")
      self.faiblesses.append("vol")
      self.faiblesses.append("psy")
      self.faiblesses.append("insecte")

    elif self.type == "poison":
      self.forces.append("plante")
      self.forces.append("insecte")
      self.faiblesses.append("poison")
      self.faiblesses.append("sol")
      self.faiblesses.append("roche")
      self.faiblesses.append("spectre")

    elif self.type == "sol":
      self.forces.append("feu")
      self.forces.append("electrique")
      self.forces.append("poison")
      self.forces.append("roche")
      self.faiblesses.append("plante")
      self.faiblesses.append("insecte")

    elif self.type == "vol":
      self.forces.append("plante")
      self.forces.append("combat")
      self.forces.append("insecte")
      self.faiblesses.append("electrique")
      self.faiblesses.append("roche")

    elif self.type == "psy":
      self.forces.append("combat")
      self.forces.append("poison")
      self.faiblesses.append("psy")

    elif self.type == "insecte":
      self.forces.append("plante")
      self.forces.append("poison")
      self.forces.append("psy")
      self.faiblesses.append("feu")
      self.faiblesses.append("combat")
      self.faiblesses.append("vol")
      self.faiblesses.append("spectre")

    elif self.type == "roche":
      self.forces.append("feu")
      self.forces.append("glace")
      self.forces.append("vol")
      self.forces.append("insecte")
      self.faiblesses.append("combat")
      self.faiblesses.append("sol")

    elif self.type == "spectre":
      self.forces.append("spectre")

    elif self.type == "dragon":
      self.forces.append("dragon")