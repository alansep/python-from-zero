"""
Atividade 03 — Estruturas Condicionais
Fase 1 · python-from-zero

COMO USAR:
  1. Leia o enunciado.md deste tópico.
  2. Substitua os TODO pelas suas respostas.
  3. Rode no terminal:
        python3 fase-1-fundamentos/03-condicionais/atividade.py
  4. Corrija até tudo ficar ✅ e marque o checkbox no README.
"""


# ============================================================
# EXERCÍCIO 1 — Faixa etária
# ------------------------------------------------------------
# Retorne EXATAMENTE um destes textos:
#   idade < 0            -> "inválida"
#   idade <= 12          -> "criança"
#   idade <= 17          -> "adolescente"
#   idade <= 64          -> "adulto"
#   idade >= 65          -> "idoso"
# Use if / elif / else. Lembre: o caso especial vai PRIMEIRO.
# ============================================================
def faixa_etaria(idade):
    # TODO: implemente
    return ""


# ============================================================
# EXERCÍCIO 2 — Pode dirigir?
# ------------------------------------------------------------
# Retorne True APENAS se tiver 18 anos ou mais E tem_cnh for True.
# ============================================================
def pode_dirigir(idade, tem_cnh):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 3 — Situação no boletim
# ------------------------------------------------------------
# Retorne EXATAMENTE:
#   nota >= 90 -> "SS"
#   nota >= 80 -> "A"
#   nota >= 70 -> "B"
#   nota >= 60 -> "C"
#   senão       -> "D"
# ============================================================
def situacao(nota):
    # TODO: implemente
    return ""


# ============================================================
# EXERCÍCIO 4 — Calculadora (múltiplas validações)
# ------------------------------------------------------------
# Execute a operação pedida e RETORNE o resultado numérico.
# A ORDEM das validações importa:
#   1. operador fora de ("+", "-", "*", "/")  -> "operador inválido"
#   2. operador "/" com b == 0                -> "divisão por zero"
#   3. senão                                  -> calcula normalmente
# ============================================================
def calcular(a, operador, b):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 5 — Previsão de saída (sem rodar!)
# ------------------------------------------------------------
# Leia o código abaixo NO PAPEL e devolva EXATAMENTE o que ele
# imprime, usando \n para as quebras de linha:
#
#   x = 3
#   if x > 5:
#       print("A")
#   elif x > 2:
#       print("B")
#   else:
#       print("C")
# ============================================================
def previsao_saida():
    # TODO: escreva a saída esperada como texto
    return ""


# ============================================================
# VALIDAÇÃO — não altere nada abaixo desta linha
# ============================================================
from checar import validar

validar(
    faixa_etaria=faixa_etaria,
    pode_dirigir=pode_dirigir,
    situacao=situacao,
    calcular=calcular,
    previsao_saida=previsao_saida,
)
