from Domain.vanzare2 import creeaza_vanzare, get_str, get_titlu, get_gen, get_pret, get_reducere
from Logic.crud import create, update, delete, read
from Logic.discount import add_discount
from Logic.modificare_gen import modificare_gen


def show_menu2():
    print(' Comenzi: ')
    print(' add ')
    print(' delete ')
    print(' showall ')
    print(' update ')
    print(' details ')
    print(' pret minim ')
    print(' modificare gen ')
    print(' quit ')


def handle_details(vanzari, comanda):
    try:
        comanda[1] = int(comanda[1])
        carte = read(vanzari, comanda[1])
        print('Detaliile despre carte sunt: ')
        print(f'Titlul este {get_titlu(carte)}')
        print(f'Genul este {get_gen(carte)}')
        print(f'Pretul este {get_pret(carte)}')
        print(f'Tipul de reducere client este {get_reducere(carte)}')

    except ValueError as ve:
        print('Eroare: ', ve)


def handle_showall2(lista_vanzari):
    for vanzare in lista_vanzari:
        print(get_str(vanzare))

def handle_add2(lista_vanzari,comanda):
    try:
        comanda[1] = int(comanda[1])
        comanda[4] = int(comanda[4])
        vanzari = create(lista_vanzari, comanda[1], comanda[2], comanda[3], comanda[4], comanda[5])
        print('lista in urma adaugarii este ')
        handle_showall2(vanzari)
    except ValueError as ve:
        print('eroare ', ve)
    return lista_vanzari

def handle_delete2(lista_vanzari,comanda):
    try:
        comanda[1] = int(comanda[1])
        vanzari = delete(lista_vanzari, comanda[1])
        print('Lista in urma stergerii este ')
        handle_showall2(vanzari)
    except ValueError as ve:
        print('Eroare: ', ve)

def handle_update2(lista_vanzari, comanda):

    try:
        comanda[1] = int(comanda[1])
        comanda[4] = int(comanda[4])
        vanzare_noua = creeaza_vanzare(comanda[1], comanda[2], comanda[3], comanda[4], comanda[5])
        carti = update(lista_vanzari, vanzare_noua)
        print('Lista updatata este: ')
        handle_showall2(carti)

    except ValueError as ve:
        print('Eroare: ', ve)


def prelucrare_input(lista_comenzi):

    comenzi = lista_comenzi.split(sep=";")

    lst_comenzi = []
    for comanda in comenzi:
        comenzi_despartite_prin_spatiu = comanda.split(sep=",")
        lst_comenzi.append(comenzi_despartite_prin_spatiu)

    return lst_comenzi




def handle_read2(vanzari, id_vanzare):
    try:
        print(' ')
        result = read(vanzari, id_vanzare)
        if result is None:
            raise ValueError(f'Nu exista o cheltuiala cu ID-ul {id_vanzare} pe care sa o afisam')
        print(get_str(result))
    except ValueError as ve:
        print('Eroare: ', ve)


def handle_discount2(lista_vanzari, comanda):
    try:
        comanda[1] = int(comanda[1])
        lista_noua = add_discount(lista_vanzarit_vanzari, comanda)
        vanzari = add_discount(lista_vanzarivanzari)
    except ValueError as ve:
        print('Eroare: ', ve)
    return vanzari


def handle_modificare_gen2(lista_vanzari, comanda):
    try:
        comanda[1] = int(comanda[1])
        lista_noua = modificare_gen(lista_vanzari, comanda[2], comanda[3])
        print('Lista in urma modificarii genului este ')
        for vanzare in lista_noua:
            print(get_str(vanzare))
    except ValueError as ve:
        print('Eroare: ', ve)

def run_ui2(lista_vanzari):
    ok = True
    while ok == True:
        show_menu2()
        lista_comenzi = input('Dati comenzi despartite prin ; si parametrii prin , ')
        lista_cu_comenzi = prelucrare_input(lista_comenzi)

        for comanda in lista_cu_comenzi:
            if comanda[0] == 'delete':
                handle_delete2(lista_vanzari, comanda)
            elif comanda[0] == 'add':
                handle_add2(lista_vanzari, comanda)
            elif comanda[0] == 'showall':
                print('Lista de carti este: ')
                handle_showall2(lista_vanzari)
            elif comanda[0] == 'update':
                handle_update2(lista_vanzari, comanda)
            elif comanda[0] == 'details':
                handle_details(lista_vanzari, comanda)
            elif comanda[0] == 'add_discount':
                handle_discount2(lista_vanzari)
            elif comanda[0] == 'modificare gen':
                handle_modificare_gen2(lista_vanzari, comanda)
            elif comanda[0] == 'quit':
                ok = False
        if ok == False:
            break

