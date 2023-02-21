import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

def convert_to_png():
    input_file = filedialog.askopenfilename(title="Choose file to convert:", filetypes=[("Text Files", "*.txt")], defaultextension=".txt")

    if not input_file:
        return

    with open(input_file, 'r') as f:
        text = f.read()

    img = Image.new('RGB', (800, 600), color='white')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('arial.ttf', size=20)
    draw.text((50, 50), text, font=font, fill='black')

    output_file = filedialog.asksaveasfilename(title="Convert to PNG:", filetypes=[("PNG Files", "*.png")], defaultextension=".png")

    if not output_file:
        return

    img.save(output_file)

root = tk.Tk()
root.title("TXT to PNG")

convert_button = tk.Button(root, text="Convert to PNG", command=convert_to_png)
convert_button.pack()

root.mainloop()
