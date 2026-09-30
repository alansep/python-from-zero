# 02 — Tuplas e Conjuntos ⏱️ ~1.5h

**Meta:** guardar dados que **não mudam** (tuplas) e coleções que **não aceitam repetição** (conjuntos).

---

## 📚 Teoria

### Tuplas — a lista que não muda

Uma tupla é quase igual à lista, mas é **imutável**: depois de criada, nenhum item pode ser trocado, adicionado ou removido.

```python
ponto = (3, 4)          # parênteses
unico = (7,)             # ⚠️ a vírgula é obrigatória para tupla de 1 item
vazia = ()
```

```python
>>> t = (1, 2, 3)
>>> t[0]
1
>>> t[-1]
3
>>> t[1:]
(2, 3)                   # fatia de tupla devolve tupla
```

### Imutabilidade — o que acontece ao tentar mudar

```python
>>> t = (1, 2, 3)
>>> t[0] = 99
TypeError: 'tuple' object does not support item assignment
```

| | Lista `[...]` | Tupla `(...)` |
|---|---|---|
| Pode mudar depois de criada? | sim | **não** |
| Sintaxe | `[1, 2, 3]` | `(1, 2, 3)` |
| Método `append`/`sort` | tem | 💥 `AttributeError` |
| Uso típico | coleção que cresce | registro fixo, coordenadas, `(x, y)` |

> 💡 **Por que usar tupla?** Ela "trava" os dados: se o código não pode alterar algo, uma tupla **impede o bug silencioso**. Também serve para **devolver vários valores** de uma vez.

```python
def min_e_max(lista):
    return (min(lista), max(lista))     # devolve uma tupla

menor, maior = min_e_max([3, 1, 4])     # desempacotamento
```

```python
>>> x, y = (3, 4)
>>> x
3
```

### Conjuntos (`set`) — sem repetição e sem ordem

```python
>>> numeros = {1, 2, 2, 3, 3, 3}
>>> numeros
{1, 2, 3}                 # as repetições somem sozinhas
>>> type(numeros)
<class 'set'>
```

- **Não tem ordem** — por isso o resultado de um `set` deve ser comparado com `sorted()` (ordenação) ou com outro `set`.
- **Não aceita duplicatas.**
- ⚠️ `{}` cria um **dicionário**, não um conjunto. Tupla vazia vira set com `set()`.

```python
>>> set([3, 1, 3, 2, 1])
{1, 2, 3}
>>> 2 in {1, 2, 3}
True
```

### Deduplicação — o truque mais útil do `set`

```python
>>> lista = ["ana", "bia", "ana", "caio", "bia"]
>>> sorted(set(lista))
['ana', 'bia', 'caio']    # ordenou E removeu duplicatas
>>> len(lista), len(set(lista))
(5, 3)                    # tamanho antes, tamanho depois
```

### Operações de conjunto

```python
>>> a = {1, 2, 3}
>>> b = {2, 3, 4}
>>> a | b                 # união      -> {1, 2, 3, 4}
>>> a & b                 # interseção -> {2, 3}
>>> a - b                 # diferença  -> {1}   (só o que tem em a)
```

| O que quer | Operador | Método equivalente |
|---|---|---|
| união | `a \| b` | `a.union(b)` |
| interseção | `a & b` | `a.intersection(b)` |
| diferença (`a` sem `b`) | `a - b` | `a.difference(b)` |
| pertinência | `valor in a` | `a.__contains__(valor)` |
| tamanho | `len(a)` | — |

