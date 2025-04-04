from visitor.AbstractVisitor import AbstractVisitor
import syntax.SintaxeAbstrata as sa

# global tab
tab = 0

def blank():
    p = ''
    for x in range(tab):
        p = p + ' '
    return p


class Visitor(AbstractVisitor):
    def __init__(self):
        self.tabela_simbolos = {}

        
    def visitProgram(self, program):
        for element in program.body:
            if element is not None:
                element.accept(self)
            

    def visitBlockConcrete2(self, node):
        node.command.accept(self)

    def visitBodyFunction(self, node):
        print("(", end="")
        node.list_pars.accept(self)
        print(")")
        node.block.accept(self)

    def visitCommandAtrib(self, node):
        node.list_vars.accept(self)
        print(" = ", end="")
        node.list_exps.accept(self)

    def visitCommandBreak(self, node):
        print("break")

    def visitCommandDivide(self, node):
        node.exp.accept(self)
        print(" / ", end="")
        node.exp2.accept(self)

    def visitCommandDoBlockEnd(self, node):
        print("do")
        node.block.accept(self)
        print("end")

    def visitCommandElseIf1(self, node):
        print("elseif ", end="")
        node.exp.accept(self)
        print(" then")
        node.block.accept(self)

    def visitCommandExpCallFunction(self, node):
        node.exp_prefix.accept(self)
        node.args.accept(self)

    def visitCommandExpPrefixExp(self, node):
        node.prefix_exp.accept(self)

    def visitCommandExpo(self, node):
        node.exp.accept(self)
        print(" ^ ", end="")
        node.exp2.accept(self)

    def visitCommandListvars1(self, node):
        node.var.accept(self)

    def visitCommandListvars2(self, node):
        node.var.accept(self)
        print(", ", end="")
        node.list_vars.accept(self)

    def visitCommandLocalListVarsAtribListExps(self, node):
        print("local ", end="")
        node.list_vars.accept(self)
        print(" = ", end="")
        node.list_exps.accept(self)

    def visitCommandMinus(self, node):
        node.exp.accept(self)
        print(" - ", end="")
        node.exp2.accept(self)

    def visitCommandNot(self, node):
        print("not ", end="")
        node.exp.accept(self)

    def visitCommandPlus(self, node):
        node.exp.accept(self)
        print(" + ", end="")
        node.exp2.accept(self)

    def visitCommandStructFor1(self, node):
        print("for ", end="")
        node.name.accept(self)
        print(" = ", end="")
        node.exp1.accept(self)
        print(", ", end="")
        node.exp2.accept(self)
        print(" do")
        node.block.accept(self)
        print("end")

    def visitCommandStructFor2(self, node):
        print("for ", end="")
        node.name.accept(self)
        print(" = ", end="")
        node.exp1.accept(self)
        print(", ", end="")
        node.exp2.accept(self)
        print(", ", end="")
        node.exp3.accept(self)
        print(" do")
        node.block.accept(self)
        print("end")

    def visitCommandTag(self, node):
        print("#", end="")
        node.exp.accept(self)

    def visitCommandVar1(self, node):
        node.name.accept(self)

    def visitCommandVar2(self, node):
        node.prefix_exp.accept(self)
        print("[", end="")
        node.exp.accept(self)
        print("]", end="")

    def visitConcreteDefFunction(self, node):
        print("function", end="")
        node.body_function.accept(self)

    def visitExpArgs1(self, node):
        print("(", end="")
        node.list_exps.accept(self)
        print(")", end="")

    def visitExpNameFunction1(self, node):
        node.name.accept(self)

    def visitExpNameFunction2(self, node):
        node.name1.accept(self)
        print(".", end="")
        node.name2.accept(self)
        print(":", end="")
        node.name3.accept(self)

    def visitExpRotulo(self, node):
        print("::", end="")
        node.name.accept(self)
        print("::", end="")

    def visitListExpsConcrete1(self, node):
        node.exp.accept(self)
        print(", ", end="")
        node.list_exps.accept(self)

    def visitListExpsConcrete2(self, node):
        node.exp.accept(self)

    def visitListNamesConcrete1(self, node):
        node.name.accept(self)
        print(", ", end="")
        node.list_names.accept(self)

    def visitListNamesConcrete2(self, node):
        node.name.accept(self)

