"""
checar.py — validação automática da Atividade 01.
Você não precisa editar este arquivo (mas pode ler — é só Python 😉).
"""

import sys


def validar(*, usuario, idade, altura, esta_ativo, pedir_dados, apresentar):
    print("\n── Atividade 01 · Variáveis e Tipos de Dados ──")
    falhas = 0

    def check(descricao, ok):
        nonlocal falhas
        print(("  ✅ " if ok else "  ❌ ") + descricao)
        if not ok:
            falhas += 1

    # ---------- Exercício 1 — tipos primitivos ----------
    check("usuario é texto (str)", type(usuario) is str)
    check("idade é inteiro (int)", type(idade) is int)
    check("altura é decimal (float)", type(altura) is float)
    check("esta_ativo é booleano (bool)", type(esta_ativo) is bool)
    check("idade faz sentido (> 0)", type(idade) is int and idade > 0)
    check(
        "altura faz sentido (entre 0.5 e 2.5 m)",
        type(altura) is float and 0.5 <= altura <= 2.5,
    )

    # ---------- Exercício 2 — entrada + conversão (interativo) ----------
    print("\n  ✏️  Exercício 2: quando implementado, o terminal pedirá seus dados")
    try:
        nome, idade_convertida = pedir_dados()
        check("nome recebido é texto não vazio", type(nome) is str and nome.strip() != "")
        check("idade foi convertida para int", type(idade_convertida) is int)
        check(
            "idade convertida faz sentido (> 0)",
            type(idade_convertida) is int and idade_convertida > 0,
        )
    except Exception as erro:
        check(f"pedir_dados() falhou ({erro})", False)

    # ---------- Exercício 3 — montagem da frase ----------
    for nome_ex, idade_ex in (("Ana", 25), ("Léo", 7)):
        try:
            frase = apresentar(nome_ex, idade_ex)
            ok = (
                type(frase) is str
                and nome_ex in frase
                and str(idade_ex) in frase
                and "ano" in frase
            )
            check(f"apresentar('{nome_ex}', {idade_ex}) montou a frase", ok)
        except Exception as erro:
            check(f"apresentar('{nome_ex}', {idade_ex}) falhou ({erro})", False)

    _resumo(falhas)


def _resumo(falhas):
    if falhas:
        print(f"\n  🔴 {falhas} verificação(ões) falhou(aram). Corrija e rode de novo.\n")
        sys.exit(1)
    print("\n  🎉 Tudo verde! Marque o checkbox no README e siga em frente.\n")
