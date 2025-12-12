import requests



def test_pikachu_endpoint():
    url = "https://pokeapi.co/api/v2/pokemon/pikachu"

    response = requests.get(url)

    # 1. Validar status code
    assert response.status_code == 200, f"Status code inesperado: {response.status_code}"

    data = response.json()

    # 2. Validar que el campo 'name' sea pikachu
    assert data["name"] == "pikachu", f"El nombre recibido es: {data['name']}"

    print("✔ Test OK: Pikachu API validada correctamente")


test_pikachu_endpoint()
