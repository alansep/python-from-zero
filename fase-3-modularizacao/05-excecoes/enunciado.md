# 05 — Tratamento de Exceções ⏱️ ~2h

**Meta:** falhar com elegância — em vez de o programa explodir, **detectar o problema, avisar e seguir em frente**.

---

## 📚 Teoria

### A estrutura completa

```python
try:
    numero = int(texto)          # código que PODE dar errado
except ValueError:
    return "valor inválido"      # só captura ESSE tipo de erro
else:
    return numero                # executa só se NADA deu errado no try
finally:
    print("sempre executa")      # executa SEMPRE: erro ou não
```

| Bloco | Quando roda |
|---|---|
| `try` | sempre (é o "risco") |
| `except Tipo` | só quando `try` levanta **aquele** tipo |
| `else` | só quando `try` terminou **sem** erro |
| `finally` | **sempre** — com erro, sem erro, mesmo com `return` no meio |

> 🔑 A pergunta de ouro: *"se este bloco falhar, o que meu programa deveria fazer em vez de morrer?"* — se a resposta for "avisar e continuar", é `try/except`.

### O que capturar?

Capture o **mais específico possível** — nunca `except:` puro (esconde bugs reais):

| Erro | Exemplo de origem | Capture quando |
|---|---|---|
| `ValueError` | `int("abc")`, `float("x")` | o formato está errado |
| `TypeError` | `int(None)`, `"a" + 1` | o TIPO está errado |
| `ZeroDivisionError` | `10 / 0` | divisor pode ser 0 |
| `IndexError` | `lista[99]` | índice pode estourar |
| `KeyError` | `d["falta"]` | chave pode faltar |
| `FileNotFoundError` | `open("sumiu.txt")` | arquivo pode não existir |

Toda a lista: [exceções embutidas](https://docs.python.org/pt-br/3/library/exceptions.html).

### Tratar ≠ engolir

```python
def converter(texto):
    try:
        return int(texto)
    except ValueError:
        return "valor inválido"   # devolve uma RESPOSTA — não passa adiante
```

- **Tratar:** o erro vira um resultado previsível (`return "..."`).
- **Engolir (ruim):** `except: pass` — o erro some e ninguém fica sabente.
- **Deixar estourar (às vezes certo):** se quem CHAMOU sabe lidar, não trate aqui.

### `raise` — levantando suas próprias exceções

```python
def validar_idade(valor):
    if not 0 <= valor <= 130:
        raise ValueError("idade inválida")   # interrompe com uma MENSAGEM clara
    return valor
```

- `raise` encerra o fluxo **no ponto exato** e entrega tipo + mensagem a quem chamou.
- Use para **entradas inválidas** logo na entrada de uma função: falha cedo e perto da causa.
- Quem chama captura com `try/except` (ou deixa estourar). Docs: [Handling Exceptions](https://docs.python.org/pt-br/3/tutorial/errors.html).

### A anatomia de um erro não tratado

```
Traceback (most recent call last):
  File "atividade.py", line 12, in <module>
    print(idades[3])
          ~~~^^^^^^^
IndexError: list index out of range
```

- **Última linha** = tipo do erro + mensagem (é o que você captura no `except`).
- O **caminho das chamadas** mostra como você chegou ali.
- Isso é assunto do tópico 06 — mas já vale reparar que o Python **sempre** diz o que e onde.

---

## ✍️ Exercícios

Abra [`atividade.py`](./atividade.py) — são 5 exercícios:

1. **`converter(texto)`** → `int(texto)` quando der; senão `"valor inválido"`.
   Deve tratar `ValueError` (ex.: `"abc"`, `""`, `"3.5"`).
2. **`dividir(a, b)`** → quociente; `b == 0` → `"divisão por zero"` (sem estourar!).
3. **`processar(valores)`** → para cada item tente `int(item)` (capture `ValueError`/`TypeError`),
   e conte em **`finally`** quantos itens passaram pelo bloco — devolva esse contador
   (ou seja, o contador deve ser igual ao tamanho da lista, mesmo com itens ruins no meio).
4. **`validar_idade(valor)`** → devolve a idade se for `int` entre 0 e 130;
   senão **`raise ValueError("idade inválida")`**.
5. **`classificar(texto)`** → converta com `try`; em **`except`** devolva `"valor inválido"`;
   em **`else`** (só se a conversão deu certo) devolva `"par"` ou `"ímpar"`.

```bash
python3 fase-3-modularizacao/05-excecoes/atividade.py
```

> 📌 A validação verifica inclusive a **mensagem** do `raise` e se o `finally` contou todo mundo. É assim que se testa código de verdade.

---

## 💡 Dicas (progressivas — sem gabarito)

**Exercício 1**
1. Qual função levanta `ValueError` quando recebe `"abc"`?
2. `int()` também rejeita `""` e `"3.5"` — todos caem no MESMO tipo de erro.
3. Envolva `return int(texto)` com `try`; no `except ValueError:` devolva a mensagem. Não trate tipos diferentes — `int()` aqui só reclama de valor.

**Exercício 2**
1. Dividir por zero levanta qual erro (não é `ValueError`)?
2. Dá para fazer a divisão ANTES de capturar? O `except` captura o que estourou no `try`.
3. `try: return a / b` + `except ZeroDivisionError: return "divisão por zero"`. A validação aceita `10/2` como `5` ou `5.0`.

**Exercício 3**
1. O contador é local e precisa sobreviver à iteração — onde ele nasce?
2. `finally` roda em TODA iteração, mesmo quando o `except` engoliu o erro.
3. Crie `contador = 0` antes do laço; dentro, monte `try: int(item)` / `except (ValueError, TypeError): pass` / `finally: contador += 1`; devolva o contador depois do laço. Itens ruins não podem deixar de ser contados.

**Exercício 4**
1. `raise` precisa de quê depois dele (tipo e mensagem)?
2. Duas condições impedem a idade de ser válida: não ser `int` e estar fora da faixa.
3. Valide primeiro (`if not isinstance(valor, int) or not 0 <= valor <= 130:`) e levante `ValueError("idade inválida")` nesse ramo; senão, devolva o valor.

**Exercício 5**
1. O que distingue o bloco que roda **só quando não houve erro** do que roda quando houve?
2. São dois ramos opostos: `except` (falhou) e `else` (deu certo).
3. No `try`, só a conversão (`numero = int(texto)`), sem `return`; no `except ValueError:` a mensagem de erro; no `else:` a decisão par/ímpar usando `numero % 2`.

## 🚀 Desafios extras

- **Duas mensagens:** faça `converter` devolver `"só número"` para `TypeError` e `"valor inválido"` para `ValueError` — dois `except` no mesmo `try`.
- **Registrador de erros:** em `processar`, acumule os itens que falharam numa lista e devolva `(contador, ruins)`.
- **`try` como expressão:** pesquise `try/except` em uma linha (`int(x) if ... `) e compare legibilidade com o bloco completo.

## ✅ Checkpoint

- [ ] Sei a ordem dos blocos `try / except / else / finally` e quando cada um roda
- [ ] Sei que `finally` executa **sempre** — inclusive com `return` no caminho
- [ ] Capturo o tipo de erro mais específico (nunca `except:` puro)
- [ ] Sei levantar meu próprio erro com `raise ValueError("mensagem")`
- [ ] Tudo verde → marque o checkbox no [README raiz](../../README.md)
