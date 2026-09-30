# 00 — Setup do Ambiente ⏱️ ~1h

**Meta:** Python instalado, VS Code configurado e seu primeiro script rodando no **terminal**.

Esse é o único tópico sem validação automática — a verificação é **visual**: você vê a saída na tela.

---

## 1. Instale o Python 3

Abra o terminal e verifique se já existe:

```bash
python3 --version
```

- **Apareceu `Python 3.10+`?** Passe para o passo 2.
- **Apareceu `command not found`?** Instale:
  - **Mac:** `brew install python` (ou baixe em [python.org](https://www.python.org/downloads/))
  - **Windows:** baixe em [python.org](https://www.python.org/downloads/) e **marque a caixinha "Add Python to PATH"** na instalação

> ⚠️ **Mac/Linux:** o comando é `python3` (o `python` sozinho pode não existir ou abrir outra versão).
> **Windows:** geralmente funciona `python` (ou `py`).

## 2. VS Code + extensão Python

1. Instale o VS Code em [code.visualstudio.com](https://code.visualstudio.com/).
2. Abra a extensões (`Cmd/Ctrl + Shift + X`) e instale a oficial **Python** (Microsoft).
3. Abra esta pasta do repositório: **File → Open Folder** → `python-from-zero`.
4. Selecione o interpretador: `Cmd/Ctrl + Shift + P` → digite **Python: Select Interpreter** → escolha a versão `3.10+`.

## 3. Rode seu primeiro script

1. Abra o terminal integrado do VS Code: `Ctrl + `` ` `` (tecla backtick) ou **Terminal → New Terminal**.
2. Rode:

   ```bash
   python3 fase-1-fundamentos/00-setup/atividade.py
   ```

3. Complete os `TODO` no arquivo `atividade.py` antes de rodar (é o exercício abaixo).
4. Rode de novo e confira as 3 frases na tela.
5. **Quebre de propósito:** mude uma linha para `print("erro)` (aspa aberta, sem fechar) e rode. Veja o erro aparecer — isso é normal e faz parte do ofício.

## 4. Erros comuns de setup

| Erro | Causa provável | Solução |
|---|---|---|
| `command not found: python3` | Python não instalado ou não está no PATH | Instale pelo python.org (Windows: marque "Add to PATH") |
| `command not found: python` | No Mac/Linux o correto é `python3` | Use `python3` |
| Abre a Microsoft Store (Windows) | Atalho envenenado do Windows | Instale pelo python.org ou digite `py` |
| `Permission denied` | Permissão de pasta | Rode o terminal como usuário normal; no Mac use `python3` do Homebrew/python.org |
| VS Code roda outro Python | Interpretador errado | `Python: Select Interpreter` |

---

## ✍️ Atividade

Edite [`atividade.py`](./atividade.py):

1. **TODO 1** — imprima uma saudação com o seu nome.
2. **TODO 2** — imprima seu ano de nascimento **como número** (sem aspas).
3. **TODO 3** — imprima a frase exata: `Vou aprender Python em 2026`.

## ✅ Checkpoint

- [ ] `python3 --version` mostra 3.10+
- [ ] O script roda e as 3 frases aparecem
- [ ] Você provocou (e entendeu) um erro de sintaxe proposital
- [ ] Marque o checkbox no [README raiz](../../README.md)
