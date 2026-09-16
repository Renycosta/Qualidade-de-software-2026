# Atividade 3: Estratégia e Projeto de Testes do LocalEats

## 1. Identificação

**Turma:** ADS 4º Semestre Manhã (Pelotas)  
**Equipe:** Reny Brito da Costa  
**Data:** 15/09/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Reny Brito da Costa | [@Renycosta](https://github.com/Renycosta) |

**Elemento de Competência:** Planejar e projetar testes selecionando técnicas adequadas.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

---

## 2. Tarefa 1: Planejamento dos testes

### 2.1 Objetivo dos testes

Verificar se os usuários conseguem utilizar os filtros por categoria 

### 2.2 Escopo

#### Funcionalidades incluídas

| Integrante | Funcionalidade incluída | O que será verificado |
|---|---|---|
| Reny | Filtro de restaurantes por categoria | Ao selecionar uma categoria (Italiana, Japonesa, Brasileira ou Mexicana), o sistema exibe corretamente apenas os restaurantes pertencentes à categoria selecionada. Também será verificado se a opção "Todos" retorna a exibição de padrão. |

#### Funcionalidade não incluída

| Funcionalidade não incluída | Justificativa |
|---|---|
| Busca por nome | O objetivo do teste é unicamente analisar o funcionamento do filtro. A funcionalidade de busca por nome não está realmente associada com o filtro,  mesmo que ambos sejam responsaveis pela pesquisa de restaurante.|

### 2.3 Abordagem

| Item | Decisão da equipe | Justificativa |
|---|---|---|
| Níveis de teste | Teste de sistema | O filtro será avaliado diretamente na aplicação, verificando seu funcionamento integrado à interface e aos dados dos restaurantes. |
| Tipos de teste | Teste funcional | Será verificado se o sistema apresenta os restaurantes correspondentes à categoria selecionada. |
| Perspectiva | Caixa-preta | A funcionalidade será analisada por meio dos resultados apresentados pelo sistema, sem analisar o código em si. |
| Técnicas de teste | Particionamento de equivalência | Permite testar diferentes categorias e comportamentos do filtro sem precisar testar todas as combinações possíveis. |

### 2.4 Ambiente e responsabilidades

| Item | Definição |
|---|---|
| Ambiente necessário | Deve haver restaurantes cadastrados em diferentes categorias para possibilitar a realização dos testes. |
| Responsáveis pelo planejamento | Equipe de QA/testes, responsável por definir o objetivo, escopo, cenários e condições necessárias para os testes do filtro por categoria. |
| Responsáveis pela especificação dos casos | Equipe de QA/testes, responsável por documentar os casos de teste, entradas, passos de execução e resultados esperados. |
| Responsáveis pela futura execução | Equipe de QA/testes, responsável por executar os casos definidos, registrar os resultados obtidos e documentar possíveis falhas encontradas. |

### 2.5 Critérios

| Critério | Definição da equipe |
|---|---|
| Entrada | Aplicação Local Eats disponível e acessível; navegador funcionando e com conexão à internet; restaurantes cadastrados em diferentes categorias; categorias disponíveis para seleção, como Italiana, Japonesa, Brasileira e Mexicana. |
| Saída | Todos os casos de teste planejados para o filtro foram executados e seus resultados registrados. O filtro deve apresentar corretamente os restaurantes correspondentes à categoria selecionada e a opção "Todos" deve apresentar todos os restaurantes disponíveis. |
| Suspensão | Os testes deverão ser interrompidos caso a aplicação fique indisponível, ocorra uma falha que impeça a utilização do filtro, os dados dos restaurantes estejam indisponíveis/incorretos ou haja problemas de conexão que impossibilitem a execução confiável dos testes. |

---

## 3. Tarefa 2: Riscos e técnicas de teste

### 3.1 Análise dos riscos

| ID | Integrante | Funcionalidade | Risco | Consequência | Probabilidade | Impacto | Prioridade | Justificativa |
|---|---|---|---|---|:---:|:---:|:---:|---|
| R01 | Reny | [funcionalidade] | [o que pode dar errado] | [quem será afetado e como] | [Baixa/Média/Alta] | [Baixo/Médio/Alto] | [Baixa/Média/Alta] | [preencher] |
| R02 | Reny | [funcionalidade] | [o que pode dar errado] | [quem será afetado e como] | [Baixa/Média/Alta] | [Baixo/Médio/Alto] | [Baixa/Média/Alta] | [preencher] |

### 3.2 Aplicação das técnicas

#### Análise do integrante 1

**Integrante:** Reny  
**Funcionalidade:** [preencher]  
**Risco relacionado:** [R01]  
**Técnica escolhida:** [particionamento de equivalência, análise de valor limite, tabela de decisão ou transição de estados]

**Por que a técnica foi escolhida:**  
[Expliquem por que a técnica é adequada à regra ou ao risco analisado.]

**Aplicação da técnica:**  
[Apresentem as classes, limites, combinações ou transições identificadas. Utilizem uma tabela ou lista quando necessário.]

**Casos derivados:** [CT01 e CT02]

---

## 4. Tarefa 3: Casos de teste e rastreabilidade

### 4.1 Casos de teste

### CT01: [Título do caso]

**Integrante responsável:** Reny
**Funcionalidade:** [preencher]  
**Risco ou requisito relacionado:** [R01 ou descrição do requisito]  
**Técnica utilizada:** [preencher]

**Pré-condição:**  
[O que precisa existir ou estar preparado antes da execução.]

**Dados de entrada:**  
[Valores ou dados necessários. Caso não sejam necessários, registrem “Não se aplica”.]

**Passos:**

1. [Primeiro passo.]
2. [Segundo passo.]
3. [Terceiro passo.]

**Resultado esperado:**  
[Comportamento observável que indicará que o teste passou.]

---

### CT02: [Título do caso]

**Integrante responsável:** Reny
**Funcionalidade:** [preencher]  
**Risco ou requisito relacionado:** [preencher]  
**Técnica utilizada:** [preencher]

**Pré-condição:**  
[preencher]

**Dados de entrada:**  
[preencher]

**Passos:**

1. [Primeiro passo.]
2. [Segundo passo.]
3. [Terceiro passo.]

**Resultado esperado:**  
[preencher]

---

### CT03: [Título do caso]

**Integrante responsável:** Reny
**Funcionalidade:** [preencher]  
**Risco ou requisito relacionado:** [preencher]  
**Técnica utilizada:** [preencher]

**Pré-condição:**  
[preencher]

**Dados de entrada:**  
[preencher]

**Passos:**

1. [Primeiro passo.]
2. [Segundo passo.]
3. [Terceiro passo.]

**Resultado esperado:**  
[preencher]

---

### 4.2 Matriz de rastreabilidade

| Integrante | Funcionalidade | Risco ou requisito | Técnica utilizada | Casos de teste |
|---|---|---|---|---|
| Reny | [funcionalidade] | [R01 ou requisito] | [técnica] | [CT01 e CT02] |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
Não utilizada
