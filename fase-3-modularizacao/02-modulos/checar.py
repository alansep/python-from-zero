"""
checar.py — validação automática da Atividade 02.
Você não precisa editar este arquivo (mas pode ler — é só Python 😉).
Inclui casos-limite de propósito: é assim que se testa código de verdade.
"""

import csv
import io
import json
import math
import sys
from datetime import date


def validar(*, raiz_de, teto, embaralhar, fim_de_semana, dias_entre, para_json, cabecalho):
    print("\n── Atividade 02 · Módulos e Importação ──")
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

    def mesma_lista(valor, original):
        if not isinstance(valor, list):
            return False
        try:
            return sorted(valor) == sorted(original)
        except Exception:
            return False

    # ---------- Exercício 1 — math.sqrt ----------
    valor, erro = tentar(raiz_de, 9)
    check("raiz_de(9) → 3.0 (float)",
          erro is None and isinstance(valor, float) and valor == 3.0)

    valor, erro = tentar(raiz_de, 0)
    check("raiz_de(0) → 0.0", erro is None and valor == 0.0)

    valor, erro = tentar(raiz_de, 2)
    check("raiz_de(2) → 1.41421356... (aprox. de math.sqrt(2))",
          erro is None and isinstance(valor, float)
          and abs(valor - math.sqrt(2)) < 1e-9)

    valor, erro = tentar(raiz_de, 16)
    check("raiz_de(16) → 4.0", erro is None and valor == 4.0)

    # ---------- Exercício 2 — math.ceil ----------
    for entrada, esperado in [(3.2, 4), (4, 4), (-3.2, -3), (-0.1, 0), (0, 0)]:
        valor, erro = tentar(teto, entrada)
        check(f"teto({entrada}) → {esperado}", erro is None and valor == esperado)

    # ---------- Exercício 3 — random (propriedades) ----------
    original = [1, 2, 3, 4, 5]
    valor, erro = tentar(embaralhar, original)
    check("embaralhar devolve uma lista",
          erro is None and isinstance(valor, list))
    check("embaralhar mantém os MESMOS elementos",
          erro is None and mesma_lista(valor, original))
    check("a lista original continua intacta",
          erro is None and isinstance(valor, list) and original == [1, 2, 3, 4, 5])

    original2 = ["a", "b", "c"]
    valor2, erro2 = tentar(embaralhar, original2)
    check("embaralhar(['a','b','c']) mantém os elementos",
          erro2 is None and mesma_lista(valor2, original2))
    check("a segunda original também continua intacta",
          erro2 is None and isinstance(valor2, list) and original2 == ["a", "b", "c"])

    # ---------- Exercício 4 — datetime.date.weekday ----------
    for ano, mes, dia, esperado in [
        (2026, 1, 1, False),    # quinta-feira
        (2026, 1, 3, True),     # sábado
        (2026, 1, 4, True),     # domingo
        (2026, 12, 31, False),  # quinta-feira
        (2026, 6, 14, True),    # domingo
    ]:
        valor, erro = tentar(fim_de_semana, ano, mes, dia)
        check(
            f"fim_de_semana({ano}, {mes}, {dia}) → {esperado}",
            erro is None and valor is esperado,
        )

    # ---------- Exercício 5 — timedelta ----------
    for a, b, esperado in [
        (date(2026, 1, 1), date(2026, 1, 31), 30),
        (date(2026, 2, 1), date(2026, 3, 1), 28),   # 2026 não é bissexto
        (date(2026, 5, 5), date(2026, 5, 5), 0),
        (date(2026, 3, 1), date(2026, 2, 1), -28),  # sinal importa
    ]:
        valor, erro = tentar(dias_entre, a, b)
        check(f"dias_entre({a}, {b}) → {esperado}", erro is None and valor == esperado)

    # ---------- Exercício 6 — json roundtrip ----------
    for dados in [
        {"nome": "José", "idade": 30},
        [1, 2, {"a": True, "b": None}],
        {"cidade": "São Paulo", "nota": 9.75},
    ]:
        valor, erro = tentar(para_json, dados)
        volta, erro_load = tentar(json.loads, valor)
        check(
            f"para_json({dados}) faz roundtrip (json.loads volta igual)",
            erro is None and isinstance(valor, str) and erro_load is None and volta == dados,
        )

    # ---------- Exercício 7 — csv.reader + next ----------
    for texto, esperado in [
        ("nome,idade\nAna,30\n", ["nome", "idade"]),
        ('"nome, sobrenome",idade\n"Silva, João",30\n', ["nome, sobrenome", "idade"]),
        ("unica_coluna\nvalor\n", ["unica_coluna"]),
    ]:
        valor, erro = tentar(cabecalho, texto)
        check(
            f"cabecalho({texto.splitlines()[0]!r}) → {esperado}",
            erro is None and valor == esperado,
        )

    if falhas:
        print(f"\n  🔴 {falhas} verificação(ões) falhou(aram). Corrija e rode de novo.\n")
        sys.exit(1)
    print("\n  🎉 Tudo verde! Marque o checkbox no README e siga em frente.\n")
