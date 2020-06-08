from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time, math, pyautogui as gui

nick = "" # Seu nick no chess.com
# Essa gameurl baixa os seus jogos Blitz e Rapid. Não inclui Bullet, nem Xadrez 960, Crazyhouse, essas coisas...
gameurl = "https://www.chess.com/games/archive/" + nick +"?gameOwner=other_game&gameType=live&gameTypeslive%5B%5D=blitz&gameTypeslive%5B%5D=rapid&rated=rated&timeSort=desc"
# Diga quantos jogos quer baixar
games = 0
# Que eu converto para quantas páginas vai precisar
pages = math.ceil(games/50)
# O site só vai até a página 101. Esse 'if' evita que ele fique baixando o mesmo PGN.
if (pages > 101):
    pages = 101


browser = None
# Ele primeiro vai tentar o Chrome
isChrome = True
# Deixe como False se estiver com Windows
isLinux = False

if (not(games == 0 or nick == '')):
    try:
        caps = DesiredCapabilities().CHROME.copy()
        caps["pageLoadStrategy"] = "eager" # interactive
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-extensions')
        # Coloque o caminho de onde você botou o ChromeDriver aqui.
        if (isLinux):
            browser = webdriver.Chrome(options=chrome_options,
            executable_path="/home/alextorres10/chromedriver")
        else:
            browser = webdriver.Chrome(options=chrome_options,
            executable_path="C:\\chromedriver.exe")
        
    except:
        try:
            isChrome = False
            caps = DesiredCapabilities().FIREFOX.copy()
            caps["pageLoadStrategy"] = "eager"
            bp = webdriver.FirefoxProfile()
            bp.set_preference("dom.webnotifications.enabled", False)
            if (isLinux):
                browser = webdriver.Firefox(capabilities=caps, firefox_profile=bp)
            else:
                browser = webdriver.Firefox(capabilities=caps, firefox_profile=bp, 
                    executable_path=r'C:\\geckodriver.exe')
            # Da mesma forma, coloque o caminho do Geckodriver.
        except:
            print("Tanto Chrome quanto Firefox deram problema.")


    for i in range(1,pages+1):
        url = gameurl + "&page=" + str(i)
        browser.get(url)
        browser.find_element_by_class_name('archive-games-check-all').click()
        time.sleep(1)
        browser.find_element_by_class_name('archive-games-download-button').click()
        time.sleep(5)
        if (not isChrome):
            if (i == 1):
                gui.press('down')
            gui.press('enter')
else:
    print("Faltou especificar seu nick ou especificou quantos jogos vai baixar.")