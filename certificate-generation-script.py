# Importing the pillow library
from PIL import Image, ImageDraw, ImageFont

import os


with open("Demo Data\\demo_data.csv", "r") as file:
    content = file.readlines()

# list variable to hold participant names
names = []

for line in content:
    names.append(line.split(',')[1])
names.pop(0)


folder_name = "certificates"
os.makedirs(folder_name, exist_ok=True)


# This is the main loop that creates all the pdf files
for name in names:
    image = Image.open('Demo Data\\demo_template.png')

    text = name.strip()

    # Draw object
    draw = ImageDraw.Draw(image)


    # Calculation of position where to put the text
    image_width, image_height = image.size
    center_location = (image_width // 2, image_height // 2)

    # Font and size are defined here and can be changed here only
    font = ImageFont.truetype("arial.ttf", 70)

    # bbox is a tuple containing the values of boundary as (left, top, right, bottom)
    bbox = draw.textbbox((0, 0), text, font=font)

    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    text_x = center_location[0] - text_width / 2
    text_y = center_location[1] - text_height / 2 + 50
    position = (text_x, text_y)


    # Text color can be changed here
    text_color = (0,0,0)

    draw.text(position, text, font=font, fill=text_color)

    image.save(f"certificates\\{name}'s certificate.pdf", "PDF")