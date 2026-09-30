"""
checar.py — validação automática do Projeto 02 (Gerenciador de Cadastro).
Você não precisa editar este arquivo (mas pode ler — é só Python 😉).
Inclui casos-limite de propósito: é assim que se testa código de verdade.
Os arquivos dos testes são gravados numa pasta TEMPORÁRIA do sistema —
nada é criado dentro do repositório.
"""

import json
import os
import sys
import tempfile


def validar(
    *,
    cadastrar,
    buscar,
    atualizar,
    listar,
    salvar_json,
    carregar_json,
    exportar_csv,
):
    print("\n── Atividade 02 · Gerenciador de Cadastro ──")
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

    ANA = {"nome": "Ana Souza", "email": "ana@exemplo.com", "telefone": "999111222"}
    BRUNO = {"nome": "Bruno Lima", "email": "bruno@exemplo.com", "telefone": "988777666"}
    CPF_ANA = "11122233344"
    CPF_BRUNO = "55566677788"

    def base():
        return {CPF_ANA: dict(ANA)}

    def ler_texto(caminho):
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return arquivo.read()

    # ---------- Exercício 1 — cadastrar ----------
    clientes = {}
    obtido, erro = tentar(cadastrar, clientes, CPF_ANA, ANA)
    check("cadastrar devolve True para um CPF novo", erro is None and obtido is True)
    check(
        "cadastrar grava o CPF com os dados certos",
        clientes.get(CPF_ANA) == ANA,
    )

    clientes = base()
    obtido, erro = tentar(cadastrar, clientes, CPF_ANA, BRUNO)
    check(
        "cadastrar recusa CPF duplicado e NÃO sobrescreve os dados originais",
        erro is None and obtido is False and clientes.get(CPF_ANA) == ANA,
    )

    for rotulo, cpf, dados in [
        ("cpf vazio", "", ANA),
        ("cpf não-string", 12345678900, ANA),
        ("dados não-dict", CPF_BRUNO, "Ana Souza"),
        ("dados vazio", CPF_BRUNO, {}),
        ("dados sem 'telefone'", CPF_BRUNO, {"nome": "Ana", "email": "a@x.com"}),
    ]:
        clientes = base()
        obtido, erro = tentar(cadastrar, clientes, cpf, dados)
        check(
            f"cadastrar recusa entrada inválida ({rotulo})",
            erro is None and obtido is False and clientes == base(),
        )

    # ---------- Exercício 2 — buscar ----------
    clientes = {CPF_ANA: ANA, CPF_BRUNO: BRUNO}
    obtido, erro = tentar(buscar, clientes, CPF_BRUNO)
    check("buscar devolve os dados do CPF encontrado", erro is None and obtido == BRUNO)
    obtido, erro = tentar(buscar, clientes, "00000000000")
    check("buscar devolve None para CPF inexistente", erro is None and obtido is None)
    obtido, erro = tentar(buscar, {}, CPF_ANA)
    check("buscar devolve None num cadastro vazio", erro is None and obtido is None)

    # ---------- Exercício 3 — atualizar ----------
    clientes = base()
    obtido, erro = tentar(atualizar, clientes, CPF_ANA, {"telefone": "911111111"})
    check("atualizar devolve True para CPF existente", erro is None and obtido is True)
    check(
        "atualizar faz fusão: muda o informado e PRESERVA o resto",
        clientes.get(CPF_ANA)
        == {"nome": "Ana Souza", "email": "ana@exemplo.com", "telefone": "911111111"},
    )

    clientes = base()
    obtido, erro = tentar(atualizar, clientes, "99999999999", {"nome": "Intruso"})
    check(
        "atualizar devolve False para CPF inexistente",
        erro is None and obtido is False and clientes == base(),
    )
    obtido, erro = tentar(atualizar, clientes, CPF_ANA, {})
    check(
        "atualizar devolve False com dicionário vazio",
        erro is None and obtido is False,
    )
    obtido, erro = tentar(atualizar, clientes, CPF_ANA, "nome=Ana")
    check(
        "atualizar devolve False com dados que não são dict",
        erro is None and obtido is False,
    )

    # ---------- Exercício 4 — listar ----------
    obtido, erro = tentar(listar, {})
    check("listar devolve [] num cadastro vazio", erro is None and obtido == [])
    obtido, erro = tentar(listar, {CPF_ANA: ANA})
    check("listar devolve a lista com o CPF", erro is None and obtido == [CPF_ANA])
    obtido, erro = tentar(listar, {CPF_ANA: ANA, CPF_BRUNO: BRUNO})
    check(
        "listar mantém a ORDEM de cadastro",
        erro is None and obtido == [CPF_ANA, CPF_BRUNO],
    )
    obtido, erro = tentar(listar, {CPF_BRUNO: BRUNO, CPF_ANA: ANA})
    check(
        "listar respeita a ordem em que os dados foram inseridos",
        erro is None and obtido == [CPF_BRUNO, CPF_ANA],
    )

    # ---------- Exercícios 5 e 6 — JSON ----------
    dados_json = {CPF_ANA: ANA, CPF_BRUNO: BRUNO}
    with tempfile.TemporaryDirectory() as pasta:
        caminho = os.path.join(pasta, "clientes.json")

        obtido, erro = tentar(salvar_json, caminho, dados_json)
        check("salvar_json devolve True quando grava", erro is None and obtido is True)
        existe = os.path.isfile(caminho)
        check("salvar_json criou o arquivo", existe)
        conteudo = None
        if existe:
            try:
                conteudo = json.loads(ler_texto(caminho))
            except Exception:
                conteudo = None
        check(
            "arquivo .json escrito é válido e idêntico aos dados",
            conteudo == dados_json,
        )

        obtido, erro = tentar(carregar_json, caminho)
        check(
            "carregar_json devolve exatamente o que foi gravado (roundtrip)",
            erro is None and obtido == dados_json,
        )

        obtido, erro = tentar(carregar_json, os.path.join(pasta, "nao_existe.json"))
        check(
            "carregar_json devolve {} para arquivo inexistente",
            erro is None and obtido == {},
        )

        quebrado = os.path.join(pasta, "quebrado.json")
        with open(quebrado, "w", encoding="utf-8") as arquivo:
            arquivo.write('{"nome": "Ana", ')
        obtido, erro = tentar(carregar_json, quebrado)
        check(
            "carregar_json devolve {} para JSON corrompido",
            erro is None and obtido == {},
        )

        lista = os.path.join(pasta, "lista.json")
        with open(lista, "w", encoding="utf-8") as arquivo:
            arquivo.write('["Ana", "Bruno"]')
        obtido, erro = tentar(carregar_json, lista)
        check(
            "carregar_json devolve {} quando o JSON não é um dicionário",
            erro is None and obtido == {},
        )

        inexistente = os.path.join(pasta, "pasta_que_nao_existe", "clientes.json")
        obtido, erro = tentar(salvar_json, inexistente, dados_json)
        check(
            "salvar_json devolve False e não grava se o diretório não existe",
            erro is None
            and obtido is False
            and not os.path.exists(inexistente),
        )

        # ---------- Exercício 7 — exportar CSV ----------
        caminho_csv = os.path.join(pasta, "clientes.csv")
        clientes_csv = {CPF_ANA: ANA, CPF_BRUNO: BRUNO}
        obtido, erro = tentar(exportar_csv, caminho_csv, clientes_csv)
        check("exportar_csv devolve True quando grava", erro is None and obtido is True)

        linhas = []
        if os.path.isfile(caminho_csv):
            linhas = [linha.strip() for linha in ler_texto(caminho_csv).splitlines()]
            linhas = [linha for linha in linhas if linha]
        check(
            "CSV começa com o cabeçalho exato 'cpf,nome,email,telefone'",
            bool(linhas) and linhas[0] == "cpf,nome,email,telefone",
        )
        check(
            "CSV tem 1 cabeçalho + 1 linha por cliente (3 no total)",
            len(linhas) == 1 + len(clientes_csv),
        )
        check(
            "CSV traz os dados de cada cliente na ordem de listar",
            len(linhas) == 1 + len(clientes_csv)
            and linhas[1].startswith(CPF_ANA)
            and "Ana Souza" in linhas[1]
            and linhas[2].startswith(CPF_BRUNO)
            and "Bruno Lima" in linhas[2],
        )

        vazio_csv = os.path.join(pasta, "vazio.csv")
        obtido, erro = tentar(exportar_csv, vazio_csv, {})
        check(
            "exportar_csv devolve False e não cria arquivo com cadastro vazio",
            erro is None and obtido is False and not os.path.exists(vazio_csv),
        )

        caminho_ruim = os.path.join(pasta, "pasta_que_nao_existe", "clientes.csv")
        obtido, erro = tentar(exportar_csv, caminho_ruim, clientes_csv)
        check(
            "exportar_csv devolve False se o diretório não existe",
            erro is None and obtido is False,
        )

    if falhas:
        print(f"\n  🔴 {falhas} verificação(ões) falhou(aram). Corrija e rode de novo.\n")
        sys.exit(1)
    print("\n  🎉 Tudo verde! Marque o checkbox no README e siga em frente.\n")
