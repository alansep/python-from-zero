# 02 — Módulos e Importação ⏱️ ~2h

**Meta:** parar de reinventar a roda — **importar** o que a biblioteca padrão já resolve por você e entender como um arquivo vira um módulo.

---

## 📚 Teoria

### Formas de importar

```python
import math                       # pacote inteiro: math.sqrt(9)
import random as rnd              # apelido
from math import sqrt, pi         # só o que preciso: sqrt(9)
from datetime import date         # direto no namespace
```

| Forma | Quando usar |
|---|---|
| `import modulo` | quando usa várias coisas do módulo (`math.ceil`, `math.floor`...) |
| `import modulo as apelido` | nomes longos (`import datetime as dt`) |
| `from modulo import nome` | quando só um item interessa |
| `from modulo import *` | ❌ evite — polui o namespace e esconde a origem |

> 📦 Tudo isso que vem **sem instalar nada** é a **biblioteca padrão** (*stdlib*): [Visão geral da stdlib](https://docs.python.org/pt-br/3/library/index.html).

### O tour da stdlib que você vai usar

**`math`** — [docs](https://docs.python.org/pt-br/3/library/math.html)

```python
math.sqrt(9)      # 3.0   (sempre float)
math.ceil(3.2)    # 4     (teto — arredonda pra CIMA)
math.floor(3.8)   # 3     (piso)
math.pi           # 3.14159...
```

**`random`** — [docs](https://docs.python.org/pt-br/3/library/random.html)

```python
random.seed(42)             # deixa a "sorte" reproduzível (ótimo pra teste)
random.randint(1, 6)        # inteiro entre 1 e 6 (inclui as pontas)
random.shuffle(lista)       # embaralha NO LÁTIMO, modificando a própria lista
nova = random.sample(lista, 3)  # sorteia 3 itens SEM repetição (nova lista)
```

**`datetime`** — [docs](https://docs.python.org/pt-br/3/library/datetime.html)

```python
from datetime import date, timedelta
d = date(2026, 1, 1)
d.weekday()          # 0=segunda ... 5=sábado, 6=domingo
date(2026, 1, 31) - d   # objeto timedelta
(date(2026, 1, 31) - d).days   # 30
```

**`json`** — [docs](https://docs.python.org/pt-br/3/library/json.html)

```python
import json
json.dumps({"nome": "José"})   # dict -> str (serialização)
json.loads('{"nome": "José"}') # str -> dict (deserialização)
```

**`csv`** — [docs](https://docs.python.org/pt-br/3/library/csv.html)

```python
import csv, io
leitor = csv.reader(io.StringIO("nome,idade\nAna,30\n"))
next(leitor)      # primeira linha (cabeçalho) -> ['nome', 'idade']
list(leitor)      # o resto -> [['Ana', '30']]
```

### `if __name__ == "__main__":`

```python
def utilidade():
    ...

if __name__ == "__main__":
    print(utilidade())   # só roda quando VOCÊ executa o arquivo
```

- Importado por outro arquivo → `__name__` vira o nome do módulo e **esse bloco não executa**.
- Executado direto no terminal → `__name__` é `"__main__"` e o bloco roda.
- É o padrão para separar **código biblioteca** de **código de teste**. Veja [Módulos](https://docs.python.org/pt-br/3/tutorial/modules.html).

---

## ✍️ Exercícios

Abra [`atividade.py`](./atividade.py) — são 7 exercícios. **Importe você mesmo** o que precisar (`math`, `random`, `datetime`, `json`, `csv`, `io`...):

1. **`raiz_de(x)`** → `math.sqrt(x)` (sempre devolve `float`).
2. **`teto(n)`** → `math.ceil(n)` — teste mentalmente com negativo: `teto(-3.2)` deve dar `-3`, não `-4`.
3. **`embaralhar(valores)`** → nova lista com os MESMOS elementos em outra ordem; a lista original **intacta**.
4. **`fim_de_semana(ano, mes, dia)`** → `True`/`False` usando `date(ano, mes, dia).weekday()` (5 e 6 são sábado/domingo).
5. **`dias_entre(a, b)`** → recebe dois objetos `date` e devolve `(b - a).days` — **aceite o sinal negativo** se `b` vier antes de `a`.
6. **`para_json(dados)`** → `json.dumps(...)` devolvendo `str` que o `json.loads` devolve igualzinho (roundtrip com acentos).
7. **`cabecalho(texto)`** → primeira linha de um CSV usando `csv.reader` + `next()` — precisa lidar com campo entre aspas que contém vírgula.

```bash
python3 fase-3-modularizacao/02-modulos/atividade.py
```

> 📌 A validação testa casos-limite (raiz de 0, teto negativo, datas fixas, campo entre aspas, Unicode). É assim que se testa código de verdade.

---

## 💡 Dicas (progressivas — sem gabarito)

**Exercício 1**
1. Qual módulo da stdlib tem a raiz quadrada? Como você importaria ele?
2. `math.sqrt` devolve sempre `float` — nem precisa converter.
3. No topo do arquivo: `import math`. Depois `return math.sqrt(x)`.

**Exercício 2**
1. `round()` arredonda para o mais PRÓXIMO — é isso que pedimos?
2. `math.ceil` devolve `int`, e ele zera a parte fracionária para cima inclusive nos negativos.
3. `import math` + `return math.ceil(n)`. Se `teto(-3.2)` der `-4`, você usou outro arredondador.

**Exercício 3**
1. `random.shuffle` modifica a lista de quem chamou — é efeito colateral. O que fazer antes de embaralhar?
2. Copie a lista primeiro (`list(valores)` ou `valores[:]`) e embaralhe a cópia.
3. `import random`; `copia = list(valores)`; `random.shuffle(copia)`; `return copia`.

**Exercício 4**
1. Você recebe ano, mês e dia separados — quem transforma isso numa data?
2. `.weekday()` devolve 0 a 6; quais dois números representam fim de semana?
3. `from datetime import date`; monte `date(ano, mes, dia)` e devolva a comparação `... in (5, 6)` (ou `>= 5`).

**Exercício 5**
1. Subtraindo uma `date` de outra, o Python devolve QUAL tipo de objeto?
2. Esse objeto tem um atributo `.days` — é ele que pedimos.
3. `return (b - a).days`. Não use `abs()`: o sinal faz parte do resultado.

**Exercício 6**
1. Qual função do `json` converte dict em texto? E a que volta?
2. "Roundtrip" = serializa e desserializa; a comparação é com o dict ORIGINAL.
3. `import json` + `return json.dumps(dados)`; a validação faz `json.loads` no que você devolveu e compara com a entrada — acentos precisam sobreviver.

**Exercício 7**
1. `texto.split(",")` quebra num CSV de verdade? E no campo `"Silva, João"`?
2. `csv.reader` aceita um *file-like* — com texto na memória, use `io.StringIO`.
3. `import csv, io`; crie o reader com `csv.reader(io.StringIO(texto))` e pegue a primeira linha com `next(leitor)`.

## 🚀 Desafios extras

- **`if __name__ == "__main__"`:** acrescente o bloco no fim do `atividade.py` e faça ele imprimir `para_json({"ok": True})` — teste rodando o arquivo e depois importando-o.
- **Dado viciado:** com `random.seed(7)`, descubra quais 6 números o `randint(1, 6)` sorteia em sequência e comente no código.
- **Formatador:** use `f"{valor:.2f}"` para devolver preços com 2 casas (`para_json` de `{"preco": 10.5}` → `10.5`, mas `f` → `"10.50"`).

## ✅ Checkpoint

- [ ] Sei as 4 formas de importar e quando usar cada uma
- [ ] Já usei `math`, `random`, `datetime`, `json` e `csv` num mesmo arquivo
- [ ] Entendi `if __name__ == "__main__"` e por que ele existe
- [ ] Sei o que é roundtrip (serializar → desserializar → igual)
- [ ] Tudo verde → marque o checkbox no [README raiz](../../README.md)
