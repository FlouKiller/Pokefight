from classes import Dresseur, Pokemon

print("Test dresseur...")
dresseur = Dresseur("Dresseur")
assert dresseur.nom == "Dresseur"
dresseur.setPotion(10)
assert dresseur.potions == 10
print("Test dresseur Ok")

print("Test Pokémon...")
pokemon = Pokemon("Pokémon", "feu", 50, 30, 5)
assert pokemon.pv == 30
pokemon.setPv(15)
assert pokemon.pv == 15 and pokemon.pvmax == 30
print("Test Pokémon OK")

print("Autre tests dresseur...")
dresseur.addPokemon(pokemon)
assert len(dresseur.listePokemon) != 0
assert pokemon.dresseur == dresseur
print("Autre tests dresseur OK")

print("Test combat...")
pokemon2 = Pokemon("Pokémon 2", "eau", 50, 30, 5)
pokemon.attack(pokemon2)
assert pokemon2.pv < pokemon2.pvmax
print("Test combat OK")

print("Test forces/faiblesses...")
assert pokemon.forces == ["plante", "glace", "insecte"]
assert pokemon.faiblesses == ["feu", "eau", "roche"]
assert pokemon2.forces == ["feu", "sol", "roche"]
assert pokemon2.faiblesses == ["eau", "plante", "dragon"]
print("Test forces/faiblesses OK")

print("Tous les tests sont OK")
input("Appuyez sur entré pour quitter")