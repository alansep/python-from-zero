# 02 — Operadores Matemáticos e Lógicos ⏱️ ~2h

**Meta:** fazer contas, comparar valores e combinar condições.

---

## 📚 Teoria

### Operadores aritméticos

Supondo `a = 17`, `b = 5`:

| Operador | Nome | Exemplo | Resultado |
|---|---|---|---|
| `+` | soma | `a + b` | `22` |
| `-` | subtração | `a - b` | `12` |
| `*` | multiplicação | `a * b` | `85` |
| `/` | divisão (vira decimal) | `a / b` | `3.4` |
| `//` | divisão inteira (corta o decimal) | `a // b` | `3` |
| `%` | resto da divisão | `a % b` | `2` |
| `**` | potência | `a ** 2` | `289` |

> 💡 `%` é o segredo de perguntas como *"é par?"*: `numero % 2 == 0`.

### Precedência (ordem em que o Python resolve)

Do mais forte para o mais fraco:

1. `**` (potência)
2. `*`, `/`, `//`, `%`
3. `+`, `-`
4. comparações (`==`, `>`, `<`...)
5. `not`
6. `and`
7. `or`

```python
2 + 3 * 4      # = 14  (multiplica antes de somar)
(2 + 3) * 4    # = 20  (parênteses mudam tudo)
```

> Regra prática: **na dúvida, use parênteses** — código claro vale mais que memória.

### Operadores relacionais (comparações)

| Operador | Significado | `10 > 4` |
|---|---|---|
| `>` | maior que | `True` |
| `<` | menor que | `False` |
| `>=` | maior ou igual | `True` |
| `<=` | menor ou igual | `False` |
| `==` | igual a | `False` |
| `!=` | diferente de | `True` |

⚠️ Um único `=` **atribui**; `==` **compara**. Nunca confunda (1.3 do roadmap).

### Operadores lógicos

Combinam condições — o resultado é `True`/`False`:

| Operador | Significado | Exemplo |
|---|---|---|
| `and` | **ambos** precisam ser `True` | `x > 5 and y > 5` |
| `or` | **pelo menos um** precisa ser `True` | `x > 5 or y > 5` |
| `not` | **inverte** o valor | `not (x == y)` |

Com `x = 10`, `y = 4`:
- `x > 5 and y > 5` → `True and False` → **`False`**
- `x > 5 or y > 5` → `True or False` → **`True`**
- `not (x == y)` → `not False` → **`True`**

---

## ✍️ Exercícios

Abra [`atividade.py`](./atividade.py) — são 5 exercícios:

1. **Aritmética** — complete 5 variáveis usando `a` e `b` (não hardcode o resultado!).
2. **Comparações e lógicos** — complete 6 booleanos com `x` e `y`.
3. **Precedência** — monte **sem parênteses** a expressão *"2 mais 3 vezes 4 ao quadrado menos 1"*. **Calcule no papel antes de rodar!** Esperado: `49`.
4. **Lógica combinada** — `True` se `numero` for divisível por 3 **E** por 5.
5. **Previsão de saída** — leia um trecho de código **no papel** e devolva a saída exata (dry-run).

```bash
python3 fase-1-fundamentos/02-operadores/atividade.py
```

---

## 💡 Dicas (progressivas — sem gabarito)

**Exercício 1**
1. `17 / 5` não dá 3 — qual operador corta a parte decimal?
2. `//` e `%` andam juntos: `a == (a // b) * b + (a % b)`.
3. Monte cada linha com os operandos `a` e `b` — nunca digite o resultado na mão.

**Exercício 2**
1. Comece pelas comparações: elas já devolvem `True`/`False` antes do `and`/`or`.
2. `and` exige os DOIS lados `True`; `or` aceita UM.
3. `not` inverte o valor — use parênteses para não se perder na leitura.

**Exercício 3**
1. Reescreva primeiro com parênteses exagerados e depois remova-os.
2. Potência antes de multiplicação; multiplicação antes de soma.
3. Ordem de pensar: `4²`, depois `3 ×`, depois `2 +` e o `-1` por último.

**Exercício 4**
1. "Divisível" quer dizer: qual comparação com o resto?
2. Os restos de `45 ÷ 3` e de `45 ÷ 5` precisam ser zero **ao mesmo tempo**.
3. Um único `and` entre duas comparações resolve.

**Previsão de saída**
1. Aplique a precedência: quem resolve primeiro, `+` ou `*`?
2. `//` descarta a fração; `%` devolve só o resto.
3. Anote o resultado de cada `print` em uma linha — a resposta é um texto com 3 linhas.

## 🚀 Desafios extras

- Peça um número ao usuário e diga se ele é **par** (`numero % 2 == 0`) ou ímpar.
- Verifique se um ano é **bissexto**: divisível por 4 **e** (não divisível por 100 **ou** divisível por 400).
- Calcule e imprima a média de 3 notas digitadas.

## ✅ Checkpoint

- [ ] Sei os 7 operadores aritméticos (incluindo `//`, `%` e `**`)
- [ ] Sei a ordem de precedência de cabeça
- [ ] Sei combinar condições com `and`, `or` e `not`
- [ ] Tudo verde → marque o checkbox no [README raiz](../../README.md)
