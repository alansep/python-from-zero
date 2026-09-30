# 03 — Dicionários ⏱️ ~2h

**Meta:** guardar dados **nomeados** (chave → valor), buscar sem percorrer tudo e trabalhar com objetos aninhados.

---

## 📚 Teoria

### O que é um dicionário

Enquanto a lista guarda itens **por posição**, o dicionário guarda por **chave**:

```python
aluno = {"nome": "Ana", "idade": 30, "nota": 9.5}
vazio = {}
```

```python
>>> aluno["nome"]
'Ana'
>>> len(aluno)
3
```

| | Lista | Dicionário |
|---|---|---|
| Acesso | por índice: `lista[0]` | por chave: `d["nome"]` |
| Ordem | ordem de inserção | ordem de inserção (Python 3.7+) |
| Chave | não tem (só posição) | precisa ser **imutável** (str, int, tuple) |
| Item repetido | pode | ❌ chave repetida **sobrescreve** |

```python
>>> d = {"a": 1, "a": 2}
>>> d
{'a': 2}                  # a última atribuição venceu
```

### Busca: `d[chave]` × `d.get(chave, padrão)`

```python
>>> perfil = {"nome": "Ana"}
>>> perfil["idade"]
KeyError: 'idade'         # 💥 a chave não existe
>>> perfil.get("idade")
None                      # devolve None (o padrão)
>>> perfil.get("idade", 0)
0                         # devolve o padrão que VOCÊ escolheu
>>> "nome" in perfil
True                      # `in` testa CHAVES, não valores
```

| Situação | `d["chave"]` | `d.get("chave", padrão)` |
|---|---|---|
| chave existe | devolve o valor | devolve o valor |
| chave **não** existe | 💥 `KeyError` | devolve `padrão` |

> 💡 Use `d["chave"]` quando a chave **precisa** existir (erro é bom: avisa do bug). Use `.get()` quando a ausência é normal.

### Criar e atualizar pares

```python
>>> d = {}
>>> d["nome"] = "Ana"        # cria a chave
>>> d["nome"] = "Bia"        # já existe? SOBRESCREVE
>>> d["idade"] = 30
>>> d
{'nome': 'Bia', 'idade': 30}
```

Contar ocorrências — o padrão mais repetido do Python:

```python
>>> palavras = ["ana", "bia", "ana"]
>>> contagem = {}
>>> for p in palavras:
...     contagem[p] = contagem.get(p, 0) + 1
>>> contagem
{'ana': 2, 'bia': 1}
```

### Remover

```python
>>> d = {"a": 1, "b": 2}
>>> del d["a"]              # apaga (KeyError se não existir)
>>> d.pop("b")              # apaga E devolve o valor
2
>>> d.pop("z", None)        # apaga com segurança: devolve o padrão
```

### Percorrer — `keys()`, `values()`, `items()`

```python
>>> notas = {"ana": 9, "bia": 7}
>>> for nome, nota in notas.items():   # desempacota os pares
...     print(nome, nota)
ana 9
bia 7

>>> list(notas.keys())      # ['ana', 'bia']
>>> list(notas.values())    # [9, 7]
```

### Dicionário aninhado — objetos dentro de objetos

É assim que se modela um "registro" com partes:

```python
perfil = {
    "nome": "Ana",
    "endereco": {
        "cidade": "São Paulo",
        "uf": "SP",
    },
}

perfil["endereco"]["cidade"]          # 'São Paulo'
perfil.get("endereco", {}).get("cidade")   # busca segura nas duas camadas
```

> ⚠️ `d2 = d1` **não copia**: as duas variáveis apontam para o mesmo dicionário. Use `d2 = dict(d1)`.

