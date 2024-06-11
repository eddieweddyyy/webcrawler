import os

files = os.listdir('fileos_test') #relative directory
files = os.listdir('C:\Users\CKIRUser\Desktop\coding_eddie') #absolute directory

for i in os.listdir('fileos_test'):
    if 'jpg' in i:
        os.rename(f'fileos_test/{i}', f'fileos_test/a{i}')

for i in os.listdir('fileos_test'):
    os.rename(r'C:\Users\CKIRUser\Desktop\coding_eddie' + f'fileos_test/{i}', f'fileos_test/a{i}')


os.path.join('path1', 'path2')

for i in os.listdir('fileos_test'):
    os.rename(os.path.join(r'C:\Users\CKIRUser\Desktop\coding_eddie', f'fileos_test/{i}'), f'fileos_test/a{i}')

os.getcwd() #absolute directory

import shutil

for i in os.listdir('fileos_test'):
    if 'jpg' in i:
        shutil.copy(f'fileos_test/{i}', f'fileos_test2/{i}')
    