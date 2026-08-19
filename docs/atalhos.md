---
title: Atalhos
nav_order: 6
---

# Atalhos de teclado e modo interativo

[← Voltar ao índice](index.md)

> Atalhos variam por plataforma e terminal. No [fullscreen rendering](https://code.claude.com/docs/en/fullscreen), aperte `?` no transcript viewer para ver os atalhos daquela tela.
>
> **macOS**: atalhos com `Alt` (`Alt+B`, `Alt+F`, `Alt+Y`, `Alt+P`) exigem configurar a tecla Option como Meta no terminal.

## Controles gerais

| Atalho | Ação |
| --- | --- |
| `Ctrl+C` | Interrompe a operação em curso; sem nada rodando, limpa o input e um segundo toque sai |
| `Ctrl+D` | Sai da sessão |
| `Ctrl+X Ctrl+K` | Para todos os subagents em background da sessão (2× em 3s para confirmar) |
| `Ctrl+G` ou `Ctrl+X Ctrl+E` | Abre no editor de texto padrão |
| `Ctrl+L` | Redesenha a tela |
| `Ctrl+O` | Alterna o transcript viewer |
| `Ctrl+R` | Busca reversa no histórico de comandos |
| `Ctrl+V` (ou `Cmd+V` no iTerm2, `Alt+V` no Windows/WSL) | Cola imagem do clipboard |
| `Ctrl+B` | Joga as tarefas em execução para background |
| `Ctrl+T` | Alterna o checklist de tarefas do Claude |
| `Ctrl+S` | Guarda/restaura o prompt (*stash*) |
| `Ctrl+Z` | Suspende o Claude Code |
| `←` / `→` | Circula entre abas de diálogos |
| `↑` / `↓` ou `Ctrl+P` / `Ctrl+N` | Move o cursor ou navega o histórico |
| `Esc` | Interrompe o Claude, ou fecha um diálogo |
| `Esc` `Esc` | Limpa o rascunho do input, ou faz *rewind* |
| `Shift+Tab` | Circula entre os modos de permissão |
| `Option+P` (macOS) / `Alt+P` | Troca de modelo |
| `Option+T` (macOS) / `Alt+T` | Alterna o extended thinking |
| `Option+O` (macOS) / `Alt+O` | Alterna o fast mode |

## Edição de texto

| Atalho | Ação |
| --- | --- |
| `Ctrl+A` | Início da linha |
| `Ctrl+E` | Fim da linha |
| `Ctrl+K` | Apaga até o fim da linha |
| `Ctrl+U` | Apaga do cursor até o início da linha |
| `Ctrl+W` | Apaga a palavra anterior |
| `Ctrl+Y` | Cola o texto apagado |
| `Alt+Y` (depois de `Ctrl+Y`) | Circula o histórico de colagens |
| `Alt+B` / `Alt+F` | Move uma palavra para trás / para frente |
| `Ctrl+_` ou `Ctrl+Shift+-` | Desfaz a última edição do input |

## Entrada em múltiplas linhas

| Método | Como |
| --- | --- |
| Escape rápido | `\` + `Enter` |
| Tecla Option | `Option+Enter` |
| Shift+Enter | `Shift+Enter` (pode exigir `/terminal-setup`) |
| Sequência de controle | `Ctrl+J` |
| Modo colagem | Cole direto |

## Prefixos rápidos no prompt

| Prefixo | Efeito |
| --- | --- |
| `/` no início | Comando ou skill |
| `!` no início | Modo shell |
| `@` | Menção a caminho de arquivo |
| `:` | Shortcode de emoji |
| `?` no input vazio | Alterna o painel de ajuda de atalhos |

## Transcript viewer

| Atalho | Ação |
| --- | --- |
| `?` | Painel de ajuda de atalhos (requer fullscreen) |
| `{` / `}` | Pula para o prompt anterior/próximo, como movimento de parágrafo do vim (requer fullscreen) |
| `Ctrl+E` | Mostra todo o conteúdo (somente renderizador clássico) |
| `[` | Escreve a conversa inteira no scrollback nativo do terminal, para buscar com `Cmd+F`/tmux (requer fullscreen) |
| `v` | Escreve a conversa em arquivo temporário e abre no `$VISUAL`/`$EDITOR` (requer fullscreen) |
| `q`, `Ctrl+C`, `Esc` | Sai da transcript view |

## Voz

| Atalho | Ação |
| --- | --- |
| Segurar ou tocar `Space` | Ditado por voz (ver `/voice`) |

## Respostas do `/btw`

| Tecla | Ação |
| --- | --- |
| `Space`, `Enter`, `Esc` | Dispensa a resposta e volta ao prompt |
| `↑` / `↓` | Rola a resposta |
| `←` / `→` | Navega entre esta resposta e as anteriores do `/btw` |
| `c` | Copia a resposta como Markdown cru |
| `f` | Bifurca em uma nova sessão herdando a conversa + esta pergunta/resposta |
| `x` | Limpa a lista de trocas anteriores do `/btw` |

---

# Modo Vim

Habilite pelo `/config` ou pelas settings. `/keybindings` permite customizar qualquer binding.

## Troca de modo

| Comando | Ação |
| --- | --- |
| `Esc` | Entra no modo NORMAL |
| `i` / `I` | Insere antes do cursor / no início da linha |
| `a` / `A` | Insere depois do cursor / no fim da linha |
| `o` / `O` | Abre linha abaixo / acima |
| `v` / `V` | Seleção visual por caractere / por linha |

## Navegação (NORMAL)

| Comando | Ação |
| --- | --- |
| `h` `j` `k` `l` | Esquerda / baixo / cima / direita |
| `Space` | Move para a direita |
| `w` / `e` / `b` | Próxima palavra / fim da palavra / palavra anterior |
| `0` / `$` / `^` | Início da linha / fim da linha / primeiro caractere não-branco |
| `gg` / `G` | Início / fim do input |
| `f{c}` / `F{c}` | Pula para a próxima / anterior ocorrência do caractere |
| `t{c}` / `T{c}` | Pula para logo antes / logo depois da ocorrência |
| `;` / `,` | Repete o último `f`/`F`/`t`/`T`, à frente / ao contrário |
| `/` | Abre a busca reversa de histórico (mesmo que `Ctrl+R`) |

## Edição (NORMAL)

| Comando | Ação |
| --- | --- |
| `x` | Apaga caractere |
| `dd` / `D` | Apaga linha / até o fim da linha |
| `dw` `de` `db` | Apaga palavra / até o fim / para trás |
| `cc` / `C` | Muda a linha / até o fim da linha |
| `cw` `ce` `cb` | Muda palavra / até o fim / para trás |
| `s` / `S` | Substitui caractere / linha (requer v2.1.211+) |
| `yy` / `Y` | Copia (*yank*) a linha |
| `yw` `ye` `yb` | Copia palavra / até o fim / para trás |
| `p` / `P` | Cola depois / antes do cursor |
| `>>` / `<<` | Indenta / desindenta a linha |
| `J` | Junta linhas |
| `u` | Desfaz |
| `.` | Repete a última mudança |

## Text objects (NORMAL)

| Comando | Ação |
| --- | --- |
| `iw` / `aw` | Palavra interna / ao redor |
| `iW` / `aW` | WORD (delimitada por espaço) interna / ao redor |
| `i"` `a"` / `i'` `a'` | Dentro / ao redor de aspas duplas / simples |
| `i(` `a(` / `i[` `a[` / `i{` `a{` | Dentro / ao redor de parênteses, colchetes, chaves |

## Modo visual

| Comando | Ação |
| --- | --- |
| `d` / `x` | Apaga a seleção |
| `y` | Copia a seleção |
| `c` / `s` | Muda a seleção |
| `p` | Substitui a seleção pelo conteúdo do registrador |
| `r{c}` | Substitui cada caractere selecionado por `{c}` |
| `~` / `u` / `U` | Alterna / minúsculas / maiúsculas na seleção |
| `>` / `<` | Indenta / desindenta as linhas selecionadas |
| `J` | Junta as linhas selecionadas |
| `o` | Troca cursor e âncora |
| `v` / `V` | Alterna entre char-wise e line-wise, ou sai |

---

_Verificado contra o binário `2.1.136` e a documentação oficial de 19/08/2026._
