import os
import requests

from flask import session
from cs50 import SQL

db = SQL('sqlite:///test.db')

def getProducts(category):
    try:
        products = []
        API_URL = f'https://api.mercadolibre.com/sites/MLB/search?q={category}'
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        
        for i in range(len(data['results'])):
            if i <= 50:
                products.append(data['results'][i])

        return products        

    except Exception as e:
        print(e)
        return None
    
def getProductById(id):
    try:
        response = requests.get(f'https://api.mercadolibre.com/items?ids={id}')
        response.raise_for_status()
        data = response.json()

        return data
    
    except Exception as e:
        print(e)
        return None

def getCart():
    return db.execute(
        'SELECT product_id FROM Products_User WHERE user_id = ?', session['user']
    )
