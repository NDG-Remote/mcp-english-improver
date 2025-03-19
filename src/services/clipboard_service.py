import pyperclip

class ClipboardService:
    @staticmethod
    def get_text():
        """Get text from the clipboard"""
        print("📋 Getting text from clipboard...")
        return pyperclip.paste()

    @staticmethod
    def save_text(text):
        """Save text to the clipboard"""
        print("📋 Saving improved text to clipboard...")
        pyperclip.copy(text)
        print("✅ Text has been improved and copied to clipboard!") 