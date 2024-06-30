import requests
from bs4 import BeautifulSoup


def get_coordinates(location):
    url = f"https://pl.wikipedia.org/wiki/{location}"
    response = requests.get(url)
    response_html = BeautifulSoup(response.text, 'html.parser')

    try:
        latitude = float(response_html.select('.latitude')[0].text.replace(",", "."))
        longitude = float(response_html.select('.longitude')[0].text.replace(",", "."))
        return latitude, longitude
    except IndexError:
        print(f'Could not find coordinates for location: {location}')
        return None, None


def show_client(clients: list[dict[str, str]]) -> None:
    for client in clients[1:]:
        print(
            f'klient {client["name"]}, location {client["location"]}, latitude {client["latitude"]}, {client["longitude"]}')


def add_client(lista: list) -> None:
    client_name = input('Podaj imie: ')
    client_surname = input('podaj nazwisko: ')
    location = input('Podaj miejscowosc: ')
    latitude, longitude = get_coordinates(location)
    if latitude and longitude:
        lista.append({
            'name': client_name,
            'surname': client_surname,
            'location': location,
            'latitude': str(latitude),
            'longitude': str(longitude)
        })


def remove_client(clients: list[dict[str, str]]) -> None:
    client_name = input('kogo usunąć?: ')
    for client in clients[1:]:
        if client['name'] == client_name:
            print(f'znaleziono uzytkownika {client["name"]} ')
            clients.remove(client)


def update_client(clients: list[dict[str, str]]) -> None:
    client_name = input('kogo zaktualizować?: ')
    for client in clients[1:]:
        if client['name'] == client_name:
            client['name'] = input('podaj nowe imie: ')
            client['surname'] = input('podaj nowe nazwisko: ')
            location = input('podaj nowa miejscowosc: ')
            latitude, longitude = get_coordinates(location)
            if latitude and longitude:
                client['location'] = location
                client['latitude'] = str(latitude)
                client['longitude'] = str(longitude)


def show_worker(workers: list[dict[str, str]]) -> None:
    for worker in workers[1:]:
        print(
            f'klient {worker["name"]}, miejscowosc {worker["location"]}, szerokosc geograficzna {worker["latitude"]}, {worker["longitude"]}')


def add_worker(lista: list) -> None:
    worker_name = input('Podaj imie: ')
    worker_surname = input('podaj nazwisko: ')
    location = input('Podaj miejscowosc: ')
    latitude, longitude = get_coordinates(location)
    if latitude and longitude:
        lista.append({
            'name': worker_name,
            'surname': worker_surname,
            'location': location,
            'latitude': str(latitude),
            'longitude': str(longitude)
        })


def remove_worker(workers: list[dict[str, str]]) -> None:
    worker_name = input('kogo usunąć?: ')
    for worker in workers[1:]:
        if worker['name'] == worker_name:
            print(f'znaleziono uzytkownika {worker["name"]} ')
            workers.remove(worker)


def update_worker(workers: list[dict[str, str]]) -> None:
    worker_name = input('kogo zaktualizować?: ')
    for worker in workers[1:]:
        if worker['name'] == worker_name:
            worker['name'] = input('podaj nowe imie: ')
            worker['surname'] = input('podaj nowe nazwisko: ')
            location = input('podaj nowa miejscowosc: ')
            latitude, longitude = get_coordinates(location)
            if latitude and longitude:
                worker['location'] = location
                worker['latitude'] = str(latitude)
                worker['longitude'] = str(longitude)


def show_companies(companies: list[dict[str, str]]) -> None:
    for company in companies[1:]:
        print(
            f'klient {company["name"]}, miejscowosc {company["location"]}, szerokosc geograficzna {company["latitude"]}, {company["longitude"]}')


def add_company(lista: list) -> None:
    company_name = input('Podaj nazwe firmy: ')
    location = input('Podaj miejscowosc: ')
    latitude, longitude = get_coordinates(location)
    if latitude and longitude:
        lista.append({
            'name': company_name,
            'location': location,
            'latitude': str(latitude),
            'longitude': str(longitude)
        })


def remove_company(companies: list[dict[str, str]]) -> None:
    company_name = input('ktora firme usunac? ')
    for company in companies[1:]:
        if company['name'] == company_name:
            print(f'znaleziono firme {company["name"]} ')
            companies.remove(company)


def update_company(companies: list[dict[str, str]]) -> None:
    company_name = input('ktora firme zaktualizowac ')
    for company in companies[1:]:
        if company['name'] == company_name:
            company['name'] = input('podaj nowe imie: ')
            location = input('podaj nowa miejscowosc: ')
            latitude, longitude = get_coordinates(location)
            if latitude and longitude:
                company['location'] = location
                company['latitude'] = str(latitude)
                company['longitude'] = str(longitude)









def show_client(clients: list[dict[str, str]]) -> None:
    for client in clients[1:]:
        print(f'klient {client["name"]}, location {client["location"]}, latitude {client["latitude"]}, {client["longitude"]}')

def add_client(lista: list) -> None:
    client_name = input('Podaj imie: ')
    client_surname = input('podaj nazwisko: ')
    lista.append({'name': client_name, 'surname': client_surname,})

def remove_client(clients: list[dict[str, str]]) -> None:
    client_name = input('kogo usunąć?: ')
    for client in clients[1:]:
        if client['name'] == client_name:
            print(f'znaleziono uzytkownika {client['name']} ')
            clients.remove(client)
