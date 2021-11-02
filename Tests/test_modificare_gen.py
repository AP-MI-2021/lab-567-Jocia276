from Domain.vanzare2 import get_gen
from Logic.crud import create, read
from Logic.modificare_gen import modificare_gen


def test_modificare_gen():

    vanzari = []
    vanzari = create(vanzari, 1, 'Ion', 'roman ', 50, 'silver')
    vanzari = modificare_gen(vanzari, 'Ion', 'roman obiectiv')

    vanzari2 = []
    vanzari2 = create(vanzari2, 2, 'Baltagul', 'roman traditional', 100, 'silver')
    vanzari2 = create(vanzari2, 3, 'Enigma Otiliei', 'roman ', 50, 'gold')
    vanzari2 = modificare_gen(vanzari2, 'Baltagul', 'nuvela')

    assert get_gen(read(vanzari, 1)) == 'roman obiectiv'
    assert get_gen(read(vanzari2, 2)) == 'nuvela'
