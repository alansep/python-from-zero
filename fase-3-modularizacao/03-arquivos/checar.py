"""
checar.py — validação automática da Atividade 03.
Você não precisa editar este arquivo (mas pode ler — é só Python 😉).
Todos os arquivos de teste são criados numa pasta TEMPORÁRIA do sistema:
nada é gravado no repositório.
"""

import csv
import json
import sys
import tempfile
from pathlib import Path


def validar(
    *,
    escrever_txt,
    ler_txt,
    contar_linhas,
    existe,
    juntar_caminho,
    salvar_json,
    carregar_json,
    salvar_csv,
    ler_csv,
):
    print("\n── Atividade 03 · Manipulação de Arquivos ──")
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

    def ler_de_disco(caminho):
        try:
            with open(caminho, encoding="utf-8") as arquivo:
                return arquivo.read()
        except OSError:
            return None

    def criar_csv(caminho, linhas):
        with open(caminho, "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            for linha in linhas:
                escritor.writerow(linha)

    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)

        # ---------- Exercício 1 — escrever_txt ----------
        caminho = base / "saida.txt"
        texto = "linha 1\nlinha 2\n"
        tentar(escrever_txt, str(caminho), texto)
        valor, erro = tentar(ler_de_disco, caminho)
        check("escrever_txt grava o texto exato (com as quebras de linha)",
              erro is None and valor == texto)

        caminho_acento = base / "acento.txt"
        texto_acento = "São João — coração ção ê\n"
        tentar(escrever_txt, str(caminho_acento), texto_acento)
        valor, erro = tentar(ler_de_disco, caminho_acento)
        check("escrever_txt preserva acentos (encoding utf-8)",
              erro is None and valor == texto_acento)

        tentar(escrever_txt, str(caminho), "primeira versão")
        tentar(escrever_txt, str(caminho), "segunda versão")
        valor, erro = tentar(ler_de_disco, caminho)
        check("escrever_txt sobrescreve o que já existia ('w')",
              erro is None and valor == "segunda versão")

        # ---------- Exercício 2 — ler_txt ----------
        caminho_leia = base / "leia.txt"
        tentar(caminho_leia.write_text("a\nção\n", encoding="utf-8"))
        valor, erro = tentar(ler_txt, str(caminho_leia))
        check("ler_txt devolve o conteúdo completo (com acento)",
              erro is None and valor == "a\nção\n")

        caminho_vazio = base / "vazio.txt"
        tentar(caminho_vazio.write_text("", encoding="utf-8"))
        valor, erro = tentar(ler_txt, str(caminho_vazio))
        check("ler_txt de arquivo vazio → ''", erro is None and valor == "")

        valor, erro = tentar(ler_txt, str(base / "nao_existe.txt"))
        check("ler_txt de arquivo inexistente → None", erro is None and valor is None)

        caminho_uma = base / "uma.txt"
        tentar(caminho_uma.write_text("sem quebra final", encoding="utf-8"))
        valor, erro = tentar(ler_txt, str(caminho_uma))
        check("ler_txt devolve linha sem quebra final direitinho",
              erro is None and valor == "sem quebra final")

        # ---------- Exercício 3 — contar_linhas ----------
        caminho_linhas = base / "linhas.txt"
        tentar(caminho_linhas.write_text("a\nb\n", encoding="utf-8"))
        valor, erro = tentar(contar_linhas, str(caminho_linhas))
        check("contar_linhas('a\\nb\\n') → 2", erro is None and valor == 2)

        caminho_um = base / "um.txt"
        tentar(caminho_um.write_text("sem quebra", encoding="utf-8"))
        valor, erro = tentar(contar_linhas, str(caminho_um))
        check("contar_linhas('sem quebra') → 1", erro is None and valor == 1)

        valor, erro = tentar(contar_linhas, str(caminho_vazio))
        check("contar_linhas de arquivo vazio → 0", erro is None and valor == 0)

        valor, erro = tentar(contar_linhas, str(base / "sumiu.txt"))
        check("contar_linhas de arquivo inexistente → None",
              erro is None and valor is None)

        cem = "".join(f"item {i}\n" for i in range(100))
        caminho_cem = base / "cem.txt"
        tentar(caminho_cem.write_text(cem, encoding="utf-8"))
        valor, erro = tentar(contar_linhas, str(caminho_cem))
        check("contar_linhas de 100 linhas → 100", erro is None and valor == 100)

        # ---------- Exercício 4 — existe (pathlib) ----------
        valor, erro = tentar(existe, str(caminho))
        check("existe() → True para arquivo gravado", erro is None and valor is True)

        valor, erro = tentar(existe, str(base / "fantasma.txt"))
        check("existe() → False para arquivo que nunca existiu",
              erro is None and valor is False)

        valor, erro = tentar(existe, str(base))
        check("existe() → True para uma pasta", erro is None and valor is True)

        # ---------- Exercício 5 — juntar_caminho ----------
        valor, erro = tentar(juntar_caminho, str(base), "notas.txt")
        check("juntar_caminho(base, 'notas.txt') monta base/notas.txt",
              erro is None and valor is not None
              and Path(valor) == base / "notas.txt")

        valor, erro = tentar(juntar_caminho, str(base) + "/", "a/b.txt")
        check("juntar_caminho ignora barra extra no fim do base",
              erro is None and valor is not None
              and Path(valor) == base / "a" / "b.txt")

        valor, erro = tentar(juntar_caminho, "dados", "2026/notas.txt")
        check("juntar_caminho('dados', '2026/notas.txt') → dados/2026/notas.txt",
              erro is None and valor is not None
              and Path(valor) == Path("dados/2026/notas.txt"))

        # ---------- Exercício 6 — JSON roundtrip ----------
        dados = {"nome": "José ção", "idade": 30, "ativo": True}
        caminho_json = base / "dados.json"
        tentar(salvar_json, str(caminho_json), dados)
        valor, erro = tentar(carregar_json, str(caminho_json))
        check("salvar_json + carregar_json fazem roundtrip (com acento)",
              erro is None and valor == dados)

        lista = [1, {"vazio": None, "n": 1.5}, [2, 3]]
        caminho_json2 = base / "lista.json"
        tentar(salvar_json, str(caminho_json2), lista)
        valor, erro = tentar(carregar_json, str(caminho_json2))
        check("salvar_json aceita lista aninhada e devolve igual",
              erro is None and valor == lista)

        valor, erro = tentar(carregar_json, str(base / "nao_existe.json"))
        check("carregar_json de arquivo inexistente → None",
              erro is None and valor is None)

        valor, erro = tentar(carregar_json, str(caminho_json))
        check("carregar_json devolve um dict para dict gravado",
              erro is None and isinstance(valor, dict))

        # ---------- Exercício 7 — CSV roundtrip ----------
        caminho_csv = base / "tabela.csv"
        tentar(criar_csv, caminho_csv, [["nome", "idade"], ["Ana", "30"]])
        valor, erro = tentar(ler_csv, str(caminho_csv))
        check("ler_csv devolve [['nome', 'idade'], ['Ana', '30']]",
              erro is None and valor == [["nome", "idade"], ["Ana", "30"]])

        caminho_aspas = base / "aspas.csv"
        tentar(criar_csv, caminho_aspas,
               [["nome", "cidade"], ["Silva, João", "Recife"]])
        valor, erro = tentar(ler_csv, str(caminho_aspas))
        check("ler_csv respeita campo entre aspas com vírgula dentro",
              erro is None and valor == [["nome", "cidade"], ["Silva, João", "Recife"]])

        caminho_csv_vazio = base / "tabela_vazia.csv"
        tentar(caminho_csv_vazio.write_text("", encoding="utf-8"))
        valor, erro = tentar(ler_csv, str(caminho_csv_vazio))
        check("ler_csv de arquivo vazio → []", erro is None and valor == [])

        linhas = [["produto", "preço"], ["café", "12,50"], ["açúcar", "4"]]
        caminho_rt = base / "roundtrip.csv"
        tentar(salvar_csv, str(caminho_rt), linhas)
        valor, erro = tentar(ler_csv, str(caminho_rt))
        check("salvar_csv + ler_csv fazem roundtrip (mesmas colunas)",
              erro is None and valor == linhas)

        caminho_rt2 = base / "roundtrip2.csv"
        tentar(salvar_csv, str(caminho_rt2), [])
        valor, erro = tentar(ler_csv, str(caminho_rt2))
        check("salvar_csv([]) gera arquivo que relê como []",
              erro is None and valor == [])

    if falhas:
        print(f"\n  🔴 {falhas} verificação(ões) falhou(aram). Corrija e rode de novo.\n")
        sys.exit(1)
    print("\n  🎉 Tudo verde! Marque o checkbox no README e siga em frente.\n")
