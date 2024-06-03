import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'N' #здесь прописывается токен тренера
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

'''Создание покемона (**POST /pokemons** (*не забудь про нужный хэдер*))
В ответе (терминале) должен прийти объект json'''

body_pokemon = {
    "name":"Бульбазавр",
    "photo":"https://dolnikov.ru/pokemons/albums/012.png"
}

response_create = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_pokemon)
print(response_create.text)

pokemon_id = response_create.json()['id']

'''Смена имени покемона (**PUT /pokemons** (*не забудь про нужный хэдер*))
В ответе (терминале) должен прийти объект json'''

change_pokemon = {
    "pokemon_id": pokemon_id,
    "name": "Кукумбер",
    "photo": "https://dolnikov.ru/pokemons/albums/012.png"
}

response_change_pokemon = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=change_pokemon)
print(response_change_pokemon.text)

'''Поймать покемона в покебол (**POST /trainers/add_pokeball** (*не забудь про нужный хэдер*))
В ответе (терминале) должен прийти объект json'''

catching_pokemon= {
     "pokemon_id":pokemon_id
}

responce_catch_pokemon = requests.post(f'{URL}/trainers/add_pokeball', headers=HEADER, json=catching_pokemon)
print(responce_catch_pokemon.text)