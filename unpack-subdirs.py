# Ungroup files from subfolders. Create groups from alphabet or create groups of a certain size.
# Carsten Engelke 2018 under MIT-license.
# version:
#    1.0.0  first working version

import sys
import os
import math
from shutil import copyfile

print ("unpack-subdirs 1.0.0 (C)opyright Carsten Engelke 2018")
print ("Use: python unpack-subdirs.py [dir] [filter] [copy-mode]")
print ("    [dir] determines the directory in which to perform the script. Use '.' to select the current directory")
print ("    [subdir-filter] Filter the subdir list according to this")
print ("    [filter] Filter the file list according to this")
print ("    [copy-mode] If 'True', the files are copied into the parent folder. If 'False' they are moved (Use with caution).")

argmax = len(sys.argv)
suffix = ""
copy = True
dir = os.getcwd()
subdirname = "subdir-"
if argmax > 1:
    if sys.argv[1] != ".":
        dir = sys.argv[1]
if argmax > 2:
    subdirname = sys.argv[2]
if argmax > 3:
    suffix = sys.argv[3]
if argmax > 4:
    c = sys.argv[4]
    if c == "0" or c == "move" or c == "Move" or c == "MOVE" or c == "false" or c == "FALSE" or c == "False":
        copy = False

list = []
with os.scandir(dir) as it:
    for entry in it:
        if (entry.name.find(subdirname) >= 0 and os.path.isdir(entry)):
            list.append(entry)
#print(list)

for subdir in list:
    with os.scandir(subdir) as it:
        for entry in it:
            if (entry.name.endswith(suffix) >= 0 and os.path.isfile(entry)):
                if copy:
                    shutil.copyfile(dir + "/" + subdir.name + "/" + entry.name, dir + "/" + entry.name)
                    print("FILE_COPIED: " + entry.name)
                else:
                    os.rename(dir + "/" + subdir.name + "/" + entry.name, dir + "/" + entry.name)
                    print("FILE_MOVED: " + entry.name)
    os.removedirs(subdir)
    print("DIR_REMOVED: " + subdir.name)