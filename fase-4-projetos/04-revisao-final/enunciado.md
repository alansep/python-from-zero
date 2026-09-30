# 04 — Revisão Final ⏱️ ~1h

**Meta:** provar, item por item, que a base está sólida — e sair desta fase pronto para o próximo repositório (bibliotecas e ecossistema).

---

## 📚 Contexto

Você chegou ao fim da trilha **python-from-zero**. Três projetos rodando, dezenas de exercícios verdes. Mas "rodou uma vez" não é o mesmo que "eu sei": o esquecimento costuma morar exatamente no que nunca foi revisado.

Esta revisão tem duas metades:

1. **Autoavaliação honesta** — ~30 itens, um por habilidade coberta nas 4 fases. Marque só o que você **consegue explicar em voz alta e reproduzir num papel em branco**. Item desmarcado não é vergonha: é mapa do que retomar.
2. **Roteiro de revisão ativa** — refatorar um projeto antigo, comentar o essencial e rodar **tudo** do zero, como se fosse o primeiro dia.

No fim existe um checkpoint único: **pronto para o repositório de bibliotecas** — ou seja, você consegue aprender `requests`, `pandas` ou `pytest` sozinho, porque a base (tipos, estruturas, funções, arquivos, depuração) não depende de ninguém.

---

## 📋 Checklist de autoavaliação (~30 itens)

> Marque apenas o que você **explica sem consultar**. Um `[ ]` restante é um tópico para reler — não um fracasso.

### Fase 1 — Fundamentos (8)

- [ ] Sei declarar variáveis com `=` e sei por que `==` (comparação) é outra coisa
- [ ] Converto entre `str`/`int`/`float` com `int()`, `float()`, `str()` sem quebrar o programa
- [ ] Reconheço os tipos primitivos (`int`, `float`, `str`, `bool`) e o que cada um guarda
- [ ] Uso `+ - * / // % **` e sei a precedência entre eles (parênteses salvam)
- [ ] Combino relacionais (`> < >= <= == !=`) com lógicos (`and`, `or`, `not`)
- [ ] Escrevo `if / elif / else` com `:` e indentação de 4 espaços
- [ ] Sei que a **ordem das validações** muda o resultado e coloco o caso especial primeiro
- [ ] Domino `for` + `range`, `while` com condição de parada, `break` e `continue`

### Fase 2 — Estruturas de dados (7)

- [ ] Indexo, fatio (*slicing*) e altero listas entendendo a **mutabilidade**
- [ ] Uso `append`, `pop`, `remove`, `sort`, `len` no momento certo
- [ ] Sei quando a **tupla** (imutável) é melhor que a lista, e uso `set` para remover duplicatas
- [ ] Navego dicionários: chave→valor, `get`, `in`, `.items()` e objetos aninhados
- [ ] Monto strings com f-string e manipulo com `split`, `join`, `strip`, `replace`
- [ ] Escrevo *list comprehension* simples e com condição (`if` no fim)
- [ ] Escolho a estrutura certa para cada problema (lista × tupla × dicionário × conjunto)

### Fase 3 — Modularização e depuração (7)

- [ ] Escrevo funções com parâmetros, padrão e `return` — e sei quando **não** devolver nada
- [ ] Explico a diferença entre escopo local e global e evito variável global
- [ ] Uso `import` / `from ... import` e sei achar na stdlib o que preciso (`json`, `csv`, `os`, `datetime`)
- [ ] Leio e escrevo `.txt`, `.json` e `.csv` com `open` + `with`, sem esquecer `encoding`
- [ ] Consigo executar busca linear e Bubble Sort **na mão**, explicando cada troca
- [ ] Uso `try`, `except`, `finally` — e nunca engolo um erro em silêncio
- [ ] Leio uma *stack trace* (arquivo, linha, tipo da exceção) e depuro com `print`/breakpoint **antes** de chamar a IA

### Fase 4 — Os 3 projetos (7)

- [ ] **Banco:** regras de depósito/saque (limite de R$ 500, 3 saques) validadas e verdes
- [ ] **Banco:** nenhuma função do núcleo usa `input()` — o menu está isolado no `meu_banco.py`
- [ ] **Cadastro:** CPF duplicado é recusado sem sobrescrever o dado original
- [ ] **Cadastro:** gravar → ler JSON devolve o mesmo dicionário e o CSV tem cabeçalho
- [ ] **Logs:** filtro por nível funciona com `error` em minúsculo e conta certo (12/7/9)
- [ ] **Logs:** o relatório sai com 3 linhas na ordem `INFO`, `WARN`, `ERROR`
- [ ] Os **3 projetos** rodam verdes no terminal, sem Traceback

