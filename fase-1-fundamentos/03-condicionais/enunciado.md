# 03 — Estruturas Condicionais ⏱️ ~2.5h

**Meta:** fazer o programa **decidir** — executar um caminho ou outro conforme o dado.

---

## 📚 Teoria

### A estrutura básica

```python
if condição:          # termina com DOIS PONTOS
    # executa SE a condição for True
elif outra_condicao:  # "else if" — opcional, pode ter vários
    # executa se a anterior era False E esta é True
else:
    # executa quando NENHUMA anterior deu True
```

- O bloco é definido pela **indentação** (4 espaços) — é como o Python sabe o que pertence a quem.
- A condição é qualquer expressão que resulte em `True`/`False` (o terceiro capítulo do roadmap 😉).

### Como o Python percorre

Ele testa **de cima para baixo e para no primeiro `True`**:

```python
idade = 20
if idade < 18:
    print("menor")
elif idade < 65:
    print("adulto")   # ← cai aqui (20 < 65)
else:
    print("idoso")    # nunca é testado depois
```

> ⚠️ **A ordem importa.** Casos especiais (negativos, limites) vão **primeiro**. Se `idade < 18` vier antes de `idade < 0`, um `-5` seria "menor" e nunca "inválido".

### Múltiplas validações

Duas formas de combinar:

```python
# 1) condições compostas com and/or (mesma linha)
if idade >= 18 and tem_cnh:
    ...

# 2) validações aninhadas (uma dentro da outra)
if idade >= 18:
    if tem_cnh:
        ...
```

### Repertório de erros

| Situação | Erro típico |
|---|---|
| Esqueceu os `:` | `SyntaxError` |
| Errou a indentação | `IndentationError` |
| Condição invertida | lógica errada (o código roda, mas decide errado) |

---

## ✍️ Exercícios

Abra [`atividade.py`](./atividade.py) — são 4 exercícios:

1. **`faixa_etaria(idade)`** → `"inválida"`, `"criança"`, `"adolescente"`, `"adulto"` ou `"idoso"`.
   Atenção aos limites: `-1` é inválida, `12` ainda é criança, `65` já é idoso.
2. **`pode_dirigir(idade, tem_cnh)`** → `True` só com **18+ E CNH**.
3. **`situacao(nota)`** → `"SS"` (≥90), `"A"` (≥80), `"B"` (≥70), `"C"` (≥60), `"D"` (o resto).
4. **`calcular(a, operador, b)`** → mini-calculadora. **Respeite a ordem das validações:**
   1. operador inválido → `"operador inválido"`
   2. `"/"` com `b == 0` → `"divisão por zero"`
   3. senão, calcula.

```bash
python3 fase-1-fundamentos/03-condicionais/atividade.py
```

> 📌 A validação testa **casos-limite** (12/13, 17/18, 64/65, 90/89...). É assim que se testa código de verdade.

## 🚀 Desafios extras

- **Par ou ímpar:** peça um número e classifique com `if numero % 2 == 0`.
- **Ano bissexto:** divisível por 4 **e** (não por 100 **ou** por 400).
- **Média com conceito + frequência:** só aprova quem tem média ≥ 60 **E** frequência ≥ 75%.

## ✅ Checkpoint

- [ ] Sei a estrutura `if / elif / else` com indentação e `:`
- [ ] Sei que o Python para no primeiro `True`
- [ ] Entendi por que **a ordem das validações** importa
- [ ] Tudo verde → marque o checkbox no [README raiz](../../README.md)
