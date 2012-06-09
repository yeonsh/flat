#!/usr/bin/python

import os
import sys
import string

if len(sys.argv) != 2:
    print "usage: " + sys.argv[0] + " <directory>"
    exit(0)

fileList = []
rootdir = sys.argv[1]

for root, subFolders, files in os.walk(rootdir):
    for file in files:
        filename = os.path.join(root,file)
        fileList.append(filename)
        #print filename

print fileList

for filename in fileList:
    new_filename = string.replace(filename, "/", "__")
    print filename + " : " + new_filename
    os.rename(filename, new_filename)
