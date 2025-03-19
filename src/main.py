import tkinter as tk
from gui import EnglishImproverGUI

def main():
    """Main function to run the GUI application"""
    root = tk.Tk()
    app = EnglishImproverGUI(root)
    root.mainloop()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ Error: {e}") 