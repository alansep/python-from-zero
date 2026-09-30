"""
checar.py — validação automática da Atividade 03.
Você não precisa editar este arquivo (mas pode ler — é só Python 😉).
Inclui casos-limite de propósito: é assim que se testa código de verdade.
"""

import sys


def validar(*, faixa_etaria, pode_dirigir, situacao, calcular):
    print("\n── Atividade 03 · Estruturas Condicionais ──")
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

    # ---------- Exercício 1 — faixa etária ----------
    for idade, esperado in [
        (-1, "inválida"),
        (0, "criança"),
        (12, "criança"),
        (13, "adolescente"),
        (17, "adolescente"),
        (18, "adulto"),
        (64, "adulto"),
        (65, "idoso"),
        (80, "idoso"),
    ]:
        valor, erro = tentar(faixa_etaria, idade)
        check(
            f"faixa_etaria({idade}) → '{esperado}'",
            erro is None and valor == esperado,
        )

    # ---------- Exercício 2 — pode dirigir ----------
    for idade, cnh, esperado in [
        (20, True, True),
        (18, True, True),
        (17, True, False),
        (20, False, False),
        (17, False, False),
    ]:
        valor, erro = tentar(pode_dirigir, idade, cnh)
        check(
            f"pode_dirigir({idade}, {cnh}) → {esperado}",
            erro is None and valor is esperado,
        )

    # ---------- Exercício 3 — situação ----------
    for nota, esperado in [
        (95, "SS"),
        (90, "SS"),
        (89, "A"),
        (80, "A"),
        (79, "B"),
        (70, "B"),
        (69, "C"),
        (60, "C"),
        (59, "D"),
        (0, "D"),
    ]:
        valor, erro = tentar(situacao, nota)
        check(f"situacao({nota}) → '{esperado}'", erro is None and valor == esperado)

    # ---------- Exercício 4 — calculadora ----------
    for a, operador, b, esperado in [
        (10, "+", 5, 15),
        (10, "-", 4, 6),
        (6, "*", 7, 42),
        (10, "/", 4, 2.5),
        (10, "/", 3, 10 / 3),
        (8, "+", 0, 8),                       # zero não atrapalha operações normais
        (5, "/", 0, "divisão por zero"),
        (5, "%", 2, "operador inválido"),
        (8, "%", 0, "operador inválido"),     # operador inválido vale até com zero
    ]:
        valor, erro = tentar(calcular, a, operador, b)
        check(
            f"calcular({a}, '{operador}', {b}) → {esperado}",
            erro is None and valor == esperado,
        )

    if falhas:
        print(f"\n  🔴 {falhas} verificação(ões) falhou(aram). Corrija e rode de novo.\n")
        sys.exit(1)
    print("\n  🎉 Tudo verde! Marque o checkbox no README e siga em frente.\n")
