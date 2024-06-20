import llvmlite.ir as ir
import llvmlite.binding as llvm

def generate_code(ast):
    module = ir.Module(name="my_module")
    func_type = ir.FunctionType(ir.IntType(32), [])
    func = ir.Function(module, func_type, name="main")
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)

    if ast[0] == 'function_definition':
        for statement in ast[2]:
            if statement[0] == 'return':
                ret_val = ir.Constant(ir.IntType(32), statement[2][1])
                builder.ret(ret_val)

    return module

llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()
