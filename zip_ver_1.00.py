import os,zipfile
from pathlib import Path

dir=os.path.abspath( os.path.dirname( __file__ ) )
os.chdir(dir)
for file in os.listdir():
    if not file.endswith('.py'):        
        myzip=zipfile.ZipFile(file+'.zip','w')
        myzip.write(file,compress_type=zipfile.ZIP_DEFLATED)
        myzip.close
print('zip done!!')