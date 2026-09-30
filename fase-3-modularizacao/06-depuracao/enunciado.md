# 06 — Depuração sem IA ⏱️ ~3h

**Meta:** aprender a **ler o erro e encontrar o culpado sozinho** — a stack trace é o seu mapa, o `print` é a sua lanterna.

---

## 📚 Teoria

### Anatomia de uma stack trace

```text
Traceback (most recent call last):                 ← começou a ler de cima
  File "exemplo.py", line 4, in <module>           ← caminho das chamadas
    resultado = dobro()
TypeError: dobro() missing 1 required...           ← ÚLTIMA LINHA: tipo + mensagem
```

| Parte | O que diz |
|---|---|
| `Traceback (most recent call last)` | a lista vai da chamada MAIS EXTERNA para a mais interna |
| `File "...", line N` | por onde o código passou (o caminho) |
| o trecho de código + `^^^^` | **onde estourou** — comece a ler AQUI |
| **última linha** | `TipoDaExceção: mensagem` — metade do diagnóstico está nela |

> 🔑 **Regra dos 3 segundos:** olhe SEMPRE a última linha primeiro. `NameError`? Alguém não existe. `TypeError`? O tipo é inesperado. `IndexError`? O índice estourou. Só depois suba para o código.

### A estratégia do depurador (sem chute)

1. **Reproduza** — rode de novo e confirme o erro (um erro que não repete é meio caminho andado).
2. **Leia a última linha** — tipo + mensagem.
3. **Olhe a linha apontada** — qual variável tem um valor estranho?
4. **Suspeite do dado, não da sintaxe** — `print` o valor **antes** da linha suspeita.
5. **Corrija UMA coisa por vez** e rode de novo. Mudou três coisas e passou? Você não sabe qual resolveu.

### `print` estratégico (plano B)

```python
print(">>> variavel:", variavel, type(variavel))   # valor + tipo, na hora
```

- Imprima **antes** da linha suspeita e **dentro** dos laços (com o índice!).
- Saída grande? Imprima só quando a condição importar: `if indice == 3: print(...)`.
- Depois de achar, **apague os prints** — debug não vai para o commit.

### Breakpoint no VS Code (o plano A)

| Tecla | Ação |
|---|---|
| `F9` | breakpoint (bolinha vermelha na margem) |
| `F10` | passo a passo (uma linha) |
| `F11` | entra dentro da função |
| `F5` | roda até o breakpoint |
| hover | passe o mouse numa variável durante a pausa |

Com o programa **pausado**, você vê o valor real de cada variável sem imprimir nada. É a ferramenta mais poderosa contra o bug "só acontece na terceira volta do laço".

### Os quatro crimes mais comuns de iniciante

| Sintoma | Suspeitos |
|---|---|
| resultado errado, sem erro | comparação invertida (`<` no lugar de `>`), `=` vs `==` |
| pula o último elemento | `range(1, n)` em vez de `range(1, n + 1)` |
| sai cedo do laço | `return`/`break` indentado **dentro** do laço |
| acumula nada | esqueceu o `total += ` (atribuiu de novo: `total = x`) |

