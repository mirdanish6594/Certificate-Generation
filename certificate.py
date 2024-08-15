from PIL import Image, ImageDraw, ImageFont
import os
import csv

template_path = "Demo_Data/demo_template.png"
output_directory = "output"
font_path = "fonts/CormorantGaramond-Italic.ttf"

csv_file_path="Demo_Data/demo_data.csv"

def fetch_data_from_csv(csv_file_path):
    data = []
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(dict(row))
    return data

users=fetch_data_from_csv(csv_file_path)

def generate_certificates(users, template_path, output_directory, font_path):
    font = ImageFont.truetype(font_path, 48)
    template = Image.open(template_path)
    for user in users:
        certificate = template.copy()
        draw = ImageDraw.Draw(certificate)
        draw.text((920,766), user["Name"], (0, 0, 0), font=font)
        certificate.save(f"{output_directory}/{user["Name"]}_certificate.png")

generate_certificates(users, template_path,output_directory,font_path)

DeleteNames=[]  #Add the names to be deleted in this list
def delete_certificates(DeleteNames,template_path,output_directory):
    for name in DeleteNames:
        file_path = f"{output_directory}/{name}_certificate.png"
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"File {name}_certificate.png has been deleted.")
        else:
            print(f"The file {name}_certificate.png does not exist.")

# delete_certificates(DeleteNames,template_path,output_directory) 

