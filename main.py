from Logic.crud import create
from Tests.test_crud import test_crud
from Tests.test_discount import test_discount
from Tests.test_modificare_gen import test_modificare_gen
from Userinterface.console2 import run_ui2


def main():
    vanzari = []
    vanzari = create(vanzari, 1, 'Ion', 'roman', 100, 'gold')
    vanzari = create(vanzari, 2, 'Moara cu noroc', 'nuvela', 50, 'silver')
    vanzari = create(vanzari, 3, 'Enigma Otiliei', 'roman balzacian', 50, 'silver')
    vanzari = create(vanzari, 4, 'Ion', 'povestire', 50, 'silver')
    vanzari = create(vanzari, 5, 'Ion', 'comedie', 50, 'silver')
    run_ui2(vanzari)


if __name__ == '__main__':
    test_crud()
    test_discount()
    test_modificare_gen()
    main()
