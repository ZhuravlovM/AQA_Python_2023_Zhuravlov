import pytest
from lesson24_api.infrastructure.people_service import PeopleService


@pytest.fixture()
def people_service():
    yield PeopleService()
