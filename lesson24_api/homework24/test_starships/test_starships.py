import pytest
from lesson24_api.homework24.test_data_starships.starships_test_data import test_data, expected_data

ids = 'test_id, expect_id'


def test_cr90_corvette(starships_service):
    response = starships_service.get_starship("2")
    assert response.json()['name'] == 'CR90 corvette'


def test_star_destroyer(starships_service):
    response = starships_service.get_starship("3")
    assert response.json()['name'] == 'Star Destroyer'


def test_sentinel_class_landing_craft(starships_service):
    response = starships_service.get_starship("5")
    assert response.json()['name'] == 'Sentinel-class landing craft'


def create_keys():
    list_of_cort = []
    for i in range(len(test_data)):
        list_of_cort.append((list(test_data.values())[i], list(expected_data.values())[i]))
    return list_of_cort


@pytest.mark.parametrize(ids, create_keys())
def test_test_multiple_starships(starships_service, test_id, expect_id):
    response = starships_service.get_starship(test_id)
    assert response.json() == expect_id