#incompleto esse
    def visitCommandCallFunction(self, commandCallFunction):
        commandCallFunction.exp_prefix.accept(self)
        commandCallFunction.args.accept(self)

    def visitCommandStructWhile(self, commandWhile):
        print(blank(), 'while', end='', sep='')
        commandWhile.exp.accept(self)
        print('do', end='', sep='')
        commandWhile.block.accept(self)
        print('end', end='', sep='')

    def visitCommandRotulo(self, commandRotulo):
        print(blank(), '::', end='', sep='')
        commandRotulo.name.accept(self)
        print('::', end='', sep='')

    def visitCommandDoEnd(self, commandDoEnd):
        print(blank(), 'do', end='', sep='')
        commandDoEnd.block.accept(self)
        print('end', end='', sep='')

    def visitCommandStructRepeat(self, commandStructRepeat):
        print(blank(), 'repeat ', end='', sep='')
        commandStructRepeat.block.accept(self)
        print('until ', end='')
        commandStructRepeat.exp.accept(self)

    def visitIfConcreteFull(self, node):
        print("if ", end='')
        node.cond.accept(self)
        print(" then")
        node.bloco.accept(self)

        for cond, bloco in node.elseif_list:
            print("elseif ", end='')
            cond.accept(self)
            print(" then")
            bloco.accept(self)

        if node.else_block:
            print("else")
            node.else_block.accept(self)
        
        print("end")

    def visitCommandStructForIn(self, commandStructForIn):
        print(blank(), 'for ', end='', sep='')
        commandStructForIn.list_names.accept(self)
        print('in ', end='', sep='')
        commandStructForIn.list_exps.accept(self)
        print('do ', end='', sep='')
        commandStructForIn.block.accept(self)
        print('end')

    def visitCommandStructFor(self, commandStructFor):
        print(blank(), 'for ', end='', sep='')
        commandStructFor.name.accept(self)
        print(' = ')
        commandStructFor.exp.accept(self)
        print(' == ')
        commandStructFor.exp.accept(self)
        print(' do ', sep='')
        commandStructFor.block.accept(self)
        print(' end ', end='', sep='')

    def visitCommandRet1(self, commandRet):
        print('return;')

    def visitCommandRet2(self, commandRet):
        print('return')
        commandRet.list_exps.accept(self)

    def visitCommandRet3(self, commandRet):
        print('return')
        commandRet.list_exps.accept(self)
        print(';')

    def visitPrefixExpSufix(self, node):
        node.prefix.accept(self)
        node.sufix.accept(self)

    def visitSufixExpColch(self, node):
        return f"[{self.visit(node.exp)}]"
        
    def visitSufixExpDot(self, node):
        print(".", end="")
        print(node.name, end="")

    def visitPrefixExpName(self, prefixExpName):
        print(prefixExpName.name, end='')

    def visitSufixExpCall(self, node):
        print(".", end="")
        node.call_function.accept(self)

    def visitFunctionConcrete(self, functionConcrete):
        print('function ', end='')
        functionConcrete.name_function.accept(self)
        functionConcrete.body_function.accept(self)

    def visitNameFunctionConcrete(self, node):
        print(node.name, end='') 



    def visitCommandDefFunction(self, commandDefFunction):
        commandDefFunction.function.accept(self)

    def visitCommandFunction(self, commandFunction):
        print('function')
        commandFunction.name_function.accept(self)
        commandFunction.body_function.accept(self)

    def visitCommandNameFunction(self, commandName):
        commandName.name.accept(self)

    def visitCommandListvars(self, commandListvars):
        commandListvars.var.accept(self)
        commandListvars.list_vars.accept(self)

    def visitCommandVar(self, commandVar):
        commandVar.name.accept(self)
        commandVar.prefix_exp.accept(self)
        commandVar.exp.accept(self)

    def visitCommandListNames(self, commandListNames):
        commandListNames.name.accept(self)
        commandListNames.list_names.accept(self)

    def visitNameConcrete(self, node):
        nome = node.value
        if nome in self.tabela_simbolos:
            print(f"Erro: variável '{nome}' já declarada.")
        else:
            self.tabela_simbolos[nome] = {"tipo": "parametro", "linha": node.linha}

    def visitCommandListExps(self, commandListExps):
        commandListExps.exp.accept(self)
        commandListExps.list_exps.accept(self)

    def visitCommandExpNil(self, commandExp):
        commandExp.nil.accept(self)

    def visitBooleanExp(self, booleanExp):
        print(booleanExp.boolValue, end='')

    def visitCommandExpTimes(self, commandExp):
        commandExp.exp.accept(self)
        print('*', end='')
        commandExp.exp2.accept(self)

    def visitExpPercentual(self, exp):
        exp.left.accept(self)
        print(" % ", end="")
        exp.right.accept(self)

    def visitExpConcat(self, exp):
        exp.left.accept(self)
        print(" .. ", end="")
        exp.right.accept(self)

    def visitExpLt(self, exp):
        exp.left.accept(self)
        print(" < ", end="")
        exp.right.accept(self)

    def visitExpLtEquals(self, exp):
        exp.left.accept(self)
        print(" <= ", end="")
        exp.right.accept(self)

    def visitExpGt(self, exp):
        exp.left.accept(self)
        print(" > ", end="")
        exp.right.accept(self)

    def visitExpGtEquals(self, exp):
        exp.left.accept(self)
        print(" >= ", end="")
        exp.right.accept(self)

    def visitExpEquals(self, exp):
        exp.left.accept(self)
        print(" == ", end="")
        exp.right.accept(self)

    def visitExpAnd(self, exp):
        exp.left.accept(self)
        print(" and ", end="")
        exp.right.accept(self)

    def visitExpOr(self, exp):
        exp.left.accept(self)
        print(" or ", end="")
        exp.right.accept(self)


    def visitCommandExpNumber(self, commandExp):
        print(f"{commandExp.number}", end='')

    def visitCommandExpString(self, commandExp):
        commandExp.string.accept(self)

    def visitCommandExpTag(self, commandExp):
        print('tag')
        commandExp.exp.accept(self)

    def visitCommandExpMinus(self, commandExp):
        commandExp.exp.accept(self)  
        print('-')
        commandExp.exp2.accept(self)
       
    def visitCommandExpNot(self, commandExp):
        print('not')
        commandExp.exp.accept(self)

    def visitCommandExpPlus(self, commandExp):
        commandExp.exp.accept(self)
        print('+')
        commandExp.exp2.accept(self)

    def visitCommandExpDivide(self, commandExp):
        commandExp.exp.accept(self)
        print('/')
        commandExp.exp2.accept(self)

    def visitCommandExpDif(self, commandExp):
        commandExp.exp1.accept(self)
        print("~=", end='')
        commandExp.exp2.accept(self)

    def visitExpPercentual(self, node):
        node.left.accept(self)
        node.right.accept(self)

    def visitExpConcat(self, node):
        node.left.accept(self)
        node.right.accept(self)

    def visitExpLt(self, node):
        node.left.accept(self)
        node.right.accept(self)

    def visitExpLtEquals(self, node):
        node.left.accept(self)
        node.right.accept(self)

    def visitExpGt(self, node):
        node.left.accept(self)
        node.right.accept(self)

    def visitExpGtEquals(self, node):
        node.left.accept(self)
        node.right.accept(self)

    def visitExpEquals(self, node):
        node.left.accept(self)
        node.right.accept(self)

    def visitExpAnd(self, node):
        node.left.accept(self)
        node.right.accept(self)

    def visitExpOr(self, node):
        node.left.accept(self)
        node.right.accept(self)

    def visitCommandExpExpo(self, commandExp):
        commandExp.exp.accept(self)
        print('^')
        commandExp.exp2.accept(self)

    def visitCommandExpPercentual(self, commandExp):
        commandExp.exp.accept(self)
        print('%')
        commandExp.exp2.accept(self)

    def visitCommandExpConcat(self, commandExp):
        commandExp.exp.accept(self)
        print('..')
        commandExp.exp2.accept(self)

    def visitCommandExpLt(self, commandExp):
        commandExp.exp.accept(self)
        print('<')
        commandExp.exp2.accept(self)

    def visitCommandExpLtEquals(self, commandExp):
        commandExp.exp.accept(self)
        print('<=')
        commandExp.exp2.accept(self)

    def visitCommandExpGt(self, commandExp):
        commandExp.exp.accept(self)
        print('>')
        commandExp.exp2.accept(self) 

    def visitCommandExpGtEquals(self, commandExp):
        commandExp.exp.accept(self)
        print('>=')
        commandExp.exp2.accept(self)

    def visitCommandExpEquals(self, commandExp):
        commandExp.exp.accept(self)
        print('==')
        commandExp.exp2.accept(self)

    def visitCommandExpDif(self, commandExp):
        commandExp.exp.accept(self)
        print('~=')
        commandExp.exp2.accept(self)

    def visitCommandExpAnd(self, commandExp):
        commandExp.exp.accept(self)
        print('and')
        commandExp.exp2.accept(self)

    def visitCommandExpOr(self, commandExp):
        commandExp.exp.accept(self)
        print('or')
        commandExp.exp2.accept(self)
   
    def visitCommandPrefix1(self, commandPrefix):
        commandPrefix.var.accept(self)

    def visitCommandPrefix2(self, commandPrefix):
        commandPrefix.call_function.accept(self)

    def visitCommandArgs(self, commandArgs):
        print('(')
        commandArgs.list_exps.accept(self)
        print(')')

    def visitCommandArgs2(self, commandArgs):
        print('()')

    def visitCommandBodyFunction(self, commandFunction):
        if commandFunction.list_pars:
            commandFunction.list_pars.accept(self)
        if commandFunction.block:
            commandFunction.block.accept(self)

    def visitCommandListPars(self, commandListPars):
        commandListPars.list_names.accept(self)

    def visitCommandListPars2(self, commandListPars):
        commandListPars.list_names.accept(self)
        print('=')
        commandListPars.varargs.accept(self)

    def visitCommandListPars3(self, commandListPars):
        commandListPars.varags.accept(self)

    def visitCommandListFields(self, commandListFields):
        commandListFields.field.accept(self)

    def visitCommandListFields2(self, commandListFields):
        commandListFields.field.accept(self)          
        commandListFields.separator_fields.accept(self)
        commandListFields.list_fields.accept(self)

    def visitCommandListFields3(self, commandListFields):
        commandListFields.field_empty.accept(self)

    def visitCommandListFields4(self, commandListFields):
        commandListFields.field_empty.accept(self)                    
        commandListFields.separator_fields.accept(self)
        commandListFields.list_fields.accept(self)

    def visitCommandListFieldEmpty(self, commandListField):
        commandListField.field_empty.accept(self)

    def visitCommandListField(self, commandListField):
        print('[')
        commandListField.exp.accept(self)
        print(']')
        print('==')
        commandListField.exp.accept(self)

    def visitCommandListField2(self, commandListField):
        commandListField.name.accept(self)
        print('==')
        commandListField.exp.accept(self)

    def visitCommandSeparatorFields(self, commandListField):
        print('=')

    def visitCommandSeparatorFields2(self, commandListField):
        print(';')

    def visitCommandLocalVar(self, commandLocalVar):
        print('LOCAL')
        commandLocalVar.list_names.accept(self)
        print('==')
        commandLocalVar.list_exps.accept(self)

    def visitCommandLocalVar2(self, commandLocalVar):
        print('LOCAL')
        commandLocalVar.list_names.accept(self)

    def visitCommandLocalVar3(self, commandLocalVar):
        print('LOCAL')
        commandLocalVar.list_names.accept(self)
        print('==')
        commandLocalVar.exp.accept(self)
