"""
Atividade 03 — Manipulação de Arquivos
Fase 3 · python-from-zero

COMO USAR:
  1. Leia o enunciado.md deste tópico.
  2. Substitua os TODO pelas suas respostas.
  3. Rode no terminal:
        python3 fase-3-modularizacao/03-arquivos/atividade.py
  4. Corrija até tudo ficar ✅ e marque o checkbox no README.

As validações usam uma pasta TEMPORÁRIA do sistema — nada é gravado
no repositório. Suas funções sempre RECEBEM o caminho como parâmetro.
"""

# ------------------------------------------------------------
# TODO: importe aqui o que precisar (pathlib, json, csv...)
# ------------------------------------------------------------


# ============================================================
# EXERCÍCIO 1 — Escrever um .txt
# ------------------------------------------------------------
# Grave EXATAMENTE `texto` no caminho informado, com
# encoding="utf-8". Use `with` para o arquivo fechar sozinho.
# ============================================================
def escrever_txt(caminho, texto):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 2 — Ler um .txt
# ------------------------------------------------------------
# Devolva o conteúdo DO ARQUIVO (texto).
# Arquivo inexistente -> None (confira antes de abrir).
# ============================================================
def ler_txt(caminho):
    # TODO: implemente
    return "..."


# ============================================================
# EXERCÍCIO 3 — Contar linhas
# ------------------------------------------------------------
# Devolva quantas linhas o arquivo tem.
#   "a\\n" -> 1 linha | "" -> 0 linhas | arquivo sumiu -> None
# ============================================================
def contar_linhas(caminho):
    # TODO: implemente
    return ""


# ============================================================
# EXERCÍCIO 4 — O caminho existe?
# ------------------------------------------------------------
# Devolva True/False com pathlib (sem abrir o arquivo).
# ============================================================
def existe(caminho):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 5 — Juntar caminhos com o operador `/`
# ------------------------------------------------------------
# Devolva como TEXTO o caminho base + nome usando Path / Path.
#   juntar_caminho("dados", "notas.txt") -> "dados/notas.txt"
# ============================================================
def juntar_caminho(base, nome):
    # TODO: implemente
    return ""


# ============================================================
# EXERCÍCIO 6 — JSON em disco (roundtrip)
# ------------------------------------------------------------
# salvar_json: grave `dados` no caminho (json.dump, utf-8).
# carregar_json: devolva o objeto de volta; se o arquivo não
# existir -> None (confira antes de abrir).
# ============================================================
def salvar_json(caminho, dados):
    # TODO: implemente
    return None


def carregar_json(caminho):
    # TODO: implemente
    return ""


# ============================================================
# EXERCÍCIO 7 — CSV em disco (roundtrip)
# ------------------------------------------------------------
# salvar_csv: grave todas as `linhas` (lista de listas).
#   lembre do newline="" no modo "w".
# ler_csv: devolva lista de listas (csv.reader); arquivo vazio -> [].
# ============================================================
def salvar_csv(caminho, linhas):
    # TODO: implemente
    return None


def ler_csv(caminho):
    # TODO: implemente
    return None


# ============================================================
# VALIDAÇÃO — não altere nada abaixo desta linha
# ============================================================
from checar import validar

validar(
    escrever_txt=escrever_txt,
    ler_txt=ler_txt,
    contar_linhas=contar_linhas,
    existe=existe,
    juntar_caminho=juntar_caminho,
    salvar_json=salvar_json,
    carregar_json=carregar_json,
    salvar_csv=salvar_csv,
    ler_csv=ler_csv,
)
