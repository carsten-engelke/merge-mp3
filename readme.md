# merge-mp3
Merge mp3 files and set correct audio length using foobar2000 with an automated python script. This script can merge all files in one directory or create one file for each subdirectory.
![merge mp3 files from subdirectories](/mergemp3subdirs.jpg)

## Version
0.1.0 initial release. Port from windows script to python, introducing automation

0.2.0 bug corrected foobar needs to be called from working directory as the command line plugin cannot handle empty spaces in file names or paths given by command line

## Requirements
- Python (script was created using python 3.7.0) (https://www.python.org/)
- foobar2000 (https://www.foobar2000.org/)

## Installation
- copy mergeMp3.py into the directory in which the files to merge are contained.
- run the script and follow the instructions, alternatively use the following command line

Command-line-use:
```
python mergeMp3.py [dir] [sub] [foobarpath] [autowaittime]
    [dir] determines the directory in which to perform. Use '.' to select the current directory
    [sub] determines wheter all mp3 files in subfolders should be merged into one file each. ('true' to do so)")
    [foobarpath] determines the path to your foobar2000 installation. Please provide in case it differs from 'C:/Program Files (x86)/foobar2000/foobar2000.exe'
    [autowaittime] determines whether to automatically clos foobar2000 after some seconds. Use -1 to disable and any number to set the waiting time.
```
