import json,os
from PIL import Image
import numpy as np
from scripts.create_pixel_values import create_image
from scripts.reshape_and_save import create_reshaped_image
from scripts.read_file import read_file
from scripts.create_video import create_video

def encode_file(file_path):
    
    file_name = file_path
    file = open(file_name, 'rb')
    metadata = {
        "file_name": file.name,
        "size": 100,
    }
    file.close()

    with open('metadata.json', 'w') as f:
        json.dump(metadata, f)

    binary_data = read_file(file_name)
    binary_metadata = read_file('metadata.json')
    pixels = add_padding(binary_data)
    meta_data = add_padding(binary_metadata)
    # complete_image = Image.new('RGB', (20000,20000))
    pixel_values = create_image(pixels)
    metadata_values = create_image(meta_data)
    img_res = 360
    create_reshaped_image(metadata_values,img_res , img_res, 0)
    create_reshaped_image(pixel_values, img_res , img_res,1)
    print("Encoded Images created successfully!")
    create_video()
    os.remove('metadata.json')
    
def add_padding(binary_data):
    
    padding = (3 - len(binary_data) % 3) % 3
    binary_data +=  b'\x00' * padding
    pixels = np.frombuffer(binary_data, dtype=np.uint8)
    pixels = pixels.reshape((-1, 3))
    return pixels

