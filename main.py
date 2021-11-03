from Logic.crud import create
from Tests.test_crud import test_crud
from Tests.test_discount import test_discount
from Tests.test_modificare_gen import test_modificare_gen
from Userinterface.console import run_ui


def main():
    vanzari = []
    vanzari = create(vanzari, 1, 'Ion', 'roman', 100, 'gold')
    vanzari = create(vanzari, 2, 'Enigma Otiliei', 'roman', 75, 'silver')
    vanzari = create(vanzari, 3, 'Baltagul', 'roman', 50, 'none')
    vanzari = create(vanzari, 4, 'O scrisoare pierduta', 'comedie', 45, 'gold')
    vanzari = create(vanzari, 5, 'Moara cu noroc', 'nuvela', 150, 'silver')
    vanzari = run_ui(vanzari)


if __name__ == '__main__':
    test_crud()
    test_discount()
    test_modificare_gen()
    main()
