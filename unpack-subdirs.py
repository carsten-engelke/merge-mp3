# Ungroup files from subfolders. Create groups from alphabet or create groups of a certain size.
# Carsten Engelke 2018 under MIT-license.
# version:
#    1.0.0  first working version

import sys
import os
from shutil import copyfile

print ("unpack-subdirs 1.0.0 (C)opyright Carsten Engelke 2018")
print ("Use: python unpack-subdirs.py [dir] [subdir-filter] [filter] [copy-mode] [remove-dir]")
print ("    [dir] determines the directory in which to perform the script. Use '.' to select the current directory")
print ("    [subdir-filter] Filter the subdir list according to this. Use '*' to select any subdirectory")
print ("    [filter] Filter the file list according to this")
print ("    [copy-mode] If 'True', the files are copied into the parent folder. If 'False' they are moved (Use with caution).")
print ("    [remove-dir] If 'True', the subdirectories are deleted. If 'False' they are left as they are.")

argmax = len(sys.argv)
suffix = ""
copy = False
remove = True
dir = os.getcwd()
subdirname = "subdir-"
yes = {'yes','y', 'ja', 'j', ''}
no = {'no','n', 'nein',}
askme = True
if argmax > 1:
    if sys.argv[1] == "-h" or sys.argv[1] == "-help" or sys.argv[1] == "-H" or sys.argv[1] == "-HELP" or sys.argv[1] == "-Help":
        sys.exit(0)
    if sys.argv[1] != ".":
        dir = sys.argv[1]
    askme = False
if argmax > 2:
    subdirname = sys.argv[2]
if argmax > 3:
    suffix = sys.argv[3]
if argmax > 4:
    c = sys.argv[4]
    if c == "0" or c == "move" or c == "Move" or c == "MOVE" or c == "false" or c == "FALSE" or c == "False":
        copy = False
if argmax > 5:
    c = sys.argv[5]
    if c == "0" or c == "false" or c == "False" or c == "FALSE":
        remove = False
print("unpackdirs: " + str(dir) + " subdirname:" + subdirname + "suffix:" + suffix + " copy:" + str(copy) + " remove:" + str(remove))
if (askme):
    print("Unpack files according to above settings into subdirectories [y/n]?")
    choice = input().lower()
    if not choice in yes:
        sys.exit()
list = []
with os.scandir(dir) as it:
    for entry in it:
        if (subdirname == "*" and os.path.isdir(entry)):
            list.append(entry)
        else:
            if (entry.name.find(subdirname) >= 0 and os.path.isdir(entry)):
                list.append(entry)
#print(list)

for subdir in list:
    with os.scandir(subdir) as it:
        for entry in it:
            if (entry.name.find(suffix) >= 0 and os.path.isfile(entry)):
                if copy:
                    copyfile(dir + "/" + subdir.name + "/" + entry.name, dir + "/" + entry.name)
                    print("FILE_COPIED: " + entry.name)
                else:
                    os.rename(dir + "/" + subdir.name + "/" + entry.name, dir + "/" + entry.name)
                    print("FILE_MOVED: " + entry.name)
    if (remove):
        os.removedirs(subdir)
        print("DIR_REMOVED: " + subdir.name)