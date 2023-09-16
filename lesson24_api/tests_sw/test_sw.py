import pytest
from lesson24_api.test_data.people_test_data import test_data, expected_data
from lesson24_api.infrastructure.people import People

ids = 'test_id, expect_id'


def test_test_luke(people_service):
    response = people_service.get_people("1")
    assert response.json()['name'] == 'Luke Skywalker'


def create_keys():
    list_of_cort = []
    for i in range(len(test_data)):
        list_of_cort.append((list(test_data.values())[i], list(expected_data.values())[i]))
    return list_of_cort


@pytest.mark.parametrize(ids, create_keys())
def test_test_multiply_person(people_service, test_id, expect_id):
    response = people_service.get_people(test_id)
    assert response.json() == expect_id


def test_luke_with_fixture(people_service, first_people1):
    response = people_service.get_people("1")
    actual_people = People(**response.json())
    print(actual_people.__dict__)
    print(first_people1.__dict__)
    assert actual_people == first_people1
