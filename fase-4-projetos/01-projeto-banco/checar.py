"""
checar.py — validação automática do Projeto 01 (Simulador Bancário).
Você não precisa editar este arquivo (mas pode ler — é só Python 😉).
Inclui casos-limite de propósito: é assim que se testa código de verdade.
"""

import re
import sys


def validar(
    *,
    validar_deposito,
    depositar,
    sacar,
    registrar_lancamento,
    formatar_extrato,
):
    print("\n── Atividade 01 · Simulador Bancário ──")
    falhas = 0

    def check(descricao, ok):
        nonlocal falhas
        print(("  ✅ " if ok else "  ❌ ") + descricao)
        if not ok:
            falhas += 1

    def tentar(funcao, *argumentos):
        try:
            return funcao(*argumentos), None
        except Exception as erro:
            return None, erro

    def tupla_ok(valor, saldo_esperado, situacao_esperada):
        if not isinstance(valor, tuple) or len(valor) != 2:
            return False
        novo_saldo, situacao = valor
        if isinstance(novo_saldo, bool) or not isinstance(novo_saldo, (int, float)):
            return False
        return abs(novo_saldo - saldo_esperado) < 1e-9 and situacao == situacao_esperada

    def tem_valor(texto, valor):
        limpo = str(texto).replace("R$", "").replace(",", ".")
        alvos = [f"{valor:.2f}"]
        if float(valor).is_integer():
            alvos.append(str(int(valor)))
        return any(
            re.search(r"(?<![\d.])" + re.escape(alvo) + r"(?![\d])", limpo)
            for alvo in alvos
        )

    # ---------- Exercício 1 — validar depósito ----------
    for valor, esperado in [
        (100, True),
        (0.01, True),
        (150.5, True),
        (0, False),
        (-50, False),
        (-0.01, False),
    ]:
        obtido, erro = tentar(validar_deposito, valor)
        check(
            f"validar_deposito({valor}) → {esperado}",
            erro is None and obtido == esperado,
        )

    # ---------- Exercício 2 — depositar ----------
    for saldo, valor, saldo_esperado, situacao_esperada in [
        (1000, 200, 1200, "depósito realizado"),
        (1000, 0.5, 1000.5, "depósito realizado"),
        (0, 150, 150, "depósito realizado"),
        (1000, 0, 1000, "valor inválido"),
        (1000, -100, 1000, "valor inválido"),
    ]:
        obtido, erro = tentar(depositar, saldo, valor)
        check(
            f"depositar({saldo}, {valor}) → ({saldo_esperado}, '{situacao_esperada}')",
            erro is None and tupla_ok(obtido, saldo_esperado, situacao_esperada),
        )

    # ---------- Exercício 3 — sacar ----------
    for saldo, valor, saques, saldo_esperado, situacao_esperada in [
        (1000, 100, 0, 900, "saque realizado"),
        (500, 500, 0, 0, "saque realizado"),
        (500, 500, 2, 0, "saque realizado"),
        (1000, 501, 0, 1000, "saque acima do limite de R$ 500"),
        (1000, 600, 5, 1000, "saque acima do limite de R$ 500"),
        (1000, 0, 0, 1000, "valor inválido"),
        (1000, -50, 0, 1000, "valor inválido"),
        (1000, 100, 3, 1000, "limite de 3 saques atingido"),
        (300, 400, 0, 300, "saldo insuficiente"),
        (0, 100, 0, 0, "saldo insuficiente"),
    ]:
        obtido, erro = tentar(sacar, saldo, valor, saques)
        check(
            f"sacar({saldo}, {valor}, {saques}) → "
            f"({saldo_esperado}, '{situacao_esperada}')",
            erro is None and tupla_ok(obtido, saldo_esperado, situacao_esperada),
        )

    # ---------- Exercício 4 — registrar lançamento ----------
    historico = []
    obtido, erro = tentar(registrar_lancamento, historico, "deposito", 200)
    check(
        "registrar_lancamento devolve a lista com 1 lançamento",
        erro is None
        and isinstance(obtido, list)
        and obtido == [("deposito", 200)],
    )
    check(
        "registrar_lancamento altera a MESMA lista que recebeu",
        historico == [("deposito", 200)],
    )

    historico = [("deposito", 200)]
    obtido, erro = tentar(registrar_lancamento, historico, "saque", 50)
    check(
        "lançamentos preservam a ordem de registro",
        erro is None
        and isinstance(obtido, list)
        and obtido == [("deposito", 200), ("saque", 50)],
    )

    for tipo, valor in [("pix", 100), ("deposito", 0), ("saque", -50)]:
        historico = [("deposito", 100)]
        obtido, erro = tentar(registrar_lancamento, historico, tipo, valor)
        check(
            f"lançamento inválido ignorado (tipo='{tipo}', valor={valor})",
            erro is None
            and isinstance(obtido, list)
            and obtido == [("deposito", 100)]
            and historico == [("deposito", 100)],
        )

    # ---------- Exercício 5 — formatar extrato ----------
    obtido, erro = tentar(
        formatar_extrato, [("deposito", 200), ("saque", 50)], 150
    )
    texto = "" if erro else str(obtido)
    check(
        "extrato lista cada lançamento (Depósito e Saque)",
        erro is None and "Depósito" in texto and "Saque" in texto,
    )
    check(
        "extrato mostra cada valor e o Saldo final correto",
        erro is None
        and "Saldo final" in texto
        and tem_valor(texto, 200)
        and tem_valor(texto, 50)
        and tem_valor(texto, 150),
    )

    obtido, erro = tentar(formatar_extrato, [], 0)
    texto = "" if erro else str(obtido)
    check(
        "extrato vazio: sem linhas de lançamento, mas com Saldo final",
        erro is None
        and "Depósito" not in texto
        and "Saque" not in texto
        and "Saldo final" in texto,
    )

    obtido, erro = tentar(formatar_extrato, [("saque", 300)], 0)
    texto = "" if erro else str(obtido)
    check(
        "extrato com um único saque não inventa depósito",
        erro is None
        and "Saque" in texto
        and "Depósito" not in texto
        and tem_valor(texto, 300),
    )

    if falhas:
        print(f"\n  🔴 {falhas} verificação(ões) falhou(aram). Corrija e rode de novo.\n")
        sys.exit(1)
    print("\n  🎉 Tudo verde! Marque o checkbox no README e siga em frente.\n")