📖 [Dicionários — docs.python.org/pt-br](https://docs.python.org/pt-br/3/tutorial/datastructures.html#dictionaries) · [`dict` na referência — docs.python.org/pt-br](https://docs.python.org/pt-br/3/library/stdtypes.html#dict)

---

## ✍️ Exercícios

Abra [`atividade.py`](./atividade.py) — são 7 exercícios:

1. **`buscar(dicionario, chave, padrao=None)`** → o valor da chave; se não existir, o **padrão**. Use `.get(chave, padrao)`.
2. **`contar(lista)`** → dicionário com quantas vezes cada item apareceu (`{"a": 2, "b": 1}`).
3. **`mesclar(d1, d2)`** → **novo** dicionário com tudo; em chave repetida, o valor de `d2` vence. Os dois dicionários de entrada **não podem mudar**.
4. **`cidade_de(perfil)`** → o valor de `perfil["endereco"]["cidade"]`; se faltar `endereco` ou `cidade`, devolva `""` (sem levantar erro).
5. **`remover_chave(dicionario, chave)`** → apaga a chave **na própria** entrada e devolve `True`; se a chave não existir, devolve `False` e não mexe em nada.
6. **`pares(dicionario)`** → lista de tuplas `(chave, valor)` na ordem de inserção, usando `.items()`.
7. **`somar_valores(dicionario)`** → soma de todos os valores numéricos (dicionário vazio → `0`).

```bash
python3 fase-2-estruturas-dados/03-dicionarios/atividade.py
```

> 📌 A validação compara dicionários com `==` (ordem dos pares não atrapalha) e confere se você **não** alterou as entradas quando o enunciado pede um novo dicionário.

---

## 💡 Dicas (progressivas — sem gabarito)

**Exercício 1 — `buscar`**
1. Qual método do dicionário aceita um segundo argumento para ser usado quando a chave falta?
2. `dicionario.get(chave, padrao)` é a chamada inteira.
3. O `padrao` já vem pronto na assinatura da função — basta repassá-lo como o segundo argumento. Não precisa de `if`: uma única chamada resolve os dois casos.

**Exercício 2 — `contar`**
1. Você precisa de um dicionário vazio **antes** do laço — e de uma forma de somar 1 sem quebrar na primeira vez. Como você faria essa soma?
2. `contagem.get(item, 0) + 1` entrega o valor atual (ou 0) e soma.
3. Monte a contagem **antes** de percorrer a lista; dentro do laço, a chave atual passa a valer o que ela já valia mais um. O que interessa no final é o dicionário montado.

**Exercício 3 — `mesclar`**
1. Comece pela cópia: qual método/função cria um dicionário novo a partir de um existente?
2. `dict(d1)` copia; depois `atualizado.update(d2)` traz os pares do segundo por cima.
3. Faça a cópia, jogue os pares do segundo em cima dela e devolva a cópia. A pegadinha é que há um jeito de "jogar por cima" que atinge o dicionário **errado** — o teste compara as entradas depois da chamada.

**Exercício 4 — `cidade_de`**
1. São DUAS chaves seguidas — e qualquer uma pode faltar. Qual método aceita padrão?
2. `perfil.get("endereco", {})` devolve o endereço ou um dict vazio; em cima dele, `.get("cidade", "")`.
3. Duas buscas encadeadas, cada uma com seu próprio padrão: a primeira precisa devolver algo que também saiba responder `.get` (um dicionário), a segunda devolve o texto vazio.

**Exercício 5 — `remover_chave`**
1. Antes de apagar, é preciso perguntar se a chave está lá — e `in` no dicionário testa **chaves**. Como fazer essa pergunta?
2. `if chave in dicionario:` → `del dicionario[chave]` (ou `dicionario.pop(chave)`) e devolva `True`.
3. A pergunta vem primeiro. Rota positiva: apaga e avisa `True`; rota negativa: responde `False` **sem tocar** em nada — o dicionário precisa sair igualzinho.

**Exercício 6 — `pares`**
1. O método que devolve os pares em formato iterável — e qual função o transforma em lista?
2. `dicionario.items()` devolve as pares; `list(...)` converte.
3. O método devolve algo **parecido** com lista, mas não é lista — converta para o tipo exigido. A ordem de inserção já vem de graça, não precisa reconstruir nada.

**Exercício 7 — `somar_valores`**
1. Some os **valores**, não as chaves — qual método devolve só eles?
2. `dicionario.values()` + `sum(...)` (dicionário vazio já devolve `0`).
3. Extraia só os valores com o método certo e deixe a soma para uma função built-in que aceita qualquer sequência — inclusive a vazia, que resolve o caso-limite sozinha.

## 🚀 Desafios extras

- **Inverter:** receba `{"a": 1}` e devolva `{1: "a"}` com um laço sobre `.items()`.
- **Agrupar:** conte palavras de uma frase (`texto.split()`) usando o padrão do exercício 2 e devolva a palavra mais frequente.
- **Aninhado profundo:** crie `{"empresa": {"funcionarios": [{"nome": "Ana"}]}}` e extraia `"Ana"` com acesso encadeado protegido por `.get()`.

## ✅ Checkpoint

- [ ] Sei que `d[chave]` dá `KeyError` e `.get(chave, padrão)` não
- [ ] Sei que `in` testa chaves e que chave repetida sobrescreve
- [ ] Consigo criar/atualizar/remover pares sem perder os dados originais
- [ ] Sei percorrer com `.items()` e ler dicionários aninhados
- [ ] Tudo verde → marque o checkbox no [README raiz](../../README.md)
