"""
checar.py — validação automática da Atividade 02.
Você não precisa editar este arquivo (mas pode ler — é só Python 😉).
Inclui casos-limite de propósito: é assim que se testa código de verdade.
"""

import sys


def validar(
    *,
    coordenadas,
    tamanho_antes_depois,
    sem_duplicatas,
    uniao,
    interseccao,
    diferenca,
    pertence,
):
    print("\n── Atividade 02 · Tuplas e Conjuntos ──")
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

    def com_tipo(funcao, esperado, *argumentos):
        """Executa e só devolve o valor se o tipo bater (senão: erro)."""
        valor, erro = tentar(funcao, *argumentos)
        if erro is not None:
            return None, erro
        if not isinstance(valor, esperado):
            return None, TypeError(f"esperava {esperado.__name__}")
        return valor, None

    def ordenar_retorno(funcao, *argumentos):
        """Devolve a lista ordenada — ordem não pode ser critério de aprovação."""
        valor, erro = com_tipo(funcao, list, *argumentos)
        if erro is not None:
            return None, erro
        return tentar(lambda: sorted(valor))

    def imutavel(valor):
        if type(valor) is not tuple:
            return False

        def atribuir():
            valor[0] = 99

        _, erro = tentar(atribuir)
        return type(erro).__name__ == "TypeError"

    # ---------- Exercício 1 — coordenadas ----------
    for x, y in [
        (3, 4),
        ("norte", 7),
        (-1.5, 0),
    ]:
        esperado = (x, y)
        valor, erro = tentar(coordenadas, x, y)
        eh_tupla = erro is None and type(valor) is tuple and valor == esperado
        check(f"coordenadas({x!r}, {y!r}) → tupla {esperado}", eh_tupla)
        check(
            f"coordenadas({x!r}, {y!r}) é imutável (TypeError ao atribuir)",
            eh_tupla and imutavel(valor),
        )

    # ---------- Exercício 2 — tamanho antes/depois ----------
    for lista, esperado in [
        ([3, 1, 3, 2, 1], (5, 3)),
        ([], (0, 0)),
        (["a", "a", "b"], (3, 2)),
        ([1, 1, 1], (3, 1)),
        (["ção", "ção"], (2, 1)),
    ]:
        valor, erro = tentar(tamanho_antes_depois, lista)
        check(
            f"tamanho_antes_depois({lista}) → {esperado}",
            erro is None and valor == esperado,
        )

    # ---------- Exercício 3 — sem_duplicatas ----------
    for lista, esperado in [
        ([3, 1, 3, 2, 1], [1, 2, 3]),
        ([], []),
        (["b", "a", "b"], ["a", "b"]),
        (["ção", "ção", "x"], ["x", "ção"]),
        ([1, 1, 1], [1]),
    ]:
        obtido, erro = ordenar_retorno(sem_duplicatas, lista)
        check(
            f"sem_duplicatas({lista}) → {esperado} (em qualquer ordem)",
            erro is None and obtido == esperado,
        )

    # ---------- Exercício 4 — uniao ----------
    for a, b, esperado in [
        ({1, 2}, {2, 3}, {1, 2, 3}),
        (set(), {1}, {1}),
        ({"a"}, {"a"}, {"a"}),
        ({"ção"}, {"x"}, {"ção", "x"}),
        ({1}, set(), {1}),
    ]:
        valor, erro = com_tipo(uniao, set, a, b)
        check(f"uniao({a}, {b}) → {esperado}", erro is None and valor == esperado)

    # ---------- Exercício 5 — interseccao ----------
    for a, b, esperado in [
        ({1, 2, 3}, {2, 3, 4}, {2, 3}),
        (set(), {1}, set()),
        ({1, 2}, {3, 4}, set()),
        ({"a", "b"}, {"b", "c"}, {"b"}),
        ({"ção", "x"}, {"ção"}, {"ção"}),
    ]:
        valor, erro = com_tipo(interseccao, set, a, b)
        check(
            f"interseccao({a}, {b}) → {esperado}",
            erro is None and valor == esperado,
        )

    # ---------- Exercício 6 — diferenca ----------
    for a, b, esperado in [
        ({1, 2, 3}, {2, 3}, {1}),
        ({1}, {1, 2}, set()),
        ({1, 2}, set(), {1, 2}),
        ({"a", "b"}, {"a"}, {"b"}),
        ({"ção", "x"}, {"x"}, {"ção"}),
    ]:
        valor, erro = com_tipo(diferenca, set, a, b)
        check(f"diferenca({a}, {b}) → {esperado}", erro is None and valor == esperado)

    # ---------- Exercício 7 — pertence ----------
    for item, colecao, esperado in [
        (3, [1, 2, 3], True),
        (9, [1, 2, 3], False),
        (5, (), False),
        ("b", {"a", "b"}, True),
        ("á", "lápis", True),
        ("z", "casa", False),
        ("ção", ["ção"], True),
    ]:
        valor, erro = tentar(pertence, item, colecao)
        check(
            f"pertence({item!r}, {colecao!r}) → {esperado}",
            erro is None and valor is esperado,
        )

    if falhas:
        print(f"\n  🔴 {falhas} verificação(ões) falhou(aram). Corrija e rode de novo.\n")
        sys.exit(1)
    print("\n  🎉 Tudo verde! Marque o checkbox no README e siga em frente.\n")
