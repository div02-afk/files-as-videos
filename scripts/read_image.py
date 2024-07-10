from PIL import Image
import numpy as np
import os,json
count = 0
def read_image(image_path):
    global count
    img = Image.open(image_path)
    read_pixels = np.array(img)
    read_pixels = read_pixels.reshape((-1, 3))
    new_binary_data = read_pixels.flatten().tobytes()
    new_binary_data  = new_binary_data.rstrip(b'\x00')
    # if count == 0:
    #     print(len(new_binary_data))
    file_name = "temp.temp"
    file_size = 0
    # new_binary_data = new_binary_data[0:len(new_binary_data)-1]
    # print(new_binary_data[-1])
    # print(new_binary_data)
    # print(count)
    if count == 0:
        with open('metadata.json', 'wb') as file:
            file.write(new_binary_data)
        count += 1
        
            
        file = open("final/"+file_name, 'wb')
        file.close()
            
        
    else:
        with open('metadata.json', 'r') as f:
            loaded_metadata = json.load(f)
            file_name = loaded_metadata['file_name']
            
        with open("final/"+file_name, 'ab') as file:
            file.write(new_binary_data[:])
        


if __name__ == '__main__':
    contents = os.listdir('../output')
    # os.remove('new_data.mkv')
    # print(contents)
    read_image(f'../tmp/temp_image_{0}.png')
    # for i in range(len(contents)):
    #     read_image(f'../tmp/temp_image_{i}.png')
    #     # read_image(f"../output/frame_{i}.png")
    print("Image read successfully!")