> 📚 Reforço teórico: [Erros e exceções](https://docs.python.org/pt-br/3/tutorial/errors.html) · [Depuração no VS Code](https://code.visualstudio.com/docs/python/debugging) (em inglês).

---

## ✍️ Exercícios

Abra [`atividade.py`](./atividade.py) — são 8 exercícios em duas partes.

### Parte A — 4 funções COM BUG (corrija rodando)

O código **roda sem dar erro**, mas o resultado está errado. Só lendo e testando você acha:

1. **`maior_de_tres(a, b, c)`** → o maior dos três números.
2. **`soma_ate(n)`** → `1 + 2 + ... + n` (`n <= 0` → `0`). Sem `sum()`.
3. **`contar_pares(valores)`** → quantos valores da lista são pares.
4. **`total_do_carrinho(precos)`** → soma dos preços (`[]` → `0`).

### Parte B — leia as stack traces e responda (exercícios 5 a 8)

Cada bloco abaixo é um arquivo `exemplo.py` e a saída **real** do Python. Responda no `atividade.py` (`resposta_1 = ""` etc.) — **minúsculas**, sem espaço nas bordas.

**Exercício 5 — stack trace 1 (NameError)**

```python
total = 0
print(soma)
```

```text
Traceback (most recent call last):
  File "exemplo.py", line 2, in <module>
    print(soma)
          ^^^^
NameError: name 'soma' is not defined
```

- `resposta_1` = tipo da exceção
- `resposta_2` = nome da variável inexistente

**Exercício 6 — stack trace 2 (TypeError)**

```python
def dobro(n):
    return n * 2

resultado = dobro()
```

```text
Traceback (most recent call last):
  File "exemplo.py", line 4, in <module>
    resultado = dobro()
TypeError: dobro() missing 1 required positional argument: 'n'
```

- `resposta_3` = tipo da exceção
- `resposta_4` = nome da função chamada sem argumento

**Exercício 7 — stack trace 3 (IndexError)**

```python
idades = [15, 22, 30]
print(idades[3])
```

```text
Traceback (most recent call last):
  File "exemplo.py", line 2, in <module>
    print(idades[3])
          ~~~~~~^^^
IndexError: list index out of range
```

- `resposta_5` = tipo da exceção
- `resposta_6` = qual índice o código tentou usar

**Exercício 8 — stack trace 4 (ValueError)**

```python
texto = "dez"
numero = int(texto)
```

```text
Traceback (most recent call last):
  File "exemplo.py", line 2, in <module>
    numero = int(texto)
ValueError: invalid literal for int() with base 10: 'dez'
```

- `resposta_7` = tipo da exceção
- `resposta_8` = qual palavra a mensagem aponta como culpada

```bash
python3 fase-3-modularizacao/06-depuracao/atividade.py
```

> 📌 A Parte A valida o comportamento **corrigido**; a Parte B compara suas respostas ignorando maiúsculas e espaços. É assim que se testa código de verdade.

---

## 💡 Dicas (progressivas — sem gabarito)

**Exercício 1 — `maior_de_tres`**
1. A variável `maior` começa igual a `a`. Nas linhas seguintes, o sinal da comparação está mesmo certo?
2. Para `maior_de_tres(1, 2, 3)` o correto é 3 — trace o valor de `maior` em cada `if` e veja em qual deles ele para.
3. Tem um `if` que deveria SUBIR `maior` quando `c` é maior — repare em qual sinal o Python está lendo ali. Troque só esse sinal e rode de novo.

**Exercício 2 — `soma_ate`**
1. `range(1, n)` gera números até qual? Confira com `print(list(range(1, 5)))`.
2. O último número da soma é `n` — ele aparece no range atual?
3. O limite do `range` é exclusivo: para incluir o `n`, some 1 no segundo argumento. Teste `soma_ate(1)` antes e depois — é o caso que denuncia.

**Exercício 3 — `contar_pares`**
1. O que acontece com `contar_pares([2, 4, 6])`: o laço roda 3 vezes ou para antes?
2. Um `return` dentro do laço encerra a FUNÇÃO, não a volta.
3. Existe um `return` que deveria acontecer só **depois** de o laço terminar — mova a indentação dele para o nível do `for`.

**Exercício 4 — `total_do_carrinho`**
1. Imprima `total` dentro do laço: ele está somando ou sobrescrevendo?
2. `total = preco` coloca o preço de UMA iteração no lugar do acumulado.
3. A soma precisa de `+=` (acumule em cima do que já tinha), não de `=` simples. Teste com 3 preços diferentes.

**Exercício 5 — stack trace 1**
1. A última linha tem o formato `Tipo: mensagem` — o que vem antes dos dois-pontos?
2. A mensagem diz `name '...' is not defined` — o nome entre aspas é o suspeito.
3. `resposta_1`: copie a palavra antes dos dois-pontos em minúsculas. `resposta_2`: olhe o trecho de código apontado e o nome citado na mensagem.

**Exercício 6 — stack trace 2**
1. De novo: leia só a última linha.
2. `missing 1 required positional argument: 'n'` — o Python está reclamando de uma chamada, então o tipo é de chamada, não de valor.
3. `resposta_3` = a palavra antes dos dois-pontos, minúscula. `resposta_4` = o nome que aparece **antes** dos parênteses na mensagem.

**Exercício 7 — stack trace 3**
1. A última linha começa com o erro de **lista**.
2. `list index out of range` — qual número aparece entre colchetes no código apontado?
3. `resposta_5` = tipo em minúsculas; `resposta_6` = só o número que foi pedido dentro de `idades[...]`.

**Exercício 8 — stack trace 4**
1. Leia a última linha inteira, com calma.
2. `invalid literal for int() with base 10: '...'` — o Python devolve a palavra que ele não conseguiu converter.
3. `resposta_7` = tipo antes dos dois-pontos; `resposta_8` = a palavra entre aspas simples no fim da mensagem (sem as aspas).

## 🚀 Desafios extras

- **Ache o bug de produção:** em um arquivo novo, copie a Parte A, adicione um `print(">>>", total)` dentro do laço e explique no comentário por que o bug acontecia.
- **Escreva sua própria stack trace:** crie um código que levante `KeyError` de propósito e cole a saída real num comentário do `atividade.py`.
- **Colecione erros:** tente `int([])`, `[1, 2][9]` e `{}["a"]` e guarde o tipo de cada um numa lista `erros_vistos = []`.

## ✅ Checkpoint

- [ ] Sei que a última linha da stack trace = tipo + mensagem e é onde começo
- [ ] Sei que o trecho apontado diz ONDE estourou (e o trace, como cheguei lá)
- [ ] Usei `print` estratégico (valor + tipo) para caçar um bug sem chute
- [ ] Sei setar breakpoint no VS Code (`F9`) e passo a passo (`F10`)
- [ ] Tudo verde → marque o checkbox no [README raiz](../../README.md)
