import os,shutil
os.makedirs('Test_Files',exist_ok=True)
def move_file(file,folder):
               name,ext=os.path.splitext(file)
               path=os.path.join('Test_Files',folder)
               os.makedirs(path,exist_ok=True)
               counter=1
               new_file=file
               while (os.path.exists(os.path.join(path,new_file))):
                        new_file=f"{name}_{counter}{ext}"
                        counter+=1
               shutil.move(os.path.join('Test_Files',file),os.path.join(path,new_file))
for file in os.listdir('Test_Files'):
         if os.path.isfile(os.path.join('Test_Files',file)) :
                 name,ext=os.path.splitext(file)
                 if ext in ['.jpg', '.jpeg', '.png', '.gif', '.webp']:
                   move_file(file,'Images')
                 elif ext in ['.pdf', '.docx', '.doc', '.txt']:
                         move_file(file,'Documents')
                 elif ext in ['.mp3', '.wav', '.aac'] :
                         move_file(file,'Audio')
                 elif ext in ['.mp4', '.mkv', '.avi', '.mov']:
                         move_file(file,'Videos')
                 elif ext in ['.csv', '.xlsx', '.json']:
                         move_file(file,'Data')
                 elif ext in ['.zip', '.rar', '.7z'] :
                         move_file(file,'Archives')
                 else:
                         move_file(file,'Others')
         
                
                
                      
        
        
        
        
        
        
    