"""
Atividade 02 — Operadores Matemáticos e Lógicos
Fase 1 · python-from-zero

COMO USAR:
  1. Leia o enunciado.md deste tópico.
  2. Substitua os TODO pelas suas respostas.
  3. Rode no terminal:
        python3 fase-1-fundamentos/02-operadores/atividade.py
  4. Corrija até tudo ficar ✅ e marque o checkbox no README.
"""

# ============================================================
# EXERCÍCIO 1 — Aritmética
# ------------------------------------------------------------
# Complete cada variável usando A e B (não digite o resultado na mão!).
#   a = 17, b = 5
# ============================================================
a = 17
b = 5

soma = None              # TODO: a + b
divisao = None           # TODO: a / b   (divisão real → decimal)
divisao_inteira = None   # TODO: a // b  (descarta a parte decimal)
resto = None             # TODO: a % b   (o que sobra da divisão)
potencia = None          # TODO: a ** b  (a elevado a b)


# ============================================================
# EXERCÍCIO 2 — Comparações e lógicos
# ------------------------------------------------------------
# x = 10, y = 4 — complete cada variável:
# ============================================================
x = 10
y = 4

maior = None        # TODO: x > y ?
igual = None        # TODO: x == y ?
diferente = None    # TODO: x != y ?
e_logico = None     # TODO: x > 5 and y > 5   (ambos são > 5?)
ou_logico = None    # TODO: x > 5 or  y > 5   (pelo menos um é > 5?)
nao_logico = None   # TODO: not (x == y)


# ============================================================
# EXERCÍCIO 3 — Precedência (calcule NO PAPEL antes de rodar!)
# ------------------------------------------------------------
# Monte UMA expressão, SEM usar parênteses, que signifique:
#   "2 mais 3 vezes 4 ao quadrado menos 1"
# Lembre: ** e * vêm ANTES de + e -.
# Esperado: 49
# ============================================================
expressao = None    # TODO: monte a expressão


# ============================================================
# EXERCÍCIO 4 — Lógica combinada
# ============================================================
numero = 45

# TODO: True se numero for divisível por 3 E por 5 ao mesmo tempo
# Dica: divisível quer dizer "resto == 0"
divisivel_3_e_5 = None


# ============================================================
# EXERCÍCIO 5 — Previsão de saída (sem rodar!)
# ------------------------------------------------------------
# Leia o código abaixo NO PAPEL e devolva EXATAMENTE o que ele
# imprime, usando \n para as quebras de linha:
#
#   a = 7
#   b = 2
#   print(a + b * 2)
#   print(a // b)
#   print(a % b)
# ============================================================
def previsao_saida():
    # TODO: escreva a saída esperada como texto
    return ""


# ============================================================
# VALIDAÇÃO — não altere nada abaixo desta linha
# ============================================================
from checar import validar

validar(
    a=a,
    b=b,
    soma=soma,
    divisao=divisao,
    divisao_inteira=divisao_inteira,
    resto=resto,
    potencia=potencia,
    maior=maior,
    igual=igual,
    diferente=diferente,
    e_logico=e_logico,
    ou_logico=ou_logico,
    nao_logico=nao_logico,
    expressao=expressao,
    divisivel_3_e_5=divisivel_3_e_5,
    previsao_saida=previsao_saida,
)
