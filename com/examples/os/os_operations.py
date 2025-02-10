import os

isFile = os.path.isfile("some_path")
print("Is file ", isFile)

isDir = os.path.isdir("some_dir path")
print("Is Directory ", isDir)

os.remove("C:\\Users\\mravi\\Personal\\work\\python_training\\resources\\employee1.csv")
os.removedirs("some directory path")

os.rename("current name", "new name")

import shutil
shutil.copy("src file", "destination file")