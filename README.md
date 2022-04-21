# PGNChessCom
Um bot que baixa as suas partidas do chess.com. Muito bom para a comunidade enxadrística do site, que agora terá menos trabalho para baixar suas partidas e poder analisá-las propriamente.

Ingredientes:
* [Python3](https://www.python.org/)   
```
sudo apt-get install python3
```
Esse comando é para Linux, mas pelo menos no Ubuntu, o Python já vem instalado.
Se estiver no Windows, baixe o instalador do Python no próprio site. Entre, clique na aba Download, escolha seu sabor e sirva-se.

## O que mudou
O código não usa mais o Selenium, nem Geckodriver, já que a interação do site era muito propensa a erros, e acabei descobrindo uma URL que tem todos os jogos de cada nick.

## Executando o código
No código, ao executar, ele já pedirá o nick do jogador no chess.com, e ele irá baixando os jogos (organizados em cada mês num JSON). No final, sairá um PGN com todos os jogos juntos, sem necessidade de juntar num ChessBase da vida.

# Contato
Se você quer contribuir com o código de alguma forma, quer tirar dúvidas, experienciou algum problema e quer ajuda, se me achou feio, se me achou bonito, entre em contato comigo através do meu [E-mail](mailto:alextcarvalho98@gmail.com).
