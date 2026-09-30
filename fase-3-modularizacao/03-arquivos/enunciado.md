# 03 — Manipulação de Arquivos ⏱️ ~2.5h

**Meta:** fazer o programa **lembrar depois que fechou** — gravar e reler `.txt`, `.json` e `.csv` sem deixar lixo no repositório.

---

## 📚 Teoria

### Abrir, ler e fechar — o `with`

```python
with open("notas.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("primeira linha\n")
# o arquivo é FECHADO sozinho, mesmo se der erro no meio
```

> ⚠️ Sem `with`, você precisa lembrar de `arquivo.close()`. Se esquecer, o Python só grava o conteúdo no disco quando o programa terminar (ou perde tudo se o processo morrer). **Sempre use `with`.**

| Modo | O que faz | Arquivo novo? |
|---|---|---|
| `"r"` | ler (padrão) | erro se não existir |
| `"w"` | escrever — **apaga o conteúdo anterior** | cria |
| `"a"` | acrescentar no fim | cria |

- **`encoding="utf-8"` não é opcional no seu código**: sem ele, acentos (`ção`, `ç`, `ê`) quebram dependendo do sistema. Especifique sempre: [função `open`](https://docs.python.org/pt-br/3/library/functions.html#open).

### Ler linha a linha

```python
with open("notas.txt", encoding="utf-8") as arquivo:
    for linha in arquivo:            # o próprio arquivo é iterável
        print(linha.rstrip("\n"))    # cuidado: cada linha traz o \n
```

Também existe `arquivo.readlines()` (lista com as linhas) e `arquivo.read()` (tudo de uma vez).

### `pathlib.Path` — caminhos como objetos

```python
from pathlib import Path

caminho = Path("dados") / "2026" / "notas.txt"   # usa o operador /
caminho.exists()          # True/False — sem tentar abrir
caminho.name              # "notas.txt"
Path("a/b").parent        # Path("a")
```

| Antes (módulo `os`) | Agora (`pathlib`) |
|---|---|
| `os.path.join(a, b)` | `Path(a) / b` |
| `os.path.exists(c)` | `Path(c).exists()` |
| string suja com `+` | objeto com método |

Docs: [`pathlib`](https://docs.python.org/pt-br/3/library/pathlib.html).

### JSON em disco

```python
import json
with open("dados.json", "w", encoding="utf-8") as arquivo:
    json.dump({"nome": "José"}, arquivo, ensure_ascii=False)   # dict -> arquivo

with open("dados.json", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)                                  # arquivo -> dict
```

`json.dumps`/`loads` trabalham com **texto**; `dump`/`load` trabalham com **arquivo**. Roundtrip: o que sai é igual ao que entrou.

### CSV em disco

```python
import csv
with open("tabela.csv", "w", newline="", encoding="utf-8") as arquivo:
    csv.writer(arquivo).writerow(["nome", "idade"])
    csv.writer(arquivo).writerow(["Ana", 30])

with open("tabela.csv", encoding="utf-8") as arquivo:
    linhas = list(csv.reader(arquivo))   # [['nome', 'idade'], ['Ana', '30']]
```

- `newline=""` no modo `"w"` evita linhas em branco extras no Windows.
- O `writer` cuida dos campos com vírgula dentro (coloca aspas sozinho).

### Quando o arquivo não existe

`open("falta.txt")` levanta `FileNotFoundError`. Trate **antes** de abrir:

```python
if not Path(caminho).exists():
    return None
```

(O tópico 05 deixa isso elegante com `try/except` — aqui o `if` resolve.)

---

## ✍️ Exercícios

Abra [`atividade.py`](./atividade.py) — são 7 exercícios. **Todas as funções RECEBEM o caminho como parâmetro** (nada de caminho fixo dentro da função) e a validação usa uma pasta temporária:

1. **`escrever_txt(caminho, texto)`** — grava o texto exato (`encoding="utf-8"`).
2. **`ler_txt(caminho)`** → o conteúdo; **arquivo inexistente → `None`**.
3. **`contar_linhas(caminho)`** → nº de linhas; **arquivo inexistente → `None`**. `"a\n"` tem 1 linha; arquivo vazio tem 0.
4. **`existe(caminho)`** → `True`/`False` com `pathlib`.
5. **`juntar_caminho(base, nome)`** → caminho final com o operador `/` do `Path` (devolva como texto).
6. **`salvar_json(caminho, dados)`** + **`carregar_json(caminho)`** → roundtrip; **arquivo inexistente → `None`**.
7. **`salvar_csv(caminho, linhas)`** + **`ler_csv(caminho)`** → roundtrip com `csv.writer`/`csv.reader` (uma linha é uma lista).

```bash
python3 fase-3-modularizacao/03-arquivos/atividade.py
```

> 📌 A validação cria os arquivos de teste numa pasta temporária do sistema — **nada fica no repositório**. Teste também você mesmo com `Path` fora do `checar.py`.

---

## 💡 Dicas (progressivas — sem gabarito)

**Exercício 1**
1. Quais três argumentos o `open` precisa para gravar texto com acento?
2. `"w"` apaga o que existia — é isso que queremos para "gravar o texto exato"?
3. `with open(caminho, "w", encoding="utf-8") as arquivo:` e dentro dele `arquivo.write(texto)`. A função não precisa devolver nada.

**Exercício 2**
1. O que acontece se você abrir um caminho que não existe no modo `"r"`?
2. Dá para conferir ANTES de abrir usando o `pathlib` — `Path(caminho).exists()`.
3. Se não existir, `return None` logo no começo; senão, `with open(..., encoding="utf-8")` e `return arquivo.read()`.

**Exercício 3**
1. Cada linha lida do arquivo termina com qual caractere invisível?
2. `read().splitlines()` já ignora a quebra final — `"a\n".splitlines()` tem quantos elementos?
3. Trate a ausência do arquivo como no exercício 2; depois conte com `len(...)` sobre as linhas. Arquivo vazio → 0.

**Exercício 4**
1. Qual classe do `pathlib` transforma texto em caminho?
2. Depois de construir o objeto, existe um método só para "está aí?".
3. `from pathlib import Path` + `return Path(caminho).exists()` — devolve o `bool` que o método já entrega.

**Exercício 5**
1. Como o `pathlib` une dois pedaços de caminho? (Dica: é um operador que você já usou em conta.)
2. `Path("dados") / "x.txt"` — e para devolver texto, `str(...)` resolve.
3. `return str(Path(base) / nome)`. A validação normaliza o resultado: funciona com barra extra no fim do `base` também.

**Exercício 6**
1. `dumps`/`loads` são para texto — quais as irmãs que trabalham com arquivo?
2. Escrever: `open(..., "w")` + `json.dump`. Ler: `open(..., "r")` + `json.load`.
3. Monte `salvar_json` com `with` + `dump(dados, arquivo, ensure_ascii=False)`; em `carregar_json`, verifique antes se o arquivo existe (senão `None`) e devolva o `load(arquivo)`.

**Exercício 7**
1. No modo `"w"`, o que o `newline=""` evita?
2. `writerow` recebe **uma linha** (uma lista) — para várias, um `for`.
3. Para gravar: `with open(..., "w", newline="", encoding="utf-8")` + `csv.writer(arquivo)` num laço. Para ler: mesmo `with` de sempre e `list(csv.reader(arquivo))`.

## 🚀 Desafios extras

- **Modo `"a"`:** crie `acrescentar_txt(caminho, texto)` que só acrescenta a linha no fim — teste com duas chamadas seguidas.
- **Backup automático:** antes de gravar `dados.json`, copie a versão antiga para `dados.bak` com `Path.replace`.
- **CSV com cabeçalho:** faça `ler_csv` devolver `dict` por linha usando `csv.DictReader`.

## ✅ Checkpoint

- [ ] Sei por que `with` + `encoding="utf-8"` são obrigatórios no meu código
- [ ] Consigo ler linha a linha sem levar o `\n` junto
- [ ] Sei conferir existência com `Path(...).exists()` antes de abrir
- [ ] Fiz roundtrip de `.json` e `.csv` (gravar e reler igual)
- [ ] Tudo verde → marque o checkbox no [README raiz](../../README.md)
