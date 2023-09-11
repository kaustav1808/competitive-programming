import sys
import os

newFile = sys.argv[1]

if newFile is None: raise SystemExit("Please mention a file name.")

fileDef = os.path.splitext(newFile)

fileName = fileDef[0]
fileExt = fileDef[1]

if not len(fileExt): fileName += ".py"
else: fileName = newFile 


#open the stub file
fstub = open("stub.txt", "r")
fnewfile = open(fileName, "w")

fnewfile.write(fstub.read())

fnewfile.close()
fstub.close()

print("Successfully create new file {newFile}".format(newFile=fileName))

