import pyheif
from PIL import Image
import pillow_heif
from pathlib import Path
import shutil


import os


def convert_heic_to_jpg():
    counter = 1
    for file_name in sorted(os.listdir("HEIC")):
        # Read HEIC file
        file_extension = Path(file_name).suffix
        jpg_path = "JPEG/" + str(counter) + ".JPEG"
        if file_extension == ".HEIC":

            heif_file = pillow_heif.read("HEIC/"+file_name)

            # Extract the first image from the HEIC file
            image = Image.frombytes(
                heif_file.mode,
                heif_file.size,
                heif_file.data,
                "raw",
                heif_file.mode,
                heif_file.stride,
            )

            # Save as JPG
            image.convert("RGB").save(jpg_path, "JPEG")
            counter += 1
        else:
            if file_name !=".DS_Store":
                source_path= "HEIC/" + file_name
                shutil.copy(source_path, jpg_path)

                counter += 1


