import os

def cleanup():
    if os.path.exists('metadata.json'):
        os.remove('metadata.json')
    if os.path.exists('output.mp4'):
        os.remove('output.mp4')
    if os.path.exists('output'):
        remove_folder_contents('output')
        os.rmdir('output')
    if os.path.exists('tmp'):
        remove_folder_contents('tmp')
        os.rmdir('tmp')
    if os.path.exists('final'):
        remove_folder_contents('final')
        os.rmdir('final')
    
    
    os.mkdir('tmp')
    os.mkdir('output')
    os.mkdir('final')
    
def remove_folder_contents(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            remove_folder_contents(file_path)
            os.rmdir(file_path)
