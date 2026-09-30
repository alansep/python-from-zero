"""
Atividade 05 — Compreensão de listas
Fase 2 · python-from-zero

COMO USAR:
  1. Leia o enunciado.md deste tópico.
  2. Substitua os TODO pelas suas respostas.
  3. Rode no terminal:
        python3 fase-2-estruturas-dados/05-compreensao-listas/atividade.py
  4. Corrija até tudo ficar ✅ e marque o checkbox no README.
"""


# ============================================================
# EXERCÍCIO 1 — Dobros (comprehension simples)
# ------------------------------------------------------------
# Devolva uma lista com o dobro de cada item.
#   dobros([1, 2, 3]) -> [2, 4, 6]
#   dobros([])        -> []
# ============================================================
def dobros(lista):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 2 — Só os pares (comprehension com if)
# ------------------------------------------------------------
# Devolva uma lista apenas com os números pares, na mesma ordem.
#   pares([1, 2, 3, 4]) -> [2, 4]
#   pares([1, 3])       -> []
# ============================================================
def pares(lista):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 3 — Palavras em maiúsculas
# ------------------------------------------------------------
# Devolva uma lista com cada palavra transformada em MAIUSCULA.
#   maiusculas(["ola", "mundo"]) -> ["OLA", "MUNDO"]
# ============================================================
def maiusculas(palavras):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 4 — Classificar números (ternário if/else)
# ------------------------------------------------------------
# Devolva uma lista com "par" ou "ímpar" para cada número,
# usando o ternário DENTRO da comprehension.
#   classificar([1, 2, 3]) -> ["ímpar", "par", "ímpar"]
# ============================================================
def classificar(numeros):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 5 — Comprimento das palavras
# ------------------------------------------------------------
# Devolva uma lista com o tamanho de cada palavra.
#   comprimentos(["a", "olá"]) -> [1, 3]
# ============================================================
def comprimentos(palavras):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 6 — Achatar matriz (comprehension aninhada)
# ------------------------------------------------------------
# Devolva UMA lista só a partir de uma lista de listas.
#   achatada([[1, 2], [3]])   -> [1, 2, 3]
#   achatada([[1, 2], [3, 4]]) -> [1, 2, 3, 4]
# ============================================================
def achatada(matriz):
    # TODO: implemente
    return None


# ============================================================
# VALIDAÇÃO — não altere nada abaixo desta linha
# ============================================================
from checar import validar

validar(
    dobros=dobros,
    pares=pares,
    maiusculas=maiusculas,
    classificar=classificar,
    comprimentos=comprimentos,
    achatada=achatada,
)
