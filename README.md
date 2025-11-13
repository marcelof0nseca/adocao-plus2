# 🐾 Sistema de Adoção de Animais

Este projeto implementa um sistema simples de cadastro e gerenciamento de animais para adoção, utilizando *Python* e **manipulação de arquivos .txt**.  
Ele foi desenvolvido com o objetivo de aplicar conceitos fundamentais de lógica de programação, estruturas condicionais, funções e persistência de dados.

---

## ✅ *Objetivos do Projeto*

- Registrar novos animais disponíveis para adoção  
- Armazenar os dados em um arquivo de texto
- Listar todos os animais cadastrados
- Manter a organização das informações em formato tabular
- Demonstrar domínio de:
  - Funções em Python
  - Manipulação de arquivos (open, read, write)
  - Tratamento de erros
  - Estruturas de repetição e decisão

---

## 📁 *Estrutura do Projeto*

### 🗂 Descrição dos Arquivos

- *adocaoDeAnimais.py*  
  Contém o código principal do sistema: menu, funções de cadastro, listagem e validação.

- *animais.txt*  
  Arquivo que armazena os registros dos animais. Cada linha representa um animal.

- *README.md*  
  Documento com explicação técnica do projeto, como executar e detalhes funcionais.

### 🗂 Explicação
- *adocaoDeAnimais.py*: contém o menu, funções de cadastro, listagem e lógica do sistema.  
- *animais.txt*: arquivo usado para armazenar os animais cadastrados.  
- *README.md*: documentação detalhada do projeto, instruções e aspectos técnicos.

---

## 🧠 *Principais Conceitos Técnicos Utilizados*

### ✅ 1. *Funções*
O código divide tarefas em funções, como:
- Adicionar animal  
- Listar animais  
- Validar entradas do usuário  
- Organizar os dados antes de gravar  

Isso deixa o programa mais modular, limpo e reutilizável.

---

### ✅ 2. *Manipulação de Arquivos*
Foi utilizado:

```python
open('animais.txt', 'a')
open('animais.txt', 'r')