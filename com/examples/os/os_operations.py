import os
from typing import List

isFile = os.path.isfile("some_path")
print("Is file ", isFile)

isDir = os.path.isdir("some_dir path")
print("Is Directory ", isDir)

# os.remove("C:\\Users\\mravi\\Personal\\work\\python_training\\resources\\employee1.csv")
# os.removedirs("some directory path")

# os.rename("current name", "new name")

# import shutil
# shutil.copy("src file", "destination file")


def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        prev2 = 1
        prev1 = 2
        current = 0
        for step in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
            print(current, prev1, prev2)

        return prev1

climbStairs(5)