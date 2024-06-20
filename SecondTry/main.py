from lexer import lexer
from parser import parser
from codegen import generate_code
import llvmlite.binding as llvm

def main():
    with open('test.c', 'r') as file:
        data = file.read()

    lexer.input(data)
    for token in lexer:
        print(token)

    ast = parser.parse(data)
    print(ast)

    module = generate_code(ast)
    llvm_ir = str(module)
    print(llvm_ir)

    with open("output.ll", "w") as f:
        f.write(llvm_ir)

    llvm.initialize()
    llvm.initialize_native_target()
    llvm.initialize_native_asmprinter()

    target = llvm.Target.from_default_triple()
    target_machine = target.create_target_machine()
    with llvm.create_mcjit_compiler(module, target_machine) as execution_engine:
        execution_engine.finalize_object()
        execution_engine.run_static_constructors()
        
        main_ptr = execution_engine.get_function_address("main")

if __name__ == '__main__':
    main()
