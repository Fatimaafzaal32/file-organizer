import os
list_of_files=['photo.jpg','picture.png','notes.txt','report.pdf','data.csv','song.mp3','video.mp4','data.csv','randon.xyz']

for file in list_of_files:
    path=os.path.join('Test_Files',file)
    if not os.path.exists(path):
        open(path,'w').close()