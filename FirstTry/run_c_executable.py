# run_c_executable.py
import subprocess

def run_c_executable(executable_name):
    try:
        result = subprocess.run([f"./{executable_name}"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Output of {executable_name}:\n{result.stdout.decode()}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run {executable_name}. Error: {e.stderr.decode()}")
