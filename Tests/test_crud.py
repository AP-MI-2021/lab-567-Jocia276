from Domain.vanzare import creeaza_vanzare, get_id
from Logic.crud import create, read, update, delete


def get_data():
    return [
        creeaza_vanzare(1, 'v1', 'SF', 50, 'silver'),
        creeaza_vanzare(2, 'v2', 'Thriller', 45.5, 'gold'),
        creeaza_vanzare(3, 'v3', 'Drama', 23, 'none'),
        creeaza_vanzare(4, 'v4', 'Stiinta', 100, 'silver'),
        creeaza_vanzare(5, 'v5', 'Crima', 35, 'none'),
    ]


def test_create():
    vanzari = get_data()
    params = (27, 'vnew', 'SF', 57, 'gold')
    v_new = creeaza_vanzare(*params)
    new_vanzari = create(vanzari, *params)

    found = False
    for vanzare in new_vanzari:
        if vanzare == v_new:
            found = True
    assert found


def test_read():
    vanzari = get_data()
    some_v = vanzari[2]
    assert read(vanzari, get_id(some_v)) == some_v
    #assert read(vanzari, None) == vanzari


def test_update():
    vanzari = get_data()
    v_updated = creeaza_vanzare(1, 'new title', 'Drama', 45, 'None')
    updated = update(vanzari, v_updated)
    assert v_updated in updated
    assert v_updated not in vanzari
    assert len(updated) == len(vanzari)


def test_delete():
    vanzari = get_data()
    to_delete = 3
    v_deleted = read(vanzari, to_delete)
    deleted = delete(vanzari, to_delete)
    assert v_deleted in vanzari
    assert v_deleted not in deleted
    assert len(deleted) == len(vanzari) - 1


def test_crud():
    test_delete()
    test_update()
    test_read()
    test_create()
