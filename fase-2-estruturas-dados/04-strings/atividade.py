"""
Atividade 04 — Strings
Fase 2 · python-from-zero

COMO USAR:
  1. Leia o enunciado.md deste tópico.
  2. Substitua os TODO pelas suas respostas.
  3. Rode no terminal:
        python3 fase-2-estruturas-dados/04-strings/atividade.py
  4. Corrija até tudo ficar ✅ e marque o checkbox no README.
"""


# ============================================================
# EXERCÍCIO 1 — Normalizar espaços
# ------------------------------------------------------------
# Remova os espacos das pontas e junte espacos duplos/triplos
# em um unico espaco.
#   limpar("  oi   mundo  ") -> "oi mundo"
#   limpar("   ")            -> ""
# ============================================================
def limpar(texto):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 2 — Primeira letra maiúscula
# ------------------------------------------------------------
# Sem espacos nas pontas, 1ª letra em MAIUSCULA e o resto em
# minuscula.
#   capitalizar("  hELLO  ") -> "Hello"
# ============================================================
def capitalizar(texto):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 3 — Juntar lista com separador
# ------------------------------------------------------------
# Une a lista numa unica string usando `separador`.
# Lista vazia -> "".
#   juntar(["a", "b", "c"], "-") -> "a-b-c"
# ============================================================
def juntar(palavras, separador):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 4 — Substituir trechos
# ------------------------------------------------------------
# Troque TODAS as ocorrencias de `antigo` por `novo`.
#   substituir("a-b-c", "-", "+") -> "a+b+c"
# ============================================================
def substituir(texto, antigo, novo):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 5 — Contar ocorrências de um trecho
# ------------------------------------------------------------
# Conte quantas vezes `trecho` aparece em `texto` (pode ter
# mais de 1 caractere).
#   contar("banana", "a")   -> 3
#   contar("banana", "z")   -> 0
# ============================================================
def contar(texto, trecho):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 6 — Trecho está dentro da string?
# ------------------------------------------------------------
# Devolva True/False se `trecho` aparece em `texto`.
#   contem("casa", "as") -> True
#   contem("Olá", "olá") -> False   (sensível a maiúsculas)
# ============================================================
def contem(texto, trecho):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 7 — Inverter a string
# ------------------------------------------------------------
# Devolva a string de trás para frente usando fatiamento.
#   reverter("abc") -> "cba"
# ============================================================
def reverter(texto):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 8 — Frase com f-string
# ------------------------------------------------------------
# Devolva EXATAMENTE (respeite vírgula, exclamação e ponto):
#   Olá, {nome}! Você tem {idade} anos.
#   frase("Ana", 30) -> "Olá, Ana! Você tem 30 anos."
# ============================================================
def frase(nome, idade):
    # TODO: implemente
    return None


# ============================================================
# VALIDAÇÃO — não altere nada abaixo desta linha
# ============================================================
from checar import validar

validar(
    limpar=limpar,
    capitalizar=capitalizar,
    juntar=juntar,
    substituir=substituir,
    contar=contar,
    contem=contem,
    reverter=reverter,
    frase=frase,
)
