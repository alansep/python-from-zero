# 02 — Gerenciador de Cadastro ⏱️ ~6h

**Meta:** manipular dados estruturados com dicionários **e** persistir em disco (`.json` e `.csv`) sem perder nada pelo caminho.

---

## 📚 Contexto

O **Banco do Terminal** gostou do simulador bancário e te chamou de volta: agora o pedido é um **cadastro de clientes** que sobreviva ao reinício do computador. Enquanto o projeto 01 vivia só na memória (fechou o terminal, acabou), aqui os dados precisam **virar arquivo** — é o que separa um exercício de um sistema de verdade.

Você vai construir a camada de dados de um sistema de inscrições:

- **dicionários** guardam cada cliente (`clientes[cpf] = {"nome": ..., "email": ..., "telefone": ...}`);
- **`.json`** é o formato de *backup*: guardo tudo, leio tudo de volta, nada se perde;
- **`.csv`** é o formato de *planilha*: o Rh abre no Excel e precisa de **cabeçalho**;
- **nada de `input()`** nas funções validadas — o menu `meu_cadastro.py` é o desafio final que você cria sozinho.

O grande risco de um cadastro é **dado duplicado** (mesmo CPF dois vezes, a segunda sobrescrevendo a primeira) e **dado perdido** (gravou JSON errado e o backup não abre). A validação ataca exatamente esses dois pontos.

---

## 📋 Especificação

> 🔑 **Contrato geral:** `clientes` é sempre um dicionário `{cpf: dados}`, onde `cpf` é uma **string** e `dados` é `{"nome": ..., "email": ..., "telefone": ...}`. A validação compara retornos de forma estrita — siga os valores exatos abaixo.

### Função 1 — `cadastrar(clientes, cpf, dados)`

- **ENTRADA:** `clientes` (dicionário), `cpf` (string), `dados` (dicionário).
- **SAÍDA:** `True` se cadastrou; `False` em **qualquer** destes casos, **sem alterar** `clientes`:
  1. `cpf` **já existe** em `clientes` (duplicado — a segunda tentativa **não** sobrescreve);
  2. `cpf` não é string ou é string vazia (`""`);
  3. `dados` não é dicionário, é dicionário **vazio** ou **não tem** as chaves `nome`, `email` e `telefone`.

### Função 2 — `buscar(clientes, cpf)`

- **ENTRADA:** `clientes`, `cpf`.
- **SAÍDA:** os `dados` daquele CPF, ou `None` se não existir (incluindo busca num dicionário vazio `{}`).

### Função 3 — `atualizar(clientes, cpf, novos_dados)`

- **ENTRADA:** `clientes`, `cpf`, `novos_dados` (dicionário com **pelo menos uma** chave).
- **SAÍDA:** `True` se atualizou; `False` se `cpf` não existe, ou se `novos_dados` não é dicionário ou é vazio.
- Comportamento: **fusão** (*merge*) — as chaves de `novos_dados` são gravadas por cima e as chaves antigas **não informadas são preservadas**.

### Função 4 — `listar(clientes)`

- **ENTRADA:** `clientes`.
- **SAÍDA:** lista de CPFs **na ordem em que foram cadastrados** (vazio → `[]`).

### Função 5 — `salvar_json(caminho, dados)`

- **ENTRADA:** `caminho` (string) e `dados` (dicionário).
- **SAÍDA:** `True` se gravou o arquivo; `False` se o **diretório** do caminho não existe (use `try/except` — não deixe o programa explodir).

### Função 6 — `carregar_json(caminho)`

- **ENTRADA:** `caminho`.
- **SAÍDA:** o dicionário gravado; **`{}`** quando:
  1. o arquivo **não existe**;
  2. o conteúdo **não é JSON válido** (arquivo corrompido);
  3. o conteúdo é JSON válido mas **não é um dicionário** (ex.: uma lista).

### Função 7 — `exportar_csv(caminho, clientes)`

- **ENTRADA:** `caminho`, `clientes`.
- **SAÍDA:** `True` se gravou; `False` se `clientes` for `{}` (não grava nada) ou se o diretório não existe.
- Formato do arquivo, **exato**:
  - 1ª linha (cabeçalho): `cpf,nome,email,telefone`
  - depois, uma linha por cliente, **na ordem de `listar`**.

---

## ✍️ Exercícios

Abra [`atividade.py`](./atividade.py) — são 7 exercícios, um por função:

1. **`cadastrar(...)`** — grava só quem é novo; recusa duplicado, CPF vazio e dados incompletos.
2. **`buscar(...)`** — devolve os dados ou `None`.
3. **`atualizar(...)`** — fusão parcial: atualiza o que foi pedido, preserva o resto.
4. **`listar(...)`** — CPFs na ordem de cadastro.
5. **`salvar_json(...)`** — grava o backup e devolve `True`/`False`.
6. **`carregar_json(...)`** — lê o backup e devolve `{}` em qualquer desastre.
7. **`exportar_csv(...)`** — gera a planilha com cabeçalho.

```bash
python3 fase-4-projetos/02-projeto-cadastro/atividade.py
```

