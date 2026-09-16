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
| Entrada | Aplicação Local Eats disponível e acessível, navegador funcionando e com conexão à internet, restaurantes cadastrados em diferentes categorias, categorias disponíveis para seleção. |
| Saída | Casos de teste executados e resultados registrados, com o filtro apresentando corretamente os restaurantes de cada categoria. |
| Suspensão | Indisponibilidade do site, falha que impeça o uso do filtro ou ausência dos dados necessários para o teste. |

---

## 3. Tarefa 2: Riscos e técnicas de teste

### 3.1 Análise dos riscos

| ID | Integrante | Funcionalidade | Risco | Consequência | Probabilidade | Impacto | Prioridade | Justificativa |
|---|---|---|---|---|:---:|:---:|:---:|---|
| R01 | Reny | Filtro por categoria | O sistema pode exibir restaurantes de categorias diferentes da selecionada. | Usuário, pois ele pode receber informações incorretas. | Média | Médio | Média | O erro afeta diretamente a principal finalidade do filtro e pode comprometer a experiência do usuário, mas não impede o funcionamento do site. |
| R02 | Reny | Filtro por categoria | O filtro pode não responder ao ser selecionado. | Usuário, pois ele não conseguirá utilizar o filtro para encontrar restaurantes | Média | Alto | Alta | A funcionalidade ficará indisponível para o usuário, tornando impossível realizar a busca por categoria e comprometendo totalmente essa funcionalidade |

### 3.2 Aplicação das técnicas

**Integrante:** Reny <br>
**Funcionalidade:** Filtro de restaurantes por categoria <br> 
**Risco relacionado:** R01 <br>  
**Técnica escolhida:** Particionamento de equivalência <br>

**Por que a técnica foi escolhida:**  
A técnica é adequada porque o filtro possui diferentes categorias que devem produzir o mesmo tipo de comportamento: ao selecionar uma categoria, somente os restaurantes pertencentes a ela devem ser exibidos. Dessa forma, podemos selecionar algumas categorias representativas para verificar se o filtro funciona corretamente, sem a necessidade de testar todas as possibilidades.

**Aplicação da técnica:**  
| Classe de equivalência | Entrada | Comportamento esperado |
|---|---|---|
| Categoria válida | Italiana | Exibir somente restaurantes italianos |
| Categoria válida | Japonesa | Exibir somente restaurantes japoneses |
| Categoria válida | Brasileira | Exibir somente restaurantes brasileiros |
| Categoria válida | Mexicana | Exibir somente restaurantes mexicanos |
| Categoria geral | Todos | Exibir restaurantes de todas as categorias |

**Casos derivados:** <br>
CT01: utiliza a categoria Italiana para verificar se somente restaurantes da categoria selecionada são apresentados. <br>
CT02: utiliza as categorias Japonesa e Mexicana para verificar se o sistema atualiza corretamente os resultados quando o usuário troca de categoria. <br>

---

## 4. Tarefa 3: Casos de teste e rastreabilidade

### 4.1 Casos de teste

### CT01: Filtrar restaurantes por categoria

**Integrante responsável:** Reny <br>
**Funcionalidade:** Filtro de restaurantes por categoria <br>
**Risco ou requisito relacionado:** R01 <br>  
**Técnica utilizada:** Particionamento de equivalência <br>

**Pré-condição:**  
A aplicação deve estar disponível e possuir restaurantes cadastrados em diferentes categorias.

**Dados de entrada:**  
Categoria: Italiana

**Passos:**

1. Acessar a página inicial do Local Eats.
2. Localizar os filtros de categoria.
3. Selecionar a categoria "Italiana".

**Resultado esperado:**  
O sistema deve exibir somente restaurantes pertencentes à categoria Italiana, não apresentando restaurantes de outras categorias.

---

### CT02: Alternar entre diferentes categorias

**Integrante responsável:** Reny <br>
**Funcionalidade:** Filtro de restaurantes por categoria <br>
**Risco ou requisito relacionado:** R02 <br>
**Técnica utilizada:** Particionamento de equivalência <br>

**Pré-condição:**  
A aplicação deve estar disponível e possuir restaurantes cadastrados nas categorias que serão utilizadas no teste.

**Dados de entrada:**  
Categorias: Japonesa e Mexicana

**Passos:**

1. Acessar a página inicial do Local Eats.
2. Selecionar a categoria "Japonesa" e observar os restaurantes apresentados.
3. Em seguida, selecionar a categoria "Mexicana".

**Resultado esperado:**  
Ao selecionar "Japonesa", devem ser exibidos os restaurantes dessa categoria. Ao selecionar "Mexicana", a lista deve ser atualizada e apresentar os restaurantes correspondentes à nova categoria, sem manter incorretamente os resultados anteriores.

---

### CT03: Exibir todos os restaurantes

**Integrante responsável:** Reny <br>
**Funcionalidade:** Filtro de restaurantes por categoria <br>
**Risco ou requisito relacionado:** Requisito funcional — A opção "Todos" deve permitir visualizar restaurantes de todas as categorias. <br>
**Técnica utilizada:** Análise de valores-limite <br>

**Pré-condição:**  
A aplicação deve estar disponível e possuir restaurantes cadastrados em mais de uma categoria.

**Dados de entrada:**  
Categoria: Todos

**Passos:**

1. Acessar a página inicial do Local Eats.
2. Selecionar uma categoria específica, como "Brasileira".
3. Selecionar a opção "Todos".

**Resultado esperado:**  
Após selecionar "Todos", o sistema deve remover a restrição de categoria e exibir novamente os restaurantes disponíveis de todas as categorias.

---

### 4.2 Matriz de rastreabilidade

| Integrante | Funcionalidade | Risco ou requisito | Técnica utilizada | Casos de teste |
|---|---|---|---|---|
| Reny | Filtro de restaurantes por categoria | R01 — O sistema pode exibir restaurantes de categorias diferentes da selecionada. R02 — O filtro pode não responder ou deixar de atualizar a lista de restaurantes. | Particionamento de equivalência | CT01 e CT02 |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
Não utilizada
