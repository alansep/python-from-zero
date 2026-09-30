# 04 — Algoritmos Clássicos ⏱️ ~2.5h

**Meta:** escrever com as próprias mãos os dois algoritmos que todo desenvolvedor precisa entender: **busca linear** e **bubble sort** — nada de mágica pronta.

---

## 📚 Teoria

### 4.1 Busca linear

Percorre a lista **do início ao fim** até achar (ou acabar):

```python
def buscar(lista, alvo):
    for indice in range(len(lista)):
        if lista[indice] == alvo:
            return indice      # achou: devolve ONDE está
    return -1                  # não achou: sentinela -1
```

Dry-run com `lista = [4, 8, 15, 16, 23, 42]`:

| passo | `indice` | `lista[indice]` | igual a `16`? |
|---|---|---|---|
| 1 | 0 | 4 | não |
| 2 | 1 | 8 | não |
| 3 | 2 | 15 | não |
| 4 | 3 | 16 | **sim → `return 3`** |

- **Lista vazia:** o `for` nem começa → devolve `-1`.
- **Duplicados:** o `for` encontra o **primeiro** — por isso o retorno é o menor índice.
- **Custo:** no pior caso visita todos os `n` elementos → **O(n)**.
- Detalhes: [laços e `range`](https://docs.python.org/pt-br/3/tutorial/controlflow.html#for-statements).

> 🔎 `-1` é um "sentinela": um valor que **não pode ser um índice válido**, então dá para testar com `if resultado != -1`.

### 4.2 Bubble Sort — a mecânica das trocas

Ideia: **comparar vizinhos e trocar se estiverem fora de ordem**. Cada varredura "borbulha" o maior até o fim:

```python
def bubble_sort(lista):
    n = len(lista)
    for rodada in range(n - 1):
        for i in range(n - 1 - rodada):     # o fim encolhe: o último já está certo
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]   # troca
    return lista
```

Trace com `[5, 1, 4, 2]`:

| rodada | comparações e trocas | resultado ao fim da rodada |
|---|---|---|
| 1 | 5>1 troca · 5>4 troca · 4>2 troca | `[1, 4, 2,` **`5`**`]` |
| 2 | 4>2 troca · 2>5 não | `[1, 2,` **`4, 5`**`]` |
| 3 | 2>4 não | `[1,` **`2, 4, 5`**`]` |

- A **troca em Python** é a famosa atribuição simultânea: `a, b = b, a` (sem variável auxiliar).
- `range(n - 1 - rodada)` evita re-comparar a cauda já ordenada.
- Pior caso **O(n²)** — é por isso que bubble sort é didático, não industrial.

> 🚫 **Neste exercício é PROIBIDO `sorted(lista)` e `lista.sort()`** — o objetivo é você escrever as trocas. A validação confere apenas o **resultado**; quem trapaceia perde o estudo (o checador não é palpiteiro 🕵️).

---

## ✍️ Exercícios

Abra [`atividade.py`](./atividade.py) — são 3 exercícios:

1. **`buscar(lista, alvo)`** → índice da **primeira** ocorrência ou `-1`.
   Casos: lista vazia, ausente, duplicado (primeiro índice), encontrado no fim.
2. **`buscar_todos(lista, alvo)`** → **lista** com TODOS os índices das ocorrências (`[]` se nenhuma).
3. **`bubble_sort(lista)`** → lista em ordem **crescente**, com laços e trocas feitos à mão.
   Você pode devolver **a mesma lista** ordenada ou **uma nova** — os dois passam.

```bash
python3 fase-3-modularizacao/04-algoritmos/atividade.py
```

> 📌 A validação testa casos-limite (lista vazia, 1 elemento, já ordenada, inversa, duplicados, negativos). É assim que se testa código de verdade.

---

## 💡 Dicas (progressivas — sem gabarito)

**Exercício 1**
1. Enquanto você não achar, o que precisa acontecer com o índice do laço? E quando achar?
2. `range(len(lista))` gera cada posição; compare `lista[indice] == alvo`.
3. Se achar, devolva na hora (senão o `-1` final nunca é alcançado); se o laço terminar, devolva `-1`. Listas vazias já caem direto no `-1`.

**Exercício 2**
1. O que muda em relação ao exercício 1: você **para** no primeiro ou **continua**?
2. Guarde as posições em uma lista nova — `append` é seu amigo.
3. Monte `achados = []`, compare cada elemento e faça `achados.append(indice)` quando bater; `return achados` no final (vazio, se nada bateu).

**Exercício 3**
1. Quantas listas você precisa percorrer: uma só, ou vizinhos par-a-par?
2. A troca `lista[i], lista[i + 1] = lista[i + 1], lista[i]` dispensa variável auxiliar.
3. Aninhe dois laços: o de fora faz `n - 1` rodadas, o de dentro compara `i` com `i + 1` até onde a cauda já ordenada começa; dentro, só `if lista[i] > lista[i + 1]:` com a troca. Devolva a lista no fim.

## 🚀 Desafios extras

- **Contador de trocas:** faça `bubble_sort` devolver `(lista, trocas)` — quantas trocas cada entrada exige? Comparar com a lista inversa.
- **Ordenação decrescente:** inverta o sinal da comparação e teste com os mesmos casos.
- **Já ordenado?** implemente `esta_ordenada(lista)` e use um `break` para encerrar o bubble sort cedo quando nenhuma troca acontecer numa rodada.

## ✅ Checkpoint

- [ ] Sei por que a busca linear é O(n) e devolve `-1` como sentinela
- [ ] Sei por que o primeiro índice é o que importa em listas com duplicados
- [ ] Consegui traçar o bubble sort à mão (rodada a rodada)
- [ ] Entendi a troca simultânea `a, b = b, a` e o `range` que encolhe
- [ ] Tudo verde → marque o checkbox no [README raiz](../../README.md)
