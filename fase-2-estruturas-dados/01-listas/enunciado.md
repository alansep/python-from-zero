# 01 — Listas ⏱️ ~4h

**Meta:** armazenar vários valores numa única variável e manipulá-los por **índice**, **fatiamento** e **métodos**.

---

## 📚 Teoria

### O que é uma lista

Uma lista é uma **coleção ordenada e mutável** de itens. Ela pode misturar tipos (mas quase sempre guarda o mesmo tipo de propósito):

```python
notas = [7.5, 9.0, 6.2]
nomes = ["ana", "bia", "caio"]
misto = [1, "dois", 3.0, True]
vazia = []
```

### 1.1 Indexação — a posição começa em ZERO

```python
frutas = ["maçã", "banana", "kiwi", "uva"]
```

| Expressão | Resultado | Por quê |
|---|---|---|
| `frutas[0]` | `"maçã"` | primeiro item é o **0** |
| `frutas[1]` | `"banana"` | segundo item é o **1** |
| `frutas[-1]` | `"uva"` | negativo conta **de trás para frente** |
| `frutas[-2]` | `"kiwi"` | último menos um |
| `frutas[4]` | 💥 `IndexError` | não existe posição 4 (0 a 3) |

```python
>>> frutas[0]
'maçã'
>>> frutas[-1]
'uva'
```

> ⚠️ `len(frutas)` devolve **4** (a contagem de itens), mas o **último índice é 3** (`len - 1`). Esse "erro dos dois" é a armadilha nº 1 desta fase.

### Fatiamento (*slicing*) — `lista[inicio:fim]`

Devolve uma **sublista nova** com os itens de `inicio` até `fim - 1` (**o `fim` não entra**):

```python
numeros = [10, 20, 30, 40, 50]

numeros[1:4]   # [20, 30, 40]  — posição 1, 2 e 3
numeros[:2]    # [10, 20]      — omitiu o início → do começo
numeros[3:]    # [40, 50]      — omitiu o fim → até o final
numeros[:]     # [10, 20, 30, 40, 50] — cópia completa da lista
numeros[-2:]   # [40, 50]      — os dois últimos
```

| Situação | Resultado |
|---|---|
| `inicio >= fim` | `[]` (lista vazia, sem erro) |
| `fim` maior que o tamanho | vai até o fim, sem `IndexError` |
| fatia **atribuída** | substitui os itens *in place* (mutabilidade!) |

```python
>>> frutas[0:2]
['maçã', 'banana']
>>> frutas[10:20]      # pediu além do tamanho — devolve []
[]
```

**`[::-1]`** inverte a ordem (e funciona em strings também):

```python
>>> [1, 2, 3][::-1]
[3, 2, 1]
```

### Mutabilidade — listas mudam de conteúdo

```python
lista = [1, 2, 3]
lista[0] = 99      # permitido: a lista agora é [99, 2, 3]
lista += [4, 5]    # permitido: [99, 2, 3, 4, 5]
```

```python
>>> lista = [1, 2, 3]
>>> copia = lista          # ⚠️ NÃO copia: as duas variáveis apontam para a MESMA lista
>>> copia[0] = 99
>>> lista
[99, 2, 3]                 # a "original" mudou junto!
>>> outra = lista[:]       # ✅ fatia vazia cria uma cópia de verdade
```

### 1.2 Métodos essenciais

Todos abaixo **alteram a própria lista**, exceto `len` (que é função) e `in` (que é operador):

| O que quer | Como | Devolve |
|---|---|---|
| pôr no **fim** | `lista.append(x)` | `None` |
| pôr em **posição** | `lista.insert(indice, x)` | `None` |
| **remover e devolver** o último | `lista.pop()` | o item removido |
| **remover e devolver** o item numa posição | `lista.pop(indice)` | o item removido |
| remover a **1ª ocorrência** de um valor | `lista.remove(x)` | `None` (💥 se `x` não existir) |
| **ordenar** no próprio lugar | `lista.sort()` | `None` |
| **inverter** no próprio lugar | `lista.reverse()` | `None` |
| contar itens | `len(lista)` | `int` |
| verificar pertinência | `"kiwi" in lista` | `True`/`False` |

