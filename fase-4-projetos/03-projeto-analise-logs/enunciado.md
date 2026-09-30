# 03 — Analisador de Logs ⏱️ ~6h

**Meta:** ler um arquivo de texto do disco, filtrar o que interessa e devolver um relatório formatado — o dia a dia de quem investiga um sistema em produção.

---

## 📚 Contexto

O **Banco do Terminal** está no ar e, de manhã, o suporte recebeu a reclamação clássica: *"o sistema caiu ontem à noite"*. Ninguém sabe quando, nem quantas vezes. A resposta está num arquivo: o **log** — um `.txt` em que cada linha é um evento com **data, hora, nível e mensagem**.

```text
2026-09-29 08:04:10 ERROR timeout ao chamar o serviço de pagamento
2026-09-29 08:04:15 INFO pagamento do pedido 1001 aprovado
```

Você vai construir o **analisador** que o time de suporte usaria: ler o arquivo inteiro, separar os eventos por nível (`INFO` = rotina, `WARN` = alerta, `ERROR` = problema) e emitir um relatório com a contagem de cada um.

Por que isso é bom treino? Porque é o projeto com **mais partes móveis**: disco (`ler_log`), texto (`split`, comparação *case-insensitive*), agregação (contador num dicionário com todas as chaves presentes) e apresentação (f-string numa string multilinha). E nada de `input()` — o menu `meu_relatorio.py` é o desafio final que você cria.

A pasta traz uma fixture versionada: [`logs_exemplo.txt`](./logs_exemplo.txt). Ele é **material de estudo** — 30 linhas fixas com uma mistura estável de níveis e duas linhas propositalmente fora do formato.

---

## 📋 Especificação

> 🔑 **Contrato geral:** a *nível* de uma linha é a **3ª palavra** (separada por espaços). Comparação **sem diferenciar maiúsculas de minúsculas** (`error` = `ERROR`). Linhas com menos de 3 palavras ou cuja 3ª palavra não seja `INFO`, `WARN` ou `ERROR` **são ignoradas** em contagens e filtros.

### Função 1 — `ler_log(caminho)`

- **ENTRADA:** `caminho` (string) de um arquivo `.txt`.
- **SAÍDA:** **lista de linhas**, cada uma **sem** o `\n` do fim; linhas em branco são descartadas. Se o arquivo **não existe** → `[]` (sem exceção escapando).

### Função 2 — `filtrar_por_nivel(linhas, nivel)`

- **ENTRADA:** `lista de linhas` (saída de `ler_log`) e `nivel` (`"INFO"`, `"WARN"` ou `"ERROR"`, em qualquer combinação de maiúsculas).
- **SAÍDA:** lista contendo **apenas** as linhas cuja 3ª palavra é `nivel` (comparação *case-insensitive*).
- Se `nivel` não for um dos três níveis válidos → `[]`. Lista vazia → `[]`.

### Função 3 — `contar_niveis(linhas)`

- **ENTRADA:** lista de linhas.
- **SAÍDA:** dicionário **com as três chaves sempre presentes**, inclusive zeradas:

```python
{"INFO": 12, "WARN": 7, "ERROR": 9}
```

- Linhas malformadas (menos de 3 palavras, ou 3ª palavra que não é nível) **não** entram na conta — mas as chaves continuam lá com `0`.

### Função 4 — `gerar_relatorio(contagens)`

- **ENTRADA:** dicionário de contagens (pode estar incompleto — chave ausente vale `0`).
- **SAÍDA:** string com **uma linha por nível, nesta ordem fixa** `INFO`, `WARN`, `ERROR`:

```text
INFO: 12
WARN: 7
ERROR: 9
```

- Formato de cada linha: `NÍVEL: quantidade`. Três linhas no total.

---

## ✍️ Exercícios

Abra [`atividade.py`](./atividade.py) — são 4 exercícios, um por função:

1. **`ler_log(caminho)`** — leitura de arquivo com `with`, devolvendo a lista de linhas.
2. **`filtrar_por_nivel(linhas, nivel)`** — filtro com comparação *case-insensitive* pela 3ª palavra.
3. **`contar_niveis(linhas)`** — agregação num dicionário que **nunca** pode faltar chave.
4. **`gerar_relatorio(contagens)`** — saída formatada com f-string e ordem fixa.

```bash
python3 fase-4-projetos/03-projeto-analise-logs/atividade.py
```

