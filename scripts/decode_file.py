import os
from scripts.video_to_frames import video_to_frames
from scripts.read_image import read_image

def decode_file(file_path):
    video_to_frames(file_path, "output")
    print("Frames extracted successfully!")
    contents = os.listdir('output')

    for i in range(len(contents)):
        # read_image(f'../tmp/temp_image_{i}.png')
        # print("Reading image...",i)
        read_image(f"output/frame_{i}.png")
    os.remove('metadata.json')

    print("Images read successfully!")