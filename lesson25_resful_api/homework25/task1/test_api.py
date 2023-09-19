import requests
import lesson25_resful_api.homework25.task1.infrastructure as infra


def test_get_single_object_7():
    response = infra.get_single_object(7)
    assert response.status_code == 200
    expected_data = {
        "id": "7",
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    actual_data = response.json()
    assert actual_data == expected_data


def test_get_single_object_2():
    response = infra.get_single_object(2)
    assert response.status_code == 200
    assert "Apple iPhone 12 Mini, 256GB, Blue" in response.text


def test_add_object_6():
    data = {
        "name": "Apple AirPods",
        "data": {
            "color": "white",
            "generation": "3rd",
            "price": 135
        }
    }
    response, created_object_id = infra.add_object(data)
    get_response = infra.get_single_object(created_object_id)
    assert response.status_code == 200
    assert get_response.status_code == 200
    print(get_response.json())
