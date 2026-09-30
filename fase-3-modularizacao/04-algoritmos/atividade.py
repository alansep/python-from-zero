"""
Atividade 04 — Algoritmos Clássicos
Fase 3 · python-from-zero

COMO USAR:
  1. Leia o enunciado.md deste tópico.
  2. Substitua os TODO pelas suas respostas.
  3. Rode no terminal:
        python3 fase-3-modularizacao/04-algoritmos/atividade.py
  4. Corrija até tudo ficar ✅ e marque o checkbox no README.

AVISO: usar sorted() ou .sort() no exercício 3 é trapacear —
o objetivo é você escrever a mecânica das trocas.
"""


# ============================================================
# EXERCÍCIO 1 — Busca linear
# ------------------------------------------------------------
# Devolva o índice da PRIMEIRA ocorrência de `alvo` em `lista`.
# Se não existir (ou a lista for vazia) -> -1.
# ============================================================
def buscar(lista, alvo):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 2 — Busca de todas as ocorrências
# ------------------------------------------------------------
# Devolva UMA LISTA com todos os índices onde `alvo` aparece,
# em ordem crescente. Nenhuma ocorrência -> [].
#   buscar_todos([1, 2, 1], 1) -> [0, 2]
# ============================================================
def buscar_todos(lista, alvo):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 3 — Bubble Sort à mão
# ------------------------------------------------------------
# Ordene em ordem CRESCENTE comparando vizinhos e trocando-os.
# PROIBIDO: sorted(lista) e lista.sort().
# Pode ordenar a MESMA lista e devolvê-la, ou devolver uma nova.
# ============================================================
def bubble_sort(lista):
    # TODO: implemente
    return None


# ============================================================
# VALIDAÇÃO — não altere nada abaixo desta linha
# ============================================================
from checar import validar

validar(
    buscar=buscar,
    buscar_todos=buscar_todos,
    bubble_sort=bubble_sort,
)
