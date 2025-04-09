import tkinter as tk
from tkinter import ttk, messagebox
import qrcode
from PIL import Image, ImageTk
import os

class QRCodeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("400x500")
        
        # Create and pack the main frame
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Input field
        ttk.Label(self.main_frame, text="Enter text:").pack(pady=5)
        self.text_input = ttk.Entry(self.main_frame, width=40)
        self.text_input.pack(pady=5)
        
        # Generate button
        ttk.Button(self.main_frame, text="Generate QR Code", 
                  command=self.generate_qr).pack(pady=10)
        
        # Label to display QR code
        self.qr_label = ttk.Label(self.main_frame)
        self.qr_label.pack(pady=10)
        
    def generate_qr(self):
        text = self.text_input.get().strip()
        if not text:
            messagebox.showerror("Error", "Please enter some text!")
            return
            
        # Generate QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(text)
        qr.make(fit=True)
        
        # Create QR code image
        qr_image = qr.make_image(fill_color="black", back_color="white")
        
        # Convert to PhotoImage for display
        qr_image = qr_image.resize((250, 250))
        self.photo = ImageTk.PhotoImage(qr_image)
        
        # Update label with new QR code
        self.qr_label.config(image=self.photo)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGenerator(root)
    root.mainloop() 