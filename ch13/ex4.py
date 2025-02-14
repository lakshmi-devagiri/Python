#(Issuing system command called “dir *.py > list.txt”)
#(The directory contents will be copied to list.txt file)
import os
cmd='dir *.py > list.txt'
os.system(cmd)