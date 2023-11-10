import os

print('Current directory: ', os.getcwd())
os.mkdir('folder')

if not os.path.isdir('folder'):
    os.mkdir('folder')

os.chdir('folder')
print(os.getcwd())
os.chdir('..')  # Exit directory
print(os.getcwd())

os.chdir('folder')
os.makedirs('One/Two/Three')

file = open('text.txt', 'w')
file.write('This is a text file')

os.rename('text.txt', 'renamed_text.txt')

os.replace('renamed_text.txt', 'folder/renamed_text.txt')

print(os.listdir())

for dirpach, dirnames, filenames in os.walk('.'):
    for dirname in dirnames:
        print('Catalogue: ', os.path.join(dirpach, dirname))
    for filename in filenames:
        print('File: ', os.path.join(dirpach, filename))

os.remove('folder/renamed_text.txt')

os.rmdir('folder/One/Two/Three')

os.removedirs('folder/One/Two')

open('text.txt', 'w').write('Text document')
print(os.stat('text.txt'))
print(os.stat('text.txt').st_size)
