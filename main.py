from Logic.crud import create
from Tests.test_crud import test_crud
from Tests.test_functionalitati import test_functionalitati
from Userinterface.console import run_ui


def main():
    vanzari = []
    vanzari = create(vanzari, 1, 'Book1', 'SF', 100, 'gold')
    vanzari = create(vanzari, 2, 'Book2', 'drama', 75, 'silver')
    vanzari = create(vanzari, 3, 'Book3', 'crima', 50, 'none')
    vanzari = create(vanzari, 4, 'Book4', 'SF', 45, 'gold')
    vanzari = create(vanzari, 5, 'Book5', 'Thirller', 150, 'silver')
    vanzari = run_ui(vanzari)


if __name__ == '__main__':
    test_crud()
    test_functionalitati()
    main()
