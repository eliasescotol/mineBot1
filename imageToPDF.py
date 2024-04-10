from io import BytesIO
import img as img
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image, ExifTags

import os


def add_image_to_pdf(pictures):
    # Create a PDF file
    counter = 0
    for file_name in sorted(os.listdir("JPG")):
        image_path = "JPG/" + file_name
        pdf_path = 'PDF/' + str(counter+2) + ".PDF"
        label = pictures[counter]
        counter += 1
        pdf_canvas = canvas.Canvas(pdf_path, pagesize=letter)

        # Get the dimensions of the letter-sized page (8.5 x 11 inches)
        page_width, page_height = letter

        # Open the image
        img = Image.open(image_path)

        # Get the dimensions of the image
        img_width, img_height = img.size

        # Calculate scaling factors to fit the image inside the page while maintaining aspect ratio
        width_ratio = page_width / img_width
        height_ratio = page_height / img_height
        scaling_factor = min(width_ratio, height_ratio)

        # Calculate the scaled dimensions of the image
        scaled_width = img_width * scaling_factor*0.55
        scaled_height = img_height * scaling_factor*0.55

        # Calculate the position to center the image on the page
        x_position = (page_width - scaled_width) / 2
        y_position = (page_height - scaled_height) / 2

        # Draw the scaled image on the PDF
        pdf_canvas.drawInlineImage(img, x_position, y_position, width=scaled_width, height=scaled_height)

        label_width = pdf_canvas.stringWidth(label, 'Helvetica', 12)

        label_x_position = (page_width - label_width) / 2
        label_y_position = y_position - 20  # Adjust the distance from the image
        pdf_canvas.drawString(label_x_position, label_y_position, label)
        # Save the PDF file
        pdf_canvas.save()
