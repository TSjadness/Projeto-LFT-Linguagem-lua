# 🌙 **Compilador Lua**

Lua é uma linguagem de programação leve, versátil e projetada para ser utilizada como linguagem de extensão em aplicações. Ela suporta vários paradigmas, como programação procedural, orientada a objetos e funcional. Sua implementação pode ser embutida em programas escritos em C, permitindo um alto grau de personalização e expansibilidade.

O objetivo deste projeto é criar um **Compilador Lua** utilizando o PLY (Python Lex-Yacc), dividindo as etapas em:

- **Análise Léxica**
- **Análise Sintática**
- **Geração de Árvore Sintática Abstrata (AST)**

---

## 🌟 **1. Visão Geral**

### 🔗 **O que é Lua?**
Lua é uma linguagem de extensão que oferece:
- **Flexibilidade** para criar linguagens personalizadas.
- **Eficiência** com implementações leves e rápidas.
- **Integração** com programas escritos em C.

Um programa Lua não possui um ponto de entrada principal, sendo controlado pelo programa hospedeiro. O hospedeiro pode chamar funções, manipular variáveis e registrar funções em C para serem chamadas pelo código Lua.

> A linguagem é **software livre**, sem garantias, e pode ser baixada no site oficial [Lua.org](http://www.lua.org/docs.html).

---

## 🛠️ **2. Estrutura do Projeto**

### 🌑 **2.1 Análise Léxica (PLY)** ✅
A análise léxica identifica os **tokens** da linguagem (palavras-chave, identificadores, números, etc.) e gera uma representação formal para a próxima etapa do compilador.

#### 📂 **Arquivos Disponíveis**:
<!-- - **Documentação PDF:** [Análise Léxica da Linguagem Lua](https://github.com/Clovijan/Compilador_Lua/blob/main/DOCUMENTACAO/Documenta%C3%A7%C3%A3o%20da%20Linguagem%20Lua.pdf)
- **Código:** [ExpressionLanguageLex.py](https://github.com/Clovijan/Compilador_Lua/blob/main/COMPILADOR_LUA/ExpressionLanguageLex.py) -->

#### 📝 **Funções Implementadas**:
- **Identificação de Tokens:**
  - Palavras-chave (e.g., `if`, `while`, `function`)
  - Operadores e delimitadores (e.g., `+`, `-`, `{`, `}`)
  - Literais (e.g., strings, números)

---

### 🌒 **2.2 Análise Sintática (Grámatica Livre de Contexto)** ✅
A análise sintática valida a estrutura da linguagem com base em uma grámatica definida, gerando uma **Árvore de Derivação**.

#### 📂 **Arquivos Disponíveis**:
<!-- - **Documentação PDF:** [Análise Sintática da Linguagem Lua](https://github.com/Clovijan/Compilador_Lua/blob/main/DOCUMENTACAO/Documenta%C3%A7%C3%A3o%20Sint%C3%A1tica%20da%20Linguagem%20LUA.pdf)
- **Código:** [ExpressionLanguageParser.py](https://github.com/Clovijan/Compilador_Lua/blob/main/COMPILADOR_LUA/ExpressionLanguageParser.py) -->

#### 📝 **Funções Implementadas**:
- **Regras de Grámatica:**
  - Estruturas de controle (e.g., `if`, `for`)
  - Declaração de variáveis e funções
  - Expressões matemáticas e lógicas
- **Geração da Árvore de Derivação:**
  - Representação hierárquica da estrutura do programa.

---

### 🌓 **2.3 Árvore Sintática Abstrata (AST)** 🚧
A geração da **AST** (Abstract Syntax Tree) está em desenvolvimento. Esta etapa transforma a árvore de derivação em uma representação mais compacta e direta do código.

#### 📈 **Objetivos Futuros**:
- **Simplificar a representação da lógica do programa.**
- **Facilitar a geração de código ou execução direta do programa.**

---

## 🚀 **3. Colaboradores**

### 👨🏾‍🏫 **Orientador**:
- [**André Luiz**](https://github.com/andreluisms)

### 👨‍🎓 **Discentes**:
- [**Jadson Tavares**](https://github.com/TSjadness)
- [**Tiago Santiago**](https://github.com/Ti4goS)
- [**Jose Geilson**](https://github.com/geilso)
- [**Jhonatas Nascimento**]()

---

## 📚 **4. Referências**

- [**Documentação Oficial do Lua**](http://www.lua.org/docs.html)
- [**Documentação Oficial do PLY**](https://www.dabeaz.com/ply/ply.html)
- [**Linguagem Sue (Exemplo)**](https://github.com/andreluisms/LinguagemSue)

---

## 🛠️ **5. Exemplos e Inspiração**
- **[Linguagem Sue](https://github.com/andreluisms/LinguagemSue):** Um exemplo de implementação com estrutura semelhante.

### **Nota Final**:
Este projeto segue as melhores práticas para implementação de compiladores, garantindo qualidade e manutenção a longo prazo. Acompanhe o progresso nos repositórios compartilhados!

