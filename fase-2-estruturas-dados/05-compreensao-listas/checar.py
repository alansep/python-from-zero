"""
checar.py — validação automática da Atividade 05.
Você não precisa editar este arquivo (mas pode ler — é só Python 😉).
Inclui casos-limite de propósito: é assim que se testa código de verdade.
"""

import sys


def validar(*, dobros, pares, maiusculas, classificar, comprimentos, achatada):
    print("\n── Atividade 05 · Compreensão de listas ──")
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

    def igual_lista(funcao, argumentos, esperado):
        valor, erro = tentar(funcao, *argumentos)
        return erro is None and type(valor) is list and valor == esperado

    # ---------- Exercício 1 — dobros ----------
    for lista, esperado in [
        ([1, 2, 3], [2, 4, 6]),
        ([], []),
        ([-1, 0], [-2, 0]),
        (["a"], ["aa"]),
        ([2.5], [5.0]),
    ]:
        ok = igual_lista(dobros, (lista,), esperado)
        check(f"dobros({lista}) → {esperado}", ok)

    # ---------- Exercício 2 — pares ----------
    for lista, esperado in [
        ([1, 2, 3, 4], [2, 4]),
        ([1, 3], []),
        ([], []),
        ([0, -2, 5], [0, -2]),
        ([7], []),
    ]:
        ok = igual_lista(pares, (lista,), esperado)
        check(f"pares({lista}) → {esperado}", ok)

    # ---------- Exercício 3 — maiusculas ----------
    for palavras, esperado in [
        (["ola", "mundo"], ["OLA", "MUNDO"]),
        ([], []),
        (["ação"], ["AÇÃO"]),
        ([""], [""]),
        (["Olá"], ["OLÁ"]),
    ]:
        ok = igual_lista(maiusculas, (palavras,), esperado)
        check(f"maiusculas({palavras}) → {esperado}", ok)

    # ---------- Exercício 4 — classificar ----------
    for numeros, esperado in [
        ([1, 2, 3, 4], ["ímpar", "par", "ímpar", "par"]),
        ([], []),
        ([0, -1], ["par", "ímpar"]),
        ([7], ["ímpar"]),
        ([8], ["par"]),
    ]:
        ok = igual_lista(classificar, (numeros,), esperado)
        check(f"classificar({numeros}) → {esperado}", ok)

    # ---------- Exercício 5 — comprimentos ----------
    for palavras, esperado in [
        (["a", "olá"], [1, 3]),
        (["ção"], [3]),
        ([], []),
        (["abc", ""], [3, 0]),
        (["Python"], [6]),
    ]:
        ok = igual_lista(comprimentos, (palavras,), esperado)
        check(f"comprimentos({palavras}) → {esperado}", ok)

    # ---------- Exercício 6 — achatada ----------
    for matriz, esperado in [
        ([[1, 2], [3]], [1, 2, 3]),
        ([[1, 2], [3, 4]], [1, 2, 3, 4]),
        ([[]], []),
        ([], []),
        ([["a"], ["b", "c"]], ["a", "b", "c"]),
        ([[1], [2], [3]], [1, 2, 3]),
    ]:
        ok = igual_lista(achatada, (matriz,), esperado)
        check(f"achatada({matriz}) → {esperado}", ok)

    if falhas:
        print(f"\n  🔴 {falhas} verificação(ões) falhou(aram). Corrija e rode de novo.\n")
        sys.exit(1)
    print("\n  🎉 Tudo verde! Marque o checkbox no README e siga em frente.\n")
