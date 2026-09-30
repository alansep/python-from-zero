"""
Projeto 02 — Gerenciador de Cadastro
Fase 4 · python-from-zero

COMO USAR:
  1. Leia o enunciado.md deste projeto e planeje no papel as entradas
     e as saídas de cada função.
  2. Substitua os TODO pelas suas implementações.
  3. Rode no terminal:
        python3 fase-4-projetos/02-projeto-cadastro/atividade.py
  4. Corrija até tudo ficar ✅ e marque o checkbox no README.

Formato dos dados (fixo, para o CSV sair sempre igual):
    clientes = {
        "11122233344": {"nome": "Ana", "email": "ana@x.com", "telefone": "999"},
        ...
    }

Nenhuma função abaixo usa input(): a lógica pura precisa ser
testável de forma determinística. O menu interativo é o desafio
final (meu_cadastro.py), um arquivo à parte que você cria.
"""

import json


# ============================================================
# EXERCÍCIO 1 — Cadastrar um cliente novo
# ------------------------------------------------------------
# ENTRADA: clientes (dict), cpf (str) e dados (dict com as
#          chaves "nome", "email" e "telefone").
# SAÍDA: True se cadastrou; False e NADA alterado se:
#   1. cpf já existe em clientes      (duplicado, não sobrescreve)
#   2. cpf não for str ou for ""      (cpf vazio)
#   3. dados não for dict / for vazio /
#      faltar alguma das 3 chaves      (dados incompletos)
# ============================================================
def cadastrar(clientes, cpf, dados):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 2 — Buscar um cliente
# ------------------------------------------------------------
# SAÍDA: os dados daquele cpf, ou None se não existir.
# ============================================================
def buscar(clientes, cpf):
    # TODO: implemente (o retorno nunca deve ser "TODO")
    return "TODO"


# ============================================================
# EXERCÍCIO 3 — Atualizar um cliente (fusão parcial)
# ------------------------------------------------------------
# ENTRADA: clientes, cpf e novos_dados (dict com ao menos 1 chave).
# SAÍDA: True se atualizou; False se cpf não existe, ou se
#        novos_dados não for dict ou for vazio.
# Comportamento: as chaves de novos_dados são gravadas por cima;
# as chaves antigas NÃO informadas são PRESERVADAS.
# ============================================================
def atualizar(clientes, cpf, novos_dados):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 4 — Listar os CPFs
# ------------------------------------------------------------
# SAÍDA: lista com os cpfs NA ORDEM do cadastro. Vazio -> [].
# ============================================================
def listar(clientes):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 5 — Salvar backup em .json
# ------------------------------------------------------------
# ENTRADA: caminho (str) e dados (dict).
# SAÍDA: True se gravou; False se o DIRETÓRIO do caminho não
#        existe (use try/except — não deixe explodir).
# ============================================================
def salvar_json(caminho, dados):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 6 — Carregar backup do .json
# ------------------------------------------------------------
# ENTRADA: caminho (str).
# SAÍDA: o dict gravado, ou {} quando:
#   1. o arquivo não existe
#   2. o conteúdo não é JSON válido
#   3. o conteúdo é JSON válido mas NÃO é um dict (ex.: lista)
# ============================================================
def carregar_json(caminho):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 7 — Exportar para planilha .csv
# ------------------------------------------------------------
# ENTRADA: caminho (str) e clientes (dict).
# SAÍDA: True se gravou; False se clientes for {} (não grava
#        nada) ou se o diretório não existe.
# Arquivo EXATO:
#   1ª linha: cpf,nome,email,telefone
#   depois:   1 linha por cliente, na ordem de listar(clientes)
# ============================================================
def exportar_csv(caminho, clientes):
    # TODO: implemente
    return None


# ============================================================
# VALIDAÇÃO — não altere nada abaixo desta linha
# ============================================================
from checar import validar

validar(
    cadastrar=cadastrar,
    buscar=buscar,
    atualizar=atualizar,
    listar=listar,
    salvar_json=salvar_json,
    carregar_json=carregar_json,
    exportar_csv=exportar_csv,
)
