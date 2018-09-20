import os

#os.remove("myfile.txt")

#----------

if os.path.exists("myfile.txt"):
  os.remove("myfile.txt")
else:
  print("The file does not exist")

#----------

os.rmdir("myfolder")
