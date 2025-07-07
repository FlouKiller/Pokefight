import tkinter as tk
from tkinter import ttk
import subprocess
import sys
import os

class GameLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Pokefight Launcher")
        self.root.geometry("400x300")
        self.root.configure(bg="#2c3e50")
        self.root.resizable(False, False)
        
        # Center the window
        self.root.eval('tk::PlaceWindow . center')
        
        self.create_interface()
    
    def create_interface(self):
        # Title
        title_label = tk.Label(self.root, text="🎮 Pokefight", 
                              font=('Arial', 24, 'bold'), 
                              bg="#2c3e50", fg="#ecf0f1")
        title_label.pack(pady=30)
        
        subtitle_label = tk.Label(self.root, text="Choose your game mode:", 
                                 font=('Arial', 14), 
                                 bg="#2c3e50", fg="#ecf0f1")
        subtitle_label.pack(pady=10)
        
        # Button frame
        button_frame = tk.Frame(self.root, bg="#2c3e50")
        button_frame.pack(pady=30)
        
        # GUI version button
        gui_btn = tk.Button(button_frame, 
                           text="🖥️ Graphical Interface\n(Recommended)", 
                           font=('Arial', 14, 'bold'),
                           bg="#3498db", fg="white",
                           width=20, height=3,
                           command=self.launch_gui,
                           relief="flat",
                           cursor="hand2")
        gui_btn.pack(pady=10)
        
        # Text version button
        text_btn = tk.Button(button_frame, 
                            text="📟 Text Interface\n(Classic)", 
                            font=('Arial', 14, 'bold'),
                            bg="#34495e", fg="white",
                            width=20, height=3,
                            command=self.launch_text,
                            relief="flat",
                            cursor="hand2")
        text_btn.pack(pady=10)
        
        # Exit button
        exit_btn = tk.Button(button_frame, 
                            text="❌ Exit", 
                            font=('Arial', 12),
                            bg="#e74c3c", fg="white",
                            width=10, height=1,
                            command=self.root.quit,
                            relief="flat",
                            cursor="hand2")
        exit_btn.pack(pady=20)
        
        # Instructions
        info_label = tk.Label(self.root, 
                             text="Pokémon battle game with team selection and strategic combat", 
                             font=('Arial', 10), 
                             bg="#2c3e50", fg="#bdc3c7")
        info_label.pack(side="bottom", pady=10)
    
    def launch_gui(self):
        """Launch the GUI version"""
        try:
            self.root.destroy()
            subprocess.run([sys.executable, "pokefight_gui.py"])
        except FileNotFoundError:
            tk.messagebox.showerror("Error", "pokefight_gui.py not found!")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Failed to launch GUI version: {str(e)}")
    
    def launch_text(self):
        """Launch the text version"""
        try:
            self.root.destroy()
            subprocess.run([sys.executable, "pokefight.py"])
        except FileNotFoundError:
            tk.messagebox.showerror("Error", "pokefight.py not found!")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Failed to launch text version: {str(e)}")

def main():
    root = tk.Tk()
    app = GameLauncher(root)
    root.mainloop()

if __name__ == "__main__":
    main()
