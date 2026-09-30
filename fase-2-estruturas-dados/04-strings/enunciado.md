# 04 — Strings ⏱️ ~1.5h

**Meta:** montar textos com **f-strings** e transformar strings com os métodos que o dia a dia exige.

---

## 📚 Teoria

### String é uma sequência (igual lista)

```python
>>> texto = "python"
>>> texto[0]
'p'
>>> texto[-1]
'n'
>>> texto[1:4]
'yth'
>>> texto[::-1]      # inverte
'nohtyp'
>>> len(texto)
6
```

String é **imutável**: `texto[0] = "P"` levanta `TypeError` — todo método devolve uma **nova** string.

### f-strings — texto com expressões dentro

```python
nome = "Ana"
nota = 9.5

print(f"Olá, {nome}!")                # Olá, Ana!
print(f"Nota final: {nota + 0.5}")    # expressão entre chaves
print(f"{nota:.1f} pontos")           # 9.5 pontos (formatação)
print("Olá, {}!".format(nome))        # jeito antigo (saiba reconhecer)
```

> A `f` antes das aspas é o que "abre" as chaves. Sem ela, `{nome}` fica literal.

### Métodos de transformação

```python
>>> "  oi   mundo  ".strip()
'oi   mundo'               # só as pontas
>>> "oi   mundo".split()
['oi', 'mundo']            # quebra nos espaços -> lista
>>> "a-b-c".split("-")
['a', 'b', 'c']            # quebra no separador que VOCÊ escolher
>>> "-".join(["a", "b", "c"])
'a-b-c'                    # junta a lista com o separador
>>> "a-b-c".replace("-", "+")
'a+b+c'                    # substitui TODAS as ocorrências
```

| Método | O que faz | Exemplo → resultado |
|---|---|---|
| `strip()` | remove espaços das **pontas** | `"  oi  "` → `"oi"` |
| `split(sep)` | quebra em **lista** | `"a b"` → `["a", "b"]` |
| `join(lista)` | junta **lista** em string | `"-".join(["a","b"])` → `"a-b"` |
| `replace(a, b)` | troca todas as ocorrências | `"a-a".replace("a","o")` → `"o-o"` |
| `upper()` / `lower()` | caixa alta / baixa | `"oi".upper()` → `"OI"` |
| `title()` | iniciais maiúsculas | `"ola mundo".title()` → `"Ola Mundo"` |
| `capitalize()` | 1ª maiúscula, resto minúsculo | `"OLA".capitalize()` → `"Ola"` |
| `count(x)` | quantas vezes aparece | `"banana".count("a")` → `3` |
| `x in texto` | pertinência | `"an" in "banana"` → `True` |

```python
>>> "  oi   mundo  ".split()
['oi', 'mundo']
>>> " ".join(["oi", "mundo"])
'oi mundo'                 # ← o truque para juntar espaços duplos
```

> ⚠️ `split()` **sem argumento** quebra em qualquer montão de espaços (até vários seguidos). `split(" ")` quebra em **cada** espaço e deixa `""` para trás — quase nunca é o que você quer.

### Acentos e UTF-8

Python trata `"ç"` e `"á"` como **um** caractere só — `len("ação")` é `4`. Os testes deste tópico usam palavras com acento de propósito.

