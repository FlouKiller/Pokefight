import tkinter as tk
from tkinter import ttk, messagebox
from classes import Dresseur, Pokemon
from pokemons import pokemons_dispos
from random import randint
import threading
import time

class PokefightGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Pokefight - Pokémon Battle Game")
        self.root.geometry("1000x700")
        self.root.configure(bg="#2c3e50")
        
        # Game state variables
        self.joueur = None
        self.ordinateur = None
        self.pokemons_disponibles = []
        self.game_phase = "selection"  # selection, battle, game_over
        self.player_turn = True
        self.battle_log = []
        
        # Style configuration
        self.setup_styles()
        
        # Initialize game
        self.init_game()
        
        # Create main interface
        self.create_main_interface()
    
    def setup_styles(self):
        """Configure tkinter styles"""
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure styles
        self.style.configure('Title.TLabel', 
                           font=('Arial', 24, 'bold'), 
                           background="#2c3e50", 
                           foreground="#ecf0f1")
        
        self.style.configure('Header.TLabel', 
                           font=('Arial', 16, 'bold'), 
                           background="#2c3e50", 
                           foreground="#ecf0f1")
        
        self.style.configure('Pokemon.TLabel', 
                           font=('Arial', 12), 
                           background="#34495e", 
                           foreground="#ecf0f1",
                           padding=10)
        
        self.style.configure('Action.TButton', 
                           font=('Arial', 12, 'bold'),
                           padding=10)
    
    def init_game(self):
        """Initialize game data"""
        self.joueur = Dresseur("Player")
        self.ordinateur = Dresseur("Computer")
        self.pokemons_disponibles = pokemons_dispos()
        
    def create_main_interface(self):
        """Create the main game interface"""
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Main title
        title_label = ttk.Label(self.root, text="🎮 Pokefight", style='Title.TLabel')
        title_label.pack(pady=20)
        
        if self.game_phase == "selection":
            self.create_selection_interface()
        elif self.game_phase == "battle":
            self.create_battle_interface()
        elif self.game_phase == "game_over":
            self.create_game_over_interface()
    
    def create_selection_interface(self):
        """Create Pokemon selection interface"""
        # Selection frame
        selection_frame = tk.Frame(self.root, bg="#2c3e50")
        selection_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Instructions
        instruction_text = f"Choose your team! Select 3 Pokémon (You have {3 - len(self.joueur.listePokemon)} left to choose)"
        instruction_label = ttk.Label(selection_frame, text=instruction_text, style='Header.TLabel')
        instruction_label.pack(pady=10)
        
        # Player team display
        team_frame = tk.Frame(selection_frame, bg="#34495e", relief="ridge", bd=2)
        team_frame.pack(fill="x", pady=10)
        
        ttk.Label(team_frame, text="Your Team:", style='Header.TLabel').pack(pady=5)
        
        team_display_frame = tk.Frame(team_frame, bg="#34495e")
        team_display_frame.pack(pady=5)
        
        for i, pokemon in enumerate(self.joueur.listePokemon):
            pokemon_text = f"{pokemon.nom} ({pokemon.type}) - HP: {pokemon.pv}/{pokemon.pvmax}"
            ttk.Label(team_display_frame, text=pokemon_text, style='Pokemon.TLabel').pack(side="left", padx=5)
        
        # Available Pokemon grid
        available_frame = tk.Frame(selection_frame, bg="#2c3e50")
        available_frame.pack(fill="both", expand=True, pady=10)
        
        ttk.Label(available_frame, text="Available Pokémon:", style='Header.TLabel').pack(pady=5)
        
        # Create scrollable frame for Pokemon
        canvas = tk.Canvas(available_frame, bg="#2c3e50", highlightthickness=0)
        scrollbar = ttk.Scrollbar(available_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#2c3e50")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pokemon selection buttons
        for i, pokemon in enumerate(self.pokemons_disponibles):
            pokemon_frame = tk.Frame(scrollable_frame, bg="#34495e", relief="ridge", bd=1)
            pokemon_frame.pack(fill="x", pady=2, padx=5)
            
            pokemon_info = f"{pokemon.nom} - Type: {pokemon.type} - HP: {pokemon.pv} - Attack: {pokemon.pa}"
            
            ttk.Label(pokemon_frame, text=pokemon_info, style='Pokemon.TLabel').pack(side="left", fill="x", expand=True)
            
            select_btn = ttk.Button(pokemon_frame, text="Select", 
                                  command=lambda p=pokemon: self.select_pokemon(p),
                                  style='Action.TButton')
            select_btn.pack(side="right", padx=5, pady=5)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def select_pokemon(self, pokemon):
        """Handle Pokemon selection"""
        if len(self.joueur.listePokemon) < 3:
            # Add to player team
            self.joueur.addPokemon(pokemon)
            self.pokemons_disponibles.remove(pokemon)
            
            # Computer selects randomly
            if self.pokemons_disponibles:
                computer_choice = self.pokemons_disponibles[randint(0, len(self.pokemons_disponibles)-1)]
                self.ordinateur.addPokemon(computer_choice)
                self.pokemons_disponibles.remove(computer_choice)
                
                # Add to battle log
                self.battle_log.append(f"You selected {pokemon.nom}")
                self.battle_log.append(f"Computer selected {computer_choice.nom}")
        
        # Check if selection is complete
        if len(self.joueur.listePokemon) == 3:
            self.game_phase = "battle"
            messagebox.showinfo("Team Complete", "Team selection complete! Let the battle begin!")
        
        # Refresh interface
        self.create_main_interface()
    
    def create_battle_interface(self):
        """Create the battle interface"""
        # Main battle frame
        battle_frame = tk.Frame(self.root, bg="#2c3e50")
        battle_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Status frame
        status_frame = tk.Frame(battle_frame, bg="#34495e", relief="ridge", bd=2)
        status_frame.pack(fill="x", pady=10)
        
        # Current Pokemon display
        current_frame = tk.Frame(status_frame, bg="#34495e")
        current_frame.pack(fill="x", pady=10)
        
        # Player Pokemon
        player_pokemon = self.joueur.listePokemon[0] if self.joueur.listePokemon else None
        computer_pokemon = self.ordinateur.listePokemon[0] if self.ordinateur.listePokemon else None
        
        if player_pokemon and computer_pokemon:
            # Player side
            player_frame = tk.Frame(current_frame, bg="#3498db", relief="ridge", bd=2)
            player_frame.pack(side="left", fill="both", expand=True, padx=5)
            
            ttk.Label(player_frame, text=f"Your Team: {len(self.joueur.listePokemon)}/3", 
                     font=('Arial', 12, 'bold'), background="#3498db", foreground="white").pack(pady=5)
            ttk.Label(player_frame, text=player_pokemon.nom, 
                     font=('Arial', 14, 'bold'), background="#3498db", foreground="white").pack()
            ttk.Label(player_frame, text=f"HP: {player_pokemon.pv}/{player_pokemon.pvmax}", 
                     font=('Arial', 12), background="#3498db", foreground="white").pack()
            ttk.Label(player_frame, text=f"Type: {player_pokemon.type}", 
                     font=('Arial', 10), background="#3498db", foreground="white").pack()
            
            # VS label
            vs_frame = tk.Frame(current_frame, bg="#34495e")
            vs_frame.pack(side="left", padx=20)
            ttk.Label(vs_frame, text="VS", font=('Arial', 20, 'bold'), 
                     background="#34495e", foreground="#e74c3c").pack()
            
            # Computer side
            computer_frame = tk.Frame(current_frame, bg="#e74c3c", relief="ridge", bd=2)
            computer_frame.pack(side="right", fill="both", expand=True, padx=5)
            
            ttk.Label(computer_frame, text=f"Enemy Team: {len(self.ordinateur.listePokemon)}/3", 
                     font=('Arial', 12, 'bold'), background="#e74c3c", foreground="white").pack(pady=5)
            ttk.Label(computer_frame, text=computer_pokemon.nom, 
                     font=('Arial', 14, 'bold'), background="#e74c3c", foreground="white").pack()
            ttk.Label(computer_frame, text=f"HP: {computer_pokemon.pv}/{computer_pokemon.pvmax}", 
                     font=('Arial', 12), background="#e74c3c", foreground="white").pack()
            ttk.Label(computer_frame, text=f"Type: {computer_pokemon.type}", 
                     font=('Arial', 10), background="#e74c3c", foreground="white").pack()
        
        # Action buttons frame
        action_frame = tk.Frame(battle_frame, bg="#2c3e50")
        action_frame.pack(fill="x", pady=20)
        
        if self.player_turn and self.game_phase == "battle":
            ttk.Label(action_frame, text="Your Turn - Choose an action:", style='Header.TLabel').pack(pady=10)
            
            button_frame = tk.Frame(action_frame, bg="#2c3e50")
            button_frame.pack()
            
            # Attack button
            attack_btn = ttk.Button(button_frame, text="⚔️ Attack", 
                                  command=self.player_attack, style='Action.TButton')
            attack_btn.pack(side="left", padx=10)
            
            # Switch Pokemon button (if available)
            if len(self.joueur.listePokemon) > 1:
                switch_btn = ttk.Button(button_frame, text="🔄 Switch Pokémon", 
                                      command=self.show_switch_menu, style='Action.TButton')
                switch_btn.pack(side="left", padx=10)
            
            # Use potion button (if available)
            if self.joueur.potions > 0:
                potion_btn = ttk.Button(button_frame, text=f"🧪 Use Potion ({self.joueur.potions})", 
                                      command=self.use_potion, style='Action.TButton')
                potion_btn.pack(side="left", padx=10)
        else:
            ttk.Label(action_frame, text="Computer's Turn...", style='Header.TLabel').pack(pady=10)
        
        # Battle log
        log_frame = tk.Frame(battle_frame, bg="#34495e", relief="ridge", bd=2)
        log_frame.pack(fill="both", expand=True, pady=10)
        
        ttk.Label(log_frame, text="Battle Log:", style='Header.TLabel').pack(pady=5)
        
        # Create scrollable text widget for battle log
        log_text = tk.Text(log_frame, height=8, bg="#2c3e50", fg="#ecf0f1", 
                          font=('Arial', 10), wrap=tk.WORD)
        log_scrollbar = ttk.Scrollbar(log_frame, orient="vertical", command=log_text.yview)
        log_text.configure(yscrollcommand=log_scrollbar.set)
        
        # Display recent battle log entries
        log_text.delete(1.0, tk.END)
        for entry in self.battle_log[-10:]:  # Show last 10 entries
            log_text.insert(tk.END, entry + "\n")
        
        log_text.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        log_scrollbar.pack(side="right", fill="y")
        
        # Auto-scroll to bottom
        log_text.see(tk.END)
        log_text.config(state=tk.DISABLED)
        
        # Handle computer turn
        if not self.player_turn and self.game_phase == "battle":
            self.root.after(2000, self.computer_turn)  # Delay for better UX
    
    def player_attack(self):
        """Handle player attack action"""
        if not self.joueur.listePokemon or not self.ordinateur.listePokemon:
            return
        
        player_pokemon = self.joueur.listePokemon[0]
        computer_pokemon = self.ordinateur.listePokemon[0]
        
        # Calculate damage
        pv_before = computer_pokemon.pv
        player_pokemon.attack(computer_pokemon)
        damage = pv_before - computer_pokemon.pv
        
        self.battle_log.append(f"{player_pokemon.nom} attacked {computer_pokemon.nom} for {damage} damage!")
        
        # Check if computer pokemon is defeated
        if not computer_pokemon.isAlive():
            self.battle_log.append(f"{computer_pokemon.nom} was defeated!")
            self.ordinateur.removePokemon(computer_pokemon)
            
            if not self.ordinateur.listePokemon:
                self.battle_log.append("You won the battle!")
                self.game_phase = "game_over"
                self.create_main_interface()
                return
        
        self.player_turn = False
        self.create_main_interface()
    
    def computer_turn(self):
        """Handle computer turn"""
        if not self.joueur.listePokemon or not self.ordinateur.listePokemon:
            return
        
        player_pokemon = self.joueur.listePokemon[0]
        computer_pokemon = self.ordinateur.listePokemon[0]
        
        # Computer AI logic
        if self.ordinateur.potions == 0 or computer_pokemon.pv == computer_pokemon.pvmax:
            action = "attack"
        else:
            action = "attack" if randint(1, 100) <= 70 else "heal"
        
        if action == "attack":
            pv_before = player_pokemon.pv
            computer_pokemon.attack(player_pokemon)
            damage = pv_before - player_pokemon.pv
            
            self.battle_log.append(f"{computer_pokemon.nom} attacked {player_pokemon.nom} for {damage} damage!")
            
            # Check if player pokemon is defeated
            if not player_pokemon.isAlive():
                self.battle_log.append(f"{player_pokemon.nom} was defeated!")
                self.joueur.removePokemon(player_pokemon)
                
                if not self.joueur.listePokemon:
                    self.battle_log.append("Computer won the battle!")
                    self.game_phase = "game_over"
                    self.create_main_interface()
                    return
        else:
            # Computer uses potion
            self.ordinateur.setPotion(self.ordinateur.potions - 1)
            computer_pokemon.setPv(computer_pokemon.pv + 20)
            self.battle_log.append(f"Computer used a potion on {computer_pokemon.nom}!")
        
        self.player_turn = True
        self.create_main_interface()
    
    def show_switch_menu(self):
        """Show Pokemon switching menu"""
        switch_window = tk.Toplevel(self.root)
        switch_window.title("Switch Pokémon")
        switch_window.geometry("400x300")
        switch_window.configure(bg="#2c3e50")
        
        ttk.Label(switch_window, text="Choose a Pokémon to switch:", style='Header.TLabel').pack(pady=10)
        
        for i in range(1, len(self.joueur.listePokemon)):
            pokemon = self.joueur.listePokemon[i]
            pokemon_frame = tk.Frame(switch_window, bg="#34495e", relief="ridge", bd=1)
            pokemon_frame.pack(fill="x", pady=5, padx=10)
            
            pokemon_text = f"{pokemon.nom} - HP: {pokemon.pv}/{pokemon.pvmax} - Type: {pokemon.type}"
            ttk.Label(pokemon_frame, text=pokemon_text, style='Pokemon.TLabel').pack(side="left")
            
            switch_btn = ttk.Button(pokemon_frame, text="Switch", 
                                  command=lambda idx=i, window=switch_window: self.switch_pokemon(idx, window))
            switch_btn.pack(side="right", padx=5, pady=5)
    
    def switch_pokemon(self, index, window):
        """Switch to selected Pokemon"""
        current_pokemon = self.joueur.listePokemon[0]
        self.joueur.listePokemon[0], self.joueur.listePokemon[index] = self.joueur.listePokemon[index], self.joueur.listePokemon[0]
        
        self.battle_log.append(f"You switched {current_pokemon.nom} for {self.joueur.listePokemon[0].nom}!")
        
        window.destroy()
        self.player_turn = False
        self.create_main_interface()
    
    def use_potion(self):
        """Use a potion on current Pokemon"""
        if self.joueur.potions > 0 and self.joueur.listePokemon:
            current_pokemon = self.joueur.listePokemon[0]
            self.joueur.setPotion(self.joueur.potions - 1)
            current_pokemon.setPv(current_pokemon.pv + 20)
            
            self.battle_log.append(f"You used a potion on {current_pokemon.nom}! HP restored to {current_pokemon.pv}")
            
            self.player_turn = False
            self.create_main_interface()
    
    def create_game_over_interface(self):
        """Create game over interface"""
        game_over_frame = tk.Frame(self.root, bg="#2c3e50")
        game_over_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Determine winner
        if len(self.joueur.listePokemon) == 0:
            result_text = "💔 You Lost!"
            result_color = "#e74c3c"
        else:
            result_text = "🎉 You Won!"
            result_color = "#27ae60"
        
        result_label = tk.Label(game_over_frame, text=result_text, 
                               font=('Arial', 32, 'bold'), 
                               bg="#2c3e50", fg=result_color)
        result_label.pack(pady=50)
        
        # Final battle log
        ttk.Label(game_over_frame, text="Final Battle Summary:", style='Header.TLabel').pack(pady=20)
        
        log_text = tk.Text(game_over_frame, height=10, bg="#2c3e50", fg="#ecf0f1", 
                          font=('Arial', 10), wrap=tk.WORD)
        log_scrollbar = ttk.Scrollbar(game_over_frame, orient="vertical", command=log_text.yview)
        log_text.configure(yscrollcommand=log_scrollbar.set)
        
        for entry in self.battle_log:
            log_text.insert(tk.END, entry + "\n")
        
        log_text.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        log_scrollbar.pack(side="right", fill="y")
        log_text.see(tk.END)
        log_text.config(state=tk.DISABLED)
        
        # Restart button
        restart_btn = ttk.Button(game_over_frame, text="🔄 Play Again", 
                               command=self.restart_game, style='Action.TButton')
        restart_btn.pack(pady=20)
        
        # Quit button
        quit_btn = ttk.Button(game_over_frame, text="❌ Quit", 
                            command=self.root.quit, style='Action.TButton')
        quit_btn.pack(pady=10)
    
    def restart_game(self):
        """Restart the game"""
        self.init_game()
        self.game_phase = "selection"
        self.player_turn = True
        self.battle_log = []
        self.create_main_interface()

def main():
    root = tk.Tk()
    app = PokefightGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