> 📌 A validação lê a fixture `logs_exemplo.txt` **pelo caminho absoluto** ao lado do `checar.py` — por isso o arquivo deve continuar nesta pasta. Os contadores esperados dela são: **12 INFO, 7 WARN, 9 ERROR** (30 linhas no total, sendo 2 fora do formato).

---

## 💡 Dicas (progressivas — sem gabarito)

**Exercício 1 — `ler_log`**
1. `open` dentro de `with` devolve um objeto em que você pode fazer um `for` — cada volta é uma linha.
2. Cada linha vem com `\n` no fim: `rstrip()` ou `strip()` resolvem (o `strip` também mata espaços sobrando).
3. Para o caso "arquivo não existe", envolva a leitura em `try/except` e devolva a lista vazia no `except` — ou confira `os.path.exists` antes (lembre do `import os`).

**Exercício 2 — `filtrar_por_nivel`**
1. Antes de olhar as linhas, confira o argumento: `nivel` só pode ser um dos três — com `nivel.upper()` a comparação ignora maiúsculas.
2. O nível está na 3ª palavra: `linha.split()` gera a lista de palavras e a posição começa em `0`.
3. Conserte as duas pontas: `palavras[2].upper() == nivel.upper()` **e** `len(palavras) >= 3` (senão a linha malformada quebra tudo).

**Exercício 3 — `contar_niveis`**
1. Um dicionário que **precisa ter três chaves mesmo vazias** é melhor criado **antes** do laço, já com zeros, do que montado no fim.
2. Você vai repetir a mesma pergunta da função anterior — a mesma checagem de 3 palavras vale aqui.
3. `contagens[nivel] += 1` só funciona se a chave já existir: é por isso que o dicionário começa completo.

**Exercício 4 — `gerar_relatorio`**
1. A ordem é fixa, então nem precisa de `for`: são três linhas montadas na mão com f-string.
2. Falta de chave num dicionário lança exceção; `contagens.get("INFO", 0)` devolve o valor **ou** zero.
3. Junte as três linhas com `"\n".join([...])` — ou concatene com `\n` — e lembre de que o relatório de uma contagem vazia também tem três linhas (todas `0`).

---

## 🎮 Desafio final: menu interativo

Crie **do zero** o arquivo `meu_relatorio.py` nesta pasta (a validação **não** cobre ele):

```bash
python3 fase-4-projetos/03-projeto-analise-logs/meu_relatorio.py
```

Requisitos:

1. `import` das funções do `atividade.py` (estão na mesma pasta).
2. Menu com `while True`: `1) Gerar relatório  2) Filtrar por nível  3) Mostrar linhas de erro  4) Sair`.
3. Caminho do log fixo em `logs_exemplo.txt` (ou lido com `input()`), sempre resolvido com `os.path.join(os.path.dirname(__file__), ...)` para funcionar de qualquer pasta.
4. Opção 1: `ler_log` → `contar_niveis` → `print(gerar_relatorio(...))`.
5. Opção 2: peça o nível com `input()`, chame `filtrar_por_nivel` e imprima cada linha; avise "nenhuma linha" quando a lista vier vazia.
6. **Arquivos gerados:** crie a pasta `dados/` com `os.makedirs("dados", exist_ok=True)` e grave o relatório em `dados/relatorio.txt`.
7. Trate `EOFError`/`KeyboardInterrupt` para o programa encerrar educadamente.

---

## ✅ Checkpoint de aceitação

**Núcleo (validação automática)**

- [ ] `python3 fase-4-projetos/03-projeto-analise-logs/atividade.py` imprime só ✅ e termina com 🎉
- [ ] Nenhuma função do `atividade.py` chama `input()` ou `print()`
- [ ] `ler_log` devolve `[]` para arquivo inexistente (sem Traceback)
- [ ] `filtrar_por_nivel` encontra `error` escrito em minúsculo
- [ ] `contar_niveis` devolve **12 / 7 / 9** sobre a fixture e nunca deixa faltar chave
- [ ] Linhas fora do formato (`servidor reiniciado`, `--- aplicação reiniciada ---`) são ignoradas
- [ ] `gerar_relatorio` tem exatamente 3 linhas na ordem `INFO`, `WARN`, `ERROR`

**Desafio (manual)**

- [ ] `meu_relatorio.py` roda e imprime o relatório da fixture
- [ ] `dados/relatorio.txt` é criado pelo menu
- [ ] Todo `input()` está **fora** das funções validadas

- [ ] Tudo verde → marque o checkbox no [README raiz](../../README.md)
