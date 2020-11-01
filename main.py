import os
import sys

if not(len(sys.argv) == 2):
    print("Not Correct amount of args")
    exit()

path = sys.argv[1]
print("Directory:",path)
print("Files in Directory:",os.listdir(path=path))

#os.chdir(path)
#print(os.listdir(path)
