import numpy as np
from PIL import Image

def reshape_to_image(pixel_values, width=4096, height=2160,i=0):
    # print(i,"Reshaping to image")
    num_pixels = width * height
    current_num_pixels = pixel_values.shape[0]
    new_size = (1000, 1000)
    # Pad with zeros if there are not enough pixels
    if current_num_pixels < num_pixels:
        padding = num_pixels - current_num_pixels
        pixel_values = np.vstack([pixel_values, np.zeros((padding, 3), dtype=np.uint8)])
        image_data = pixel_values.reshape((height, width, 3))
        img = Image.fromarray(image_data, 'RGB')
        # img  = img.resize(new_size)
        img.save(f'tmp/temp_image_{i}.png')
        return -1
    
    # Truncate if there are too many pixels
    elif current_num_pixels > num_pixels:
        next_pixel_values = pixel_values[num_pixels:]
        pixel_values = pixel_values[:num_pixels]
        image_data = pixel_values.reshape((height, width, 3))
        img = Image.fromarray(image_data, 'RGB')
        # img  = img.resize(new_size)
        img.save(f'tmp/temp_image_{i}.png')
        # print("Image saved successfully! ",i)
        i+=1
        return (next_pixel_values, width, height,i)
        
def create_reshaped_image(pixel_values, width=1920, height=1080,i=0):
    x = (pixel_values, width, height,i)
    print(x)
    while(x !=-1):
        x = reshape_to_image(x[0],x[1],x[2],x[3])
        # print(x)
    
    