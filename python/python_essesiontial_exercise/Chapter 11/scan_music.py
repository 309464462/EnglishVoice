import  os
import re
# print(os.getcwd())
# print(os.state('.'))
# def print_music(root,dir,files):
#     for file in files:
#         path = os.path.join(root,file)
#         path = os.path.normcase(path)
#         if not re.search(r".*\.flac",path):continue
#         if re.search(r" ",path):continue
#
#         print(path)
#
# for root, dirs, files in os.walk('F:\\'):
#     print_music(root, dirs, files)
s = ('xxx','abxxxxabc','xyx','abc','x.x','axa','axxxa','axxya')
a = filter((lambda q:re.match(r"xxx",q)),s)
print(*a)
# def action(x):
#     return lambda y:x+y
# b = action(2)
# print(b(22))