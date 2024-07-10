import numpy as np
from PIL import Image
if __name__ == '__main__':
    from read_file import read_file
def create_image_with_redundancy(data, block_size=10):
    # Convert data to binary
    binary_data = ''.join(format(byte, '08b') for byte in data)
    print(binary_data)
    
    # Calculate the number of blocks needed
    num_blocks = len(binary_data)
    num_pixels_per_block = block_size * block_size
    total_pixels_needed = num_blocks * num_pixels_per_block

    # Calculate the required image dimensions
    image_size = int(np.ceil(np.sqrt(total_pixels_needed)))
    if image_size % block_size != 0:
        image_size = (image_size // block_size + 1) * block_size

    # Create an empty image with white background
    image = np.full((image_size, image_size, 3), 255, dtype=np.uint8)

    # Fill the image with the binary data
    index = 0
    for i in range(0, image_size, block_size):
        for j in range(0, image_size, block_size):
            if index+24 < len(binary_data):
                byte1 = int(str(binary_data[index:index + 8]),2)
                byte2 = int(str(binary_data[index + 8:index + 16]),2)
                byte3 = int(str(binary_data[index + 16:index + 24]),2)
                
                color = (byte1, byte2, byte3)
                print(color)
                for x in range(block_size):
                    for y in range(block_size):
                        image[i + x, j + y] = color
                index += 24

    return Image.fromarray(image)

# data = b"Hello, World!"  # Example data
# image = create_image_with_redundancy(data)
# image.save('encoded_image.png')

if __name__ == "__main__":
    data = read_file("../tmp.mkv")
    i = 0
    while(len(data)  != 0):
        index = max(len(data),1920*108)
        image = create_image_with_redundancy(data[:index])
        image.save(f'../tmp/encoded_image_{i}.png')
        print(f"Encoded image {i} created successfully!")
        data = data[index:]
    print("Encoded image created successfully!")