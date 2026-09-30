"""
Atividade 05 — Tratamento de Exceções
Fase 3 · python-from-zero

COMO USAR:
  1. Leia o enunciado.md deste tópico.
  2. Substitua os TODO pelas suas respostas.
  3. Rode no terminal:
        python3 fase-3-modularizacao/05-excecoes/atividade.py
  4. Corrija até tudo ficar ✅ e marque o checkbox no README.
"""


# ============================================================
# EXERCÍCIO 1 — Converter texto em número (try/except)
# ------------------------------------------------------------
# Devolva int(texto) quando a conversão der certo.
# Quando levantar ValueError -> devolva "valor inválido".
#   converter("42")   -> 42
#   converter("abc")  -> "valor inválido"
# ============================================================
def converter(texto):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 2 — Dividir sem explodir
# ------------------------------------------------------------
# Devolva a divisão a / b.
# Quando b for 0 -> devolva "divisão por zero" (não deixe estourar).
# ============================================================
def dividir(a, b):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 3 — finally que SEMPRE executa
# ------------------------------------------------------------
# Para cada item de `valores`, tente int(item) dentro de um try;
# capture (ValueError, TypeError) e siga em frente.
# No BLOCO finally, incremente um contador LOCAL.
# Devolva esse contador (ou seja, igual a len(valores), mesmo
# com itens inválidos no meio da lista).
# ============================================================
def processar(valores):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 4 — Levantar seu próprio erro (raise)
# ------------------------------------------------------------
# Se valor for int entre 0 e 130 -> devolva ele mesmo.
# Qualquer outra coisa -> raise ValueError("idade inválida")
#   validar_idade(20)   -> 20
#   validar_idade(-1)   -> levanta ValueError
# ============================================================
def validar_idade(valor):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 5 — try / except / else
# ------------------------------------------------------------
# No try: apenas converta (numero = int(texto)).
# No except ValueError: devolva "valor inválido".
# No else (só quando a conversão deu certo): devolva
# "par" ou "ímpar" conforme numero % 2.
# ============================================================
def classificar(texto):
    # TODO: implemente
    return ""


# ============================================================
# VALIDAÇÃO — não altere nada abaixo desta linha
# ============================================================
from checar import validar

validar(
    converter=converter,
    dividir=dividir,
    processar=processar,
    validar_idade=validar_idade,
    classificar=classificar,
)
