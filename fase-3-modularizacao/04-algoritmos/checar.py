"""
checar.py — validação automática da Atividade 04.
Você não precisa editar este arquivo (mas pode ler — é só Python 😉).
Inclui casos-limite de propósito: é assim que se testa código de verdade.
"""

import sys


def validar(*, buscar, buscar_todos, bubble_sort):
    print("\n── Atividade 04 · Algoritmos Clássicos ──")
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

    # ---------- Exercício 1 — busca linear ----------
    for lista, alvo, esperado in [
        ([4, 8, 15, 16, 23, 42], 16, 3),
        ([4, 8, 15, 16, 23, 42], 42, 5),   # encontrado no fim
        ([4, 8, 15, 16, 23, 42], 4, 0),    # encontrado no início
        ([4, 8, 15, 16, 23, 42], 99, -1),  # ausente
        ([], 1, -1),                       # lista vazia
        ([5, 3, 5, 3], 5, 0),              # duplicado -> primeiro índice
        ([5, 3, 5, 3], 3, 1),              # duplicado -> primeiro índice
        (["a", "b", "c"], "c", 2),         # funciona com strings
        ([0], 0, 0),                       # lista de um elemento
    ]:
        valor, erro = tentar(buscar, lista, alvo)
        check(f"buscar({lista}, {alvo}) → {esperado}", erro is None and valor == esperado)

    # ---------- Exercício 2 — todas as ocorrências ----------
    for lista, alvo, esperado in [
        ([1, 2, 1, 3, 1], 1, [0, 2, 4]),
        ([1, 2, 3], 9, []),
        ([], 9, []),
        ([4, 4, 4], 4, [0, 1, 2]),
        ([7], 7, [0]),
        ([0, 1, 0], 0, [0, 2]),
    ]:
        valor, erro = tentar(buscar_todos, lista, alvo)
        check(f"buscar_todos({lista}, {alvo}) → {esperado}", erro is None and valor == esperado)

    # ---------- Exercício 3 — bubble sort ----------
    for entrada, esperado in [
        ([], []),
        ([1], [1]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),          # já ordenada
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),    # inversa
        ([3, 1, 3, 2, 1], [1, 1, 2, 3, 3]),    # duplicados
        ([-2, 0, -5, 3.5], [-5, -2, 0, 3.5]),  # negativos e float
        ([9, 7, 8, 6], [6, 7, 8, 9]),
        (["b", "a", "c"], ["a", "b", "c"]),    # strings também ordenam
    ]:
        valor, erro = tentar(bubble_sort, entrada)
        check(f"bubble_sort({entrada}) → {esperado}", erro is None and valor == esperado)

    # ---------- resultado coerente: devolveu uma lista de verdade ----------
    valor, erro = tentar(bubble_sort, [2, 1])
    check("bubble_sort devolve uma lista ordenada de verdade",
          erro is None and isinstance(valor, list) and valor == [1, 2])

    if falhas:
        print(f"\n  🔴 {falhas} verificação(ões) falhou(aram). Corrija e rode de novo.\n")
        sys.exit(1)
    print("\n  🎉 Tudo verde! Marque o checkbox no README e siga em frente.\n")
