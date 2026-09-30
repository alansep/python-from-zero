"""
checar.py — validação automática do Projeto 03 (Analisador de Logs).
Você não precisa editar este arquivo (mas pode ler — é só Python 😉).
Inclui casos-limite de propósito: é assim que se testa código de verdade.
A fixture logs_exemplo.txt é lida pelo caminho absoluto desta pasta.
"""

import os
import sys
import tempfile

FIXTURE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs_exemplo.txt")
TOTAL_LINHAS = 30
CONTAGENS_ESPERADAS = {"INFO": 12, "WARN": 7, "ERROR": 9}


def validar(*, ler_log, filtrar_por_nivel, contar_niveis, gerar_relatorio):
    print("\n── Atividade 03 · Analisador de Logs ──")
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

    def como_lista(valor):
        return valor if isinstance(valor, list) else []

    # ---------- Exercício 1 — ler_log ----------
    linhas, erro = tentar(ler_log, FIXTURE)
    check(
        "ler_log devolve uma lista de strings",
        erro is None
        and isinstance(linhas, list)
        and all(isinstance(linha, str) for linha in linhas),
    )
    check(
        f"ler_log leu as {TOTAL_LINHAS} linhas da fixture logs_exemplo.txt",
        erro is None and isinstance(linhas, list) and len(linhas) == TOTAL_LINHAS,
    )
    check(
        "nenhuma linha termina com \\n",
        erro is None
        and isinstance(linhas, list)
        and len(linhas) > 0
        and all(not linha.endswith("\n") for linha in linhas),
    )
    check(
        "primeira linha traz data, hora e nível INFO",
        erro is None
        and isinstance(linhas, list)
        and len(linhas) > 0
        and linhas[0].startswith("2026-09-29")
        and " INFO " in linhas[0],
    )

    with tempfile.TemporaryDirectory() as pasta:
        inexistente = os.path.join(pasta, "nao_existe.txt")
        obtido, erro = tentar(ler_log, inexistente)
        check(
            "ler_log devolve [] para arquivo inexistente",
            erro is None and obtido == [],
        )

        temporario = os.path.join(pasta, "curto.txt")
        with open(temporario, "w", encoding="utf-8") as arquivo:
            arquivo.write("linha um\nlinha dois\nlinha tres\n")
        obtido, erro = tentar(ler_log, temporario)
        check(
            "ler_log lê um arquivo pequeno linha a linha",
            erro is None
            and obtido == ["linha um", "linha dois", "linha tres"],
        )

    linhas = como_lista(linhas)

    # ---------- Exercício 2 — filtrar_por_nivel ----------
    for nivel, esperado in [
        ("INFO", CONTAGENS_ESPERADAS["INFO"]),
        ("WARN", CONTAGENS_ESPERADAS["WARN"]),
        ("ERROR", CONTAGENS_ESPERADAS["ERROR"]),
        ("error", CONTAGENS_ESPERADAS["ERROR"]),
        ("Info", CONTAGENS_ESPERADAS["INFO"]),
    ]:
        obtido, erro = tentar(filtrar_por_nivel, linhas, nivel)
        check(
            f"filtrar_por_nivel(linhas, '{nivel}') → {esperado} linha(s)",
            erro is None
            and isinstance(obtido, list)
            and len(obtido) == esperado,
        )

    obtido, erro = tentar(filtrar_por_nivel, linhas, "ERROR")
    filtradas = como_lista(obtido)
    check(
        "filtro devolve APENAS linhas cuja 3ª palavra é o nível pedido",
        erro is None
        and len(filtradas) > 0
        and all(len(l.split()) >= 3 and l.split()[2].upper() == "ERROR" for l in filtradas)
        and all(l in linhas for l in filtradas),
    )

    obtido, erro = tentar(filtrar_por_nivel, linhas, "DEBUG")
    check(
        "filtro devolve [] para nível que não é INFO/WARN/ERROR",
        erro is None and obtido == [],
    )
    obtido, erro = tentar(filtrar_por_nivel, [], "INFO")
    check("filtro devolve [] para lista vazia", erro is None and obtido == [])

    # ---------- Exercício 3 — contar_niveis ----------
    obtido, erro = tentar(contar_niveis, linhas)
    check(
        "contar_niveis zera a fixture em INFO=12, WARN=7, ERROR=9",
        erro is None and obtido == CONTAGENS_ESPERADAS,
    )
    obtido, erro = tentar(contar_niveis, [])
    check(
        "contar_niveis de lista vazia mantém as 3 chaves zeradas",
        erro is None and obtido == {"INFO": 0, "WARN": 0, "ERROR": 0},
    )
    obtido, erro = tentar(
        contar_niveis,
        ["servidor reiniciado", "a b c", "", "2026-09-29 08:00:00 INFO ok"],
    )
    check(
        "contar_niveis ignora linhas malformadas e ainda conta o INFO",
        erro is None and obtido == {"INFO": 1, "WARN": 0, "ERROR": 0},
    )
    obtido, erro = tentar(
        contar_niveis,
        [
            "2026-09-29 10:00:00 info tudo certo",
            "2026-09-29 10:00:01 warn quase cheio",
            "2026-09-29 10:00:02 error falhou",
        ],
    )
    check(
        "contar_niveis aceita níveis em minúsculas",
        erro is None and obtido == {"INFO": 1, "WARN": 1, "ERROR": 1},
    )

    # ---------- Exercício 4 — gerar_relatorio ----------
    obtido, erro = tentar(gerar_relatorio, CONTAGENS_ESPERADAS)
    relatorio = "" if erro else str(obtido)
    check(
        "relatório traz a contagem de cada nível",
        erro is None
        and "INFO: 12" in relatorio
        and "WARN: 7" in relatorio
        and "ERROR: 9" in relatorio,
    )

    linhas_relatorio = [linha for linha in relatorio.splitlines() if linha.strip()]
    check(
        "relatório tem exatamente 3 linhas (uma por nível)",
        erro is None and len(linhas_relatorio) == 3,
    )
    check(
        "relatório segue a ordem fixa INFO, WARN, ERROR",
        erro is None
        and len(linhas_relatorio) == 3
        and linhas_relatorio[0].startswith("INFO")
        and linhas_relatorio[1].startswith("WARN")
        and linhas_relatorio[2].startswith("ERROR"),
    )

    obtido, erro = tentar(gerar_relatorio, {"INFO": 3})
    relatorio = "" if erro else str(obtido)
    check(
        "relatório trata chave ausente como 0",
        erro is None
        and "INFO: 3" in relatorio
        and "WARN: 0" in relatorio
        and "ERROR: 0" in relatorio,
    )

    if falhas:
        print(f"\n  🔴 {falhas} verificação(ões) falhou(aram). Corrija e rode de novo.\n")
        sys.exit(1)
    print("\n  🎉 Tudo verde! Marque o checkbox no README e siga em frente.\n")
