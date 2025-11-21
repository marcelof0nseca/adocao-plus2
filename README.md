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
```

# Area de desenvolvimento :
## 🧩 Divisão de Funcionalidades do Projeto

Abaixo estão listadas as principais funcionalidades complementares ao CRUD do sistema, com a descrição e responsabilidades de cada módulo.  
Cada funcionalidade será implementada em **arquivos separados**, e todas serão integradas no **arquivo principal** através de **importações**.

---

### 1. 📅 Módulo de Cadastro de Tarefas (`tarefas.py`) - Marcelo

**Descrição:**  
Permite cadastrar, visualizar e gerenciar tarefas relacionadas a cada animal (como vacinas, banhos, consultas veterinárias, treinos, etc.).

**Principais funções:**
- `cadastrar_tarefa(id_animal, descricao, data, responsavel)`
- `listar_tarefas(id_animal)`
- `remover_tarefa(id_animal, id_tarefa)`
- `editar_tarefa(id_animal, id_tarefa)`

**Objetivo:**  
Registrar as atividades programadas para cada animal com base no **ID** cadastrado no CRUD.

---

### 2. ⏰ Módulo de Contagem Regressiva e Alertas (`alertas.py`) - Mateus
**Descrição:**  
Exibe quantos dias faltam para as próximas tarefas importantes, vacinas ou consultas de cada animal.

**Principais funções:**
- `dias_para_evento(data_evento)`
- `exibir_alertas(id_animal)`
- `verificar_alertas_proximos()`

**Objetivo:**  
Avisar o usuário sobre tarefas próximas da data marcada, gerando um sistema de **alerta automático** ao acessar o animal.

---

### 3. 💾 Módulo de Armazenamento de Dados (`armazenamento.py`) - Mateus
**Descrição:**  
Garante o salvamento e leitura de todos os registros (animais, tarefas, adoções) em arquivos `.csv` ou `.txt`.

**Principais funções:**
- `salvar_dados(tipo, dados)`
- `ler_dados(tipo)`
- `atualizar_dados(tipo, novos_dados)`

**Objetivo:**  
Manter o histórico completo de informações de forma organizada e persistente.

---

### 4. 💡 Módulo de Sugestões Personalizadas (`sugestoes.py`) - Mafra
**Descrição:**  
Com base nas informações dos animais (idade, espécie e comportamento), o sistema sugere possíveis adotantes, cuidados especiais e atividades de socialização.

**Principais funções:**
- `gerar_sugestoes(id_animal)`
- `avaliar_compatibilidade(id_animal_1, id_animal_2)`
- `sugerir_cuidados_especiais(id_animal)`

**Objetivo:**  
Fornecer recomendações automáticas para melhorar o bem-estar e a adoção dos animais.

---

### 5. 🌟 Funcionalidade Extra (`extra.py`) - Everyone
**Descrição:**  
Espaço para implementação de ideias criativas adicionais, como:
- Relatórios estatísticos de adoções.
- Ranking de animais mais ativos.
- Sistema de pontuação por cuidados realizados.

**Objetivo:**  
Tornar o sistema mais completo, interativo e inovador.

---


##integrantes
-Marcelo
-Gabriel
-Joao
-Meira
-Eduardo