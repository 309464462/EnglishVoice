import  os
import re
# print(os.getcwd())
# print(os.state('.'))
def print_music(root,dir,files):
    for file in files:
        path = os.path.join(root,file)
        path = os.path.normcase(path)
        if re.search(r".*\.flac",path):
            print(path)

for root, dirs, files in os.walk('F:\\'):
    print_music(root, dirs, files)