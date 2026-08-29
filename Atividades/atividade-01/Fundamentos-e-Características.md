# Atividade 1: Fundamentos e Características da Qualidade no LocalEats

## 1. Identificação

**Turma:** ADS 4º Semestre Manhã (Pelotas)
**Equipe:** Reny Brito da Costa
**Data:** 18/08/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Reny | [@Renycosta](https://github.com/Renycosta) |

**Elemento de Competência:** Compreender os fundamentos de qualidade de software e sua aplicação no desenvolvimento de sistemas.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

---

## 2. Tarefa 1: Fundamentos da qualidade

### 2.1 Necessidades explícitas e implícitas

| Tipo | Necessidade | Interessado | Consequência se não for atendida |
|---|---|---|---|
| Explícita | Filtro de pesquisa | Usuários que tem inresseem um tipo específico de estabelecimento | Dificultara na busca do usuário é fara com que ele não tem interesse em utiliazar o site |
| Explícita | Favoritar | Usuários que gostaria de realizar um pedido nesse restaurante futuramente | O usuário precisará buscar pelo restaurante manualmente toda vez que quiser pedir novamente, gerando incomodo |
| Implícita | Histórico de pedidos | Usuários que desejam consultar pedidos realizados anteriormente | O usuário não poderá consultar facilmente seus pedidos anteriores, dificultando o acompanhamento e a realização de novos pedidos |
| Implícita | Detalhes do restaurante | Usuários que desejam conhecer melhor o estabelecimento antes de realizar um pedido | Ocorrera dificuldade para escolher um restaurante, pois não terá acesso suficiente a informações como localização, tipo de culinária e opções disponíveis |

### 2.2 Questão sobre os fundamentos da qualidade

**Um sistema que implementa todas as funcionalidades explicitamente solicitadas pode, ainda assim, apresentar baixa qualidade? Justifiquem utilizando pelo menos uma necessidade implícita identificada pela equipe.**

Sim, pois as necessidades implícitas também influenciam a experiência e a satisfação dos usuários.
Por exemplo: como a necessidade implícita o histórico de pedidos. Mesmo que a plataforma tenha a função de busca e a possibilidade de marcar restaurantes como favoritos, a falta de um registro tornaria difícil para o usuário revisar pedidos passados.

---

## 3. Tarefa 2: Exploração da aplicação

| Integrante | Funcionalidade | O que foi realizado | O que foi observado | Evidência |
|---|---|---|---|---|
| Reny | Favoritar | uso esperado: Ao clicar uma vez o restaurante e adicionado a lista de favoritos. uso alternativo: Ao clicar novamente em um restaurante favoritado deve impedir a duplicação ou informar que o restaurante já está favoritado. | Ao realizar o uso esperado ocorreu tudo como previsto, mas ao realizar o uso alternativo não ocorreu nenhuma das possibilidades, ele apenas continuou favoritado e não teve nenhum aviso dizendo que ele já estava favoritado | [ver evidência](evidencias/evidencias.pdf) |

---

## 4. Tarefa 3: Requisitos e características de qualidade

| Integrante | Requisito de Qualidade | Característica ou subcaracterística | Justificativa | Como avaliar |
|---|---|---|---|---|
| Reny | O sistema deve informar ao usuário quando ele tentar favoritar um restaurante que já está favoritado. | Usabilidade | Durante o uso alternativo, o restaurante permaneceu favoritado, porém o sistema não apresentou nenhum aviso informando que ele já estava na lista de favoritos. Isso pode gerar dúvidas sobre o resultado da ação. | Tentar favoritar novamente um restaurante que já está favoritado e verificar se o sistema apresenta uma mensagem ou indicação visual informando que o restaurante já está favoritado. |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
Não utilizada
