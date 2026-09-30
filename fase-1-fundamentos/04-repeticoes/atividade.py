"""
Atividade 04 — Estruturas de Repetição
Fase 1 · python-from-zero

COMO USAR:
  1. Leia o enunciado.md deste tópico.
  2. Substitua os TODO pelas suas respostas.
  3. Rode no terminal:
        python3 fase-1-fundamentos/04-repeticoes/atividade.py
  4. Corrija até tudo ficar ✅ e marque o checkbox no README.
"""


# ============================================================
# EXERCÍCIO 1 — Some com WHILE
# ------------------------------------------------------------
# Some 1 + 2 + ... + n usando a estrutura while.
# Se n <= 0, retorne 0.
# Ex: soma_ate(5) -> 15
# ============================================================
def soma_ate(n):
    # TODO: implemente com while
    return None


# ============================================================
# EXERCÍCIO 2 — Conte com FOR + RANGE
# ------------------------------------------------------------
# Quantos números INTEIROS no intervalo [inicio, fim] (inclusive)
# são divisíveis por divisor?
#   contar_divisiveis(1, 20, 3) -> 6   (3, 6, 9, 12, 15, 18)
# Divisível = resto da divisão == 0.
# Se divisor for 0, retorne 0 (evite o erro!).
# ============================================================
def contar_divisiveis(inicio, fim, divisor):
    # TODO: implemente com for + range + %
    return None


# ============================================================
# EXERCÍCIO 3 — Some os pares com CONTINUE
# ------------------------------------------------------------
# Some os números PARES de 1 até n.
# Use for e a palavra continue para PULAR os ímpares.
# Ex: soma_pares_ate(5) -> 2 + 4 = 6
# ============================================================
def soma_pares_ate(n):
    # TODO: implemente com for + continue
    return None


# ============================================================
# EXERCÍCIO 4 — Pare com BREAK
# ------------------------------------------------------------
# Percorra 1, 2, 3, ... (até o limite) e USE break quando achar
# o primeiro número divisível por 7.
# Retorne quantos números foram percorridos ANTES de parar.
# Ex: contar_antes_do_sete(30) -> 6   (1,2,3,4,5,6 -> parou no 7)
# ============================================================
def contar_antes_do_sete(limite):
    # TODO: implemente com for + break
    return None


# ============================================================
# VALIDAÇÃO — não altere nada abaixo desta linha
# ============================================================
from checar import validar

validar(
    soma_ate=soma_ate,
    contar_divisiveis=contar_divisiveis,
    soma_pares_ate=soma_pares_ate,
    contar_antes_do_sete=contar_antes_do_sete,
)
