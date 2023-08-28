import pytest
from lesson18_pytests_locators.code_for_testing import Human


@pytest.fixture
def human():
    print('setup for test')
    yield Human('Joshua',25,'black')
    print('teardown for test')