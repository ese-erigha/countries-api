import requests


def load_data():
    url = 'https://restcountries.eu/rest/v2/all'
    response = requests.get(url, headers={'Content-Type': 'application/json; charset=utf-8'})
    country_list = response.json()

    for num, country in enumerate(country_list):

        print(num + 1)
        resp = requests.post('http://127.0.0.1:5000/country/create', json=country)
        if resp.status_code != 201:
            print(resp.status_code)
            print(country['name'])

        print()


load_data()