> 📌 A validação usa pastas temporárias do sistema para os arquivos — nada é gravado dentro do repositório. Seus `check` de JSON fazem *roundtrip* (gravar → ler → comparar byte a byte com o original).

---

## 💡 Dicas (progressivas — sem gabarito)

**Exercício 1 — `cadastrar`**
1. São **três recusas** antes da gravação: teste cada uma e devolva `False` logo; só no fim devolva `True`.
2. "A chave já existe num dicionário" é uma pergunta que o próprio dicionário responde com `in`.
3. Para garantir as três chaves sem aninhar `if`: `all(chave in dados for chave in ("nome", "email", "telefone"))` — mas lembre de também exigir que `dados` **seja** dict.

**Exercício 2 — `buscar`**
1. Um único método do dicionário devolve o valor **ou** um padrão quando a chave não existe — e ele nem precisa saber se a chave está lá.
2. `clientes.get(cpf)` já é quase tudo; só confirme que o padrão é `None`.

**Exercício 3 — `atualizar`**
1. Primeiro recuse (CPF inexistente / dicionário vazio), depois **una**.
2. O método de *merge* de dicionários **modifica** o dicionário de destino no lugar — ele não devolve um novo.
3. `clientes[cpf].update(novos_dados)` preserva as chaves antigas automaticamente: só as informadas são sobrescritas.

**Exercício 4 — `listar`**
1. Você já tem o dicionário certo — falta extrair só uma das duas metades de cada par chave-valor.
2. `list(...)` sobre um dicionário devolve as **chaves**; a ordem delas é a de inserção no Python 3.7+.

**Exercício 5 — `salvar_json`**
1. `json.dump` **grava** (diferente de `json.dumps`, que só **converte** em texto).
2. Abra com `open(caminho, "w", encoding="utf-8")` dentro de um `with`.
3. Coloque a gravação inteira em `try:` e devolva `False` no `except` — assim diretório inexistente vira resposta, não crash.

**Exercício 6 — `carregar_json`**
1. Mesma estratégia do exercício anterior: `try` envolvendo a leitura, `except` devolvendo o dicionário vazio.
2. Depois de ler, confira **dois** pontos: deu certo? e o que veio é mesmo um `dict`?
3. `isinstance(conteudo, dict)` cobre o terceiro desastre (um JSON que é lista).

**Exercício 7 — `exportar_csv`**
1. O `csv` do Python tem duas funções com nomes parecidos: uma grava **linhas** (`writerow`) e outra **várias** de uma vez (`writerows`).
2. Três passos: abre no modo texto com `encoding="utf-8"`, escreve o cabeçalho fixo, depois varre `listar(clientes)` montando cada linha a partir de `clientes[cpf]`.
3. Faça as recusas (`{}` vazio, diretório inexistente) **antes** de abrir o arquivo — assim nada é criado em vão.

---

## 🎮 Desafio final: menu interativo

Crie **do zero** o arquivo `meu_cadastro.py` nesta pasta (a validação **não** cobre ele):

```bash
python3 fase-4-projetos/02-projeto-cadastro/meu_cadastro.py
```

Requisitos:

1. `import` das funções do `atividade.py` (estão na mesma pasta).
2. Ao iniciar, tente `carregar_json("dados/clientes.json")` — se voltar `{}`, comece do zero. Assim o cadastro **sobrevive** ao reinício.
3. Laço `while True` com menu: `1) Cadastrar  2) Buscar  3) Atualizar  4) Listar  5) Exportar CSV  6) Salvar e sair`.
4. `input()` **só** aqui: monte o `dados = {"nome": ..., "email": ..., "telefone": ...}` com as leituras do teclado e mande para `cadastrar(...)`.
5. Imprima a mensagem de retorno (`True`/`False`) para o usuário — sem enfeitar.
6. **Arquivos gerados:** crie a pasta `dados/` com `os.makedirs("dados", exist_ok=True)` e grave em `dados/clientes.json` (opção 6) e `dados/clientes.csv` (opção 5).
7. Trate `ValueError`/`EOFError` no `input` com `try/except` para o menu não quebrar.

---

## ✅ Checkpoint de aceitação

**Núcleo (validação automática)**

- [ ] `python3 fase-4-projetos/02-projeto-cadastro/atividade.py` imprime só ✅ e termina com 🎉
- [ ] CPF duplicado devolve `False` e **não** sobrescreve os dados originais
- [ ] `buscar` devolve `None` para CPF inexistente
- [ ] `atualizar` preserva chaves não informadas (fusão parcial)
- [ ] `listar` mantém a ordem de cadastro
- [ ] Gravar → ler JSON devolve **exatamente** o mesmo dicionário (*roundtrip*)
- [ ] Arquivo inexistente, JSON quebrado e JSON-lista devolvem `{}`
- [ ] CSV tem cabeçalho `cpf,nome,email,telefone` e 1 linha por cliente

**Desafio (manual)**

- [ ] `meu_cadastro.py` roda, fecha e **reabre com os mesmos dados**
- [ ] `dados/clientes.json` e `dados/clientes.csv` são gerados pelo menu
- [ ] Todo `input()` está **fora** das funções validadas

- [ ] Tudo verde → marque o checkbox no [README raiz](../../README.md)
