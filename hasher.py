import hashlib
import os
import pathlib

dir=os.path.abspath( os.path.dirname( __file__ ) )
os.chdir(dir)
folder_name='hash_result'
folder = os.path.join(dir,folder_name)
file_name='{}.txt'.format(folder_name)
result_file=os.path.join(folder,file_name)

hash_list=[]
Buff_size=65535
for file in os.listdir():
    if not file.endswith('.py'):
        hash=hashlib.sha256()
        with open(file,'rb')as f:
            fb=f.read(Buff_size)
            while len(fb)>0:
                hash.update(fb)
                fb=f.read(Buff_size)
            result=file+"   :  "+hash.hexdigest()
        hash_list.append(result)  

os.mkdir(folder)
with open(result_file,'w')as f:
    for i in hash_list:    
        f.write(i+'\n')
print('done!!!')