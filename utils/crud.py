def show_client(clients: list[dict[str, str]]) -> None:
    for client in clients[1:]:
        print(f'klient {client["name"]}, miejscowosc {client["miejscowosc"]}, szerokosc geograficzna {client["latitude"]}, {client["longitude"]}')

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
            client['miejscowosc'] = input('podaj nowa miejscowosc')
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
            worker['miejscowosc'] = input('podaj nowa miejscowosc')
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
            company['surname'] = input('podaj nowe nazwisko')
            company['miejscowosc'] = input('podaj nowa miejscowosc')
            company['latitude'] = input('podaj nowa szerokosc')
            company['longitude'] = input('podaj nowa dlugosc')