"""
Atividade 06 — Depuração sem IA
Fase 3 · python-from-zero

COMO USAR:
  1. Leia o enunciado.md deste tópico (tem o erro de verdade e as regras).
  2. Rode, leia a saída da validação e CORRIJA os bugs; responda as
     questões de stack trace nas variáveis resposta_1 ... resposta_8.
  3. Rode no terminal:
        python3 fase-3-modularizacao/06-depuracao/atividade.py
  4. Corrija até tudo ficar ✅ e marque o checkbox no README.

Os 4 primeiros exercícios já vêm COM BUG de propósito — o código
roda, mas o resultado está errado. Leia, rode, pense. Sem IA.
"""


# ============================================================
# EXERCÍCIO 1 — maior_de_tres (bug escondido)
# ------------------------------------------------------------
# Deve devolver o MAIOR dos três números.
#   maior_de_tres(1, 2, 3) -> 3   |   maior_de_tres(3, 2, 1) -> 3
# TODO: rode, compare com o esperado e encontre a linha culpada.
# ============================================================
def maior_de_tres(a, b, c):
    maior = a
    if b > maior:
        maior = b
    if c < maior:
        maior = c
    return maior


# ============================================================
# EXERCÍCIO 2 — soma_ate (bug escondido)
# ------------------------------------------------------------
# Deve devolver 1 + 2 + ... + n. Se n <= 0 -> 0.
# Proibido usar sum() — o laço é o exercício.
#   soma_ate(5) -> 15   |   soma_ate(1) -> 1   |   soma_ate(0) -> 0
# TODO: rode, compare com o esperado e encontre a linha culpada.
# ============================================================
def soma_ate(n):
    total = 0
    for i in range(1, n):
        total += i
    return total


# ============================================================
# EXERCÍCIO 3 — contar_pares (bug escondido)
# ------------------------------------------------------------
# Deve devolver quantos valores da lista são pares.
#   contar_pares([1, 2, 3, 4]) -> 2   |   contar_pares([2, 4, 6]) -> 3
# TODO: rode, compare com o esperado e pergunte-se:
# o laço está terminando antes da hora?
# ============================================================
def contar_pares(valores):
    total = 0
    for valor in valores:
        if valor % 2 == 0:
            total += 1
        return total
    return total


# ============================================================
# EXERCÍCIO 4 — total_do_carrinho (bug escondido)
# ------------------------------------------------------------
# Deve devolver a SOMA dos preços.
#   total_do_carrinho([10, 20, 30]) -> 60   |   total_do_carrinho([]) -> 0
# TODO: rode, compare com o esperado e olhe com carinho o que
# está acontecendo com a variável `total` dentro do laço.
# ============================================================
def total_do_carrinho(precos):
    total = 0
    for preco in precos:
        total = preco
    return total


# ============================================================
# EXERCÍCIO 5 — Stack trace 1 (NameError)
# ------------------------------------------------------------
# Veja o código e a saída de erro no enunciado.md (Parte B).
# resposta_1 = tipo da exceção, em minúsculas (ex.: "typeerror")
# resposta_2 = nome da variável que não existe
# ============================================================
resposta_1 = ""
resposta_2 = ""


# ============================================================
# EXERCÍCIO 6 — Stack trace 2 (TypeError)
# ------------------------------------------------------------
# resposta_3 = tipo da exceção, em minúsculas
# resposta_4 = nome da função chamada sem o argumento
# ============================================================
resposta_3 = ""
resposta_4 = ""


# ============================================================
# EXERCÍCIO 7 — Stack trace 3 (IndexError)
# ------------------------------------------------------------
# resposta_5 = tipo da exceção, em minúsculas
# resposta_6 = qual índice o código tentou usar (só o número)
# ============================================================
resposta_5 = ""
resposta_6 = ""


# ============================================================
# EXERCÍCIO 8 — Stack trace 4 (ValueError)
# ------------------------------------------------------------
# resposta_7 = tipo da exceção, em minúsculas
# resposta_8 = qual palavra a mensagem aponta como culpada
# ============================================================
resposta_7 = ""
resposta_8 = ""


# ============================================================
# VALIDAÇÃO — não altere nada abaixo desta linha
# ============================================================
from checar import validar

validar(
    maior_de_tres=maior_de_tres,
    soma_ate=soma_ate,
    contar_pares=contar_pares,
    total_do_carrinho=total_do_carrinho,
    resposta_1=resposta_1,
    resposta_2=resposta_2,
    resposta_3=resposta_3,
    resposta_4=resposta_4,
    resposta_5=resposta_5,
    resposta_6=resposta_6,
    resposta_7=resposta_7,
    resposta_8=resposta_8,
)
