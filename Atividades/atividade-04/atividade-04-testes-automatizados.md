# Atividade 4: Testes Automatizados do LocalEats

> **Orientação:** substitua os textos entre colchetes pelas informações da equipe. Remova as orientações que não fizerem parte da entrega final.

---

## 1. Identificação

- **Turma:** ADS 4º Semestre Manhã (Pelotas)
- **Modalidade:** Individual
- **Repositório:** https://github.com/Renycosta/Qualidade-de-software-2026/tree/main/Atividades
- **Diretório da atividade:** https://github.com/Renycosta/Qualidade-de-software-2026/tree/main/Atividades/atividade-04
- **Data da última execução:** 10/11/2026

### Integrantes

1. Reny Brito da Costa
---

## 2. Integrantes e responsabilidades

| ID | Integrante responsável | Tipo | Comportamento verificado | Arquivo e função de teste |
|---|---|---|---|---|
| TU01 | Reny | Unitário | Verifica se uma quantidade entre 1 e 10 é considerada válida | `tests/test_regras_localeats.py::test_quantidade_itens_valida` |
| TU02 | Reny | Unitário | Verifica se uma quantidade negativa gera uma exceção ValueError | `tests/test_regras_localeats.py::test_quantidade_itens_negativa` |
| TF01 | Reny | Funcional | Verifica a apresentação da tela de login e o preenchimento do campo de e-mail | `tests/test_localeats.py::test_apresentacao_tela_login` |

---

## 3. Testes unitários

### Registro das regras implementadas

#### Regra de Reny

- **Regra escolhida:** Validar a quantidade de itens permitida, aceitando valores entre 1 e 10, rejeitando zero e valores superiores a 10 e gerando uma exceção para quantidades negativas
- **Função implementada:** `quantidade_itens_valida`
- **Arquivo da implementação:** `src/regras_localeats.py`
- **Testes criados:** `test_quantidade_itens_valida`; `test_quantidade_itens_negativa`
- **Comportamentos verificados:** Verifica se uma quantidade válida retorna True e se uma quantidade negativa gera a exceção ValueError

---

## 4. Aplicação do TDD

### TDD de Reny

- **Regra escolhida:** Validar a quantidade de itens permitida pelo sistema, considerando o intervalo de 1 a 10
- **Primeiro teste escrito:** `test_quantidade_itens_valida`
- **Por que o teste falhou inicialmente:** O teste falhou porque a função ainda não havia sido implementada, portanto não existia uma lógica para validar a quantidade de itens
- **Implementação mínima realizada:** Foi criada a função quantidade_itens_valida, responsável por verificar se a quantidade está dentro do intervalo permitido e retornar True ou False
- **Segundo teste escrito:** `test_quantidade_itens_negativa`
- **Melhoria ou refatoração realizada:** Foi adicionada uma condição para identificar quantidades negativas e gerar uma exceção ValueError, garantindo o tratamento adequado desse tipo de entrada
---

## 5. Testes funcionais com Playwright

**Sistema:** https://local-eats-unisenac.vercel.app/

### Teste funcional de Reny

- **ID:** `TF01`
- **Fluxo automatizado:** Acessar a página inicial do LocalEats e verificar a apresentação da tela de login
- **Interação realizada:** O teste localiza o campo de e-mail e preenche com o endereço teste@teste.com
- **Primeira assertion:** Verifica se o campo de e-mail está visível na tela
- **Segunda assertion:** Verifica se o e-mail foi preenchido corretamente no campo após a interação
- **Arquivo e função:** `tests/test_localeats.py::test_apresentacao_tela_login`
- **Resultado final:** Aprovado

---

## 6. Resultado da execução

- **Quantidade total de testes:** 3
- **Testes aprovados:** 3
- **Testes reprovados:** 0
- **Link para o relatório:** [relatorio-pytest.txt](relatorio-pytest.txt)
- **Observações:** Todos os testes foram aprovados

---

## 7. Explicações individuais

### Explicação do teste de Reny

- **Teste escolhido:** `test_quantidade_itens_valida`
- **Comportamento verificado:** Verifica se a função consegue identificar corretamente uma quantidade de itens dentro do intervalo permitido pelo sistema
- **Dados ou estado inicial:** A função recebe o valor inteiro 5, representando a quantidade de itens
- **Resultado esperado:** A função deve retornar True, pois cinco está dentro do intervalo permitido, entre 1 e 10
- **O que faria o teste falhar:** O teste falharia caso a função retornasse False, apresentasse uma exceção inesperada ou não reconhecesse corretamente uma quantidade válida

---

## 8. Uso de inteligência artificial

O uso de inteligência artificial é permitido como apoio, mas todo o conteúdo e código devem ser revisados, executados e compreendidos pela equipe.

Ferramenta utilizada:
Utilizada para correção de gramatica e correção de texto.
