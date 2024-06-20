# create_c_file.py
def create_c_file(filename):
    c_code = """
    #include <stdio.h>

    int main() {
        printf("Hello, World!\\n");
        return 0;
    }
    """
    with open(filename, 'w') as file:
        file.write(c_code)
    print(f"{filename} has been created.")
