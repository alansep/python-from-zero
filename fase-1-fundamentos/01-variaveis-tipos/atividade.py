"""
Atividade 01 — Variáveis e Tipos de Dados
Fase 1 · python-from-zero

COMO USAR:
  1. Leia o enunciado.md deste tópico.
  2. Substitua os TODO pelas suas respostas.
  3. Rode no terminal:
        python3 fase-1-fundamentos/01-variaveis-tipos/atividade.py
  4. Corrija até tudo ficar ✅ e marque o checkbox no README.
"""

# ============================================================
# EXERCÍCIO 1 — Tipos primitivos
# ------------------------------------------------------------
# Declare 4 variáveis com valores REAIS e TIPOS corretos:
#   usuario    -> str    (ex: seu nome)
#   idade      -> int    (ex: 25 — inteiro, sem decimal)
#   altura     -> float  (ex: 1.75 — em METROS, com decimal)
#   esta_ativo -> bool   (True ou False — sem aspas!)
# ============================================================
usuario = None
idade = None
altura = None
esta_ativo = None


# ============================================================
# EXERCÍCIO 2 — Entrada de dados + conversão
# ------------------------------------------------------------
# Complete a função para que ela:
#   a) pergunte o nome com input()                 -> texto
#   b) pergunte a idade com input()                -> chega como TEXTO!
#   c) converta a idade para int()                 -> agora é número
#   d) devolva os dois:  return nome, idade_int
#      (dois valores separados por vírgula = tupla, assunto da Fase 2)
# ============================================================
def pedir_dados():
    # TODO: implemente (2 inputs + 1 conversão + 1 return)
    return ("", None)


# ============================================================
# EXERCÍCIO 3 — Saída de dados (sem f-string ainda!)
# ------------------------------------------------------------
# Monte e RETORNE a frase (não use print, use return):
#   "Olá, Ana! Você tem 25 anos."
# Use concatenação com + e converta o número com str().
# ============================================================
def apresentar(nome, idade):
    # TODO: implemente com + e str()
    return ""


# ============================================================
# EXERCÍCIO 4 — Previsão de saída (sem rodar!)
# ------------------------------------------------------------
# Leia o código abaixo NO PAPEL e devolva EXATAMENTE o que ele
# imprime, usando \n para as quebras de linha:
#
#   nome = "isaque"
#   idade = 30
#   print("Olá,", nome)
#   print("ano:", idade + 1)
# ============================================================
def previsao_saida():
    # TODO: escreva a saída esperada como texto
    return ""


# ============================================================
# VALIDAÇÃO — não altere nada abaixo desta linha
# ============================================================
from checar import validar

validar(
    usuario=usuario,
    idade=idade,
    altura=altura,
    esta_ativo=esta_ativo,
    pedir_dados=pedir_dados,
    apresentar=apresentar,
    previsao_saida=previsao_saida,
)
