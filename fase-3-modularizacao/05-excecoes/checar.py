"""
checar.py — validação automática da Atividade 05.
Você não precisa editar este arquivo (mas pode ler — é só Python 😉).
Inclui casos-limite de propósito: é assim que se testa código de verdade.
"""

import sys


def validar(*, converter, dividir, processar, validar_idade, classificar):
    print("\n── Atividade 05 · Tratamento de Exceções ──")
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

    def levantou_value_error(erro, mensagem):
        return (
            erro is not None
            and isinstance(erro, ValueError)
            and mensagem in str(erro)
        )

    # ---------- Exercício 1 — converter ----------
    for texto, esperado in [
        ("42", 42),
        (" 7 ", 7),
        ("-5", -5),
        ("0", 0),
        ("abc", "valor inválido"),
        ("", "valor inválido"),
        ("3.5", "valor inválido"),
    ]:
        valor, erro = tentar(converter, texto)
        check(f"converter({texto!r}) → {esperado}", erro is None and valor == esperado)

    # ---------- Exercício 2 — dividir ----------
    for a, b, esperado in [
        (10, 2, 5),
        (9, 4, 2.25),
        (-6, 3, -2),
        (7, 0, "divisão por zero"),
        (0, 0, "divisão por zero"),
    ]:
        valor, erro = tentar(dividir, a, b)
        check(f"dividir({a}, {b}) → {esperado}", erro is None and valor == esperado)

    # ---------- Exercício 3 — finally ----------
    for valores, esperado in [
        (["1", "2", "3"], 3),
        (["a", None, "5"], 3),           # itens ruins não podem furar o contador
        ([], 0),
        (["1", "x"] * 25, 50),           # 50 itens, metade inválida
        (["0", " 12 ", "-3"], 3),          # espaços e negativos o int aceita
    ]:
        valor, erro = tentar(processar, valores)
        check(f"processar({valores}) → {esperado}", erro is None and valor == esperado)

    # ---------- Exercício 4 — raise ValueError ----------
    for idade, esperado in [(20, 20), (0, 0), (130, 130)]:
        valor, erro = tentar(validar_idade, idade)
        check(f"validar_idade({idade}) → {esperado}", erro is None and valor == esperado)

    for idade in [-1, 200, "20", 3.5]:
        valor, erro = tentar(validar_idade, idade)
        check(
            f"validar_idade({idade!r}) levanta ValueError('idade inválida')",
            levantou_value_error(erro, "idade inválida"),
        )

    # ---------- Exercício 5 — try / except / else ----------
    for texto, esperado in [
        ("4", "par"),
        ("7", "ímpar"),
        ("-2", "par"),
        (" 8 ", "par"),
        ("abc", "valor inválido"),
        ("", "valor inválido"),
    ]:
        valor, erro = tentar(classificar, texto)
        check(f"classificar({texto!r}) → '{esperado}'", erro is None and valor == esperado)

    if falhas:
        print(f"\n  🔴 {falhas} verificação(ões) falhou(aram). Corrija e rode de novo.\n")
        sys.exit(1)
    print("\n  🎉 Tudo verde! Marque o checkbox no README e siga em frente.\n")
