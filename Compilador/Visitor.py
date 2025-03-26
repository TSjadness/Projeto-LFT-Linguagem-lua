from AbstractVisitor import AbstractVisitor
from ExpressionLanguageParser import *

# global tab
tab = 0

def blank():
    p = ''
    for x in range(tab):
        p = p + ' '
    return p

class Visitor(AbstractVisitor):
    def visitProgramConcrete(self, programConcrete):
        programConcrete.block.accept(self)
      
    def visitProgramConcrete2(self, programConcrete):
        programConcrete.function.accept(self)

    def visitBlockConcrete(self, blockConcrete):
        blockConcrete.command.accept(self)

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

    def visitCommandIf(self, commandIf):
        print('if')
        commandIf.exp.accept(self)
        print('then')
        commandIf.block.accept(self)
        print('end')

    def visitCommandIf2(self, commandIf):
        print('if')
        commandIf.exp.accept(self)
        print('then')
        commandIf.block.accept(self)
        commandIf.else1.accept(self)
     
    def visitCommandIf3(self, commandIf):
        print('if')
        commandIf.exp.accept(self)
        print('then')
        commandIf.block.accept(self)
        commandIf.else_if.accept(self)
        commandIf.else1.accept(self)

    def visitCommandElseIf(self, commandIf):
        print('elseif')
        commandIf.exp.accept(self)
        print('then')
        commandIf.block.accept(self)

    def visitCommandElse(self, commandIf):
        print('else')
        commandIf.block.accept(self)
        print('end')

    def visitCommandElseIf2(self, commandIf):
        print('elseif')
        commandIf.exp.accept(self)
        print('then')
        commandIf.block.accept(self)
        commandIf.else_if.accept(self)

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

    def visitCommandListExps(self, commandListExps):
        commandListExps.exp.accept(self)
        commandListExps.list_exps.accept(self)

    def visitCommandExpNil(self, commandExp):
        commandExp.nil.accept(self)

    def visitBooleanExp(self, booleanExp):
        print(booleanExp.boolValue, end='')
      
    def visitCommandExpNumber(self, commandExp):
        commandExp.number.accept(self)

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
        print('(')
        commandFunction.list_pars.accept(self)
        print(')')
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