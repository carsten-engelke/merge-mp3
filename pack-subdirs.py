# Group files into subfolders. Create groups from alphabet or create groups of a certain size.
# Carsten Engelke 2018 under MIT-license.
# version:
#    0.1.0  initial port from windows script
#    1.0.0  first working version

import sys
import os
import math
from shutil import copyfile

print ("pack-subdirs 1.0.0 (C)opyright Carsten Engelke 2018")
print ("Use: python pack-subdirs.py [group-size] [dir] [filter] [copy-mode]")
print ("    [group-size] determines the number of files to put into each directory")
print ("    [dir] determines the directory in which to perform the script. Use '.' to select the current directory")
print ("    [filter] Filter the file list according to this")
print ("    [copy-mode] If 'True', the files are copied into the created subfolders. If 'False' they are moved (Use with caution).")

argmax = len(sys.argv)
filenum = 15
suffix = ""
copy = True
dir = os.getcwd()
yes = {'yes','y', 'ja', 'j', ''}
no = {'no','n', 'nein',}
askme = True
if argmax > 1:
    filenum = int(sys.argv[1])
    askme = False
if argmax > 2:
    if sys.argv[2] != ".":
        dir = sys.argv[2]
if argmax > 3:
    suffix = sys.argv[3]
if argmax > 4:
    c = sys.argv[4]
    if c == "0" or c == "move" or c == "Move" or c == "MOVE" or c == "false" or c == "FALSE" or c == "False":
        copy = False

list = []
with os.scandir(dir) as it:
    for entry in it:
        if (entry.name.find(suffix) >= 0 and os.path.isfile(entry)):
            list.append(entry)
            #print(entry)
dirnum = math.ceil(len(list) / filenum)
print("pack-subdirs.py [group-size=" + str(filenum) + "] [dir=" + dir + "] [filter=" + suffix + "] [copy=" + str(copy) +"]")
if (askme):
    print("Pack files according to above settings into subdirectories [y/n]?")
    choice = input().lower()
    if not choice in yes:
        sys.exit()
anz = 0
dirnumactual = 1
dirname = dir + "/subdir-" + str(dirnumactual)
try:
    os.makedirs(dirname)
except:
    print("directory already exists")
for entry in list:
    if anz >= filenum:
        anz = 0
        dirnumactual += 1
        dirname = dir + "/subdir-" + str(dirnumactual)
        print ("create: " + dirname)
        try:
            os.mkdir(dirname)
        except:
            print("directory already exists")
    if copy:
        copyfile(dir + "/" + entry.name, dirname + "/" + entry.name)
        print("FILE_COPIED: " + entry.name)
    else:
        os.rename(dir + "/" + entry.name, dirname + "/" + entry.name)
        print("FILE_MOVED: " + entry.name)
    anz += 1