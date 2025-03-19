import tkinter as tk
from tkinter import ttk, scrolledtext
from services.text_improvement_service import TextImprovementService

class EnglishImproverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MCP English Text Improver")
        self.root.geometry("1200x600")
        
        # Initialize the text improvement service
        self.text_service = TextImprovementService()
        
        # Create main container
        self.main_container = ttk.Frame(self.root, padding="10")
        self.main_container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.main_container.columnconfigure(0, weight=1)
        self.main_container.columnconfigure(1, weight=1)
        self.main_container.rowconfigure(1, weight=1)
        
        # Create labels
        ttk.Label(self.main_container, text="Input Text").grid(row=0, column=0, sticky=tk.W)
        ttk.Label(self.main_container, text="Improved Text").grid(row=0, column=1, sticky=tk.W)
        
        # Create text areas
        self.input_text = scrolledtext.ScrolledText(self.main_container, wrap=tk.WORD, width=50, height=20)
        self.input_text.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5)
        
        self.output_text = scrolledtext.ScrolledText(self.main_container, wrap=tk.WORD, width=50, height=20)
        self.output_text.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5)
        
        # Create button
        self.improve_button = ttk.Button(self.main_container, text="Improve Text", command=self.improve_text)
        self.improve_button.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Status label
        self.status_label = ttk.Label(self.main_container, text="")
        self.status_label.grid(row=3, column=0, columnspan=2)
        
    def improve_text(self):
        """Improve the text from the input field and display it in the output field"""
        input_text = self.input_text.get("1.0", tk.END).strip()
        
        if not input_text:
            self.status_label.config(text="Please enter some text to improve", foreground="red")
            return
            
        try:
            self.status_label.config(text="Improving text...", foreground="blue")
            self.root.update()
            
            improved_text = self.text_service.improve_text(input_text)
            
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert("1.0", improved_text)
            self.status_label.config(text="Text improved successfully!", foreground="green")
            
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}", foreground="red") 