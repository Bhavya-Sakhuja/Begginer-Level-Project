import os,shutil 

current_dir = os.getcwd()

audio = ['.mp3','.m4a','.wav','.flac']
video = ['.mp4','.mkv','.mpg']
img = ['.jpeg','.jpg','.png']
documents = ['.doc','.pdf','.txt']

os.makedirs('Audio',exist_ok=True)
os.makedirs('Video',exist_ok=True)
os.makedirs('Image',exist_ok=True)
os.makedirs('Documents',exist_ok=True)
os.makedirs('Others',exist_ok=True)


for root,dirct,files in os.walk(current_dir):
    for file in files:
        full_path = os.path.join(root,file)
        get_ext = os.path.splitext(file)[1]
        if get_ext.lower() == '.py':
            continue
        elif get_ext.lower() in audio:
           shutil.move(full_path,os.path.join(current_dir,'Audio',file))  
        elif get_ext.lower() in video:
           shutil.move(full_path,os.path.join(current_dir,'Video',file)) 
        elif get_ext.lower() in img:
            shutil.move(full_path,os.path.join(current_dir,'Image',file))
        elif get_ext.lower() in documents:
            shutil.move(full_path,os.path.join(current_dir,'Documents',file))
        else:
            shutil.move(full_path,os.path.join(current_dir,'Others',file))