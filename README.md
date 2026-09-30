# 🐍 python-from-zero

> **Repositório de estudo: lógica de programação com Python — do zero ao primeiro projeto.**

**Objetivo:** elevar o conhecimento em lógica de programação e Python até a postura de um desenvolvedor Python com boa base de conhecimento. **Escopo: apenas a linguagem** — bibliotecas, frameworks e ecossistema ficam para um repositório futuro.

**Filosofia:** aprender a *pensar* (não decorar sintaxe) e aprender a depurar **sem depender de IA**.

**Trilha criada para:** @Isaque

---

## 🧭 Como usar

| Arquivo | Papel |
|---|---|
| `enunciado.md` | Teoria resumida + lista de exercícios do tópico |
| `atividade.py` | **Você edita este.** Substitua os `TODO` pelas suas respostas |
| `checar.py` | Validação automática — não precisa mexer (pode ler por curiosidade) |

> 🔒 **Não existe gabarito no repositório.** O esforço de resolver — e errar — é parte do estudo.

1. Faça o [Setup](./fase-1-fundamentos/00-setup/) e confirme que o Python roda no terminal.
2. Avance as fases **em ordem**. Em cada tópico:
   - leia o `enunciado.md`;
   - implemente os `TODO` no `atividade.py`;
   - rode no terminal:
     ```bash
     python3 fase-1-fundamentos/01-variaveis-tipos/atividade.py
     ```
   - a validação imprime ✅/❌ item a item — **corrija até tudo ficar verde**;
   - marque o checkbox do roadmap abaixo.
3. Travou? Leia o erro no terminal **antes** de perguntar à IA — interpretar a stack trace é treino (Fase 3).

> 💡 **Regra de ouro:** a IA pode explicar, mas o código é você quem escreve.

---

## 📁 Estrutura

```text
python-from-zero/
├── README.md                        ← roadmap + progresso (você está aqui)
├── fase-1-fundamentos/
│   ├── 00-setup/                    ← Python + VS Code + terminal
│   ├── 01-variaveis-tipos/          ← tipos, input/print, conversão
│   ├── 02-operadores/               ← aritméticos, relacionais, lógicos
│   ├── 03-condicionais/             ← if / elif / else
│   └── 04-repeticoes/               ← for, while, break/continue
├── fase-2-estruturas-dados/         ← listas, tuplas, dicionários, strings
├── fase-3-modularizacao/            ← funções, módulos, arquivos, algoritmos, debug
└── fase-4-projetos/                 ← 3 projetos que fecham o ciclo
```

---

## 🗺️ Roadmap

**Progresso: 0/30 tópicos** *(atualize o contador ao marcar os checkboxes)* · **⏱️ ~55h no total** *(≈ 1h/dia → ~2 meses)*

### Fase 1 — Fundamentos da Lógica e Pensamento Computacional
*Meta: instruir o computador de forma determinística e decompor problemas.* **⏱️ ~12h**

- [ ] **Setup do ambiente** — Python 3, VS Code e terminal ([pasta](./fase-1-fundamentos/00-setup/)) — 1h

#### [1. Variáveis e Tipos de Dados](./fase-1-fundamentos/01-variaveis-tipos/) — 4h
- [ ] 1.1 Tipos primitivos: `int`, `float`, `str`, `bool` e variáveis — 1.5h
- [ ] 1.2 Entrada/saída (`input`, `print`) e conversão de tipos (`int()`, `float()`, `str()`) — 1.5h
- [ ] 1.3 Atribuição `=` × comparação `==`; erro de sintaxe × exceção — 1h

#### [2. Operadores Matemáticos e Lógicos](./fase-1-fundamentos/02-operadores/) — 2h
- [ ] 2.1 Aritmética básica e precedência — 1h
- [ ] 2.2 Relacionais (`>`, `<`, `==`, `!=`) e lógicos (`and`, `or`, `not`) — 1h

#### [3. Estruturas Condicionais](./fase-1-fundamentos/03-condicionais/) — 2.5h
- [ ] 3.1 Fluxo de controle com `if`, `elif` e `else` — 1.5h
- [ ] 3.2 Cenários com múltiplas validações (e a ordem delas!) — 1h

