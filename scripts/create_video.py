from moviepy.editor import ImageSequenceClip, concatenate_videoclips
import os

def create_video():
    if __name__ == "__main__":
        tmp = '../tmp'
    else:
        tmp = 'tmp'
    contents = os.listdir(tmp)
    
    print(f"Creating video from {len(contents)} frames")
    for i in range(len(contents)):
        contents[i] = f'{tmp}/'+contents[i]
    clip = ImageSequenceClip(contents, fps=2)
    
    clip.write_videofile('output.mp4', codec='png',bitrate = "100000k", fps=2)
    
if __name__ == "__main__":
    create_video()
    # print("Video created successfully!