```python
>>> notas = [7.0, 4.5, 9.0]
>>> notas.append(6.0)
>>> notas
[7.0, 4.5, 9.0, 6.0]
>>> notas.sort()
>>> notas
[4.5, 6.0, 7.0, 9.0]
>>> notas.pop(0)
4.5
>>> notas
[6.0, 7.0, 9.0]
```

> ⚠️ `lista.remove(99)` com o valor ausente levanta **`ValueError`**. Proteja com `if 99 in lista:` antes.

### `sort()` × `sorted()` — a diferença que mais cai em prova

```python
lista = [3, 1, 2]

lista.sort()          # ⚠️ ordena NA própria lista e devolve None
resultado = lista.sort()
print(resultado)      # None

novo = sorted(lista)  # ✅ devolve uma NOVA lista ordenada, a original fica intacta
```

| | `lista.sort()` | `sorted(lista)` |
|---|---|---|
| Ordena a lista original? | sim | não |
| O que devolve | `None` | nova lista ordenada |
| Serve para qualquer iterável? | só listas | sim (tuplas, strings, dicionários...) |

📖 [Sequências comuns — docs.python.org/pt-br](https://docs.python.org/pt-br/3/library/stdtypes.html#common-sequence-operations) · [Tutoria: estruturas de dados](https://docs.python.org/pt-br/3/tutorial/datastructures.html)

---

## ✍️ Exercícios

Abra [`atividade.py`](./atividade.py) — são 9 exercícios:

1. **`extremos(lista)`** → tupla `(primeiro, último)`. Lista vazia → `(None, None)`.
2. **`ultimos(lista, n)`** → sublista com os **n últimos** itens. `n = 0` → `[]`; `n` maior que o tamanho → lista inteira; lista vazia → `[]`.
3. **`trocar(lista, i, j)`** → troca os itens nas posições `i` e `j` **na própria lista** e devolve a **mesma lista** (o objeto original, não uma cópia).
4. **`adicionar(lista, valor, indice=None)`** → se `indice` for `None`, usa `append`; caso contrário usa `insert`. Devolve o **novo tamanho** (`len`) da lista.
5. **`ordenar_em_origem(lista)`** → ordena **in place** com `sort()` e devolve **`None`**.
6. **`reverter_em_origem(lista)`** → inverte **in place** com `reverse()` e devolve **`None`**.
7. **`remover_indice(lista, indice)`** → remove com `pop(indice)`, **devolve o valor removido** e deixa a lista menor. Índice negativo é válido.
8. **`remover_primeira(lista, valor)`** → remove a **1ª ocorrência** com `remove(valor)` e devolve `True`. Se o valor não existir, devolve `False` e **não mexe** na lista.
9. **`resumo(lista)`** → tupla `(soma, média)`. Lista vazia → `(None, None)` (sem dividir por zero!).

```bash
python3 fase-2-estruturas-dados/01-listas/atividade.py
```

> 📌 A validação verifica **casos-limite**: listas vazias, listas de 1 item, índices negativos, listas já ordenadas e strings com acento.

---

## 💡 Dicas (progressivas — sem gabarito)

**Exercício 1 — `extremos`**
1. Como você pediria o primeiro item de uma lista... e o último, sem saber o `len`?
2. `lista[0]` e `lista[-1]` resolvem — mas e quando a lista não tem nenhum item?
3. Comece por uma guarda de lista vazia que encerra a função imediatamente; só depois puxe os dois extremos pelos índices e entregue os dois numa tupla.

**Exercício 2 — `ultimos`**
1. Fatiar com início **negativo** já te dá o rabo da lista — quanto falta para pegar `n` itens a partir da ponta?
2. `lista[-n:]` é o candidato natural. Pense em o que acontece quando `n = 0` (`-0` é `0`!).
3. Proteja primeiro o caso `n <= 0` com um `if` que devolve lista vazia; no resto do caminho, uma única fatia de início negativo já entrega os `n` últimos e ainda devolve a lista inteira quando `n` passa do tamanho.

**Exercício 3 — `trocar`**
1. Em Python dá para trocar duas variáveis numa linha só — isso também funciona com posições de lista, certo?
2. `lista[i], lista[j] = lista[j], lista[i]` faz a troca no próprio objeto.
3. Faça a troca com atribuição múltipla (um lado escrevendo no outro) e devolva a **mesma** variável recebida — nunca uma fatia, porque o teste compara a identidade do objeto.

**Exercício 4 — `adicionar`**
1. Um ramo para `indice is None`, outro para o resto. Qual método cada ramo usa?
2. `indice is None` → `lista.append(valor)`; senão → `lista.insert(indice, valor)`.
3. Depois dos dois métodos, o valor a devolver é o mesmo nos dois ramos — calcule o tamanho da lista uma única vez, quando o ramo já tiver feito o trabalho.

**Exercício 5 — `ordenar_em_origem`**
1. Qual método ordena a própria lista (e não devolve uma nova)?
2. `lista.sort()` ordena *in place* e devolve `None` — é exatamente o que se pede.
3. O método faz tudo sozinho: basta devolver o que ele entrega. Atenção: `None` **é** um retorno legítimo aqui — não tente devolver a lista.

**Exercício 6 — `reverter_em_origem`**
1. Qual método inverte a própria lista — e por que `lista[::-1]` **não** serve aqui?
2. `lista.reverse()` inverte no lugar e devolve `None`.
3. Mesma pegadinha do exercício anterior: devolva o resultado do método, e lembre de que ele não é a lista (mesmo parecendo).

**Exercício 7 — `remover_indice`**
1. Qual método remove **e devolve** o item da posição?
2. `lista.pop(indice)` já te entrega o valor removido numa expressão só.
3. Não separe em "remover" e depois "buscar o que saiu": o método faz as duas coisas numa chamada — e encolhe a lista sozinho, sem você precisar avisar.

**Exercício 8 — `remover_primeira`**
1. `remove` **explode** (`ValueError`) se o valor não estiver na lista. Como perguntar antes?
2. `"x" in lista` devolve `True`/`False` — é a proteção natural.
3. Duas rotas: a pergunta com `in` vem primeiro; na rota positiva mande remover e responda `True`, na negativa responda `False` **sem tocar** na lista.

**Exercício 9 — `resumo`**
1. Soma é laço com acumulador — ou uma função built-in que já faz isso. E a média?
2. `sum(lista)` soma tudo; `len(lista)` dá o divisor.
3. A lista vazia é o caso que **não** pode chegar até a divisão — trate-a com um `if` que devolve a tupla de ausência e encerra. No caminho normal, monte os dois números na mesma tupla, com a média calculada depois da soma.

## 🚀 Desafios extras

- **`insert` na prática:** escreva `inserir_no_fim(lista, valor)` usando `lista.insert(len(lista), valor)` e compare com `append`.
- **Ordenação decrescente:** faça `lista.sort(reverse=True)` e devolve a lista; depois tente com `sorted(lista, reverse=True)`.
- **Cópia segura:** receba uma lista, trabalhe numa cópia (`lista[:]`) e devolva a original intacta — some tudo com `sum` numa cópia e prove que a entrada não mudou.
- **Previsão de saída:** sem rodar, diga o que imprime `print([1, 2, 3][1:10], len([1, 2, 3]))`.

## ✅ Checkpoint

- [ ] Sei que índices começam em 0 e que `len(lista) - 1` é o último
- [ ] Sei que `lista[inicio:fim]` **não inclui** o `fim` e devolve uma **nova** lista
- [ ] Entendi a diferença entre mutar *in place* (`sort`, `reverse`, `append`) e criar cópias (`sorted`, `[:]`)
- [ ] Sei que `pop` devolve o item removido e `remove` só funciona se o valor existir
- [ ] Tudo verde → marque o checkbox no [README raiz](../../README.md)
