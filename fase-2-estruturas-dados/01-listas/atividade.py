"""
Atividade 01 — Listas
Fase 2 · python-from-zero

COMO USAR:
  1. Leia o enunciado.md deste tópico.
  2. Substitua os TODO pelas suas respostas.
  3. Rode no terminal:
        python3 fase-2-estruturas-dados/01-listas/atividade.py
  4. Corrija até tudo ficar ✅ e marque o checkbox no README.
"""


# ============================================================
# EXERCÍCIO 1 — Extremos da lista
# ------------------------------------------------------------
# Devolva uma tupla (primeiro, ultimo).
# Lista vazia -> (None, None).
# ============================================================
def extremos(lista):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 2 — Os n últimos itens
# ------------------------------------------------------------
# Devolva uma sublista com os n ultimos itens de `lista`.
#   n <= 0           -> []
#   n >= len(lista)  -> a lista inteira
#   lista vazia      -> []
# Dica: fatiamento com inicio negativo.
# ============================================================
def ultimos(lista, n):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 3 — Trocar itens de posição
# ------------------------------------------------------------
# Troque os itens nas posicoes `i` e `j` NA PROPRIO objeto lista
# e devolva a MESMA lista (nao uma copia).
#   [1, 2, 3], 0, 2  ->  [3, 2, 1]
# ============================================================
def trocar(lista, i, j):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 4 — Adicionar item (append ou insert)
# ------------------------------------------------------------
#   indice is None  -> lista.append(valor)
#   indice informado -> lista.insert(indice, valor)
# Em ambos os casos devolva o NOVO TAMANHO da lista (len).
#   adicionar([1, 2], 9)        -> 3  e lista [1, 2, 9]
#   adicionar([1, 2], 9, 0)     -> 3  e lista [9, 1, 2]
# ============================================================
def adicionar(lista, valor, indice=None):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 5 — Ordenar in place
# ------------------------------------------------------------
# Ordene a PROPRIO lista com sort() e devolva None.
#   ordenar_em_origem([3, 1, 2]) -> lista [1, 2, 3] e retorno None
# ============================================================
def ordenar_em_origem(lista):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 6 — Reverter in place
# ------------------------------------------------------------
# Inverta a PROPRIO lista com reverse() e devolva None.
#   reverter_em_origem([1, 2, 3]) -> lista [3, 2, 1] e retorno None
# ============================================================
def reverter_em_origem(lista):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 7 — Remover por índice e devolver o item
# ------------------------------------------------------------
# Use pop(indice): ele ja deixa a lista menor e devolve o valor
# removido. Aceita indice negativo.
#   remover_indice([10, 20, 30], 1) -> 20  e lista [10, 30]
# ============================================================
def remover_indice(lista, indice):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 8 — Remover a 1ª ocorrência de um valor
# ------------------------------------------------------------
# Se `valor` estiver na lista: remove com remove(valor) e
# devolve True. Se nao estiver: devolve False e NAO mexe na lista.
#   remover_primeira([1, 2, 3, 2], 2) -> True  e lista [1, 3, 2]
#   remover_primeira([1, 2], 9)       -> False e lista [1, 2]
# ============================================================
def remover_primeira(lista, valor):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 9 — Soma e média (com proteção para lista vazia)
# ------------------------------------------------------------
# Devolva a tupla (soma, media).
# Lista vazia -> (None, None)   (nao pode dividir por zero)
#   resumo([2, 4, 6]) -> (12, 4.0)
# ============================================================
def resumo(lista):
    # TODO: implemente
    return None


# ============================================================
# VALIDAÇÃO — não altere nada abaixo desta linha
# ============================================================
from checar import validar

validar(
    extremos=extremos,
    ultimos=ultimos,
    trocar=trocar,
    adicionar=adicionar,
    ordenar_em_origem=ordenar_em_origem,
    reverter_em_origem=reverter_em_origem,
    remover_indice=remover_indice,
    remover_primeira=remover_primeira,
    resumo=resumo,
)
