from moviepy.editor import VideoFileClip
from PIL import Image
def video_to_frames(video_path, output_path):
    fps = 6
    clip = VideoFileClip(video_path)
    
    
    # Extract frames
    count = 0
    
    num_frames = clip.reader.nframes
    
    print(f"Extracting {num_frames} frames from {video_path}")
    for frame in clip.iter_frames():
        if(count%3 !=0):
            count+=1
            continue
        image = Image.fromarray(frame)
        image.save(f"{output_path}/frame_{count//3}.png")
        image.close()
        count+=1
        
    print(f"Extracted {count} frames from {video_path}")
    clip.close()
if __name__ == "__main__":
    video_to_frames('../output.mp4', '../output/')