"""
checar.py — validação automática da Atividade 02.
Você não precisa editar este arquivo (mas pode ler — é só Python 😉).
"""

import sys


def validar(
    *,
    a,
    b,
    soma,
    divisao,
    divisao_inteira,
    resto,
    potencia,
    maior,
    igual,
    diferente,
    e_logico,
    ou_logico,
    nao_logico,
    expressao,
    divisivel_3_e_5,
):
    print("\n── Atividade 02 · Operadores ──")
    falhas = 0

    def check(descricao, ok):
        nonlocal falhas
        print(("  ✅ " if ok else "  ❌ ") + descricao)
        if not ok:
            falhas += 1

    # ---------- Exercício 1 — aritmética ----------
    check("soma = a + b", soma == a + b)
    check("divisao = a / b", divisao == a / b)
    check("divisao_inteira = a // b", divisao_inteira == a // b)
    check("resto = a % b", resto == a % b)
    check("potencia = a ** b", potencia == a ** b)

    # ---------- Exercício 2 — comparações e lógicos ----------
    check("maior → True (x > y)", maior is True)
    check("igual → False (x == y)", igual is False)
    check("diferente → True (x != y)", diferente is True)
    check("e_logico → False (10>5 and 4>5)", e_logico is False)
    check("ou_logico → True (10>5 or 4>5)", ou_logico is True)
    check("nao_logico → True (not x==y)", nao_logico is True)

    # ---------- Exercício 3 — precedência ----------
    check("expressão SEM parênteses resulta em 49", expressao == 49)

    # ---------- Exercício 4 — lógica combinada ----------
    check("45 é divisível por 3 e 5 → True", divisivel_3_e_5 is True)

    if falhas:
        print(f"\n  🔴 {falhas} verificação(ões) falhou(aram). Corrija e rode de novo.\n")
        sys.exit(1)
    print("\n  🎉 Tudo verde! Marque o checkbox no README e siga em frente.\n")
