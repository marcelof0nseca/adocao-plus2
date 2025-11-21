# 🐾 Sistema de Adoção de Animais

Um sistema completo desenvolvido em Python para auxiliar no gerenciamento de um abrigo de animais: cadastro, cuidados, alertas, recomendações e sugestões inteligentes.

---

## 📂 Estrutura do Projeto


---

## 🐶 CRUD de Animais (`CrudAnimais.py`)

Responsável por todas as operações relacionadas aos animais do abrigo.

### Funcionalidades:
- ➕ Adicionar animal  
- 👁️ Visualizar animais  
- ✏️ Editar dados  
- 🎨 Cores para melhorar o terminal  
- 🆔 IDs automáticos  
- 🔄 Integração com outros módulos

### Dados armazenados:
- ID  
- Nome  
- Espécie  
- Sexo  
- Raça  
- Idade  
- Saúde  
- Comportamento  
- Data de chegada  

---

## 📝 Cadastro de Cuidados (`CadastroDeCuidados.py`)

Gerencia tarefas e atividades importantes para cada animal.

### Funcionalidades:
- Cadastrar tarefa  
- Listar tarefas  
- Editar  
- Excluir  
- Carregar e salvar dados  

### Cada tarefa contém:
- ID do animal  
- Descrição  
- Responsável  
- Data prevista  

---

## ⏳ Contagem Regressiva (`ContagemRegressiva.py`)

Sistema de alertas baseado na data prevista das tarefas.

### Funções principais:
- **exibir_alertas()**  
  Exibe todos os cuidados classificados por cores:
  - 🟥 Atrasado  
  - 🟨 Próximo (≤ 7 dias)  
  - 🟩 Dentro do prazo  

- **verificar_alertas_proximos()**  
  Retorna apenas os cuidados que vencem em breve.

- **exibir_alertas_proximos()**  
  Mostra no terminal apenas os itens urgentes.

---

## 🤝 Recomendador de Animais (`Recomendador.py`)

Sugere o melhor animal com base no perfil do adotante.

### Critérios de análise:
- Espécie desejada  
- Idade ideal  
- Temperamento  
- Tipo de lar  
- Compatibilidade  

Resultado:
- Lista de possíveis animais  
- Destaque com o mais recomendado  

---

## ⭐ Sugestões Personalizadas (`SugestoesPersonalizadas.py`)

Gera recomendações automáticas com base em **espécie + idade**.

### Gera:
- Tipo de adotante ideal  
- Cuidados necessários  
- Compatibilidade  
- Atividades recomendadas  

Exemplo:  
*“Gato de 2 anos → alimentação balanceada, ambiente enriquecido, compatível com outros gatos calmos.”*

---

## 🎮 Menu Principal (`main.py`)

Arquivo principal que integra todos os módulos.

### Opções do menu:


---

## ▶️ Como Executar

1. Entre na pasta do projeto  
2. Execute no terminal:

```bash
python main.py
