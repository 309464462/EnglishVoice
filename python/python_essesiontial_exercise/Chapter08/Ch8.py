import os
import sys
# import shutil
#asdf
# def print_line_lengths():
#         a=open("test.txt","r")
#         text=a.readlines()
#         for line in text:
#             print(line+"%d\n"%(len(line)-1))
#
# print_line_lengths()
# #Splitting a path completely into directory names using a recursive function
# def split_fully(path):
#         parent_path, name = os.path.split(path)
#         if name == "":
#             return (parent_path, )
#         else:
#             print(name)
#             return split_fully(parent_path) + (name, )
# split_fully(sys.path[1])
#
#     # A function that lists the contents of a directory
# # but prints full paths instead of just the file and directory names
# def print_dir(dir_path):
#     for name in os.listdir(dir_path):
#         print(os.path.join(dir_path, name))

# print_dir(sys._home)
#
# import  time
# mod_time = os.path.getmtime(sys.path[1])
# print(time.ctime(mod_time))


# #Listing directory contents, sorted by file extension
#     def cmp_extension(path0, path1):
#         return cmp(os.path.splitext(path0)[1], os.path.splitext(path1)[1])
#
#
#     def print_dir_by_ext(dir_path):
#         for name in sorted(os.listdir(dir_path), cmp_extension):
#             print(os.path.join(dir_path, name))
#
#     #Processing subdirectories recursively
#     def print_tree(dir_path):
#         for name in os.listdir(dir_path):
#             full_path = os.path.join(dir_path, name)
#             print(full_path)
#             if os.path.isdir(full_path):
#                 print_tree(full_path)
#
#     #Now you know how to modify print dir to print
#     #the contents of a directory. The following code
#     #prints only the names of the entries, not their full paths:
#     def print_dir_info(dir_path):
#         for name in os.listdir(dir_path):
#             full_path = os.path.join(dir_path, name)
#             file_size = os.path.getsize(full_path)
#             mod_time = time.ctime(os.path.getmtime(full_path))
#             print("%-32s: %8d bytes, modified %s" % (name, file_size, mod_time))
#
#     #A function that rotates the next-older version of the log-file before
#     #overwriting it:
#

#
#     def make_version_path(path, version):
#         if version == 0:
#             # No suffix for version 0, the current version.
#             return path
#         else:
#             # Append a suffix to indicate the older version.
#             return path + "." + str(version)
#
#     def rotate(path, version=0):
#         # Construct the name of the version wee rotating.
#         old_path = make_version_path(path, version)
#         if not os.path.exists(old_path):
#             # It doesn't exist, so complain.
#             raise IOError("'%s' doesn't exist" % path)
#         # Construct the new version name for this file.
#         new_path = make_version_path(path, version + 1)
#         # Is there already a version with this name?
#         if os.path.exists(new_path):
#             # Yes.  Rotate it out of the way first!
#             rotate(path, version + 1)
#         # Now we can rename the version safely.
#         shutil.move(old_path, new_path)
#
#     #A function that rotates a log file that may or may not exist, creating it first
#     #if it does not:
#
#     def rotate_log_file(path):
#         if not os.path.exists(path):
#             # The file is missing, so create it.
#             new_file = file(path, "w")
#             # Close the new file immediately, which leaves it empty.
#             del new_file
#         # Now rotate it.
#         rotate(path)
#

import  glob
# print(glob.glob("D:\\Program Files\\M*"))
# ['D:\\Program Files\\MariaDB 10.1', 'D:\\Program Files\\Microsoft VS Code', 'D:\\Program Files\\MinGW', 'D:\\Program Files\\mysql-5.7.19-winx64']
# print(glob.glob("D:\\Program Files\\[ASDF]*"))
# ['D:\\Program Files\\Adobe', 'D:\\Program Files\\Android', 'D:\\Program Files\\apache-tomcat-7.0.75', 'D:\\Program Files\\arduino-1.8.5', 'D:\\Program Files\\Autodesk', 'D:\\Program Files\\data', 'D:\\Program Files\\SoftMgr', 'D:\\Program Files\\speed', 'D:\\Program Files\\Sublime Text 3']
# print(glob.glob("D:\\Program Files\\[!ZXCVBNMASDFGHJKQWERTYU]*"))

print(glob.glob("D:\\Program Files\\*.txt"))