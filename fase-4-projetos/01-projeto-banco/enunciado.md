# 01 — Simulador Bancário ⏱️ ~5h

**Meta:** transformar regras de negócio de um banco em funções pequenas, puras e testáveis — sem uma única linha de `input()`.

---

## 📚 Contexto

Você foi contratado pelo **Banco do Terminal** para escrever o *núcleo* de um caixa eletrônico de texto. O banco não quer um sistema bonito no primeiro dia: quer **regras confiáveis** — depósito só se o valor for positivo, saque limitado a R$ 500 por operação e no máximo 3 saques, extrato legível no fim do mês.

O pedido vem em duas partes, e essa separação é o coração deste projeto:

1. **Núcleo (o que você faz agora)** — funções puras: entram dados, sai resultado. Nenhuma delas pergunta nada ao usuário. Por quê? Porque função que mistura `input()` com regra de negócio **não pode ser testada automaticamente** — você teria que digitar teclas para descobrir se o saldo está certo.
2. **Menu interativo (desafio final)** — o arquivo `meu_banco.py` que **você cria sozinho**, no final. Ele sim usa `input()`, monta o laço de opções e **chama as funções já validadas**.

A validação (`checar.py`) prova que o núcleo está correto até nos casos-limite: depósito negativo, saque de R$ 501, quarto saque do mês, extrato vazio. É assim que se testa código de verdade.

---

## 📋 Especificação

> 🔑 **Contrato geral:** toda função devolve o resultado **exatamente** como está escrito abaixo (textos e tuplas literais). A validação compara os valores de forma estrita — se você escrever `"Depósito realizado"` onde pedimos `"depósito realizado"`, o check falha. É treino de seguir especificação, como em qualquer time de desenvolvimento.

### Função 1 — `validar_deposito(valor)`

- **ENTRADA:** `valor` — número (int ou float).
- **SAÍDA:** `True` se `valor > 0`; `False` se `valor <= 0`.
- Zero e números negativos são **inválidos**. `0.01` já é válido.

### Função 2 — `depositar(saldo, valor)`

- **ENTRADA:** `saldo` — saldo atual (número ≥ 0); `valor` — valor do depósito.
- **SAÍDA:** uma **tupla** `(novo_saldo, situação)`:

| Condição | Tupla devolvida |
|---|---|
| `valor <= 0` | `(saldo, "valor inválido")` — o saldo **não muda** |
| caso contrário | `(saldo + valor, "depósito realizado")` |

### Função 3 — `sacar(saldo, valor, saques_realizados)`

- **ENTRADA:** `saldo` (número ≥ 0); `valor` do saque; `saques_realizados` — quantos saques a conta já fez (0, 1, 2...).
- **SAÍDA:** tupla `(novo_saldo, situação)`.
- **A ORDEM das validações importa** (o primeiro caso que engolir a operação decide o retorno):

| # | Se... | Tupla devolvida |
|---|---|---|
| 1 | `valor <= 0` | `(saldo, "valor inválido")` |
| 2 | `valor > 500` | `(saldo, "saque acima do limite de R$ 500")` |
| 3 | `saques_realizados >= 3` | `(saldo, "limite de 3 saques atingido")` |
| 4 | `valor > saldo` | `(saldo, "saldo insuficiente")` |
| 5 | senão | `(saldo - valor, "saque realizado")` |

- Em **todos** os casos de recusa o saldo devolvido é o **mesmo** que entrou.
- Casos exatos: saque de `500` com saldo `500` **pode** (devolve `(0, "saque realizado")`); saque de `501` **não pode**.

### Função 4 — `registrar_lancamento(historico, tipo, valor)`

- **ENTRADA:** `historico` — **lista** de tuplas `(tipo, valor)`; `tipo` — `"deposito"` ou `"saque"`; `valor` — número.
- **SAÍDA:** a **mesma lista** `historico`, com a tupla `(tipo, valor)` acrescentada **no final**.
- Regras:
  - `tipo` fora de `("deposito", "saque")` → devolve `historico` **sem alterar nada**;
  - `valor <= 0` → devolve `historico` **sem alterar nada**;
  - a ordem dos lançamentos deve ser a ordem em que foram registrados.

### Função 5 — `formatar_extrato(historico, saldo_final)`

- **ENTRADA:** `historico` — lista de `(tipo, valor)`; `saldo_final` — número.
- **SAÍDA:** **string** com:
  - uma linha por lançamento, no formato `Depósito: R$ 200.00` ou `Saque: R$ 50.00` (use f-string com `:.2f`);
  - a **última linha** sempre `Saldo final: R$ 150.00`.
- Histórico vazio: **nenhuma linha** pode conter `Depósito` ou `Saque`, mas a linha `Saldo final: R$ 0.00` continua obrigatória.
- Acentos importam: `Depósito` tem acento (o tipo no histórico, `deposito`, não tem).

---

## ✍️ Exercícios

Abra [`atividade.py`](./atividade.py) — são 5 exercícios, um por função:

