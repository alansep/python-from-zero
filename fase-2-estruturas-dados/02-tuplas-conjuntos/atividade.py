"""
Atividade 02 — Tuplas e Conjuntos
Fase 2 · python-from-zero

COMO USAR:
  1. Leia o enunciado.md deste tópico.
  2. Substitua os TODO pelas suas respostas.
  3. Rode no terminal:
        python3 fase-2-estruturas-dados/02-tuplas-conjuntos/atividade.py
  4. Corrija até tudo ficar ✅ e marque o checkbox no README.
"""


# ============================================================
# EXERCÍCIO 1 — Coordenada como tupla
# ------------------------------------------------------------
# Devolva a tupla (x, y). Precisa ser tuple de verdade.
#   coordenadas(3, 4) -> (3, 4)
# ============================================================
def coordenadas(x, y):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 2 — Tamanho antes e depois da deduplicação
# ------------------------------------------------------------
# Devolva a tupla (tamanho da lista, tamanho sem duplicatas).
#   tamanho_antes_depois([3, 1, 3, 2, 1]) -> (5, 3)
# ============================================================
def tamanho_antes_depois(lista):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 3 — Remover duplicatas
# ------------------------------------------------------------
# Devolva UMA LISTA com cada item aparecendo uma unica vez.
# A ordem nao importa (o teste ordena antes de comparar).
#   sem_duplicatas([3, 1, 3, 2, 1]) -> [1, 2, 3]  (em qualquer ordem)
# ============================================================
def sem_duplicatas(lista):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 4 — União de conjuntos
# ------------------------------------------------------------
# Devolva um CONJUNTO (set) com tudo que existe em a OU em b.
#   uniao({1, 2}, {2, 3}) -> {1, 2, 3}
# ============================================================
def uniao(a, b):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 5 — Interseção de conjuntos
# ------------------------------------------------------------
# Devolva um CONJUNTO (set) só com os itens presentes nos DOIS.
#   interseccao({1, 2, 3}, {2, 3, 4}) -> {2, 3}
# ============================================================
def interseccao(a, b):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 6 — Diferença de conjuntos
# ------------------------------------------------------------
# Devolva um CONJUNTO (set) com o que existe em a e NAO existe em b.
#   diferenca({1, 2, 3}, {2, 3}) -> {1}
# ============================================================
def diferenca(a, b):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 7 — Pertinência
# ------------------------------------------------------------
# Devolva True se `item` esta dentro de `colecao`, False se nao.
# Funciona para lista, tupla, conjunto e string.
#   pertence(3, [1, 2, 3])     -> True
#   pertence("á", "lápis")     -> True
# ============================================================
def pertence(item, colecao):
    # TODO: implemente
    return None


# ============================================================
# VALIDAÇÃO — não altere nada abaixo desta linha
# ============================================================
from checar import validar

validar(
    coordenadas=coordenadas,
    tamanho_antes_depois=tamanho_antes_depois,
    sem_duplicatas=sem_duplicatas,
    uniao=uniao,
    interseccao=interseccao,
    diferenca=diferenca,
    pertence=pertence,
)