def update_client(clients: list[dict[str, str]]) -> None:
    client_name = input('kogo zaktualizować?: ')
    for client in clients[1:]:
        if client['name'] == client_name:
            client['name'] = input('podaj nowe imie')
            client['surname'] = input('podaj nowe nazwisko')
            client['location'] = input('podaj nowa miejscowosc')
            client['latitude'] = input('podaj nowa latitude')
            client['longitude'] = input('podaj nowa longitude')


def show_worker(workers: list[dict[str, str]]) -> None:
    for worker in workers[1:]:
        print(f'klient {worker["name"]}, miejscowosc {worker["miejscowosc"]}, szerokosc geograficzna {worker["latitude"]}, {worker["longitude"]}')

def add_worker(lista: list) -> None:
    worker_name = input('Podaj imie: ')
    worker_surname = input('podaj nazwisko: ')
    lista.append({'name': worker_name, 'surname': worker_surname,})

def remove_worker(workers: list[dict[str, str]]) -> None:
    worker_name = input('kogo usunąć?: ')
    for worker in workers[1:]:
        if worker['name'] == worker_name:
            print(f'znaleziono uzytkownika {worker['name']} ')
            workers.remove(worker)

def update_worker(workers: list[dict[str, str]]) -> None:
    worker_name = input('kogo zaktualizować?: ')
    for worker in workers[1:]:
        if worker['name'] == worker:
            worker['name'] = input('podaj nowe imie')
            worker['surname'] = input('podaj nowe nazwisko')
            worker['location'] = input('podaj nowa miejscowosc')
            worker['latitude'] = input('podaj nowa latitude')
            worker['longitude'] = input('podaj nowa longitude')

def show_companies(companies: list[dict[str, str]]) -> None:
    for company in companies[1:]:
        print(f'klient {company["name"]}, miejscowosc {company["miejscowosc"]}, szerokosc geograficzna {company["latitude"]}, {company["longitude"]}')

def add_company(lista: list) -> None:
    company_name = input('Podaj nazwe firmy: ')

    lista.append({'name': company_name,})
def remove_company(companies: list[dict[str, str]]) -> None:
    company_name = input('ktora firme usunac? ')
    for company in companies[1:]:
        if company['name'] == company:
            print(f'znaleziono firme {company['name']} ')
            companies.remove(company)
def update_company(companies: list[dict[str, str]]) -> None:
    company_name = input('ktora firme zaktualizowac ')
    for company in companies[1:]:
        if company['name'] == company_name:
            company['name'] = input('podaj nowe imie')
            company['location'] = input('podaj nowa miejscowosc')
            company['latitude'] = input('podaj nowa szerokosc')
            company['longitude'] = input('podaj nowa dlugosc')


import requests
from bs4 import BeautifulSoup

def get_coordinates(location):
    url: str = f"https://pl.wikipedia.org/wiki/{location}"
    response = requests.get(url)
    response_html = BeautifulSoup(response.text, 'html.parser')
    latitude = float(response_html.select('.latitude')[1].text.replace(",", "."))
    longitude = float(response_html.select('.longitude')[1].text.replace(",", "."))



customers: list[dict] = [
    {"name": "Staś", "surname": "Grzymski",  "location":"Konin", 'latitdue': 18.234, 'longitude': 16.422, "my_company" :"budpol" },
    {"name": "Kacper", "surname": "Macioch", "location":"Ząbki", 'latitdue': 15.234, 'longitude': 18.422, "my_company" :"januszbud" },
    {"name": "Michał", "surname": "Krzywiński", "location":'Brodnica', 'latitdue': 11.234, 'longitude': 17.422, "my_company" :"januszbud" },
    {"name": "Tymon", "surname": "Leszczyc",  "location":"Toruń", 'latitdue': 16.234, 'longitude': 13.422, "my_company" :"mirbudex" },
    {"name": "Michał", "surname": "Lębryk",  "location":"Lublin", 'latitdue': 14.234, 'longitude': 12.422, "my_company" :"markwork" },
]

employees: list[dict] = [
    {"name": "Ivan", "surname": "Skolsky", "location":"Konin", 'latitdue': 10.234, 'longitude': 14.422, "work_place" : "budpol"},
    {"name": "Michael", "surname": "Macioch",  "location":"Ząbki", 'latitdue': 11.234, 'longitude': 12.422, "work_place" : "mixbud"},
    {"name": "Sasha", "surname": "mikrkov", "location":"Brodnica", 'latitdue': 13.234, 'longitude': 15.422, "work_place" : "budpol"},
    {"name": "fredrich", "surname": "julak", "location":"Toruń", 'latitdue': 13.234, 'longitude': 17.422, "work_place" : "markwork"},
    {"name": "Szymon", "surname": "Lębryk", "location":"Lublin", 'latitdue': 18.234, 'longitude': 19.422, "work_place" : "budpol"},
]

companies: list[dict] = [
    {"name": "budpol","location":"Konin", 'latitdue': 11.234, 'longitude': 14.422, "company" : "budpol"},
    {"name": "januszbud","location":"Ząbki", 'latitdue': 14.234, 'longitude': 16.422, "company" : "januszbud"},
    {"name": "mirbudex", "location":"Brodnica", 'latitdue': 16.234, 'longitude': 14.422, "company" : "mirbudex"},
    {"name": "mixbud", "location":"Toruń", 'latitdue': 14.234, 'longitude': 13.422, "company" : "mixbud"},
    {"name": "markwork", "location":"Lublin", 'latitdue': 16.234, 'longitude': 12.422, "company" : "markwork"},
]