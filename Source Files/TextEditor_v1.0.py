import tkinter as tk
from tkinter import filedialog, messagebox
import string
import webbrowser

class TextEditor:
    def __init__(self, Window):
        self.Window = Window
        Window.title("Text Editor")

        # Menu
        self.Menu()

        # Text Canvas
        self.Text_Canvas = tk.Text(Window)
        self.Text_Canvas.pack(fill="both", expand=True)

        # Bind the Counter
        self.Text_Canvas.bind("<KeyRelease>", self.Counter)

        # Frame
        self.Statistics_Frame = tk.Frame(Window)
        self.Statistics_Frame.pack(side="bottom", fill="x")

        # Labels on Frame
        self.Letters = tk.Label(self.Statistics_Frame, text="Letters: 0")
        self.Numbers = tk.Label(self.Statistics_Frame, text="Numbers: 0")
        self.SpecialCharacters = tk.Label(self.Statistics_Frame, text="Special Characters: 0")
        self.Spaces = tk.Label(self.Statistics_Frame, text="Spaces: 0")
        self.TotalCharacter = tk.Label(self.Statistics_Frame, text="Total Characters: 0")

    def Menu(self):
        # Create 'Menu'
        self.Menu = tk.Menu(self.Window)
        self.Window.config(menu=self.Menu)

        # Create 'Menu' -> 'File'
        self.File = tk.Menu(self.Menu, tearoff=0)
        self.Menu.add_cascade(label="File", menu=self.File)

        # Create 'Menu' -> 'File' -> 'New'
        self.File.add_command(label="New", command=self.New)

        # Create 'Menu' -> 'File' -> 'Open'
        self.File.add_command(label="Open", command=self.Open)

        # Create 'Menu' -> 'File' -> 'Save'
        self.File.add_command(label="Save", command=self.Save)

        self.File.add_separator()

        # Create 'Menu' -> 'File' -> 'Exit'
        self.File.add_command(label="Exit", command=self.Exit)

        # Create 'Menu' -> 'View'
        self.View = tk.Menu(self.Menu, tearoff=0)
        self.Menu.add_cascade(label="View", menu=self.View)

        # Create 'Menu' -> 'View' -> 'Show' 
        self.Show = tk.Menu(self.View, tearoff=0)
        self.View.add_cascade(label="Show", menu=self.Show)

        # Create Checkboxes in 'Show'
        self.Show_Letters = tk.BooleanVar(value=False)
        self.Show_Numbers = tk.BooleanVar(value=False)
        self.Show_SpecialCharacters = tk.BooleanVar(value=False)
        self.Show_Spaces = tk.BooleanVar(value=False)
        self.Show_TotalCharacters = tk.BooleanVar(value=False)

        self.Show.add_checkbutton(label="Letters", variable=self.Show_Letters, command=self.Display_on_Statistics_Frame)
        self.Show.add_checkbutton(label="Numbers", variable=self.Show_Numbers, command=self.Display_on_Statistics_Frame)
        self.Show.add_checkbutton(label="Special Characters", variable=self.Show_SpecialCharacters, command=self.Display_on_Statistics_Frame)
        self.Show.add_checkbutton(label="Spaces", variable=self.Show_Spaces, command=self.Display_on_Statistics_Frame)
        self.Show.add_checkbutton(label="Total Characters", variable=self.Show_TotalCharacters, command=self.Display_on_Statistics_Frame)

        # Create 'Menu' -> 'Help'
        self.Help = tk.Menu(self.Menu, tearoff=0)
        self.Menu.add_cascade(label="Help", menu=self.Help)

        # Create 'Menu' -> 'Help' -> 'Check for Updates'
        self.Help.add_command(label="Check for Updates", command=self.Check_for_Updates)

        self.Help.add_separator()

        # Create 'Menu' -> 'Help' -> 'About'
        self.Help.add_command(label="About", command=self.About)

    def New(self):
        self.Text_Canvas.delete("1.0", tk.END)
        self.Window.title("Text Editor")
        self.Counter(None)

    def Open(self):
        file_path = tk.filedialog.askopenfilename(filetypes=[("Text Files (*.txt)", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
            self.Text_Canvas.delete("1.0", "end")
            self.Text_Canvas.insert("1.0", content)
            self.Window.title(f"Text Editor - {file_path}")
            self.Counter(None)

    def Save(self):
        content = self.Text_Canvas.get("1.0", "end-1c")
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files (*.txt)", "*.txt")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(content)
            self.Window.title(f"Text Editor - {file_path}")

    def Exit(self):
        self.Window.quit()

    def Counter(self, event):
        Text = self.Text_Canvas.get("1.0", "end-1c")
        
        # Count
        Count_Letters = sum(1 for char in Text if char.isalpha())
        Count_Numbers = sum(1 for char in Text if char.isdigit())
        Count_SpecialCharacters = sum(1 for char in Text if char in string.punctuation)
        Count_Spaces = sum(1 for char in Text if char.isspace())

        # Count Update
        self.Letters.config(text=f"Letters: {Count_Letters}")
        self.Numbers.config(text=f"Numbers: {Count_Numbers}")
        self.SpecialCharacters.config(text=f"Special Characters: {Count_SpecialCharacters}")
        self.Spaces.config(text=f"Spaces: {Count_Spaces}")
        self.TotalCharacter.config(text=f"Total Characters: {len(Text)}")

    def Display_on_Statistics_Frame(self):
        if not any([self.Show_Letters.get(), self.Show_Numbers.get(), self.Show_SpecialCharacters.get(), self.Show_Spaces.get(), self.Show_TotalCharacters.get()]):
            # If no Checkbox is Checked, Hide the Statistics Frame
            self.Statistics_Frame.pack_forget()
            return
    
        # Otherwise, Display the Statistics Frame
        self.Statistics_Frame.pack(side="bottom", fill="x")

        # Remove previously Packed Labels on Statistics Frame
        self.Letters.pack_forget()
        self.Numbers.pack_forget()
        self.SpecialCharacters.pack_forget()
        self.Spaces.pack_forget()
        self.TotalCharacter.pack_forget()

        # Pack Labels on Statistics Frame
        if self.Show_Letters.get():
            self.Letters.pack(side="left", padx=10, pady=5)
        if self.Show_Numbers.get():
            self.Numbers.pack(side="left", padx=10, pady=5)
        if self.Show_SpecialCharacters.get():
            self.SpecialCharacters.pack(side="left", padx=10, pady=5)
        if self.Show_Spaces.get():
            self.Spaces.pack(side="left", padx=10, pady=5)
        if self.Show_TotalCharacters.get():
            self.TotalCharacter.pack(side="right", padx=10, pady=5)

    def Check_for_Updates(self):
        webbrowser.open("https://www.github.com/satishkumarsingh2024/TextEditor/")

    def About(self):
        messagebox.showinfo("About", "Text Editor (v1.0)\nDeveloped by Satish Kumar Singh")

def main():
    root = tk.Tk()
    Editor = TextEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()