import time

from PIL import Image
import os
from PIL import Image, ImageOps


def compress_jpeg(quality=20):
    for file_name in sorted(os.listdir("JPEG")):
        time.sleep(2)
        input_path = 'JPEG/' + file_name
        output_path = 'JPG/' + file_name
        print(input_path)
        try:
            with Image.open(input_path) as img:
                # Save the image with the specified quality
                img = ImageOps.exif_transpose(img, in_place=False)

                img.save(output_path, 'JPEG', quality=quality)
                print("save")
        except Exception as e:
            print(f"Error: {e}")
