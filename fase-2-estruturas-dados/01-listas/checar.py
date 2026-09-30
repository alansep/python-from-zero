"""
checar.py — validação automática da Atividade 01.
Você não precisa editar este arquivo (mas pode ler — é só Python 😉).
Inclui casos-limite de propósito: é assim que se testa código de verdade.
"""

import sys


def validar(
    *,
    extremos,
    ultimos,
    trocar,
    adicionar,
    ordenar_em_origem,
    reverter_em_origem,
    remover_indice,
    remover_primeira,
    resumo,
):
    print("\n── Atividade 01 · Listas ──")
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

    # ---------- Exercício 1 — extremos ----------
    for lista, esperado in [
        ([10, 20, 30], (10, 30)),
        ([1, 2, 3, 4], (1, 4)),
        (["a"], ("a", "a")),
        (["ção", "xyz"], ("ção", "xyz")),
        ([], (None, None)),
    ]:
        valor, erro = tentar(extremos, lista)
        check(f"extremos({lista}) → {esperado}", erro is None and valor == esperado)

    # ---------- Exercício 2 — ultimos ----------
    for lista, n, esperado in [
        ([1, 2, 3, 4, 5], 3, [3, 4, 5]),
        ([1, 2], 5, [1, 2]),
        ([1, 2, 3], 0, []),
        ([1, 2, 3], -2, []),
        ([], 2, []),
        (["a", "b"], 1, ["b"]),
    ]:
        valor, erro = tentar(ultimos, lista, n)
        check(
            f"ultimos({lista}, {n}) → {esperado}",
            erro is None and valor == esperado,
        )

    # ---------- Exercício 3 — trocar ----------
    for lista, i, j, esperado in [
        ([1, 2, 3], 0, 2, [3, 2, 1]),
        (["á", "b", "c"], 0, 1, ["b", "á", "c"]),
        ([1, 2, 3], 1, 1, [1, 2, 3]),
        ([10, 20], -1, 0, [20, 10]),
    ]:
        original = list(lista)
        valor, erro = tentar(trocar, lista, i, j)
        check(
            f"trocar({original}, {i}, {j}) → {esperado} (mesma lista)",
            erro is None and valor is lista and lista == esperado,
        )

    # ---------- Exercício 4 — adicionar ----------
    for lista, valor_item, indice, esperado_len, esperado_lista in [
        ([1, 2], 9, None, 3, [1, 2, 9]),
        ([1, 2], 9, 0, 3, [9, 1, 2]),
        ([], "a", None, 1, ["a"]),
        (["a", "b"], "x", -1, 3, ["a", "x", "b"]),
        (["ção"], "!", 1, 2, ["ção", "!"]),
    ]:
        original = list(lista)
        valor, erro = tentar(adicionar, lista, valor_item, indice)
        check(
            f"adicionar({original}, {valor_item!r}, {indice}) → {esperado_len} "
            f"e lista {esperado_lista}",
            erro is None
            and valor == esperado_len
            and lista == esperado_lista,
        )

    # ---------- Exercício 5 — ordenar_em_origem ----------
    for lista, esperado in [
        ([3, 1, 2], [1, 2, 3]),
        (["b", "a", "c"], ["a", "b", "c"]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([2.5, 1.5], [1.5, 2.5]),
        (["á", "a", "z"], sorted(["á", "a", "z"])),
    ]:
        original = list(lista)
        valor, erro = tentar(ordenar_em_origem, lista)
        check(
            f"ordenar_em_origem({original}) → {esperado} e retorno None",
            erro is None and valor is None and lista == esperado,
        )

    # ---------- Exercício 6 — reverter_em_origem ----------
    for lista, esperado in [
        ([1, 2, 3], [3, 2, 1]),
        (["a", "b"], ["b", "a"]),
        ([1, 2, 3, 4], [4, 3, 2, 1]),
        (["á", "b"], ["b", "á"]),
    ]:
        original = list(lista)
        valor, erro = tentar(reverter_em_origem, lista)
        check(
            f"reverter_em_origem({original}) → {esperado} e retorno None",
            erro is None and valor is None and lista == esperado,
        )

    # ---------- Exercício 7 — remover_indice ----------
    for lista, indice, esperado_item, esperado_lista in [
        ([10, 20, 30], 1, 20, [10, 30]),
        (["a", "b"], -1, "b", ["a"]),
        ([7], 0, 7, []),
        (["ção", "x"], 0, "ção", ["x"]),
    ]:
        original = list(lista)
        valor, erro = tentar(remover_indice, lista, indice)
        check(
            f"remover_indice({original}, {indice}) devolve {esperado_item}",
            erro is None and valor == esperado_item,
        )
        check(
            f"remover_indice({original}, {indice}) deixa {esperado_lista}",
            lista == esperado_lista,
        )

    # ---------- Exercício 8 — remover_primeira ----------
    for lista, item, esperado_bool, esperado_lista in [
        ([1, 2, 3, 2], 2, True, [1, 3, 2]),
        (["a", "b"], "z", False, ["a", "b"]),
        (["á", "b", "á"], "á", True, ["b", "á"]),
        (["ção", "x"], "ção", True, ["x"]),
        ([], "a", False, []),
    ]:
        original = list(lista)
        valor, erro = tentar(remover_primeira, lista, item)
        check(
            f"remover_primeira({original}, {item!r}) → {esperado_bool} "
            f"e lista {esperado_lista}",
            erro is None
            and valor is esperado_bool
            and lista == esperado_lista,
        )

    # ---------- Exercício 9 — resumo ----------
    for lista, esperado in [
        ([1, 2, 3], (6, 2.0)),
        ([5], (5, 5.0)),
        ([-1, 1], (0, 0.0)),
        ([10.5, 1.5], (12, 6.0)),
        ([], (None, None)),
    ]:
        original = list(lista)
        valor, erro = tentar(resumo, lista)
        check(f"resumo({original}) → {esperado}", erro is None and valor == esperado)

    if falhas:
        print(f"\n  🔴 {falhas} verificação(ões) falhou(aram). Corrija e rode de novo.\n")
        sys.exit(1)
    print("\n  🎉 Tudo verde! Marque o checkbox no README e siga em frente.\n")
