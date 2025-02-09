import os

file_path = "C:\\Users\\mravi\\Personal\\work\python_training\\resources\\number1.txt"

def print_file_data(file_path):
    file = open(file_path)
    for line in file:
        print(line)
    file.close()


file_path = input("Enter file path:")
print(f"Given file : {file_path}")
mode = 'w'
if os.path.exists(file_path):
    mode = 'a'
print(f"File mode is {mode}")
isTruncate = False
file = open(file_path, mode)
while isTruncate is False:
    data = input("Enter data:")
    if data == "stop":
        isTruncate = True
    else:
        file.write(data+'\n')

file.close()

print_file_data(file_path)
