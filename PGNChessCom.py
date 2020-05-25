from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time, math, pyautogui as gui


login = ""
password = ""

loginUrl = "https://www.chess.com/login_and_go?returnUrl=https%3A%2F%2Fwww.chess.com%2F"
# Esteja já logado no site
#gameurl = "https://www.chess.com/games/archive?gameOwner=my_game&gameType=live&gameTypeslive%5B%5D=blitz&gameTypeslive%5B%5D=rapid&timeSort=desc"
gameurl = "https://www.chess.com/games/archive/tpros?show=live_blitz&gameType=live_blitz&rated=rated"
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

if (not(login == '' or password == '' or games == 0)):
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

    browser.get(loginUrl)
    browser.find_element_by_id('username').send_keys(login)
    browser.find_element_by_id('password').send_keys(password)
    browser.find_element_by_id('login').click()

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
    print("Estão faltando dados ou você não especificou quantos jogos vai baixar.")