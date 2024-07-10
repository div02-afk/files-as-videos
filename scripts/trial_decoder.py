from PIL import Image
import numpy as np

def decode_image_with_redundancy(image_path, block_size=10):
    image = Image.open(image_path)
    image_data = np.array(image)
    print(image_data)
    binary_data = ''
    for i in range(0, image_data.shape[0], block_size):
        for j in range(0, image_data.shape[1], block_size):
            block = image_data[i:i + block_size, j:j + block_size]
            avg_color = np.mean(block, axis=(0, 1))
            bit = 1 if avg_color[0] < 128 else 0
            binary_data += str(bit)

    # Convert binary data to bytes
    byte_data = bytearray()
    for i in range(0, len(binary_data), 8):
        byte_chunk = binary_data[i:i + 8]
        byte_data.append(int(byte_chunk, 2))

    return bytes(byte_data).rstrip(b'\x00')

decoded_data = decode_image_with_redundancy('encoded_image.png')
print(decoded_data.decode())
