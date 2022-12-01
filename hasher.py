import hashlib
import os
import pathlib


dir=os.path.abspath( os.path.dirname( __file__ ) )
os.chdir(dir)

hash_logic = input('Enter s for SHA256 , Enter m for MD5 : ')
folder_name='SHA256' if hash_logic=='s' else 'MD5'
folder = os.path.join(dir,folder_name)
file_name='{}.txt'.format(folder_name)
result_file=os.path.join(folder,file_name)


hash_list=[]
Buff_size=65535
for file in os.listdir():
    if not file.endswith('.py') and os.path.isfile(file):
        if hash_logic=='s':
            hash=hashlib.sha256()
        else:
            hash=hashlib.md5()
        with open(file,'rb')as f:
            fb=f.read(Buff_size)
            while len(fb)>0:
                hash.update(fb)
                fb=f.read(Buff_size)
            result=file+"   :  "+hash.hexdigest()
        hash_list.append(result)
        print('loading.....')

os.mkdir(folder)
with open(result_file,'w')as f:
    f.write('Used Hash_Logic : ')
    f.write('SHA256\n\n'if hash_logic=='s'else 'MD5\n\n')
    for i in hash_list:    
        f.write(i+'\n')
print('done!!!')
