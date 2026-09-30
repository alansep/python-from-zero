"""
checar.py — validação automática da Atividade 03.
Você não precisa editar este arquivo (mas pode ler — é só Python 😉).
Inclui casos-limite de propósito: é assim que se testa código de verdade.
"""

import sys


def validar(
    *,
    buscar,
    contar,
    mesclar,
    cidade_de,
    remover_chave,
    pares,
    somar_valores,
):
    print("\n── Atividade 03 · Dicionários ──")
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

    # ---------- Exercício 1 — buscar ----------
    for dicionario, chave, padrao, esperado in [
        ({"a": 1}, "a", 0, 1),
        ({"a": 1}, "z", "N/A", "N/A"),
        ({"nome": "Ana"}, "idade", 0, 0),
        ({"ação": "ok"}, "ação", "?", "ok"),
        ({}, "x", False, False),
        ({"a": 1}, "z", -1, -1),
    ]:
        valor, erro = tentar(buscar, dicionario, chave, padrao)
        check(
            f"buscar({dicionario}, {chave!r}, {padrao!r}) → {esperado!r}",
            erro is None and valor == esperado,
        )

    # ---------- Exercício 2 — contar ----------
    for lista, esperado in [
        (["a", "b", "a"], {"a": 2, "b": 1}),
        ([], {}),
        (["ção", "x", "ção"], {"ção": 2, "x": 1}),
        ([1, 2, 1], {1: 2, 2: 1}),
        (["a"], {"a": 1}),
    ]:
        valor, erro = tentar(contar, lista)
        check(f"contar({lista}) → {esperado}", erro is None and valor == esperado)

    # ---------- Exercício 3 — mesclar ----------
    for d1, d2, esperado in [
        ({"a": 1}, {"b": 2}, {"a": 1, "b": 2}),
        ({"a": 1}, {"a": 9, "b": 2}, {"a": 9, "b": 2}),
        ({}, {}, {}),
        ({"ação": "sim"}, {"ação": "não"}, {"ação": "não"}),
        ({"x": 1}, {}, {"x": 1}),
    ]:
        original1, original2 = dict(d1), dict(d2)
        valor, erro = tentar(mesclar, d1, d2)
        check(
            f"mesclar({original1}, {original2}) → {esperado} sem alterar as entradas",
            erro is None
            and valor == esperado
            and d1 == original1
            and d2 == original2,
        )

    # ---------- Exercício 4 — cidade_de ----------
    for perfil, esperado in [
        ({"endereco": {"cidade": "São Paulo"}}, "São Paulo"),
        ({"endereco": {"cidade": ""}}, ""),
        ({"endereco": {}}, ""),
        ({}, ""),
        ({"nome": "Ana"}, ""),
        ({"endereco": {"uf": "SP"}}, ""),
    ]:
        valor, erro = tentar(cidade_de, perfil)
        check(
            f"cidade_de({perfil}) → {esperado!r}",
            erro is None and valor == esperado,
        )

    # ---------- Exercício 5 — remover_chave ----------
    for dicionario, chave, esperado_bool, esperado_dict in [
        ({"a": 1, "b": 2}, "a", True, {"b": 2}),
        ({"a": 1}, "z", False, {"a": 1}),
        ({}, "a", False, {}),
        ({"ação": "ok"}, "ação", True, {}),
        ({"x": 1, "y": 2}, "y", True, {"x": 1}),
    ]:
        original = dict(dicionario)
        valor, erro = tentar(remover_chave, dicionario, chave)
        check(
            f"remover_chave({original}, {chave!r}) → {esperado_bool} "
            f"e dict {esperado_dict}",
            erro is None
            and valor is esperado_bool
            and dicionario == esperado_dict,
        )

    # ---------- Exercício 6 — pares ----------
    for dicionario, esperado in [
        ({"nome": "Ana", "idade": 30}, [("nome", "Ana"), ("idade", 30)]),
        ({}, []),
        ({"ação": "ok"}, [("ação", "ok")]),
        ({"z": 1}, [("z", 1)]),
    ]:
        valor, erro = tentar(pares, dicionario)
        check(f"pares({dicionario}) → {esperado}", erro is None and valor == esperado)

    # ---------- Exercício 7 — somar_valores ----------
    for dicionario, esperado in [
        ({"a": 1, "b": 2}, 3),
        ({}, 0),
        ({"a": -1, "b": 1}, 0),
        ({"x": 1.5}, 1.5),
        ({"a": 10, "b": 20, "c": 30}, 60),
    ]:
        valor, erro = tentar(somar_valores, dicionario)
        check(
            f"somar_valores({dicionario}) → {esperado}",
            erro is None and valor == esperado,
        )

    if falhas:
        print(f"\n  🔴 {falhas} verificação(ões) falhou(aram). Corrija e rode de novo.\n")
        sys.exit(1)
    print("\n  🎉 Tudo verde! Marque o checkbox no README e siga em frente.\n")