#### [4. Estruturas de Repetição](./fase-1-fundamentos/04-repeticoes/) — 3h
- [ ] 4.1 Iterações definidas com `for` e `range` — 1h
- [ ] 4.2 Repetições baseadas em condição com `while` — 1h
- [ ] 4.3 Controle de fluxo em loops com `break` e `continue` — 1h

---

### Fase 2 — Estruturas de Dados e Manipulação
*Meta: organizar e manipular coleções de dados na memória.* **⏱️ ~10h** *(pasta em construção)*

#### [1. Listas](./fase-2-estruturas-dados/) — 4h
- [ ] 1.1 Indexação, fatiamento (*slicing*) e mutabilidade — 2h
- [ ] 1.2 Métodos essenciais: `append`, `pop`, `remove`, `sort`, `len` — 2h

#### [2. Tuplas e Conjuntos](./fase-2-estruturas-dados/) — 1.5h
- [ ] 2.1 Imutabilidade e remoção de duplicatas — 1.5h

#### [3. Dicionários](./fase-2-estruturas-dados/) — 2h
- [ ] 3.1 Mapeamento chave-valor, busca e objetos aninhados — 2h

#### [4. Strings](./fase-2-estruturas-dados/) — 1.5h
- [ ] 4.1 Interpolação (f-strings) e métodos: `split`, `join`, `strip`, `replace` — 1.5h

#### [5. Compreensão de listas](./fase-2-estruturas-dados/) — 1h
- [ ] 5.1 *List comprehension* — 1h

---

### Fase 3 — Modularização, Algoritmos e Depuração
*Meta: sair dos scripts lineares, escrever código sustentável e achar bugs sozinho.* **⏱️ ~15h** *(pasta em construção)*

#### [1. Funções e Escopo](./fase-3-modularizacao/) — 3h
- [ ] 1.1 `def`, parâmetros, argumentos padrão e `return` — 2h
- [ ] 1.2 Escopo local × global — 1h

#### [2. Módulos e Importação](./fase-3-modularizacao/) — 2h
- [ ] 2.1 `import`, `from ... import` e stdlib (`math`, `random`, `datetime`, `json`, `csv`) — 2h

#### [3. Manipulação de Arquivos](./fase-3-modularizacao/) — 2.5h
- [ ] 3.1 `open`, `with`, ler/escrever `.txt`, `.json` e `.csv` — 2.5h

#### [4. Algoritmos Clássicos](./fase-3-modularizacao/) — 2.5h
- [ ] 4.1 Busca linear — 1h
- [ ] 4.2 Bubble Sort (mecânica de trocas) — 1.5h

#### [5. Tratamento de Exceções](./fase-3-modularizacao/) — 2h
- [ ] 5.1 Blocos `try`, `except`, `finally` — 2h

#### [6. Depuração sem IA](./fase-3-modularizacao/) — 3h
- [ ] 6.1 Leitura e interpretação de *stack traces* — 1.5h
- [ ] 6.2 Breakpoints no VS Code + `print` estratégico — 1.5h

---

### Fase 4 — Transição para Desenvolvedor (Projetos Práticos)
*Meta: consolidar a lógica construindo sem depender do autocompletar da IA.* **⏱️ ~18h** *(pasta em construção)*

- [ ] **Projeto 1 — Validador de regras de negócio:** simulador bancário de terminal (depósito, saque, extrato, saldo e limites) — 5h
- [ ] **Projeto 2 — Gerenciador de dados estruturados:** cadastro/consulta com dicionários + persistência em `.json`/`.csv` — 6h
- [ ] **Projeto 3 — Analisador de logs:** ler arquivo de texto, filtrar informações e gerar relatório formatado — 6h
- [ ] **Revisão final:** refatorar, comentar e validar se está pronto para a fase de bibliotecas — 1h

---

> ✅ **Concluído quando:** os 30 itens estiverem marcados e os 3 projetos rodarem sem erros no terminal.
