from PIL import Image, ImageDraw, ImageFont
import os
import csv

template_path = "Demo Data/demo_template.png"
output_directory = "output"
fontGaramondIt = "fonts/CormorantGaramond-Italic.ttf"
csv_file_path = "Demo Data/demo_data.csv"

def fetch_data_from_csv(csv_file_path):
    data = []
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(dict(row))
    return data

users = fetch_data_from_csv(csv_file_path)

def generate_certificates(users, template_path, output_directory, font_path):
    font = ImageFont.truetype(font_path, 70)
    template = Image.open(template_path)
    certificate_images = []

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    for user in users:
        certificate = template.copy()
        draw = ImageDraw.Draw(certificate)
        draw.text((800, 738), user["Name"], (0, 0, 0), font=font)
        certificate_images.append(certificate)

    
        pdf_path = os.path.join(output_directory, f"{user['Name']}_certificate.pdf")
    
    # Save as pdf
        certificate.save(pdf_path, "PDF", resolution=100.0)
        print(f"PDF saved for {user['Name']} at {pdf_path}")

# Generate the certificates and save them as a PDF
generate_certificates(users, template_path, output_directory, fontGaramondIt)


