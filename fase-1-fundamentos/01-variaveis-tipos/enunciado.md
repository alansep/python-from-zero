# 01 — Variáveis e Tipos de Dados ⏱️ ~4h

**Meta:** guardar dados em memória, saber *que tipo* cada dado é e converter entre tipos.

---

## 📚 Teoria

### Variável = nome para um valor

```python
usuario = "Isaque"   # o nome "usuario" segura o texto "Isaque"
idade = 25            # agora o nome "idade" segura o número 25
```

**Regras de nome:**
- Aceita letras, números e `_` — **nunca começa com número** (`2nome` ❌)
- Boa prática: `snake_case` (`idade_usuario`, não `IdadeUsuario`)
- Sem acento, sem espaço
- Diferencia maiúsculas: `Nome` ≠ `nome`
- Palavras reservadas não servem de nome: `if`, `for`, `class`...

### Os 4 tipos primitivos

| Tipo | O quê | Exemplo |
|---|---|---|
| `int` | número inteiro | `idade = 25` |
| `float` | número decimal | `altura = 1.75` |
| `str` | texto (entre aspas) | `nome = "Isaque"` |
| `bool` | booleano: `True` ou `False` | `ativo = True` |

Para conferir o tipo de qualquer valor: `type(valor)` → `<class 'int'>`.

### Entrada e saída

- `print(...)` → mostra no terminal.
- `input("sua pergunta? ")` → **para e espera o usuário digitar**.
  ⚠️ `input()` **sempre devolve TEXTO (`str`)** — mesmo você digitando `25`.

### Conversão de tipos (*casting*)

```python
idade_texto = "25"          # str (texto)
idade = int(idade_texto)    # 25  (int)
altura = float("1.75")      # 1.75 (float)
nome = str(25)              # "25" (str)
```

> ⚠️ `int("abc")` explode com `ValueError` — você aprende a capturar isso com `try/except` na Fase 3.

### `=` não é "igual"

| Símbolo | Nome | O quê faz |
|---|---|---|
| `=` | atribuição | **guarda** um valor: `idade = 25` |
| `==` | comparação | **pergunta** se são iguais → devolve `True`/`False` |

### Erro de sintaxe × exceção

- **`SyntaxError`**: o Python **nem entende** o código (faltou `:`, aspa aberta...). Acontece **antes** de rodar.
- **Exceção** (ex.: `ValueError`): ele entendeu, mas algo **quebrou durante a execução** (conversão impossível).

---

## ✍️ Exercícios

Abra [`atividade.py`](./atividade.py) — são 3 exercícios:

1. **Tipos primitivos** — declare 4 variáveis com os tipos corretos (`str`, `int`, `float`, `bool`).
2. **Entrada + conversão** — pergunte nome e idade com `input()` e converta a idade para `int`.
3. **Saída** — monte a frase `Olá, Ana! Você tem 25 anos.` usando **concatenação com `+`** e `str()` (sem f-string — ela é o desafio da Fase 2).

 rode no terminal:

```bash
python3 fase-1-fundamentos/01-variaveis-tipos/atividade.py
```

## 🚀 Desafios extras (fora da validação)

- Peça 2 números ao usuário, converta e imprima a soma deles.
- Faça `input()` pedir uma frase e imprima ela **ao contrário** (dica: `texto[::-1]` é fatiamento — Fase 2 😉).
- Troque `idade = 25` por `idade = "25"` e veja o que acontece quando o código tenta calcular com ela.

## ✅ Checkpoint

- [ ] Sei explicar a diferença entre `int`, `float`, `str` e `bool`
- [ ] Sei que `input()` sempre devolve texto e como converter
- [ ] Sei a diferença entre `=` e `==`
- [ ] Tudo verde no terminal → marque o checkbox no [README raiz](../../README.md)
