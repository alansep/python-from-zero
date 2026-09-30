"""
Projeto 03 — Analisador de Logs
Fase 4 · python-from-zero

COMO USAR:
  1. Leia o enunciado.md deste projeto e abra a fixture logs_exemplo.txt
     para ver o formato das linhas.
  2. Substitua os TODO pelas suas implementações.
  3. Rode no terminal:
        python3 fase-4-projetos/03-projeto-analise-logs/atividade.py
  4. Corrija até tudo ficar ✅ e marque o checkbox no README.

Formato de uma linha de log:
    2026-09-29 08:04:10 ERROR timeout ao chamar o serviço de pagamento
    ^ data      ^ hora  ^ NÍVEL (3ª palavra)  ^ mensagem

Regra de ouro: a 3ª palavra define o nível, comparada SEM diferenciar
maiúsculas de minúsculas. Linhas com menos de 3 palavras ou com uma
3ª palavra que não seja INFO/WARN/ERROR são ignoradas.

Nenhuma função abaixo usa input(): a lógica pura precisa ser
testável de forma determinística. O menu interativo é o desafio
final (meu_relatorio.py), um arquivo à parte que você cria.
"""


# ============================================================
# EXERCÍCIO 1 — Lê o arquivo de log
# ------------------------------------------------------------
# ENTRADA: caminho (str) de um .txt.
# SAÍDA: lista de linhas, CADA UMA SEM o \\n do fim,
#        descartando linhas em branco.
#        Arquivo inexistente -> [] (sem exceção escapando).
# ============================================================
def ler_log(caminho):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 2 — Filtra as linhas de um nível
# ------------------------------------------------------------
# ENTRADA: linhas (lista) e nivel ("INFO", "WARN" ou "ERROR",
#          aceitando também minúsculas).
# SAÍDA: só as linhas cuja 3ª palavra é o nivel
#        (comparação case-insensitive).
#   - nivel fora dos três válidos -> []
#   - lista vazia                 -> []
# ============================================================
def filtrar_por_nivel(linhas, nivel):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 3 — Conta ocorrências por nível
# ------------------------------------------------------------
# ENTRADA: linhas (lista).
# SAÍDA: dicionário COM AS TRÊS CHAVES SEMPRE PRESENTES,
#        inclusive zeradas:
#            {"INFO": 12, "WARN": 7, "ERROR": 9}
# Linhas malformadas não entram na conta.
# ============================================================
def contar_niveis(linhas):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 4 — Gera o relatório
# ------------------------------------------------------------
# ENTRADA: contagens (dict — pode faltar chave; ausente vale 0).
# SAÍDA: string com UMA LINHA POR NÍVEL, NESTA ORDEM FIXA:
#        INFO: 12
#        WARN: 7
#        ERROR: 9
# Formato de cada linha: "NÍVEL: quantidade".
# ============================================================
def gerar_relatorio(contagens):
    # TODO: implemente
    return None


# ============================================================
# VALIDAÇÃO — não altere nada abaixo desta linha
# ============================================================
from checar import validar

validar(
    ler_log=ler_log,
    filtrar_por_nivel=filtrar_por_nivel,
    contar_niveis=contar_niveis,
    gerar_relatorio=gerar_relatorio,
)
