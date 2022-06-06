import os

path = "/home/kikazei/n0zer0.github.io/images"

files = os.listdir(path)
files_file = [f for f in files if os.path.isfile(os.path.join(path, f))]
print(files_file)

f = open('/home/kikazei/n0zer0.github.io/files', 'w', encoding='UTF-8')

f.write(str(files_file))
f.close()