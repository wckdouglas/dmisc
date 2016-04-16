import os
import sys

def makeFolder(folder):
    if not os.path.isdir(folder):
        sys.stderr.write('Created %s\n' %folder)
        os.mkdir(folder)
    else:
        sys.stderr.write('%s exists!\n' %folder)
    return 0
