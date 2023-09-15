import json

import lesson25_resful_api.infrastructure as infra


def test_get_object():
    assert infra.get_an_object(4).status_code == 200


def test_create_an_object():
    response, obj_id = infra.create_an_object()
    get_response = infra.get_an_object(obj_id)
    assert response.status_code == 200
    assert get_response.status_code == 200
    print(get_response.json())


def test_update_obj():
    response, obj_id = infra.create_an_object()
    infra.update_an_object(obj_id, )