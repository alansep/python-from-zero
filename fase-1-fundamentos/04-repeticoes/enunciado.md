# 04 — Estruturas de Repetição (Loops) ⏱️ ~3h

**Meta:** fazer o computador repetir tarefas sem copiar e colar código.

---

## 📚 Teoria

### `for` — repetição com contagem definida

Usa quando você **sabe quantas vezes** vai repetir (ou tem uma sequência):

```python
for numero in range(1, 6):
    print(numero)      # imprime 1, 2, 3, 4, 5
```

`range(inicio, fim)` vai de `inicio` até **`fim - 1`** — o fim é **exclusivo**!

| Chamada | Gera |
|---|---|
| `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(5)` | 0, 1, 2, 3, 4 (começa em 0) |
| `range(0, 11, 2)` | 0, 2, 4, 6, 8, 10 (passo 2) |

> ⚠️ **Bug clássico:** queria de 1 a 10 e escreveu `range(1, 10)` → para no 9. Use `range(1, 11)`.

### `while` — repetição por condição

Usa quando você **não sabe** quantas vezes (ex.: esperar o usuário acertar):

```python
contador = 1
while contador <= 5:      # repete ENQUANTO for True
    print(contador)
    contador += 1         # ESSENCIAL: senão, repete para sempre!
```

- Sem atualizar a condição → **loop infinito**. Saia com `Ctrl + C` no terminal.
- `contador += 1` significa `contador = contador + 1`.

### `break` e `continue` — controlando o fluxo

```python
for n in range(1, 101):
    if n % 7 == 0:
        break            # ENCERRA o laço inteiro agora
    if n % 2 != 0:
        continue         # PULA para a próxima volta (não executa o resto)
    print(n)
```

| Palavra | Efeito |
|---|---|
| `break` | **aborta** o laço por completo |
| `continue` | **ignora esta volta** e vai para a próxima |

### Qual usar?

| Situação | Escolha |
|---|---|
| "repita 10 vezes" / percorrer algo | `for` + `range` |
| "repita **enquanto**..." / quantidade desconhecida | `while` |

---

## ✍️ Exercícios

Abra [`atividade.py`](./atividade.py) — são 5 exercícios:

1. **`soma_ate(n)`** — some `1 + 2 + ... + n` com **`while`** (`n <= 0` → `0`).
2. **`contar_divisiveis(inicio, fim, divisor)`** — quantos números do intervalo `[inicio, fim]` são divisíveis pelo divisor? Use **`for` + `range` + `%`**. Divisor `0` → retorne `0`.
3. **`soma_pares_ate(n)`** — some os pares de 1 a n usando **`continue`** para pular os ímpares.
4. **`contar_antes_do_sete(limite)`** — conte de 1 em diante e pare com **`break`** ao achar o primeiro múltiplo de 7. Retorne **quantos números foram percorridos antes de parar**.
5. **Previsão de saída** — leia um trecho de código **no papel** e devolva a saída exata (dry-run).

```bash
python3 fase-1-fundamentos/04-repeticoes/atividade.py
```

---

## 💡 Dicas (progressivas — sem gabarito)

**Exercício 1**
1. Você precisa de um acumulador e de um contador — o `while` compara qual dos dois?
2. Comece com `atual = 1`; dentro do laço: some e depois avance (`atual += 1`).
3. Se `n <= 0` o laço nem deve começar — deixe o total zerado.

**Exercício 2**
1. `range` tem fim EXCLUSIVO: como incluir o próprio `fim`?
2. Dentro do `for`, um `if numero % divisor == 0` decide se o número conta.
3. Trate `divisor == 0` antes de entrar no laço.

**Exercício 3**
1. Percorra de 1 a n; antes de somar, desvie os ímpares.
2. `if numero % 2 != 0:` + `continue` pula aquela volta inteira.
3. Só os pares chegam na linha do `total += numero`.

**Exercício 4**
1. O contador só deve avançar quando o número NÃO encerrou o laço.
2. Teste o `break` ANTES de incrementar.
3. Ex.: limite 30 → para no 7, então foram percorridos 1..6.

**Previsão de saída**
1. `range(1, 5)` gera quais números?
2. Quais deles são pares — e o que o `continue` faz com eles?
3. Some manualmente os ímpares: 1 + 3 = ?

## 🚀 Desafios extras

- **Fatorial** com `for`: `5! = 5*4*3*2*1 = 120`.
- **Tabuada** de um número: imprima as 10 linhas com `for`.
- **Jogo da adivinhação:** número secreto, `while` perguntando até o usuário acertar (use `break` ao acertar).

## ✅ Checkpoint

- [ ] Sei a diferença entre `for` e `while` e quando usar cada um
- [ ] Entendi que `range(fim)` é **exclusivo**
- [ ] Sei o que `break` e `continue` fazem
- [ ] Sei como um loop infinito nasce (e como sair dele com `Ctrl + C`)
- [ ] Tudo verde → marque o checkbox no [README raiz](../../README.md)
