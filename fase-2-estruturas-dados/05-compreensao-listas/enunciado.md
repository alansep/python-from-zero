# 05 — Compreensão de listas ⏱️ ~1h

**Meta:** escrever a sintaxe mais *pythonica* da linguagem: construir uma lista inteira numa linha, sem perder legibilidade.

---

## 📚 Teoria

### O problema do `for` "manual"

```python
dobros = []
for x in [1, 2, 3]:
    dobros.append(x * 2)
# dobros -> [2, 4, 6]
```

Funciona, mas gasta 3 linhas e uma variável "lixo" (`dobros = []` só existe para acumular).

### A *list comprehension*

```python
dobros = [x * 2 for x in [1, 2, 3]]
# dobros -> [2, 4, 6]
```

| Parte | Papel |
|---|---|
| `x * 2` | a **expressão** que entra na lista |
| `for x in ...` | o laço (igual um `for` normal) |
| `[ ... ]` | os colchetes criam a **lista** |

Leia como: *"lista de `x * 2` **para cada** `x` em `[1, 2, 3]`"*.

```python
>>> [len(p) for p in ["oi", "abc"]]
[2, 3]
>>> [p.upper() for p in ["ana", "bia"]]
['ANA', 'BIA']
```

### Com filtro — `if` no final

```python
>>> [x for x in [1, 2, 3, 4] if x % 2 == 0]
[2, 4]
```

> ⚠️ A ordem importa: é `for ... if ...` (o `if` **depois** do laço). Escrever `if ... for` dá `SyntaxError`.

```python
# equivalente ao laço completo:
pares = []
for x in [1, 2, 3, 4]:
    if x % 2 == 0:
        pares.append(x)
```

### Com dois resultados — `if / else` na expressão

Quando cada item vira **uma de duas coisas**, o `if/else` vai **antes** do `for` (é um ternário, não um filtro):

```python
>>> [n if n % 2 == 0 else 0 for n in [1, 2, 3]]
[0, 2, 0]

>>> ["par" if n % 2 == 0 else "ímpar" for n in [1, 2, 3, 4]]
['ímpar', 'par', 'ímpar', 'par']
```

| Objetivo | Sintaxe |
|---|---|
| só filtrar (manter ou descartar) | `[x for x in lista **if cond**]` |
| transformar em um dos dois valores | `[**a if cond else b** for x in lista]` |

### Compreensão aninhada

Os `for` aparecem **na ordem em que rodariam**:

```python
>>> matriz = [[1, 2], [3, 4]]
>>> [valor for linha in matriz for valor in linha]
[1, 2, 3, 4]
```

Leia: *"`valor` para cada `valor` em `linha`, **para cada** `linha` em `matriz`"*. Dá para juntar filtro e ternário, mas se passar de dois níveis prefira um `for` tradicional — legibilidade > uma linha.

### Existe comprehension para tudo?

| Tipo | Literal |
|---|---|
| lista | `[x for x in ...]` |
| conjunto | `{x for x in ...}` (remove duplicatas!) |
| dicionário | `{k: v for ...}` |

```python
>>> {len(p) for p in ["oi", "abc", "oi"]}
{2, 3}                      # repetições somem
```

📖 [List comprehensions — docs.python.org/pt-br](https://docs.python.org/pt-br/3/tutorial/datastructures.html#list-comprehensions)

---

## ✍️ Exercícios

Abra [`atividade.py`](./atividade.py) — são 6 exercícios:

1. **`dobros(lista)`** → o dobro de cada item, com comprehension simples. Lista vazia → `[]`.
2. **`pares(lista)`** → só os números **pares**, com comprehension **com `if`**.
3. **`maiusculas(palavras)`** → cada palavra transformada com `.upper()`.
4. **`classificar(numeros)`** → lista de `"par"`/`"ímpar"` usando **ternário** `if/else` **dentro** da comprehension.
5. **`comprimentos(palavras)`** → o `len()` de cada palavra.
6. **`achatada(matriz)`** → uma lista só a partir de lista de listas (comprehension **aninhada**).

```bash
python3 fase-2-estruturas-dados/05-compreensao-listas/atividade.py
```

> 📌 Os testes verificam a **ordem** dos itens — comprehension preserva a ordem do laço. E conferem listas vazias em todos os exercícios.

---

## 💡 Dicas (progressivas — sem gabarito)

**Exercício 1 — `dobros`**
1. O que sobra de um `for` com `append` quando você joga tudo para uma linha entre colchetes?
2. A expressão vem **antes** do `for`: `x * 2 for x in lista`.
3. O cálculo ocupa o lugar do item na lista que você está construindo — envolva a expressão e o laço nos colchetes e devolva o resultado.

**Exercício 2 — `pares`**
1. Aqui a expressão é o próprio item — então quem é que faz o filtrar?
2. O `if` vai **depois** do `in` (é filtro, não é ternário) e a expressão continua sendo o próprio item.
3. Comece pela comprehension que devolve o próprio item e acrescente o filtro **depois** do `in`, com um `if` que compara o resto da divisão por 2.

**Exercício 3 — `maiusculas`**
1. Nenhum filtro entra aqui — como trocar cada palavra por ela mesma em outra caixa?
2. Existe um método de string que devolve tudo maiúsculo.
3. Mesma estrutura do exercício 1: mude só o que vai antes do `for`, para o método de caixa alta aplicado ao item.

**Exercício 4 — `classificar`**
1. Cada número **não** é descartado: ele vira um texto ou outro. Isso é filtro ou ternário?
2. `valor_se_verdadeiro if condição else valor_se_falso` é a expressão que ocupa o lugar do `x`.
3. Monte primeiro o ternário sozinho (testando um número só) e, quando sair certo, ponha-o no lugar da expressão da comprehension — repare que o `if/else` vem **antes** do `for`.

**Exercício 5 — `comprimentos`**
1. Só trocar cada palavra pelo resultado de uma função built-in — qual é ela?
2. `len(palavra)` é a expressão.
3. Estrutura idêntica ao exercício 1 — só muda o que se escreve antes do `for`: a chamada de tamanho sobre o item.

**Exercício 6 — `achatada`**
1. São dois laços aninhados — como eles aparecem, e em que ordem, dentro da comprehension?
2. Os dois `for` saem um do lado do outro, **depois** da expressão, na mesma ordem em que rodariam.
3. Se travar, escreva primeiro o `for` duplo com `append` e só depois encolha: os dois `for` saem na ordem em que rodariam (o de fora primeiro) e a expressão continua na frente deles.

## 🚀 Desafios extras

- **Sem comprehension:** reescreva o exercício 1 com `for` + `append` e compare as duas versões.
- **Filtro + transformação:** `[x * 2 for x in [1, 2, 3, 4] if x > 2]` — descubra a saída **no papel** e confirme rodando.
- **Set comprehension:** conte os tamanhos únicos das palavras de uma lista com `{len(p) for p in palavras}` e veja as repetições sumirem.

## ✅ Checkpoint

- [ ] Sei montar uma comprehension simples: `[expressao for item in iteravel]`
- [ ] Sei que o filtro vai **depois** do `for` e o ternário **antes**
- [ ] Consigo ler uma comprehension aninhada de duas formas (de dentro e de fora)
- [ ] Sei quando **não** usar comprehension (aninhamento difícil de ler → `for` tradicional)
- [ ] Tudo verde → marque o checkbox no [README raiz](../../README.md)
