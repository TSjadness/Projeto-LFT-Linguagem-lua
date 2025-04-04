# -*- coding: utf-8 -*-
from lexer.ExpressionLanguageLex import lexer
from parser.ExpressionLanguageParser import parser
from visitor.Visitor import Visitor
from syntax.SintaxeAbstrata import *


PATH = "../arquivos_lua/calculadora.lua"


def analisar_codigo(codigo: str, debug=False):
    print("\n" + "=" * 50)
    print("Código de entrada:")
    print(codigo.strip())
    print("=" * 50 + "\n")
    
    lexer.input(codigo)
    result = parser.parse(debug=debug)

    if result is None:
        print("Erro: análise sintática falhou. Verifique seu código.")
    else:
        print("Análise sintática concluída com sucesso.")
        print("\nIniciando análise semântica:\n")
        visitor = Visitor()
        result.accept(visitor)
        print("\nAnálise semântica finalizada.")


def carregar_arquivo_lua(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Arquivo '{path}' não encontrado.")
        return None


if __name__ == "__main__":
    codigo = carregar_arquivo_lua(PATH)
    if codigo:
        analisar_codigo(codigo)
