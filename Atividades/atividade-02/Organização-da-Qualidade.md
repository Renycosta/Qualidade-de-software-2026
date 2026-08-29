# Atividade 2: Organização da Qualidade no LocalEats

## 1. Identificação

**Turma:** ADS 4º Semestre Manhã (Pelotas)  
**Equipe:** Reny Brito da Costa  
**Data:** 25/08/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Reny Brito da Costa | [@Renycosta](https://github.com/Renycosta) |

**Elemento de Competência:** Identificar papéis, responsabilidades e competências relacionadas às atividades de qualidade e testes.

---

## 2. Tarefa 1: Diagnóstico da situação

### 2.1 Problemas organizacionais

| Problema identificado | Possível consequência para o produto ou para a equipe |
|---|---|
| Os critérios para considerar uma funcionalidade como pronta não estão claros. | Funcionalidades podem ser disponibilizadas mesmo apresentando defeitos ou sem terem sido devidamente testadas, afetando a qualidade do produto. |
| Os defeitos identificados não são sempre registrados ou acompanhados. | Defeitos podem ser esquecidos ou voltar a ocorrer, dificultando o controle da qualidade e aumentando a quantidade de problemas no produto. |
| algumas atividades são realizadas por mais de uma pessoa, enquanto outras não possuem responsável definido. | Algumas atividades podem ficar sem serem realizadas, enquanto outras podem ser feitas por mais de uma pessoa, causando desorganização e desperdício de tempo. |

### 2.2 Responsabilidade pela qualidade

**A qualidade do LocalEats deve ser responsabilidade exclusiva do profissional de QA? Justifiquem.**

A qualidade de um produto não é responsabilidade exclusiva do QA por que ela deve ser construída durante todo o processo de desenvolvimento, e não apenas verificada no final. Cada integrante da equipe possui uma responsabilidade diferente: 
desenvolvedores devem produzir código de qualidade e corrigir defeitos, 
analistas e responsáveis pelos requisitos devem garantir que as funcionalidades estejam bem definidas,
QA deve planejar e executar testes e identificar problemas,
gestores devem organizar processos e responsabilidades.

---

## 3. Tarefa 2: Papéis e competências

| Integrante | Papel analisado | Responsabilidades relacionadas à qualidade | Competências técnicas | Competências comportamentais |
|---|---|---|---|---|
| Reny | Analista de sistemas/negócio | Levantar e documentar requisitos, esclarecer dúvidas sobre as funcionalidades e garantir que os requisitos estejam bem definidos. | Análise de requisitos, modelagem de sistemas e documentação. | Comunicação, capacidade de análise, organização e trabalho em equipe. |
| Reny | Desenvolvedor | Implementar as funcionalidades, realizar testes durante o desenvolvimento, corrigir defeitos e garantir a qualidade do código. | Programação, banco de dados, testes e controle de versão (Git). | Trabalho em equipe, atenção aos detalhes, responsabilidade e resolução de problemas. |
| Reny | QA/Analista de qualidade | Planejar e executar testes, identificar e registrar defeitos, acompanhar suas correções e verificar se os critérios de qualidade foram atendidos. | Testes funcionais, testes de integração, automação de testes e gerenciamento de defeitos. | Pensamento crítico, atenção aos detalhes, comunicação e imparcialidade. |
| Reny | Liderança técnica | Definir padrões técnicos, orientar os desenvolvedores, revisar decisões técnicas e garantir que boas práticas sejam seguidas. | Arquitetura de software, programação, revisão de código, Git e padrões de desenvolvimento. | Liderança, comunicação, tomada de decisão, orientação e trabalho em equipe. |

---

## 4. Tarefa 3: Matriz de responsabilidades

Utilizem:

- **R:** responsável por executar a atividade;
- **A:** aprovador ou responsável final;
- **C:** consultado antes da execução ou decisão;
- **I:** informado sobre o resultado.

| Atividade de qualidade | Analista de sistemas/negócio | Desenvolvedor | QA/Analista de qualidade | Liderança técnica |
|---|:---:|:---:|:---:|:---:|
| Definir critérios de aceitação | R/A | C | C | C |
| Revisar requisitos | R/A | C | C | C |
| Implementar a funcionalidade | C | R | C | A |
| Revisar o código | I | R | I | A |
| Criar testes unitários | I | R/A | C | C |
| Planejar e executar testes do sistema | C | C | R/A | C |
| Registrar e acompanhar defeitos | I | C | R/A | I |
| Priorizar a correção dos defeitos | C | R | C | A |
| Aprovar a disponibilização da versão | I | C | R | A |

### 4.1 Lacuna ou conflito encontrado

**Lacuna ou conflito:**  
A atividade de aprovar a disponibilização da versão está concentrada na Liderança Técnica, enquanto o QA é responsável por verificar a qualidade da versão. Não está definido claramente quais critérios a Liderança Técnica deve considerar para tomar essa decisão.

**Consequência:**  
Uma versão pode ser disponibilizada mesmo apresentando defeitos ou sem que todos os testes tenham sido concluídos, podendo causar problemas para os usuários e retrabalho para a equipe.

### 4.2 Práticas de QA recomendadas

| Prática recomendada | Problema que ajuda a resolver | Papéis envolvidos |
|---|---|---|
| Definição de critérios de aceitação antes do desenvolvimento | Critérios para considerar uma funcionalidade pronta não estão claros, podendo gerar funcionalidades incompletas ou com defeitos. | Analista de sistemas/negócio, Desenvolvedor, QA e Liderança técnica |
| Registro e acompanhamento de defeitos em uma ferramenta compartilhada | Defeitos são identificados, mas nem sempre são registrados ou acompanhados, podendo causar problemas recorrentes e perda de informações. | QA, Desenvolvedor e Liderança técnica |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
Não utilizada
