# 🎮 Pokefight

A text-based Pokémon battle game developed in Python, inspired by the classic Pokémon universe.

## 📋 Description

Pokefight is a turn-based battle game where you face off against a computer-controlled opponent. Each player selects a team of 3 Pokémon from a list of 10 randomly available Pokémon, then battle until one of them has no valid Pokémon left.

## ✨ Features

- **Team Selection**: Choose 3 Pokémon from 10 randomly proposed options
- **Strategic Combat**: Strength/weakness system based on Pokémon types
- **Multiple Actions**:
  - Attack the opponent
  - Switch active Pokémon
  - Use potions to heal
- **Adaptive AI**: Computer makes intelligent decisions (70% attack, 30% heal)
- **Two Game Modes**:
  - **Text-based**: Classic terminal interface
  - **GUI**: Modern graphical interface with tkinter
- **Intuitive Interface**: Clear display of stats and options

## 🎯 Pokémon Types and Combat System

The game includes a complete type system with their strengths and weaknesses:

- **Fire**: Strong against Plant, Ice, Bug
- **Water**: Strong against Fire, Ground, Rock  
- **Plant**: Strong against Water, Ground, Rock
- **Electric**: Strong against Water, Flying
- **And many more...**

Damage is multiplied by 2 with type advantage, divided by 2 with type disadvantage.

## 🚀 Installation and Launch

### Prerequisites
- Python 3.x

### Installation
1. Clone or download this repository
2. Navigate to the project folder

### Launch the game

**Easy launcher (choose between text/GUI):**
```bash
python launcher.py
```

**Text-based version:**
```bash
python pokefight.py
```

**Graphical version (GUI):**
```bash
python pokefight_gui.py
```

### Tests
To verify the code is working properly:
```bash
python "fichier test.py"
```

## 📁 Project Structure

```
Pokefight/
├── launcher.py         # Game launcher (choose text/GUI)
├── pokefight.py        # Main game file (text-based)
├── pokefight_gui.py    # Graphical interface version
├── classes.py          # Trainer and Pokemon classes
├── pokemons.py         # List of available Pokémon
├── fichier test.py     # Unit tests
└── README.md           # This file
```

## 🎮 How to Play

1. **Selection Phase**: Choose 3 Pokémon from the 10 proposed
2. **Combat**: Each turn, you can:
   - **Attack**: Deal damage to the opponent
   - **Switch Pokémon**: Replace your current Pokémon (if you have others)
   - **Use a potion**: Restore 20 HP to your Pokémon (limited stock)
3. **Victory**: First to eliminate all opponent's Pokémon wins!

## 🔧 Technical Details

### Main Classes

#### `Dresseur` (Trainer)
- Manages the Pokémon team
- Has a potion stock (3-5 randomly)
- Methods to add/remove Pokémon

#### `Pokemon`
- Attributes: name, type, level, HP, attack points
- Strength/weakness system by type
- Attack and HP management methods

### Available Pokémon
The game includes 20 first-generation Pokémon:
- **Starters**: Venusaur, Charizard, Blastoise
- **Classics**: Pikachu/Raichu, Pidgeot, Raticate
- **And many more...**

## 🎲 Random Elements

- Selection of the 10 proposed Pokémon
- AI opponent choices
- Initial potion stock (3-5)
- Damage multiplier (85-100%)
- AI decisions (70% attack, 30% heal)

## 🛠️ Customization

You can easily:
- Add new Pokémon in `pokemons.py`
- Modify types and their interactions in `classes.py`
- Adjust Pokémon stats (HP, attack)
- Change AI logic in `pokefight.py`

## 🐛 Tests

The `fichier test.py` file contains unit tests to verify:
- Trainer creation and management
- Pokémon functionality
- Combat system
- Strength/weakness relationships

## 📝 Development Notes

- French interface
- Commented code for easy understanding
- Modular architecture for easy extensions
- Basic error handling (user input validation)

## 🎯 Possible Improvements

- ~~Graphical interface~~ ✅ **COMPLETED!**
- Game saves
- Battle animations
- More attack types
- System d'expérience and leveling system
- Network multiplayer
- Sound effects and background music
- Pokemon sprites and images

---

*Have fun in the Pokémon universe! 🎮*
