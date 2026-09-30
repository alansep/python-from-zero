# Fase 4 — Transição para Desenvolvedor (Projetos Práticos)

> ⏱️ **~18h** · Acompanhe o progresso no [README raiz](../README.md).

**Meta:** consolidar a lógica construindo projetos completos **sem depender do autocompletar da IA**.

| # | Projeto | O que consolida | Tempo |
|---|---|---|---|
| 1 | [**Simulador bancário**](./01-projeto-banco/) | Regras de negócio, validações, loops de menu, saída formatada | 5h |
| 2 | [**Gerenciador de cadastro**](./02-projeto-cadastro/) | Dicionários + persistência em `.json`/`.csv` em disco | 6h |
| 3 | [**Analisador de logs**](./03-projeto-analise-logs/) | Leitura de arquivos, filtragem e geração de relatório | 6h |
| 4 | [**Revisão final**](./04-revisao-final/) | Checklist de autoavaliação das 4 fases "pronto para a fase de libs" | 1h |

## Regras dos projetos

1. Ler o enunciado e **planejar no papel** (entradas, saídas, regras) antes de codar.
2. **Não existe gabarito nem `solucao.py` no repositório** — planeje, code e valide pelo próprio `enunciado.md` e pela validação. O esforço de resolver (e errar) é parte do estudo.
3. Errou? Leia o erro no terminal **antes** de chamar a IA.
4. Cada projeto termina com um checklist de aceitação (como um teste de verdade).
5. **Nada de `input()`** nas funções validadas — toda função do núcleo recebe dados por parâmetro e devolve o resultado.

## Como cada projeto é validado

- O `atividade.py` cobre apenas a **lógica pura**: validação 100% determinística, sem interação e sem depender do teclado.
- O **menu interativo completo é desafio extra** (`meu_banco.py`, `meu_cadastro.py`, `meu_relatorio.py`): um arquivo que **você cria sozinho**, importando as funções já validadas. Ele não é coberto pela validação — quem avalia é o enunciado e você mesmo.
- Os arquivos gerados pelos menus ficam em `dados/` (criada pelo seu código). A validação grava **só em pastas temporárias do sistema** — o repositório não suja.

> 🔒 Não existe gabarito no repositório. A validação (`checar.py`) diz **o que** está errado; descobrir **como** consertar é com você.
