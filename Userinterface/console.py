from Domain.vanzare import get_str, creeaza_vanzare
from Logic.crud import create, update, delete


def show_menu():
    print('1. CRUD')
    print('2. Aplicare discount de 5% pentru toate reducerile silver, si 10% pentru toate reducerile gold.')
    print('x. Exit')


def handle_add(vanzari):
    id_vanzare = int(input("Dati id-ul vanzarii: "))
    titlu_carte = input("Dati titlul cartii: ")
    gen_carte = input("Dati genul cartii: ")
    pret = float(input("Dati pretul vanzarii: "))
    tip_reducere_client = input("Dati tipul de reducere acordata clientului: ")
    return create(vanzari, id_vanzare, titlu_carte, gen_carte, pret, tip_reducere_client)


def handle_update(vanzari):
    id_vanzare = int(input("Dati id-ul vanzarii care se actualizeaza: "))
    titlu_carte = input("Dati noul titlu al cartii: ")
    gen_carte = input("Dati noul gen al cartii: ")
    pret = float(input("Dati noul pret al vanzarii: "))
    tip_reducere_client = input("Dati noul tip de reducere acordata clientului: ")
    print('Modificarea a fost efectuata cu succes!')
    return update(vanzari, creeaza_vanzare(id_vanzare, titlu_carte, gen_carte, pret, tip_reducere_client))


def handle_delete(vanzari):
    id_vanzare = int(input("Dati id-ul vanzarii care se va sterge: "))
    vanzari = delete(vanzari, id_vanzare)
    print('Stergerea a fost efectuata cu succes!')
    return vanzari



def handle_crud(vanzari):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('a. Afisare')
        print('b. Revenire')

        optiune = input("Alege optiunea: ")
        if optiune == '1':
            vanzari = handle_add(vanzari)
        elif optiune == '2':
            vanzari = handle_update(vanzari)
        elif optiune == '3':
            vanzari = handle_delete(vanzari)
        elif optiune == 'a':
            handle_show_all(vanzari)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida!')
    return vanzari


def handle_show_all(vanzari):
    for vanzare in vanzari:
        print(get_str(vanzare))


def run_ui(vanzari):
    while True:
        show_menu()
        optiune = input("Alege optiunea: ")
        if optiune == '1':
            vanzari = handle_crud(vanzari)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida!')
    return vanzari