📖 [Métodos de string — docs.python.org/pt-br](https://docs.python.org/pt-br/3/library/stdtypes.html#string-methods) · [f-strings — docs.python.org/pt-br](https://docs.python.org/pt-br/3/reference/lexical_analysis.html#formatted-string-literals)

---

## ✍️ Exercícios

Abra [`atividade.py`](./atividade.py) — são 8 exercícios:

1. **`limpar(texto)`** → remove os espaços das pontas **e** junta espaços duplos/triplos num só. `"  oi   mundo  "` → `"oi mundo"`.
2. **`capitalizar(texto)`** → sem espaços nas pontas, **1ª letra maiúscula** e o resto minúsculo. `"  hELLO  "` → `"Hello"`.
3. **`juntar(palavras, separador)`** → une a lista numa string usando o separador. Lista vazia → `""`.
4. **`substituir(texto, antigo, novo)`** → troca **todas** as ocorrências.
5. **`contar(texto, trecho)`** → quantas vezes `trecho` aparece (substring, não só letra).
6. **`contem(texto, trecho)`** → `True`/`False` se `trecho` está dentro de `texto` (`in`).
7. **`reverter(texto)`** → a string de trás para frente usando **fatiamento**.
8. **`frase(nome, idade)`** → devolva **exatamente** `Olá, {nome}! Você tem {idade} anos.` com f-string.

```bash
python3 fase-2-estruturas-dados/04-strings/atividade.py
```

> 📌 Os testes incluem string vazia, espaço só nas pontas e palavras com **ç** e **á** — é assim que se confere que o código não quebra com acento.

---

## 💡 Dicas (progressivas — sem gabarito)

**Exercício 1 — `limpar`**
1. São duas operações: sobrar só o miolo, e depois juntar de novo. Qual método quebra a string em lista?
2. `texto.split()` (sem parênteses com argumento) já ignora todos os espaços seguidos; `" ".join(...)` é o que recompõe.
3. As duas etapas cabem na mesma expressão: primeiro transforme em lista de palavras e, em cima da lista, junte de volta com um espaço só — quem for juntar mora no separador.

**Exercício 2 — `capitalizar`**
1. Três transformações entram aqui: tirar as pontas, deixar tudo minúsculo e subir a 1ª letra. Qual método cobre cada uma?
2. `strip()`, `lower()` e `capitalize()` — o `capitalize()` sozinho já faz as duas últimas.
3. Só uma etapa fica de fora do método de capitalização: a das pontas. Acople-a na frente e deixe o resto por conta dele.

**Exercício 3 — `juntar`**
1. O método que cola lista em string fica **no separador**, não na lista.
2. `separador.join(palavras)` — repare na ordem dos lados.
3. É uma única chamada, com a lista vindo como argumento. Não precisa tratar a lista vazia: o método já devolve string vazia nesse caso.

**Exercício 4 — `substituir`**
1. Qual método troca um trecho por outro — e quantas ocorrências ele pega?
2. `texto.replace(antigo, novo)` substitui **todas** as aparições de uma vez.
3. Um único método de string resolve, e os três valores que ele precisa já estão na assinatura da função — repasse todos.

**Exercício 5 — `contar`**
1. Não é para localizar a posição, é para **contar** — qual método devolve esse `int`?
2. `texto.count(trecho)` conta inclusive substrings de mais de 1 caractere.
3. Devolva direto o número que esse método entrega; ele aceita tanto letra quanto trecho de vários caracteres e devolve `0` quando não há nada.

**Exercício 6 — `contem`**
1. O operador de pertinência de strings é o mesmo das listas e conjuntos.
2. `trecho in texto` já é a expressão completa (cuidado com a ordem: o **parte** vem antes do `in`).
3. Não há método a procurar — um `return` com o operador já entrega o `True`/`False` pedido.

**Exercício 7 — `reverter`**
1. Qual fatiamento percorre a string do fim para o começo?
2. `texto[::-1]` percorre a string do fim para o começo.
3. São três partes no fatiamento (início, fim, passo) e duas delas ficam vazias aqui; o passo é o único que precisa de atenção.

**Exercício 8 — `frase`**
1. Como você escreveria essa frase deixando `nome` e `idade` dentro de chaves?
2. A assinatura já entrega `nome` e `idade`; a `f` vai na frente das aspas.
3. Transcrição literal: a `f` abre a string, as chaves apontam para as variáveis e **vírgula, exclamação e ponto** fazem parte da resposta — erro de digitação aqui reprova no teste.

## 🚀 Desafios extras

- **Caso das palavras:** transforme `"ola MUNDO"` em `"Ola Mundo"` usando `title()` e compare com `capitalize()` — por que `title()` trata `"d'água"` de um jeito estranho?
- **Esconder dado:** escreva `mascarar(texto)` que devolve só os 2 últimos caracteres (ex.: `"1234567"` → `"67"`).
- **Split invertido:** conte as palavras de uma frase com `len(texto.split())` e compare com `len(texto.split(" "))`.

## ✅ Checkpoint

- [ ] Sei montar texto com f-string e interpolar variáveis/expressões
- [ ] Domino `strip`, `split`, `join`, `replace`, `upper`/`lower`/`capitalize`
- [ ] Sei que `count` conta substrings e `in` testa pertinência
- [ ] Sei que string é imutável e que fatiamento devolve **nova** string
- [ ] Tudo verde → marque o checkbox no [README raiz](../../README.md)
