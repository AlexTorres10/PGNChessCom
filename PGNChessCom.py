#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json

def dict_url(url):
    return json.loads(requests.get(url).text)
try:
    nick = input('Digite o nick do jogador no chess.com: ')
    url = 'https://api.chess.com/pub/player/'+nick.lower()+'/games/archives'
    page = dict_url(url)
    if (page['archives']):
        print("Jogador encontrado.")
except:
    print("Jogador não encontrado.")
    input("Aperte Enter para sair.")
    exit()


# In[2]:


todos_jogos = ''
i=0
for month in page['archives']:
    period = month[-7:].replace('/','-')
    print("Período",period,"-",round(i/len(page['archives'])*100,2),"%", end='\r')
    try:
        for game in dict_url(month)['games']:
            todos_jogos += (game['pgn'] + '\n')
    #     tj = open(nick+period+".pgn", "w",errors='ignore')
    except:
        print("Período",period,"teve problemas")
    i+=1
tj = open(nick+"-AllGames.pgn", "w",errors='ignore')
tj.write(todos_jogos)
tj.close()
print("100% dos jogos foram baixados!")
input("Aperte Enter para sair.")

