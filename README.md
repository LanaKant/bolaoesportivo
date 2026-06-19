# Bolão Esportivo - Copa do Mundo 2026

## Integrantes

* Hilana Izabelle Serra Cavalcanti

## Descrição do Projeto

Este projeto consiste em um sistema de bolão esportivo desenvolvido em Python inpirado na Copa do Mundo de 2026.

O programa permite que participantes registrem seus palpites para o campeão, vice-campeão e terceiro colocado da competição. Após o cadastro dos palpites, o sistema realiza uma simulação dos resultados da Copa utilizando sorteio aleatório entre as seleções participantes.

Em seguida, os palpites são comparados com o resultado oficial gerado pelo programa, sendo atribuídas pontuações de acordo com os acertos de cada participante. Ao final, é criado um ranking com a classificação dos usuários e um arquivo de texto contendo os resultados.

## Arquivos do Projeto

* `main.py` → Código principal do sistema.
* `selecoes_copa_2026.txt` → Arquivo contendo as seleções participantes, gerado automaticamente caso já não exista.
* `resultado_bolao_2026.txt` → Arquivo com os resultados e ranking gerado automaticamente ao fim do programa.

## Bibliotecas Utilizadas

* `random` (biblioteca padrão do Python)

Nenhuma biblioteca externa foi utilizada.

## Como Executar o Projeto

### Pré-requisitos

* Python 3 instalado no computador.

### Passo a Passo

1. Baixe ou clone o repositório do GitHub.
2. Abra o terminal na pasta do projeto.
3. Execute o arquivo principal com o comando:

```bash
python main.py
```

4. Digite o nome dos participantes e seus respectivos palpites.
5. Quando terminar os cadastros, digite:

```text
sair
```

6. O programa irá simular o resultado da Copa, calcular a pontuação dos participantes e gerar o arquivo:

```text
resultado_bolao_2026.txt
```

7. Consulte o arquivo gerado para visualizar o ranking final.

## Sistema de Pontos e Regras de Pontuação

* Caso o usuário acerte a seleção e a sua posição no placar (campeão, vice ou terceiro): +3 pontos.
* Caso acerte uma das seleções do pódio, porém em uma posição diferente: +1 ponto.
* Caso não haja acertos: 0 pontos.

### Exemplo:

====================   RESULTADO OFICIAL   ====================

* 1° Lugar: Brasil
* 2° Lugar: Chile
* 3° Lugar: Japão

===================   PALPITES DO JOGADOR   ===================

* 1° Lugar: Brasil    (+3 Pontos)
* 2° Lugar: Japão     (+1 Ponto)
* 3° Lugar: Noruega   (+0 Pontos)

## Divisão das Responsabilidades

### Hilana Izabelle

* Desenvolvimento da estrutura principal do programa.
* Cadastro dos participantes e registro dos palpites.
* Implementação da lógica de pontuação e ranking.
* Manipulação de arquivos, testes e documentação do projeto.

## Observações

O projeto foi desenvolvido para fins acadêmicos utilizando programação em Python e conceitos como listas, dicionários, estruturas de repetição, estruturas condicionais, funções da biblioteca random e manipulação de arquivos texto.
