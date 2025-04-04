from lexer.ExpressionLanguageLex import tokens
import syntax.SintaxeAbstrata as sa
import ply.yacc as yacc

precedence = (('left', 'OR'), ('left', 'AND'), ('left', 'GT', 'LT', 'GTEQUALS',
                                                'LTEQUALS', 'EQUALS', 'DIF'),
              ('left', 'CONCAT'), ('left', 'PLUS', 'MINUS'),
              ('left', 'PERCENTUAL', 'TIMES',
               'DIVIDE'), ('left', 'NOT', 'TAG'), ('left', 'EXPO'))


# definição de trecho
def p_program(p):
    '''program : element_list'''
    p[0] = sa.Program(p[1])

def p_element_list(p):
    '''element_list : element
                    | element element_list'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]


def p_element(p):
    '''element : block
               | function'''
    p[0] = p[1]


# definição de bloco
def p_block(p):
    '''block : command
             | command block'''
    if (p[1] == 1):
        p[0] = sa.BlockConcrete(p[1])
    if (p[1] == 2):
        p[0] = sa.BlockConcrete2(p[1], p[2])


def p_command(p):
    '''command : list_vars ATRIB list_exps
               | call_function
               | rotulo
               | BREAK
               | DO block END
               | struct_while
               | struct_repeat
               | if
               | struct_for
               | struct_for_in
               | LOCAL list_vars ATRIB list_exps
               | command_ret'''

    if len(p) == 4 and p[2] == '=':
        p[0] = sa.CommandAtrib(p[1], p[3])

    elif len(p) == 2 and isinstance(p[1], sa.CallFunctionConcrete):
        p[0] = sa.CommandCallFunction(p[1])

    elif len(p) == 2 and isinstance(p[1], sa.ExpRotulo):
        p[0] = sa.CommandRotulo(p[1])

    elif len(p) == 2 and p.slice[1].type == 'BREAK':
        p[0] = sa.CommandBreak()

    elif len(p) == 4 and p.slice[1].type == 'DO':
        p[0] = sa.CommandDoBlockEnd(p[2])

    elif len(p) == 2 and isinstance(p[1], sa.CommandStructWhile):
        p[0] = p[1]  # ✅ Corrigido

    elif len(p) == 2 and isinstance(p[1], sa.CommandStructRepeat):
        p[0] = p[1]

    elif len(p) == 2 and isinstance(p[1], sa.IfConcreteFull):
        p[0] = p[1]

    elif len(p) == 2 and isinstance(p[1], sa.StructForConcrete):
        p[0] = sa.CommandStructFor(p[1])

    elif len(p) == 2 and isinstance(p[1], sa.StructForInConcret):
        p[0] = sa.CommandStructForIn(p[1].list_names, p[1].list_exps, p[1].block)

    elif len(p) == 5 and p.slice[1].type == 'LOCAL' and p[3] == '=':
        p[0] = sa.CommandLocalListVarsAtribListExps(p[2], p[4])

    elif len(p) == 2 and isinstance(p[1], sa.CommandRet):
        p[0] = p[1]



#Retorno da funcao
def p_command_ret(p):
    '''command_ret : RETURN SEMICOLON
                   | RETURN list_exps
                   | RETURN list_exps SEMICOLON'''
    if len(p) == 3 and p[2] == ';':
        p[0] = sa.CommandReturnNone()
    elif len(p) == 3:
        p[0] = sa.CommandReturnListExps(p[2])
    elif len(p) == 4:
        p[0] = sa.CommandReturnListExpsSemicolon(p[2])


# definição de rótulo
def p_rotulo(p):
    '''rotulo : DUALCOLON NAME DUALCOLON'''
    p[0] = sa.ExpRotulo(p[1], p[2], p[3])


# definicao de nomefuncao
def p_name_function(p):
    '''name_function : NAME
                     | NAME COLON NAME'''
    if (len(p) == 2):
        p[0] = sa.NameFunction.ExpNameFunction1(p[1])
    else:
        p[0] = sa.NameFunction.ExpNameFunction2(p[1], p[2], p[3])


# definição de listavars
def p_list_vars(p):
    '''list_vars : var 
                 | var COMMA list_vars'''
    if (len(p) == 2):
        p[0] = sa.ListvarsConcrete1(p[1])
    else:
        p[0] = sa.ListvarsConcrete2(p[1], p[3])


def p_var(p):
    '''var : NAME 
           | prefix_exp COLCH exp RCOLCH'''
    if len(p) == 2:
        p[0] = sa.VarConcrete1(p[1])
    elif len(p) == 5:
        p[0] = sa.VarConcrete2(p[1], p[3])


def p_exp_call_function(p):
    '''exp : prefix_exp args'''
    p[0] = sa.CallFunctionConcrete(p[1], p[2])


def p_prefix_exp(p):
    '''prefix_exp : NAME
                  | LPAREN exp RPAREN
                  | prefix_exp sufix_exp'''
    if len(p) == 2:
        p[0] = sa.PrefixExpName(p[1])
    elif len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = sa.PrefixExpSufix(p[1], p[2])


def p_sufix_exp(p):
    '''sufix_exp : DOT NAME
                 | DOT call_function
                 | COLCH exp RCOLCH'''
    if len(p) == 3:
        if isinstance(p[2], str):
            p[0] = sa.SufixExpDot(p[2])
        else:
            p[0] = sa.SufixExpCall(p[2])
    else:
        p[0] = sa.SufixExpColch(p[2])

        
# definição de listanomes
def p_list_names(p):
    '''list_names : NAME
                  | NAME COMMA list_names'''
    if len(p) == 2:
        p[0] = sa.ListNamesConcrete2(sa.NameConcrete(p[1]))
    else:
        p[0] = sa.ListNamesConcrete1(sa.NameConcrete(p[1]), p[3])


# definição de listaexps
def p_list_exps(p):
    '''list_exps : exp COMMA list_exps
                 | exp'''
    if (len(p) == 3):
        p[0] = sa.ListExpsConcrete1(p[1], p[3])
    else:
        p[0] = sa.ListExpsConcrete2(p[1])


# definição de exp 
def p_exp(p):
    '''exp : NIL 
           | FALSE
           | TRUE 
           | NUMBER
           | STRING 
           | VARARGS 
           | def_function 
           | prefix_exp
           | TAG exp
           | MINUS exp
           | NOT exp
           | exp PLUS exp
           | exp MINUS exp
           | exp TIMES exp
           | exp DIVIDE exp
           | exp EXPO exp
           | exp PERCENTUAL exp
           | exp CONCAT exp
           | exp LT exp
           | exp LTEQUALS exp
           | exp GT exp
           | exp GTEQUALS exp
           | exp EQUALS exp
           | exp DIF exp
           | exp AND exp
           | exp OR exp'''

    if len(p) == 2:
        if p[1] == 'nil':
            p[0] = sa.ExpNil(p[1])
        elif isinstance(p[1], bool):
            p[0] = sa.ExpBool(p[1])
        elif isinstance(p[1], float):
            p[0] = sa.ExpNumber(p[1])
        elif isinstance(p[1], str):
            p[0] = sa.ExpString(p[1])
        else:
            p[0] = p[1]  # fallback
    elif len(p) == 3:
        if p[1] == '#':
            p[0] = sa.ExpTag(p[2])
        elif p[1] == '-':
            p[0] = sa.ExpMinus(p[2], None)
        elif p[1] == 'not':
            p[0] = sa.ExpNot(p[2])
    elif len(p) == 4:
        if p[2] == '+':
            p[0] = sa.ExpPlus(p[1], p[3])
        elif p[2] == '-':
            p[0] = sa.ExpMinus(p[1], p[3])
        elif p[2] == '*':
            p[0] = sa.ExpTimes(p[1], p[3])
        elif p[2] == '/':
            p[0] = sa.ExpDivide(p[1], p[3])
        elif p[2] == '^':
            p[0] = sa.ExpExpo(p[1], p[3])
        elif p[2] == '~=':
            p[0] = sa.ExpDif(p[1], p[3])
        elif p[2] == '%':
            p[0] = sa.ExpPercentual(p[1], p[3])
        elif p[2] == '..':
            p[0] = sa.ExpConcat(p[1], p[3])
        elif p[2] == '<':
            p[0] = sa.ExpLt(p[1], p[3])
        elif p[2] == '<=':
            p[0] = sa.ExpLtEquals(p[1], p[3])
        elif p[2] == '>':
            p[0] = sa.ExpGt(p[1], p[3])
        elif p[2] == '>=':
            p[0] = sa.ExpGtEquals(p[1], p[3])
        elif p[2] == '==':
            p[0] = sa.ExpEquals(p[1], p[3])
        elif p[2] == 'and':
            p[0] = sa.ExpAnd(p[1], p[3])
        elif p[2] == 'or':
            p[0] = sa.ExpOr(p[1], p[3])



def p_call_function(p):
    '''call_function : prefix_exp args'''
    p[0] = sa.CallFunctionConcrete(p[1], p[2])


# definição de deffunção
def p_def_function(p):
    '''def_function : function'''
    p[0] = sa.ConcreteDefFunction(p[1])

def p_args(p):
    '''args : LPAREN list_exps RPAREN'''
    p[0] = sa.ExpArgs1(p[2])

# definição de corpofunção
def p_body_function(p):
    '''body_function : LPAREN RPAREN block END
                     | LPAREN list_pars RPAREN block END'''
    if len(p) == 5:
        p[0] = sa.ConcreteBodyFunction(None, p[3])
    else:
        p[0] = sa.ConcreteBodyFunction(p[2], p[4])


# definição de listapars
def p_list_pars(p):
    '''list_pars : list_names
                 | list_names COMMA VARARGS
                 | VARARGS'''
    if len(p) == 2 and isinstance(p[1], sa.ListNames):
        p[0] = sa.ListParsConcrete1(p[1])
    elif len(p) == 4:
        p[0] = sa.ListPars2(p[1], p[3])
    else:
        p[0] = sa.ListPars3(p[1])


# definicao de função
def p_function(p):
    '''function : FUNCTION name_function body_function'''
    p[0] = sa.FunctionConcrete(p[2], p[3])

def p_name_function(p):
    '''name_function : NAME'''
    p[0] = sa.NameFunctionConcrete(p[1])

# definicao de if
def p_if(p):
    '''if : IF exp THEN block elseif_list else_opt END'''
    p[0] = sa.IfConcreteFull(p[2], p[4], p[5], p[6])

def p_elseif_list(p):
    '''elseif_list : elseif_list ELSEIF exp THEN block
                   | empty'''
    if len(p) == 6:
        p[0] = p[1] + [(p[3], p[5])]
    else:
        p[0] = []

def p_else_opt(p):
    '''else_opt : ELSE block
                | empty'''
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = None

def p_empty(p):
    'empty :'
    pass


# definicao de while
def p_struct_while(p):
    '''struct_while : WHILE exp DO block END'''
    

# definicao de for
def p_struct_for(p):
    '''struct_for : FOR NAME ATRIB exp COMMA exp DO block END
                  | FOR NAME ATRIB exp COMMA exp COMMA exp DO block END'''
    if len(p) == 9:
        p[0] = sa.StructForConcrete(p[4], p[6], p[8])
    elif len(p) == 11:
        p[0] = sa.StructForConcrete(p[4], p[6], p[10], p[8])



# definicao de forin
def p_struct_for_in(p):
    '''struct_for_in : FOR list_names IN list_exps DO block END'''
    p[0] = sa.StructForInConcret(p[2], p[4], p[6])


# definição de repeat
def p_struct_repeat(p):
    '''struct_repeat : REPEAT block UNTIL exp'''
    p[0] = sa.StructRepeatConcrete(p[2], p[4])


# definicao de error
def p_error(p):
    if p:
        print(f"Erro de sintaxe na linha {p.lineno}: {p.value}")
    else:
        print("Erro de sintaxe: fim de entrada inesperado")


# REFERÊNCIAS (NO FINAL DO MANUAL TEM A DEFINIÇÃO DE TUDO)
# LINK DO MANUAL : https://www.lua.org/manual/5.2/pt/manual.html
parser = yacc.yacc()