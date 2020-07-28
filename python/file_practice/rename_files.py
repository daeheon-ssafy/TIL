import os #window에 접근

os.chdir(r'C:\Users\aclass\TIL\python\file_practice\dummy')

filenames = os.listdir('.')

print(filenames)

for filename in filenames:
    os.rename(filename,f'SAMSUNG_{filename}')