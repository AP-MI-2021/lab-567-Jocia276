# modificarea genului pentru un titlu dat
from Domain.vanzare2 import get_titlu, get_id, get_pret, get_reducere, creeaza_vanzare


def modificare_gen(lst_vanzari, titlul, gen_nou):
    """
    Modifica genul unei carti in functie de un titlu dat de la tastatura.
    :param lst_vanzari: lista de vanzari
    :param titlul: titlul cartii care se introduce de la tastatura. Acesta trebuie sa existe in lista.
    :param gen_nou: Noul gen al cartii ce se modifica. Si acesta va fi introdus de la tastatura
    :return: O noua lista de vanzari ce contine noul gen al cartii.
    """

    if titlul == '':
        raise ValueError('Titlul cartii careia vrem sa ii modificam genul nu poate fi gol.')

    result = []

    for vanzare in lst_vanzari:
        if titlul == get_titlu(vanzare):
            result.append(creeaza_vanzare(
                get_id(vanzare),
                get_titlu(vanzare),
                gen_nou,
                get_pret(vanzare),
                get_reducere(vanzare)
            ))
        else:
            result.append(vanzare)

    return result
