import os
import sys

files = os.listdir()

for file in files:
    os.system("cp " + "\"{0}\"".format(file) + " " + sys.argv[1])

