#! python3
#! FileSize
import os
totalSize = 0
for filename in os.listdir('C:\\Windows'):
   totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows', filename))
print(totalSize)
