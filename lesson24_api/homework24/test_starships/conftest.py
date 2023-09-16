import pytest
from lesson24_api.homework24.infrastructure_starships.starships_service import StarshipsService


@pytest.fixture()
def starships_service():
    yield StarshipsService()
