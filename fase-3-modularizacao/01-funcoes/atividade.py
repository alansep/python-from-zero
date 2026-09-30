"""
Atividade 01 — Funções e Escopo
Fase 3 · python-from-zero

COMO USAR:
  1. Leia o enunciado.md deste tópico.
  2. Substitua os TODO pelas suas respostas.
  3. Rode no terminal:
        python3 fase-3-modularizacao/01-funcoes/atividade.py
  4. Corrija até tudo ficar ✅ e marque o checkbox no README.
"""


# Variável de MÓDULO (escopo global) — a validação confere que ela
# continua valendo 0 depois de todas as chamadas. Não mexa nela!
contador = 0


# ============================================================
# EXERCÍCIO 1 — Saudação com valor padrão
# ------------------------------------------------------------
# Devolva EXATAMENTE: f"{cumprimento}, {nome}!"
# Deve funcionar nos 3 formatos de chamada:
#   saudacao("Ana")                       -> "Olá, Ana!"
#   saudacao("Ana", "Bom dia")            -> "Bom dia, Ana!"
#   saudacao("Ana", cumprimento="Oi")     -> "Oi, Ana!"
# ============================================================
def saudacao(nome, cumprimento="Olá"):
    # TODO: implemente
    return ""


# ============================================================
# EXERCÍCIO 2 — Menor e maior
# ------------------------------------------------------------
# Devolva UMA tupla (menor, maior).
# Lista vazia -> None (não deixe estourar o min()/max()).
# ============================================================
def min_max(valores):
    # TODO: implemente
    return ""


# ============================================================
# EXERCÍCIO 3 — Dobrar sem efeito colateral (função pura)
# ------------------------------------------------------------
# Devolva uma NOVA lista com cada valor multiplicado por 2.
# A lista RECEBIDA não pode ser modificada em hipótese alguma.
# ============================================================
def dobrar(valores):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 4 — Contar pares (com docstring OBRIGATÓRIA)
# ------------------------------------------------------------
# Devolva quantos valores da lista são pares (0 conta como par).
# A função PRECISA ter uma docstring de pelo menos 5 caracteres:
#   def contar_pares(valores):
#       """texto aqui"""          <- a validação verifica
#       ...
# ============================================================
def contar_pares(valores):
    # TODO: implemente (e escreva a docstring!)
    return None


# ============================================================
# EXERCÍCIO 5 — Soma usando escopo LOCAL
# ------------------------------------------------------------
# Some os valores com uma variável LOCAL (criada dentro da função)
# e devolva a soma. É PROIBIDO alterar a variável de módulo
# `contador` — ela deve continuar valendo 0.
# ============================================================
def acumular(valores):
    # TODO: implemente sem usar `global`
    return None


# ============================================================
# VALIDAÇÃO — não altere nada abaixo desta linha
# ============================================================
from checar import validar

validar(
    saudacao=saudacao,
    min_max=min_max,
    dobrar=dobrar,
    contar_pares=contar_pares,
    acumular=acumular,
)
