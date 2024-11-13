import requests
import json
from dotenv import load_dotenv
import os

def execute(query):
    load_dotenv()
    os.environ[""] = ""
    res = requests.post(os.getenv('database'),{'query': query, 'pw':os.getenv('pw')})
    response = json.loads(res.text)
    
    if 'error' in response:
        print('\033[91m'+response['error'])
    
    if 'result' in response:
        print('\033[92m'+'SQL STATEMENT COMPLETED')
        
        return response['result']
    return []
    
    
# damit die database.py funktioniert, benötigt das Program eine .env Datei.
# In diese Datei gehört 
# pw='techstarter2024!'
# database='https://sql-api-ysa4.onrender.com/api/sql'

# pw zum absichern, damit nicht jeder dödel die Tabellen drop kann und database für den Entpunkt der API

# sollte dotenv bzw load_dotenv probleme machen, muss dies installiert werden:
# pip install dotenv

# Fügt diese Python Datei in euer Gruppenprojekt und ruft diese per
# from database import execute
# auf und nutzt die execute() um SQL Statements an die SQLite Online zu senden.

# Die Online Datenbank antwortet mit error und result, der User sieht nur result, error wird als Print ausgegeben.
# Dies soll eine SQL Datenbank simulieren, falls wir nochmal an einem Gruppenprojekt arbeiten, was schwierig ist in einer VM.