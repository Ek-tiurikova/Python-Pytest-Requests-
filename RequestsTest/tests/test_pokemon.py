import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'N' #здесь прописывается токен тренера
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '4202' 

def test_trainers():
    response1 = requests.get(url=f'{URL}/trainers')
    assert response1.status_code == 200

def test_find_trainer():
    response2 = requests.get(url=f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response2.json()["data"][0]["trainer_name"] == 'Камин'

@pytest.mark.parametrize('key, value', [('id', TRAINER_ID), ('trainer_name', 'Камин')])
def test_find_tr(key, value):
    response3 = requests.get(url=f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response3.json()["data"][0][key] == value