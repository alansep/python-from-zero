"""
checar.py — validação automática da Atividade 04.
Você não precisa editar este arquivo (mas pode ler — é só Python 😉).
Inclui casos-limite de propósito: é assim que se testa código de verdade.
"""

import sys


def validar(
    *,
    limpar,
    capitalizar,
    juntar,
    substituir,
    contar,
    contem,
    reverter,
    frase,
):
    print("\n── Atividade 04 · Strings ──")
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

    # ---------- Exercício 1 — limpar ----------
    for texto, esperado in [
        ("  oi   mundo  ", "oi mundo"),
        ("   ", ""),
        ("", ""),
        ("só", "só"),
        ("ção   você  ", "ção você"),
        ("a b", "a b"),
    ]:
        valor, erro = tentar(limpar, texto)
        check(f"limpar({texto!r}) → {esperado!r}", erro is None and valor == esperado)

    # ---------- Exercício 2 — capitalizar ----------
    for texto, esperado in [
        ("  hELLO  ", "Hello"),
        ("PYTHON", "Python"),
        ("jOhN", "John"),
        ("a", "A"),
        ("", ""),
        ("   ", ""),
        ("olá mundo", "Olá mundo"),
    ]:
        valor, erro = tentar(capitalizar, texto)
        check(
            f"capitalizar({texto!r}) → {esperado!r}",
            erro is None and valor == esperado,
        )

    # ---------- Exercício 3 — juntar ----------
    for palavras, separador, esperado in [
        (["a", "b", "c"], "-", "a-b-c"),
        ([], "-", ""),
        (["só", "uma"], "", "sóuma"),
        (["ção", "você"], " ", "ção você"),
        (["a"], "|", "a"),
        (["olá", "mundo"], " ", "olá mundo"),
    ]:
        valor, erro = tentar(juntar, palavras, separador)
        check(
            f"juntar({palavras}, {separador!r}) → {esperado!r}",
            erro is None and valor == esperado,
        )

    # ---------- Exercício 4 — substituir ----------
    for texto, antigo, novo, esperado in [
        ("a-b-c", "-", "+", "a+b+c"),
        ("banana", "a", "o", "bonono"),
        ("ola", "x", "y", "ola"),
        ("ação ação", "ção", "cao", "acao acao"),
        ("", "a", "b", ""),
        ("olá olá", "lá", "la", "ola ola"),
    ]:
        valor, erro = tentar(substituir, texto, antigo, novo)
        check(
            f"substituir({texto!r}, {antigo!r}, {novo!r}) → {esperado!r}",
            erro is None and valor == esperado,
        )

    # ---------- Exercício 5 — contar ----------
    for texto, trecho, esperado in [
        ("banana", "a", 3),
        ("banana", "z", 0),
        ("aaa", "aa", 1),
        ("", "a", 0),
        ("çãoção", "ção", 2),
        ("abab", "aba", 1),
    ]:
        valor, erro = tentar(contar, texto, trecho)
        check(
            f"contar({texto!r}, {trecho!r}) → {esperado}",
            erro is None and valor == esperado,
        )

    # ---------- Exercício 6 — contem ----------
    for texto, trecho, esperado in [
        ("casa", "as", True),
        ("casa", "z", False),
        ("ação", "ç", True),
        ("ação", "ção", True),
        ("Olá", "olá", False),
        ("abc", "", True),
    ]:
        valor, erro = tentar(contem, texto, trecho)
        check(
            f"contem({texto!r}, {trecho!r}) → {esperado}",
            erro is None and valor is esperado,
        )

    # ---------- Exercício 7 — reverter ----------
    for texto, esperado in [
        ("abc", "cba"),
        ("", ""),
        ("olá", "álo"),
        ("ação", "oãça"),
        ("a b", "b a"),
        ("Python", "nohtyP"),
    ]:
        valor, erro = tentar(reverter, texto)
        check(f"reverter({texto!r}) → {esperado!r}", erro is None and valor == esperado)

    # ---------- Exercício 8 — frase ----------
    for nome, idade, esperado in [
        ("Ana", 30, "Olá, Ana! Você tem 30 anos."),
        ("José", 7, "Olá, José! Você tem 7 anos."),
        ("bia", 18, "Olá, bia! Você tem 18 anos."),
        ("Carol", 100, "Olá, Carol! Você tem 100 anos."),
    ]:
        valor, erro = tentar(frase, nome, idade)
        check(
            f"frase({nome!r}, {idade}) → {esperado!r}",
            erro is None and valor == esperado,
        )

    if falhas:
        print(f"\n  🔴 {falhas} verificação(ões) falhou(aram). Corrija e rode de novo.\n")
        sys.exit(1)
    print("\n  🎉 Tudo verde! Marque o checkbox no README e siga em frente.\n")
