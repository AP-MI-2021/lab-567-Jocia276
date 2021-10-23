from Logic.crud import create
from Tests.test_crud import test_crud
from Userinterface.console import run_ui


def main():
    vanzari = []
    vanzari = create(vanzari, 1, 'Book1', 'SF', 25, 'gold')
    vanzari = run_ui(vanzari)

if __name__ == '__main__':
    test_crud()
    main()
