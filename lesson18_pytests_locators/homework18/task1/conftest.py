import pytest
from code_for_testing import JSONConverter


@pytest.fixture
def json_converter():
    return JSONConverter()