1. **`validar_deposito(valor)`** → `True` só para valores positivos.
2. **`depositar(saldo, valor)`** → tupla `(novo_saldo, situação)` com as duas situações possíveis.
3. **`sacar(saldo, valor, saques_realizados)`** → tupla com **5 validações em ordem** (valor, limite de R$ 500, número de saques, saldo).
4. **`registrar_lancamento(historico, tipo, valor)`** → acrescenta no final da lista e devolve a mesma lista; ignora lixo (`tipo` errado, valor ≤ 0).
5. **`formatar_extrato(historico, saldo_final)`** → texto do extrato com uma linha por lançamento e o saldo final no fim.

```bash
python3 fase-4-projetos/01-projeto-banco/atividade.py
```

> 📌 A validação cobre **casos-limite de propósito**: saldo exato, limite exato de R$ 500, R$ 501, o quarto saque, extrato vazio. Se passar por esses, suas regras estão de verdade.

---

## 💡 Dicas (progressivas — sem gabarito)

**Exercício 1**
1. `True`/`False` é o retorno de **qualquer comparação** — não precisa de `if`.
2. Qual comparação cobre os dois inválidos (zero *e* negativo) de uma vez?
3. `valor > 0` é literalmente o enunciado invertido: é só devolver essa expressão.

**Exercício 2**
1. A função precisa devolver **duas coisas** — o Python agrupa várias coisas com `( )`.
2. Trate o caso ruim ANTES: se a validação falhar, devolva o **saldo de entrada** intocado.
3. Um `return` por ramo: `(saldo, "valor inválido")` e depois `(saldo + valor, "depósito realizado")`.

**Exercício 3**
1. São cinco portões em fila — cada um com seu `if` e seu `return`; quem passa em todos chega na operação.
2. Nos quatro primeiros portões o saldo devolvido é o **mesmo** que entrou; a única linha que mexe no saldo é a última.
3. Cuidado com a ordem: `valor > 500` precisa ser testado **antes** de `valor > saldo`, senão um saque de R$ 600 com saldo de R$ 300 diria "saldo insuficiente" quando o banco quer dizer "acima do limite".

**Exercício 4**
1. Primeiro pergunte se o lançamento **merece** ser registrado (tipo válido E valor positivo).
2. Só depois chame o método que junta um item ao fim de uma lista.
3. Devolva a **mesma** lista (a que entrou por parâmetro), não uma nova — o menu espera receber o histórico de volta.

**Exercício 5**
1. Percorra a lista com `for`; para cada linha, um `if` decide se o rótulo é `Depósito` ou `Saque`.
2. Acumule as linhas numa lista e junte tudo com `"\n".join(...)` no final.
3. O `Saldo final` é uma linha só, escrita **depois** do laço — e ele existe mesmo quando a lista está vazia.

---

## 🎮 Desafio final: menu interativo

Crie **do zero** o arquivo `meu_banco.py` nesta pasta (a validação **não** cobre ele — quem te avalia é o enunciado e você mesmo):

```bash
python3 fase-4-projetos/01-projeto-banco/meu_banco.py
```

Requisitos:

1. `import` das funções do `atividade.py` (ex.: `from atividade import depositar, sacar, ...` — o Python encontra o arquivo porque estão na mesma pasta).
2. Laço `while True` com menu numerado: `1) Depositar  2) Sacar  3) Extrato  4) Sair`.
3. Estado mantido em variáveis: `saldo = 0`, `historico = []`, `saques_realizados = 0`.
4. Depósito: leia o valor com `input()`, converta com `float()`, chame `depositar(...)` e **atualize** `saldo` com o que voltou na tupla.
5. Saque: chame `sacar(saldo, valor, saques_realizados)`; se a situação for `"saque realizado"`, incremente `saques_realizados`.
6. Extrato: `print(formatar_extrato(historico, saldo))`.
7. **Arquivos gerados:** crie a pasta `dados/` (com `os.makedirs("dados", exist_ok=True)`) e grave a opção 5) `Salvar extrato em arquivo` em `dados/extrato.txt`.
8. Trate entrada inválida (`ValueError` na conversão do `input`) com `try/except` — o menu não pode quebrar com uma letra.

---

## ✅ Checkpoint de aceitação

**Núcleo (validação automática)**

- [ ] `python3 fase-4-projetos/01-projeto-banco/atividade.py` imprime só ✅ e termina com 🎉
- [ ] Nenhuma função do `atividade.py` chama `input()` ou `print()`
- [ ] Depósito de `0` e de `-100` são recusados
- [ ] Saque de `R$ 501` é recusado mesmo com saldo alto; saque de `R$ 500` passa
- [ ] O 4º saque é recusado; o 3º passa
- [ ] Extrato vazio mostra `Saldo final` sem nenhuma linha de lançamento

**Desafio (manual)**

- [ ] `meu_banco.py` roda, aceita as 4 opções e não quebra com entrada não numérica
- [ ] `dados/extrato.txt` é criado pelo menu
- [ ] Todo `input()` do programa está **fora** das funções validadas

- [ ] Tudo verde → marque o checkbox no [README raiz](../../README.md)
