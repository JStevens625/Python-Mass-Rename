import os
import sys

if (len(sys.argv) == 2):
    os.chdir(sys.argv[1])
    appendName = os.getcwd().split('\\')[len(os.getcwd().split('\\'))-1]
    for folder in os.listdir():
        newFolderName = folder +"_"+ appendName
        os.rename(folder,newFolderName)