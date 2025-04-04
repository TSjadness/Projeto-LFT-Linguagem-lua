# -*- coding: utf-8 -*-
from lexer.ExpressionLanguageLex import lexer
from parser.ExpressionLanguageParser import parser
from visitor.Visitor import Visitor
from syntax.SintaxeAbstrata import *
import sys


PATH = "../arquivos_lua/teste3.lua"


def analisar_codigo(codigo):
    print("="*50)
    print("Código de entrada:")
    print(codigo)
    print("="*50)

    lexer.input(codigo)

    try:
        # Salvar o debug em arquivo
        with open("debug.txt", "w") as debug_file:
            original_stdout = sys.stdout  # Salva a saída original
            sys.stdout = debug_file       # Redireciona para o arquivo

            result = parser.parse(debug=False)

            sys.stdout = original_stdout  # Restaura a saída normal

        print("\nAnálise sintática concluída com sucesso.")
        print("Debug salvo em 'debug.txt'.")

        if result is None:
            print("Erro: análise sintática falhou.")
        else:
            print("\nIniciando análise semântica:\n")
            visitor = Visitor()
            result.accept(visitor)
            print("\nAnálise semântica finalizada.")
    except Exception as e:
        sys.stdout = original_stdout  # Em caso de erro, restaura saída
        print("Erro durante a análise:")
        print(e)


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
