"""
Atividade 03 — Dicionários
Fase 2 · python-from-zero

COMO USAR:
  1. Leia o enunciado.md deste tópico.
  2. Substitua os TODO pelas suas respostas.
  3. Rode no terminal:
        python3 fase-2-estruturas-dados/03-dicionarios/atividade.py
  4. Corrija até tudo ficar ✅ e marque o checkbox no README.
"""


# ============================================================
# EXERCÍCIO 1 — Busca com valor padrão
# ------------------------------------------------------------
# Devolva o valor da `chave`. Se ela nao existir, devolva `padrao`.
#   buscar({"a": 1}, "a", 0)       -> 1
#   buscar({"a": 1}, "z", "N/A")   -> "N/A"
# ============================================================
def buscar(dicionario, chave, padrao=None):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 2 — Contar ocorrências
# ------------------------------------------------------------
# Devolva um dicionário com quantas vezes cada item apareceu.
#   contar(["a", "b", "a"]) -> {"a": 2, "b": 1}
#   contar([])              -> {}
# ============================================================
def contar(lista):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 3 — Mesclar dois dicionários
# ------------------------------------------------------------
# Devolva um NOVO dicionário com os pares dos dois. Em chave
# repetida, o valor de d2 vence. NAO altere d1 nem d2.
#   mesclar({"a": 1}, {"a": 9, "b": 2}) -> {"a": 9, "b": 2}
# ============================================================
def mesclar(d1, d2):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 4 — Valor aninhado com proteção
# ------------------------------------------------------------
# Devolva perfil["endereco"]["cidade"]. Se faltar `endereco`
# ou `cidade`, devolva "" sem levantar nenhum erro.
#   cidade_de({"endereco": {"cidade": "SP"}}) -> "SP"
#   cidade_de({})                             -> ""
# ============================================================
def cidade_de(perfil):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 5 — Remover chave (e dizer se removeu)
# ------------------------------------------------------------
# Apague a chave NA PROPRIO dicionario de entrada e devolva True.
# Se a chave nao existir, devolva False e nao mexa em nada.
#   remover_chave({"a": 1, "b": 2}, "a") -> True  e dict {"b": 2}
#   remover_chave({"a": 1}, "z")         -> False e dict {"a": 1}
# ============================================================
def remover_chave(dicionario, chave):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 6 — Pares em lista
# ------------------------------------------------------------
# Devolva uma lista de tuplas (chave, valor) na ordem de inserção.
#   pares({"nome": "Ana", "idade": 30})
#       -> [("nome", "Ana"), ("idade", 30)]
# ============================================================
def pares(dicionario):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 7 — Somar valores
# ------------------------------------------------------------
# Some todos os valores numéricos do dicionário.
# Dicionário vazio -> 0.
#   somar_valores({"a": 1, "b": 2}) -> 3
# ============================================================
def somar_valores(dicionario):
    # TODO: implemente
    return None


# ============================================================
# VALIDAÇÃO — não altere nada abaixo desta linha
# ============================================================
from checar import validar

validar(
    buscar=buscar,
    contar=contar,
    mesclar=mesclar,
    cidade_de=cidade_de,
    remover_chave=remover_chave,
    pares=pares,
    somar_valores=somar_valores,
)
