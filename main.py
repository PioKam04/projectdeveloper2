from utils.crud import show_company, show_customer, show_employee, add_new_company, add_new_customer, add_new_employee, \
    update_company, update_customer, update_employee, remove_company, remove_customer, remove_employee, \
    map_single_company, map_single_customer, map_single_employee, map_all_companies, map_all_customers, \
    map_all_employees, assign_customers_to_companies, assign_employees_to_companies
from models.data import companies, customers, employees

if __name__ == '__main__':
    print('Logowanie')
    print('Login: Sentencja zyciowa nr 1')
    print('Haslo: Sentencja zyciowa nr 2')
    print('')

    Login = "geomatykaislove"
    Haslo = "geomatykaislife"
    login: str = input("Podaj Sentencja zyciowa nr 1:")
    haslo: str = input("Podaj Sentencja zyciowa nr 2:")
    if Login == login and Haslo == haslo:
        print("Doskonale sentencje zyciowe")
    else:
        print("Zle motto zyciowe")
        login: str = input("Podaj Sentencja zyciowa nr 1:")
        haslo: str = input("Podaj Sentencja zyciowa nr 2:")

while True:
    print('0. zakoncz program ')
    print('1. wyswietl biura nieruchomosci ')
    print('2. dodaj biuro nieruchomosci ')
    print('3. usun biuro nieruchomosci ')
    print('4. biuro nieruchomosci do aktualizacji')
    print('5. mapa pokazujaca jedna biuro nieruchomosci ')
    print('6. mapa wszystkich biuro nieruchomosci ')
    print('')
    print('11. wyswietl klientow')
    print('12. dodaj klienta')
    print('13. usun klienta')
    print('14. klient do aktualizacji')
    print('15. mapa pokazujaca jednego pracownika')
    print('16. mapa wszystkich pracownikow')
    print('17. lista klientow i biur nieruchomosci')
    print('')
    print('21. wyswietl pracownikow')
    print('22. dodaj pracownika')
    print('23. usun pracownika')
    print('24. pracownik do aktualizacji')
    print('25. mapa pokazujaca jednego klienta')
    print('26. mapa wszystkich klientow')
    print('27. lista pracownikow i miejsca ich pracy')

    menu_option = input('wybierz opcje menu: ')
    if menu_option == '0': break
    if menu_option == '1': show_company(companies)
    if menu_option == '2': add_new_company(companies)
    if menu_option == '3': remove_company(companies)
    if menu_option == '4': update_company(companies)
    if menu_option == '5': map_single_company(companies)
    if menu_option == '6': map_all_companies(companies)
    if menu_option == '11': show_customer(customers)
    if menu_option == '12': add_new_customer(customers)
    if menu_option == '13': remove_customer(customers)
    if menu_option == '14': update_customer(customers)
    if menu_option == '15': map_single_customer(customers)
    if menu_option == '16': map_all_customers(customers)
    if menu_option == '17': assign_customers_to_companies(companies, customers)
    if menu_option == '21': show_employee(employees)
    if menu_option == '22': add_new_employee(employees)
    if menu_option == '23': remove_employee(employees)
    if menu_option == '24': update_employee(employees)
    if menu_option == '25': map_single_employee(employees)
    if menu_option == '26': map_all_employees(employees)
    if menu_option == '27': assign_employees_to_companies(companies, employees)