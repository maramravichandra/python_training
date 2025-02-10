import subprocess

#subprocess.run(["cp", "src_file_path", "destination_file_path"])
#subprocess.run(["dir"], )
subprocess.run(["python", "--version"])
subprocess.run(["python ", "C:\\Users\\mravi\\Personal\\work\python_training\\com\\examples\\functions\\lamda_functions.py"])

code = """
for num in range(1,10):
    print("Number ", num)
"""
subprocess.run(['python'], input=code, encoding="UTF-8")
