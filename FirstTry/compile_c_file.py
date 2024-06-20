# compile_c_file.py
import subprocess

def compile_c_file(c_filename, executable_name):
    try:
        result = subprocess.run(["gcc", c_filename, "-o", executable_name], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"{c_filename} has been compiled into {executable_name}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to compile {c_filename}. Error: {e.stderr.decode()}")
