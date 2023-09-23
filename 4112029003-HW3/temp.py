import os
import shutil
os.mkdir("CS")


f = open("CS/homework.txt", "w+")
f.write( "4112029003_彭建翔")

f = open('CS/homework.txt', 'r')
lines = f.read() 
print(lines)
print(type(lines))

f.close()

if os.path.exists('CS'):
    shutil.rmtree("CS")