### Síntese (3)

- [ ] Consigo decompor um problema novo em funções com **entrada e saída** claras
- [ ] Planejo no papel (entradas, saídas, regras) **antes** de abrir o editor
- [ ] Leio o erro no terminal e formulo uma hipótese **antes** de perguntar à IA

---

## ✍️ Roteiro de revisão (faça agora, nesta ordem)

### 1. Refatore um projeto antigo (não reescreva — mude)

Escolha **um** dos três projetos e aplique pelo menos três destas melhorias:

- extraiga um trecho repetido para uma **função nova** com nome verboso (`def validar_saque(...)`);
- reduza uma função muito longa em duas menores, cada uma com **uma** responsabilidade;
- troque uma variável com nome genérico (`x`, `dado`, `res`) por algo que **conte a história** (`saldo_disponivel`, `historico`);
- elimine código duplicado (a mesma regra escrita dois vezes);
- normalize as mensagens de retorno para **uma constante só** no topo do arquivo.

### 2. Comente o essencial (o porquê, nunca o óbvio)

- **Comente:** regra de negócio estranha, limite arbitrário (`LIMITE_SAQUE = 500`), decisão que você levou tempo para entender.
- **Não comente:** `i += 1  # incrementa i`, `# abre o arquivo` em cima de `open(...)`.
- Regra prática: se o código ficasse **sem** comentário, um colega entenderia? Comente só onde a resposta for "não".

### 3. Rode tudo do zero

```bash
# todas as atividades do repositório, de uma vez
for a in $(find fase-* -name atividade.py | sort); do python3 "$a"; done
```

Ou, uma por uma:

```bash
python3 fase-1-fundamentos/01-variaveis-tipos/atividade.py
python3 fase-1-fundamentos/02-operadores/atividade.py
python3 fase-1-fundamentos/03-condicionais/atividade.py
python3 fase-1-fundamentos/04-repeticoes/atividade.py
python3 fase-4-projetos/01-projeto-banco/atividade.py
python3 fase-4-projetos/02-projeto-cadastro/atividade.py
python3 fase-4-projetos/03-projeto-analise-logs/atividade.py
```

Depois, **na mão**, rode também os menus que você criou: `meu_banco.py`, `meu_cadastro.py` e `meu_relatorio.py`.

> 🧹 Ao final, deixe a árvore limpa: nada de `solucao.py`, nada de arquivo gerado por teste. A fixture `logs_exemplo.txt` **permanece** — é material de estudo.

### 4. Marque o roadmap

Abra o [README raiz](../../README.md) e marque os checkboxes que ficaram pendentes. O contador no topo (`Progresso: X/30`) deve refletir a realidade.

---

## 💡 Dicas (progressivas — sem gabarito)

1. **Comece pela autoavaliação, não pelo código.** Você leva ~15 min lendo os 30 itens; anote mentalmente os 5 que te fizeram pensar. Eles definem a ordem da revisão.
2. **Refatorar é mudar a estrutura sem mudar o comportamento.** Faça uma mudança, rode a validação, só então faça a próxima. Se ficou vermelho, você mudou comportamento sem querer — desfaça (`Cmd+Z`/`Ctrl+Z`) e recomece pela menor mudança possível.
3. **O teste da entrevista imaginária:** abra o seu projeto e, para cada função, diga em voz alta "esta função recebe X e devolve Y porque a regra é Z". Travar em alguma = releia aquele tópico **antes** de marcar o checkbox.

---

## ✅ Checkpoint de aceitação

- [ ] Li os ~30 itens e **só marquei o que sei explicar**
- [ ] Escolhi um projeto e apliquei **pelo menos 3** melhorias de refatoração
- [ ] Comentei o essencial (porquê) e removi comentários que só repetiam o código
- [ ] Rodei **todas** as atividades do zero, todas verdes
- [ ] Rodei os 3 menus que criei, sem Traceback
- [ ] Árvore limpa: nenhum `solucao.py`, nenhum arquivo gerado por teste, `logs_exemplo.txt` intacto
- [ ] Roadmap do [README raiz](../../README.md) atualizado com os checkboxes marcados
- [ ] **Checkpoint: pronto para o repositório de bibliotecas** 🚀
