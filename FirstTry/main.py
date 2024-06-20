# main.py
from create_c_file import create_c_file
from compile_c_file import compile_c_file
from run_c_executable import run_c_executable

def main():
    c_filename = "hello_world.c"
    executable_name = "hello_world"
    
    # Créer le fichier C
    create_c_file(c_filename)
    
    # Compiler le fichier C
    compile_c_file(c_filename, executable_name)
    
    # Exécuter le fichier exécutable
    run_c_executable(executable_name)

if __name__ == "__main__":
    main()
