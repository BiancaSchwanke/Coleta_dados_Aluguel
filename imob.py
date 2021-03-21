#!/usr/bin/env python3
# -*- coding: utf-8 -*

from bs4 import BeautifulSoup
import requests
import pandas as pd

urls = ["https://imoveis.mercadolivre.com.br/apartamentos/aluguel/rio-grande-do-sul/canoas/marechal-rondon/_DisplayType_LF"]

propriedades = []

for url in urls:
    c=requests.get(url).content
    soup=BeautifulSoup(c)
    
    cards = soup.findAll("ol", {"class": "ui-search-layout--stack"}) 
    propriedades = []
    
    for card in cards:
        propriedade = {}
        try:
            propriedade["endereco"] = card.find("span", {"class": "ui-search-item__location"}).text
        except:
            propriedade["endereco"] = None
        try:
            propriedade["area"] = card.find("li", {"class": "ui-search-card-attributes__attribute"}).text
        except:
            propriedade["area"] = None
        try:
            propriedade["preco"] = card.find("span", {"class": "ui-search-price__part"}).text
        except:
            propriedade["preco"] = None
      
    propriedades.append(propriedade)
        

