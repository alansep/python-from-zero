"""
checar.py — validação automática da Atividade 06.
Você não precisa editar este arquivo (mas pode ler — é só Python 😉).
A Parte A valida o comportamento CORRIGIDO dos bugs; a Parte B compara
suas respostas sobre as stack traces (minúsculas, sem espaço nas bordas).
"""

import sys


def validar(
    *,
    maior_de_tres,
    soma_ate,
    contar_pares,
    total_do_carrinho,
    resposta_1,
    resposta_2,
    resposta_3,
    resposta_4,
    resposta_5,
    resposta_6,
    resposta_7,
    resposta_8,
):
    print("\n── Atividade 06 · Depuração sem IA ──")
    falhas = 0

    def check(descricao, ok):
        nonlocal falhas
        print(("  ✅ " if ok else "  ❌ ") + descricao)
        if not ok:
            falhas += 1

    def tentar(funcao, *argumentos, **argumentos_nomeados):
        try:
            return funcao(*argumentos, **argumentos_nomeados), None
        except Exception as erro:
            return None, erro

    def normalizar(texto):
        return str(texto).strip().strip('"\'').strip().lower()

    # ---------- Parte A · Exercício 1 — maior_de_tres ----------
    for a, b, c, esperado in [
        (1, 2, 3, 3),
        (3, 2, 1, 3),
        (5, 5, 5, 5),
        (-1, -5, -9, -1),
        (2, 9, 4, 9),
    ]:
        valor, erro = tentar(maior_de_tres, a, b, c)
        check(f"maior_de_tres({a}, {b}, {c}) → {esperado}",
              erro is None and valor == esperado)

    # ---------- Parte A · Exercício 2 — soma_ate ----------
    for n, esperado in [(5, 15), (1, 1), (0, 0), (-3, 0), (10, 55), (100, 5050)]:
        valor, erro = tentar(soma_ate, n)
        check(f"soma_ate({n}) → {esperado}", erro is None and valor == esperado)

    # ---------- Parte A · Exercício 3 — contar_pares ----------
    for valores, esperado in [
        ([1, 2, 3, 4], 2),
        ([2, 4, 6], 3),
        ([], 0),
        ([0, -2, 7, 9, 10], 3),
        ([7, 9], 0),
    ]:
        valor, erro = tentar(contar_pares, valores)
        check(f"contar_pares({valores}) → {esperado}", erro is None and valor == esperado)

    # ---------- Parte A · Exercício 4 — total_do_carrinho ----------
    for precos, esperado in [
        ([10, 20, 30], 60),
        ([], 0),
        ([5], 5),
        ([-2, 2], 0),
        ([2.5, 2.5, 2.5], 7.5),
    ]:
        valor, erro = tentar(total_do_carrinho, precos)
        check(f"total_do_carrinho({precos}) → {esperado}", erro is None and valor == esperado)

    # ---------- Parte B · leitura de stack traces ----------
    for descricao, obtido, esperado in [
        ("resposta_1 · tipo da exceção da stack trace 1", resposta_1, "nameerror"),
        ("resposta_2 · variável inexistente", resposta_2, "soma"),
        ("resposta_3 · tipo da exceção da stack trace 2", resposta_3, "typeerror"),
        ("resposta_4 · função chamada sem argumento", resposta_4, "dobro"),
        ("resposta_5 · tipo da exceção da stack trace 3", resposta_5, "indexerror"),
        ("resposta_6 · índice tentado", resposta_6, "3"),
        ("resposta_7 · tipo da exceção da stack trace 4", resposta_7, "valueerror"),
        ("resposta_8 · palavra culpada na mensagem", resposta_8, "dez"),
    ]:
        check(f"{descricao} → '{esperado}'", normalizar(obtido) == esperado)

    if falhas:
        print(f"\n  🔴 {falhas} verificação(ões) falhou(aram). Corrija e rode de novo.\n")
        sys.exit(1)
    print("\n  🎉 Tudo verde! Marque o checkbox no README e siga em frente.\n")
