"""
checar.py — validação automática da Atividade 01.
Você não precisa editar este arquivo (mas pode ler — é só Python 😉).
Inclui casos-limite de propósito: é assim que se testa código de verdade.
"""

import sys


def validar(*, saudacao, min_max, dobrar, contar_pares, acumular):
    print("\n── Atividade 01 · Funções e Escopo ──")
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

    def contador_de_modulo():
        modulo = sys.modules.get("__main__")
        return getattr(modulo, "contador", "ausente")

    # ---------- Exercício 1 — saudação ----------
    for descricao, chamada, esperado in [
        ("saudacao('Ana')", lambda: tentar(saudacao, "Ana"), "Olá, Ana!"),
        ("saudacao('Ana', 'Bom dia')", lambda: tentar(saudacao, "Ana", "Bom dia"), "Bom dia, Ana!"),
        ("saudacao('Ana', cumprimento='Oi')",
         lambda: tentar(saudacao, "Ana", cumprimento="Oi"), "Oi, Ana!"),
        ("saudacao('José da Silva', 'Bem-vindo')",
         lambda: tentar(saudacao, "José da Silva", "Bem-vindo"), "Bem-vindo, José da Silva!"),
    ]:
        valor, erro = chamada()
        check(f"{descricao} → '{esperado}'", erro is None and valor == esperado)

    # ---------- Exercício 2 — min_max ----------
    for entrada, esperado in [
        ([4, 7, 1, 9], (1, 9)),
        ([5], (5, 5)),
        ([-3, -10, 0], (-10, 0)),
        ([2.5, 2.5], (2.5, 2.5)),
        ([], None),
    ]:
        valor, erro = tentar(min_max, entrada)
        check(f"min_max({entrada}) → {esperado}", erro is None and valor == esperado)

    # ---------- Exercício 3 — dobrar (função pura) ----------
    original = [1, 2, 3]
    valor, erro = tentar(dobrar, original)
    check("dobrar([1, 2, 3]) → [2, 4, 6]", erro is None and valor == [2, 4, 6])
    check("dobrar devolve uma NOVA lista",
          erro is None and isinstance(valor, list) and valor is not original)
    check("a lista original continua intacta",
          erro is None and isinstance(valor, list) and original == [1, 2, 3])

    valor, erro = tentar(dobrar, [-2, 0.5])
    check("dobrar([-2, 0.5]) → [-4, 1.0]", erro is None and valor == [-4, 1.0])

    valor, erro = tentar(dobrar, [])
    check("dobrar([]) → []", erro is None and valor == [])

    # ---------- Exercício 4 — contar_pares com docstring ----------
    doc = getattr(contar_pares, "__doc__", None)
    check("contar_pares tem docstring (>= 5 caracteres)",
          isinstance(doc, str) and len(doc.strip()) >= 5)

    for entrada, esperado in [
        ([1, 2, 3, 4], 2),
        ([0, -2, 7, 9, 10], 3),
        ([], 0),
    ]:
        valor, erro = tentar(contar_pares, entrada)
        check(f"contar_pares({entrada}) → {esperado}", erro is None and valor == esperado)

    # ---------- Exercício 5 — escopo local (contador global intacto) ----------
    antes = contador_de_modulo()
    executou = False
    for entrada, esperado in [
        ([1, 2, 3], 6),
        ([], 0),
        ([-5, 5, 10], 10),
    ]:
        valor, erro = tentar(acumular, entrada)
        depois = contador_de_modulo()
        if erro is None and valor is not None:
            executou = True
        check(
            f"acumular({entrada}) → {esperado} e `contador` global intacto",
            erro is None and valor == esperado and antes == depois == 0,
        )

    check("a variável de módulo `contador` seguiu valendo 0 após somas de verdade",
          executou and contador_de_modulo() == 0)

    if falhas:
        print(f"\n  🔴 {falhas} verificação(ões) falhou(aram). Corrija e rode de novo.\n")
        sys.exit(1)
    print("\n  🎉 Tudo verde! Marque o checkbox no README e siga em frente.\n")
