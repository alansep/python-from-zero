"""
Atividade 02 — Módulos e Importação
Fase 3 · python-from-zero

COMO USAR:
  1. Leia o enunciado.md deste tópico.
  2. Substitua os TODO pelas suas respostas (importe você mesmo o que precisar).
  3. Rode no terminal:
        python3 fase-3-modularizacao/02-modulos/atividade.py
  4. Corrija até tudo ficar ✅ e marque o checkbox no README.
"""

# ------------------------------------------------------------
# TODO: importe aqui o que precisar — math, random, datetime,
# json, csv, io... (a validação NÃO importa por você)
# ------------------------------------------------------------


# ============================================================
# EXERCÍCIO 1 — Raiz quadrada (math)
# ------------------------------------------------------------
# Devolva math.sqrt(x) como float. Ex.: raiz_de(9) -> 3.0
# ============================================================
def raiz_de(x):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 2 — Teto (math)
# ------------------------------------------------------------
# Devolva math.ceil(x): o menor inteiro >= x.
# Ex.: teto(3.2) -> 4   |   teto(-3.2) -> -3   |   teto(4) -> 4
# ============================================================
def teto(x):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 3 — Embaralhar (random)
# ------------------------------------------------------------
# Devolva UMA NOVA lista com os mesmos elementos em outra ordem.
# A lista RECEBIDA não pode ser modificada (use cópia antes do shuffle).
# ============================================================
def embaralhar(valores):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 4 — É fim de semana? (datetime)
# ------------------------------------------------------------
# Devolva True se date(ano, mes, dia).weekday() for 5 (sábado)
# ou 6 (domingo); False para os demais (0 a 4).
# ============================================================
def fim_de_semana(ano, mes, dia):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 5 — Dias entre duas datas (datetime)
# ------------------------------------------------------------
# `a` e `b` são objetos datetime.date.
# Devolva (b - a).days — COM SINAL (se b for anterior, o resultado é negativo).
# ============================================================
def dias_entre(a, b):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 6 — Dict -> JSON (json)
# ------------------------------------------------------------
# Devolva json.dumps(dados) como str.
# A validação faz json.loads() no seu retorno e espera receber
# EXATAMENTE o mesmo objeto de entrada (roundtrip, acentos inclusos).
# ============================================================
def para_json(dados):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 7 — Cabeçalho de CSV (csv)
# ------------------------------------------------------------
# `texto` é um CSV completo (com \\n entre as linhas).
# Devolva a PRIMEIRA linha como lista de campos, usando
# csv.reader + next() — deve respeitar campos entre aspas
# que contêm vírgula (ex.: "nome, sobrenome").
# ============================================================
def cabecalho(texto):
    # TODO: implemente
    return None


# ============================================================
# VALIDAÇÃO — não altere nada abaixo desta linha
# ============================================================
from checar import validar

validar(
    raiz_de=raiz_de,
    teto=teto,
    embaralhar=embaralhar,
    fim_de_semana=fim_de_semana,
    dias_entre=dias_entre,
    para_json=para_json,
    cabecalho=cabecalho,
)
