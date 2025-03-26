from abc import abstractmethod, ABCMeta


class AbstractVisitor(metaclass=ABCMeta):
    @abstractmethod
    def visitProgramConcrete(self, programConcrete):
        pass

    @abstractmethod
    def visitProgramConcrete2(self, programConcrete2):
        pass

    @abstractmethod
    def visitBlockConcrete(self, blockConcrete):
        pass

    @abstractmethod
    def visitBlockConcrete2(self, blockConcrete2):
        pass

    @abstractmethod
    def visitCommandAtrib(self, commandAtrib):
        pass

    @abstractmethod
    def visitCommandExpCallFunction(self, commandExpCallFunction):
        pass

    @abstractmethod
    def visitCommandCallFunction(self, commandCallFunction):
        pass

    @abstractmethod
    def visitCommandBreak(self, commandBreak):
        pass

    @abstractmethod
    def visitCommandDoBlockEnd(self, commandDoBrlockEnd):
        pass

    @abstractmethod
    def visitCommandStructWhile(self, StructWhileConcret):
        pass

    @abstractmethod
    def visitCommandStructFor1(self, StructForConcret1):
        pass

    @abstractmethod
    def visitCommandStructFor2(self, StructForConcret2):
        pass

    @abstractmethod
    def visitCommandStructRepeat(self, structRepeatConcrete):
        pass

    @abstractmethod
    def visitCommandStructForIn(self, structForInConcret):
        pass

    @abstractmethod
    def visitCommandStructFor(self, commandStructFor):
        pass

    @abstractmethod
    def visitCommandDefFunction(self, commandDefFunction):
        pass

    @abstractmethod
    def visitCommandRotulo(self, commandRotulo):
        pass

    @abstractmethod
    def visitCommandDoEnd(self, commandDoEnd):
        pass

    @abstractmethod
    def visitCommandLocalListVarsAtribListExps(
            self, commandLocalListVarsAtribListExps):
        pass

    @abstractmethod
    def visitCommandIf(self, ifConcrete):
        pass

    @abstractmethod
    def visitCommandIf2(self, ifConcrete2):
        pass

    @abstractmethod
    def visitCommandIf3(self, ifConcrete3):
        pass

    @abstractmethod
    def visitCommandElseIf1(self, concreteElseIf1):
        pass

    @abstractmethod
    def visitCommandElse(self, concreteElse):
        pass

    @abstractmethod
    def visitCommandElseIf2(self, concreteElseIf2):
        pass

    @abstractmethod
    def visitCommandRet(self, commandRetConcrete):
        pass

    @abstractmethod
    def visitExpRotulo(self, expRotulo):
        pass

    @abstractmethod
    def visitExpNameFunction1(self, expNameFunction1):
        pass

    @abstractmethod
    def visitExpNameFunction2(self, expNameFunction2):
        pass

    @abstractmethod
    def visitCommandListvars1(self, listvarsConcrete1):
        pass

    @abstractmethod
    def visitCommandListvars2(self, listvarsConcrete2):
        pass

    @abstractmethod
    def visitCommandVar1(self, varConcrete1):
        pass

    @abstractmethod
    def visitCommandVar2(self, varConcrete2):
        pass

    @abstractmethod
    def visitListNamesConcrete1(self, listNamesConcrete1):
        pass

    @abstractmethod
    def visitListNamesConcrete2(self, listNamesConcrete2):
        pass

    @abstractmethod
    def visitListExpsConcrete1(self, ListExpsConcrete1):
        pass

    @abstractmethod
    def visitListExpsConcrete2(self, ListExpsConcrete1):
        pass

    @abstractmethod
    def visitCommandExpPrefixExp(self, commandExpPrefixExp):
        pass

    @abstractmethod
    def visitCommandTag(self, commandTag):
        pass

    @abstractmethod
    def visitCommandMinus(self, commandMinus):
        pass

    @abstractmethod
    def visitCommandNot(self, commandNot):
        pass

    @abstractmethod
    def visitCommandPlus(self, commandPlus):
        pass

    @abstractmethod
    def visitCommandDivide(self, commandDivide):
        pass

    @abstractmethod
    def visitCommandExpo(self, commandExpo):
        pass
      
    @abstractmethod
    def visitConcreteDefFunction(self, concreteDefFunction):
        pass

    @abstractmethod
    def visitFunctionConcrete(self, functionConcrete):
        pass

    @abstractmethod
    def visitCommandFunction(self, commandFunction):
        pass

    @abstractmethod
    def visitCommandNameFunction(self, commandName):
        pass

    @abstractmethod
    def visitCommandListvars(self, commandListvars):
        pass

    @abstractmethod
    def visitCommandVar(self, commandVar):
        pass

    @abstractmethod
    def visitCommandListNames(self, commandListNames):
        pass

    @abstractmethod
    def visitCommandListExps(self, commandListExps):
        pass

    @abstractmethod
    def visitCommandExpNil(self, commandExp):
        pass

    @abstractmethod
    def visitBooleanExp(self, booleanExp):
        pass

    @abstractmethod
    def visitCommandExpNumber(self, commandExpNumber):
        pass

    @abstractmethod
    def visitCommandExpString(self, commandExp):
        pass

    @abstractmethod
    def visitCommandExpTag(self, commandExp):
        pass

    @abstractmethod
    def visitCommandExpMinus(self, commandExp):
        pass

    @abstractmethod
    def visitCommandExpNot(self, commandExp):
        pass

    @abstractmethod
    def visitCommandExpPlus(self, commandExp):
        pass

    @abstractmethod
    def visitCommandExpDivide(self, commandExp):
        pass

    @abstractmethod
    def visitCommandExpExpo(self, commandExp):
        pass

    @abstractmethod
    def visitCommandExpPercentual(self, commandExp):
        pass

    @abstractmethod
    def visitCommandExpConcat(self, commandExp):
        pass

    @abstractmethod
    def visitCommandExpLt(self, commandExp):
        pass

    @abstractmethod
    def visitCommandExpLtEquals(self, commandExp):
        pass

    @abstractmethod
    def visitCommandExpGt(self, commandExp):
        pass

    @abstractmethod
    def visitCommandExpGtEquals(self, commandExp):
        pass

    @abstractmethod
    def visitCommandExpEquals(self, commandExp):
        pass

    @abstractmethod
    def visitCommandExpDif(self, commandExp):
        pass

    @abstractmethod
    def visitCommandExpAnd(self, commandExp):
        pass

    @abstractmethod
    def visitCommandExpOr(self, commandExp):
        pass

    @abstractmethod
    def visitCommandPrefix1(self, commandPrefix):
        pass

    @abstractmethod
    def visitCommandPrefix2(self, commandPrefix):
        pass

    @abstractmethod
    def visitCommandArgs(self, commandArgs):
        pass

    @abstractmethod
    def visitCommandArgs2(self, commandArgs):
        pass

    @abstractmethod
    def visitCommandBodyFunction(self, commandFunction):
        pass

    @abstractmethod
    def visitBodyFunction(self, commandBodyFunction):
        pass

    @abstractmethod
    def visitCommandListPars(self, listPars):
        pass

    @abstractmethod
    def visitCommandListPars2(self, listPars2):
        pass

    @abstractmethod
    def visitCommandListPars3(self, listPars3):
        pass

    @abstractmethod
    def visitCommandLocalVar(self, localVarConcrete):
        pass

    @abstractmethod
    def visitCommandLocalVar2(self, localVarConcrete2):
        pass

    @abstractmethod
    def visitCommandLocalVar3(self, localVarConcrete3):
        pass
