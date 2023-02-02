#! python3
#! osREmovingFiles
import os
for filename in os.listdir(r'/home/an5/Desktop/'):
   if filename.endswith('.rxt'):
   #os.unlink(filename)
      print(filename)
