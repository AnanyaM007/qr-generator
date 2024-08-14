import qrcode
from PIL import Image
import tkinter as tk

def generate_qr():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link.get())
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr.png")
    img.show()

def main():
    global link
    root = tk.Tk()
    root.title("QR Code Generator")

    frame = tk.Frame(root)
    frame.pack(pady=20, padx=20)

    tk.Label(frame, text="Enter the link:").pack(side=tk.LEFT)
    link = tk.Entry(frame, width=50)
    link.pack(side=tk.LEFT, padx=10)

    generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
    generate_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
