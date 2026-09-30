# 01 — Funções e Escopo ⏱️ ~3h

**Meta:** transformar trechos soltos de código em blocos com **nome, parâmetros e retorno previsíveis** — e entender onde cada variável "vive".

---

## 📚 Teoria

### 1.1 Definindo e chamando

```python
def saudacao(nome, cumprimento="Olá"):   # parâmetro com VALOR PADRÃO
    return f"{cumprimento}, {nome}!"     # devolve o resultado p/ quem chamou
```

| Conceito | Como funciona |
|---|---|
| `def` | declara a função; o corpo é o que está **indentado** |
| parâmetro posicional | `saudacao("Ana")` — ordem importa |
| parâmetro nomeado | `saudacao("Ana", cumprimento="Oi")` — ordem deixa de importar |
| valor padrão (default) | `cumprimento="Olá"` → usado quando o argumento não é passado |
| `return` | **encerra** a função e devolve um valor |
| sem `return` | a função devolve `None` (o `None` é implícito) |

```python
def somar(a, b):
    return a + b      # um valor

def min_max(v):       # vários valores: viram UMA tupla
    return min(v), max(v)

menor, maior = min_max([3, 9, 1])   # desempacotamento
```

> ⚠️ **Valor padrão é avaliado UMA vez**, na hora do `def`. Por isso nunca se escreve `def f(lista=[])` — a mesma lista seria reutilizada em toda chamada. Prefira `lista=None` e trate `None` dentro da função.

- Quer detalhes oficiais? [Definindo funções](https://docs.python.org/pt-br/3/tutorial/controlflow.html#defining-functions) e [`return`](https://docs.python.org/pt-br/3/reference/compound_stmts.html#return).

### Função pura × função com efeito colateral

| | **Pura** (preferida) | **Com efeito colateral** |
|---|---|---|
| Entrada → saída | sempre o mesmo resultado | pode depender do "mundo externo" |
| Modifica argumentos? | **não** | sim (ex.: `lista.append`) |
| Facilidade de testar | alta | baixa |

```python
def dobrar(valores):
    return [v * 2 for v in valores]   # devolve OUTRA lista — a original intocada
```

### 1.2 Escopo: onde a variável vive

```python
contador = 0              # escopo GLOBAL (módulo)

def acumular(total):
    contador = total      # escopo LOCAL: cria uma variável NOVA, não mexe na global
    return contador
```

- **Local:** nasce dentro da função e **morre** quando ela termina.
- **Global:** vive no arquivo; qualquer função **lê**, mas alterar exige `global contador` (quase sempre sinal de má ideia).
- Uma função local **não vaza** para fora; uma global **é visível** de dentro (leitura).
- Escopo na norma oficial: [Nomes e escopos](https://docs.python.org/pt-br/3/tutorial/classes.html#python-scopes-and-namespaces).

> 🔑 Pergunta-chave ao ler código: *"esta variável foi criada DENTRO da função ou FORA dela?"* — metade dos bugs de iniciante é responder isso errado.

---

## ✍️ Exercícios

Abra [`atividade.py`](./atividade.py) — são 5 exercícios:

1. **`saudacao(nome, cumprimento="Olá")`** → `"{cumprimento}, {nome}!"`.
   Teste os três caminhos: só `nome`, `cumprimento` posicional e `cumprimento` nomeado.
2. **`min_max(valores)`** → tupla `(menor, maior)`; lista vazia → `None`.
3. **`dobrar(valores)`** → **nova** lista com cada valor × 2. A lista original **não pode mudar** (função pura).
4. **`contar_pares(valores)`** → quantidade de números pares. **Obrigatório: a função precisa ter docstring** (texto entre `"""` logo abaixo do `def`, com pelo menos 5 caracteres) — a validação verifica isso.
5. **`acumular(valores)`** → soma da lista usando uma variável **local**. A variável de módulo `contador` **permanece `0`** — a validação confere.

```bash
python3 fase-3-modularizacao/01-funcoes/atividade.py
```

> 📌 A validação testa casos-limite (lista vazia, negativos, `None` implícito, docstring ausente). É assim que se testa código de verdade.

---

## 💡 Dicas (progressivas — sem gabarito)

**Exercício 1**
1. Quantos parâmetros a assinatura precisa? Qual deles tem valor padrão?
2. `f"{cumprimento}, {nome}!"` já monta a frase inteira — o `return` é uma linha só.
3. Não faça `if cumprimento is None:`: quem decide o texto padrão é o valor colocado **depois do `=`** no `def`. Basta devolver a f-string com os dois parâmetros.

**Exercício 2**
1. O que acontece com `min([])`? Deveria explodir ou devolver algo?
2. Toda função que precisa "não ter resposta" devolve `None` — mas só no caso vazio.
3. Trate `if not valores: return None` antes de calcular; no resto, devolva uma tupla com os dois resultados separados por vírgula.

**Exercício 3**
1. `append` modifica a lista de quem chamou — quer esse efeito colateral?
2. Monte uma lista NOVA com `for` + `append` (ou list comprehension) e devolva a nova.
3. Crie `resultado = []` antes do loop, preencha `resultado` com `v * 2`, e no final `return resultado`. A `valores` original não deve ser tocada em nenhum ponto.

**Exercício 4**
1. Onde, exatamente, a docstring precisa ficar para o Python reconhecer?
2. Todo `def` pode ter uma string logo na primeira linha do corpo — entre três aspas.
3. Escreva `"""Conta quantos valores da lista são pares."""` logo abaixo do `def`; depois conte com um contador local e `if valor % 2 == 0: ...`.

**Exercício 5**
1. A soma pode ficar em qual variável — na `contador` de módulo ou em outra criada dentro da função?
2. `total = 0` antes do loop; `total = total + valor` dentro dele; `return total` depois.
3. Não escreva `global contador` em lugar nenhum: crie uma variável nova com outro nome dentro do corpo, Some nela e devolva — a global nem fica sabente.

## 🚀 Desafios extras

- **`apresentar(pessoa, pet=None)`** — devolva `"Ana e Rex"` ou `"Ana (sem pet)"` conforme o argumento opcional.
- **Função que aceita o gatilho:** faça `dobrar` devolver `None` (e não uma lista) quando receber `[]` — pratique o `return` condicional.
- **Pura de verdade:** reescreva `dobrar` sem usar `for` nem list comprehension, só com `map`.

## ✅ Checkpoint

- [ ] Sei declarar função com `def`, usar padrão, posicional e nomeado
- [ ] Sei que sem `return` a função devolve `None`
- [ ] Consigo devolver vários valores numa tupla e desempacotar
- [ ] Entendi a diferença entre variável local e global (e evito `global`)
- [ ] Tudo verde → marque o checkbox no [README raiz](../../README.md)
