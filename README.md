# PGNChessCom
Um bot que baixa as suas partidas do chess.com. Muito bom para a comunidade enxadrística do site, que agora terá menos trabalho para baixar suas partidas e poder analisá-las propriamente.

O projeto foi testado no Linux e no Windows. Talvez deva funcionar no MacOS.

Ingredientes:
* [Python3](https://www.python.org/)   
```
sudo apt-get install python3
```
Esse comando é para Linux, mas pelo menos no Ubuntu, o Python já vem instalado.
Se estiver no Windows, baixe o instalador do Python no próprio site.
* [Selenium](https://www.seleniumhq.org/) para simular a navegação 
```
pip install selenium
```
O comando serve tanto para Windows quanto Linux. Mas tenha o Python instalado antes.
* [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) (caso for usar no Chrome)
* [Geckodriver](https://github.com/mozilla/geckodriver/releases)
## Geckodriver (Linux)
Execute os seguintes comandos quando baixar a mais recente versão (cheque a versão no link acima!):
```
wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
tar -xvzf geckodriver*
chmod +x geckodriver
sudo mv geckodriver /usr/local/bin/
```

## Geckodriver (Windows)
1. Visite o site e escolha conforme seu OS (Windows 32 ou 64 bits). 
2. Descompacte o arquivo .exe exatamente no Diretório C:\.
3. No Menu Iniciar, pesquise "variáveis de ambiente" e selecione o primeiro resultado.
4. Clique em Variáveis de Ambiente.
5. Na parte "Variáveis do Sistema", clique em Path (ou Caminho), depois Editar e depois Novo.
6. Digite "C:\geckodriver.exe" (é o endereço onde você colocou o arquivo)
7. Dê o enter, e aperte os OKs.

## Mexendo no código
Agora vai no código, linha 7 e 8, coloque seu login e senha, e veja a festa acontecer. Aos leigos, não tenham medo, o código não guarda nenhum dado seu.

# Contato
Se você quer contribuir com o código de alguma forma, quer tirar dúvidas, experienciou algum problema e quer ajuda, se me achou feio, se me achou bonito, entre em contato com meu [Twitter](https://twitter.com/AlexTowerss10)
