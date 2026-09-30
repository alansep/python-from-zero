"""
checar.py — validação automática da Atividade 04.
Você não precisa editar este arquivo (mas pode ler — é só Python 😉).
"""

import sys


def validar(*, soma_ate, contar_divisiveis, soma_pares_ate, contar_antes_do_sete):
    print("\n── Atividade 04 · Estruturas de Repetição ──")
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

    # ---------- Exercício 1 — while ----------
    for n, esperado in [(0, 0), (-3, 0), (1, 1), (5, 15), (10, 55), (100, 5050)]:
        valor, erro = tentar(soma_ate, n)
        check(f"soma_ate({n}) → {esperado}", erro is None and valor == esperado)

    # ---------- Exercício 2 — for + range ----------
    for inicio, fim, divisor, esperado in [
        (1, 20, 3, 6),
        (1, 10, 2, 5),
        (1, 10, 0, 0),
        (5, 5, 5, 1),
        (1, 10, 11, 0),
        (0, 0, 0, 0),
    ]:
        valor, erro = tentar(contar_divisiveis, inicio, fim, divisor)
        check(
            f"contar_divisiveis({inicio}, {fim}, {divisor}) → {esperado}",
            erro is None and valor == esperado,
        )

    # ---------- Exercício 3 — continue ----------
    for n, esperado in [(0, 0), (1, 0), (2, 2), (5, 6), (10, 30)]:
        valor, erro = tentar(soma_pares_ate, n)
        check(f"soma_pares_ate({n}) → {esperado}", erro is None and valor == esperado)

    # ---------- Exercício 4 — break ----------
    for limite, esperado in [(0, 0), (3, 3), (6, 6), (7, 6), (30, 6), (100, 6)]:
        valor, erro = tentar(contar_antes_do_sete, limite)
        check(
            f"contar_antes_do_sete({limite}) → {esperado}",
            erro is None and valor == esperado,
        )

    if falhas:
        print(f"\n  🔴 {falhas} verificação(ões) falhou(aram). Corrija e rode de novo.\n")
        sys.exit(1)
    print("\n  🎉 Tudo verde! Marque o checkbox no README e siga em frente.\n")