📖 [Tuplas — docs.python.org/pt-br](https://docs.python.org/pt-br/3/tutorial/datastructures.html#tuples-and-sequences) · [Conjuntos — docs.python.org/pt-br](https://docs.python.org/pt-br/3/library/stdtypes.html#set)

---

## ✍️ Exercícios

Abra [`atividade.py`](./atividade.py) — são 7 exercícios:

1. **`coordenadas(x, y)`** → devolve a **tupla** `(x, y)`. Precisa ser `tuple` de verdade — o teste tenta atribuir num índice para provar que é imutável.
2. **`tamanho_antes_depois(lista)`** → tupla `(tamanho original, tamanho sem duplicatas)`.
3. **`sem_duplicatas(lista)`** → **lista** com cada item aparecendo uma única vez. A ordem não importa (o teste ordena antes de comparar).
4. **`uniao(a, b)`** → **conjunto** união (`|`).
5. **`interseccao(a, b)`** → **conjunto** com os itens presentes nos dois (`&`).
6. **`diferenca(a, b)`** → **conjunto** com o que existe em `a` e **não** existe em `b` (`-`).
7. **`pertence(item, colecao)`** → `True`/`False` se `item` está dentro de `colecao` (`in`) — serve para lista, tupla, conjunto e até string.

```bash
python3 fase-2-estruturas-dados/02-tuplas-conjuntos/atividade.py
```

> 📌 Os testes comparam conjuntos com `==` (ordem não importa) e listas com `sorted()` — é assim que se testa quem trabalha com `set`.

---

## 💡 Dicas (progressivas — sem gabarito)

**Exercício 1 — `coordenadas`**
1. O que separa os itens numa tupla literal?
2. A tupla literal usa parênteses **e** uma vírgula entre os itens — sem a vírgula, `(x)` é só um valor entre parênteses.
3. É uma construção de uma linha. Para conferir a imutabilidade na mão, abra o Python, pegue o resultado em `co` e tente atribuir em `co[0]`.

**Exercício 2 — `tamanho_antes_depois`**
1. Dois tamanhos: o da lista como está e o da lista **sem repetições**. Qual função transforma lista em conjunto?
2. `len(lista)` e `len(set(lista))` já são os dois números.
3. Os dois números vêm de duas chamadas que **contam** — monte as duas juntas numa tupla de retorno, na ordem que o enunciado pede.

**Exercício 3 — `sem_duplicatas`**
1. O `set(...)` remove as repetições — mas o enunciado pede uma **lista** no final. Como voltar ao tipo certo?
2. `set` remove duplicatas; `list(...)` devolve para lista. A ordem pode ficar embaralhada, por isso o teste ordena.
3. São duas conversões encadeadas: primeiro a estrutura que rejeita repetição, depois o tipo que o enunciado exige. Deixe a ordenação por conta da validação.

**Exercício 4 — `uniao`**
1. Qual operador junta dois conjuntos mesmo se houver itens repetidos nos dois?
2. `a | b` é a união (o pipe fica ao lado do `]` no teclado).
3. O resultado de um operador de conjunto **já** é conjunto: devolva a operação direto, sem converter nada.

**Exercício 5 — `interseccao`**
1. Você quer só o que aparece **nos dois** conjuntos — é `&` ou `|`?
2. `a & b` devolve os elementos comuns.
3. Mesmo formato do exercício anterior: uma operação entre `a` e `b` e um `return` que entrega o que ela gerou.

**Exercício 6 — `diferenca`**
1. Ordem importa aqui: `a - b` é diferente de `b - a`. De qual dos dois conjuntos o enunciado quer que sobrem os itens?
2. `a - b` remove de `a` tudo o que existe em `b`.
3. Antes de escolher o símbolo, decida qual dos dois conjuntos é o "resto" da conta — o enunciado já diz, é só reler.

**Exercício 7 — `pertence`**
1. Existe um operador que testa "está dentro" e devolve `True`/`False` — ele é o mesmo para lista, tupla, conjunto e string.
2. `item in colecao` é a expressão inteira.
3. Não há método a procurar: a expressão inteira **é** a resposta — um `return` e nada mais.

## 🚀 Desafios extras

- **Desempacotamento:** escreva `min_e_max(lista)` que devolve `(menor, maior)` e use `menor, maior = min_e_max([...])` num print.
- **Frozenset:** conjuntos imutáveis existem (`frozenset({1, 2})`) — tente criar um e rodar `fs.add(3)` para ver o erro.
- **Diferença simétrica:** descubra o que `a ^ b` faz e use para achar os itens que estão em **um** dos conjuntos, mas não nos dois.

## ✅ Checkpoint

- [ ] Sei que tupla é imutável e que `t[0] = 1` levanta `TypeError`
- [ ] Sei que `(7,)` tem vírgula e `{}` cria dicionário (não conjunto)
- [ ] Sei deduplicar com `set(lista)` e ordenar com `sorted(...)`
- [ ] Domino `|`, `&`, `-` e `in` em conjuntos
- [ ] Tudo verde → marque o checkbox no [README raiz](../../README.md)
