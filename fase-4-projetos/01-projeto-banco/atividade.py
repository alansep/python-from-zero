"""
Projeto 01 — Simulador Bancário
Fase 4 · python-from-zero

COMO USAR:
  1. Leia o enunciado.md deste projeto e planeje no papel as entradas
     e as saídas de cada função.
  2. Substitua os TODO pelas suas implementações.
  3. Rode no terminal:
        python3 fase-4-projetos/01-projeto-banco/atividade.py
  4. Corrija até tudo ficar ✅ e marque o checkbox no README.

Nenhuma função abaixo usa input(): a lógica pura precisa ser
testável de forma determinística. O menu interativo é o desafio
final (meu_banco.py), um arquivo à parte que você cria.
"""


# ============================================================
# EXERCÍCIO 1 — Valida um depósito
# ------------------------------------------------------------
# Retorne True se valor > 0 e False caso contrário.
# Zero e números negativos são INVÁLIDOS.
# ============================================================
def validar_deposito(valor):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 2 — Deposita
# ------------------------------------------------------------
# ENTRADA: saldo atual e valor do depósito.
# SAÍDA: tupla (novo_saldo, situação), EXATAMENTE:
#   valor <= 0 -> (saldo, "valor inválido")      [saldo não muda]
#   caso contrário -> (saldo + valor, "depósito realizado")
# ============================================================
def depositar(saldo, valor):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 3 — Saca (5 validações, NESTA ORDEM)
# ------------------------------------------------------------
# ENTRADA: saldo atual, valor do saque e quantos saques
#          a conta já fez neste mês (0, 1, 2...).
# SAÍDA: tupla (novo_saldo, situação), EXATAMENTE:
#   1. valor <= 0                    -> (saldo, "valor inválido")
#   2. valor > 500                   -> (saldo, "saque acima do limite de R$ 500")
#   3. saques_realizados >= 3        -> (saldo, "limite de 3 saques atingido")
#   4. valor > saldo                 -> (saldo, "saldo insuficiente")
#   5. senão                         -> (saldo - valor, "saque realizado")
# Nos casos 1 a 4 o saldo devolvido é o MESMO que entrou.
# ============================================================
def sacar(saldo, valor, saques_realizados):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 4 — Registra um lançamento no histórico
# ------------------------------------------------------------
# ENTRADA: historico (lista de tuplas (tipo, valor)),
#          tipo ("deposito" ou "saque") e valor.
# SAÍDA: a MESMA lista recebida, com (tipo, valor) acrescentado
#        NO FINAL.
#   tipo fora de ("deposito", "saque") -> devolve sem alterar
#   valor <= 0                        -> devolve sem alterar
# ============================================================
def registrar_lancamento(historico, tipo, valor):
    # TODO: implemente
    return None


# ============================================================
# EXERCÍCIO 5 — Monta o texto do extrato
# ------------------------------------------------------------
# ENTRADA: historico (lista de tuplas (tipo, valor)) e saldo_final.
# SAÍDA: string com UMA LINHA POR LANÇAMENTO:
#   "Depósito: R$ 200.00"   ou   "Saque: R$ 50.00"
# e a ÚLTIMA linha sempre:
#   "Saldo final: R$ 150.00"
# Histórico vazio: nenhuma linha com "Depósito"/"Saque",
# mas a linha "Saldo final: R$ 0.00" continua obrigatória.
# Dica: f"Depósito: R$ {valor:.2f}" e junte as linhas com "\n".
# ============================================================
def formatar_extrato(historico, saldo_final):
    # TODO: implemente
    return None


# ============================================================
# VALIDAÇÃO — não altere nada abaixo desta linha
# ============================================================
from checar import validar

validar(
    validar_deposito=validar_deposito,
    depositar=depositar,
    sacar=sacar,
    registrar_lancamento=registrar_lancamento,
    formatar_extrato=formatar_extrato,
)
