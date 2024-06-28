import ply.lex as lex
import ply.yacc as yacc

# --- Lexer ---

# Liste des tokens
tokens = (
    'INT',
    'MAIN',
    'RETURN',
    'PRINTF',
    'STRING',
    'NUMBER',
    'LBRACE',
    'RBRACE',
    'LPAREN',
    'RPAREN',
    'SEMICOLON',
)

# Définitions des tokens
t_INT = r'int'
t_MAIN = r'main'
t_RETURN = r'return'
t_PRINTF = r'printf'
t_STRING = r'\".*?\"'
t_NUMBER = r'\d+'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# --- Parser ---

# Définition des règles de grammaire
def p_program(p):
    '''program : INT MAIN LPAREN RPAREN LBRACE statements RBRACE'''
    p[0] = ('main', p[6])

def p_statements(p):
    '''statements : statement
                  | statements statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : PRINTF LPAREN STRING RPAREN SEMICOLON
                 | RETURN NUMBER SEMICOLON'''
    if p[1] == 'printf':
        p[0] = ('printf', p[3])
    else:
        p[0] = ('return', p[2])

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

# --- Génération de code assembleur ---

class AsmGenerator:
    def __init__(self):
        self.asm_code = []

    def generate(self, node):
        method_name = 'gen_' + node[0]
        method = getattr(self, method_name, self.gen_default)
        return method(node)

    def gen_main(self, node):
        self.asm_code.append(".section .data")
        self.generate_statements(node[1])
        self.asm_code.append(".section .text")
        self.asm_code.append(".globl _start")
        self.asm_code.append("_start:")
        self.generate_statements(node[1])
        self.asm_code.append("mov rax, 60")  # syscall: exit
        self.asm_code.append("xor rdi, rdi")  # status 0
        self.asm_code.append("syscall")
        return '\n'.join(self.asm_code)

    def generate_statements(self, statements):
        for stmt in statements:
            self.generate(stmt)

    def gen_printf(self, node):
        _, string = node
        string_label = f'str_{len(self.asm_code)}'
        self.asm_code.append(f'{string_label}: .asciz {string}')
        self.asm_code.append(f"""
        # Print message
        mov rax, 1
        mov rdi, 1
        mov rsi, {string_label}
        mov rdx, {len(string) - 2}
        syscall
        """)
        self.asm_code.append("mov rsp, rbp")  # Restore stack pointer

    def gen_return(self, node):
        _, value = node
        self.asm_code.append(f"""
        # Return
        mov rdi, {value}
        mov rax, 60
        syscall
        """)

    def gen_default(self, node):
        raise Exception(f'No generate method for {node[0]}')

# --- Test complet ---

with open('test.c', 'r') as f:
    data = f.read()

# Lexing and parsing
lexer.input(data)
ast = parser.parse(data)

# Generating assembly
asm_gen = AsmGenerator()
asm_code = asm_gen.generate(ast)
print(asm_code)
