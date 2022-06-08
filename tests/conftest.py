import pytest

def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="http://localhost:5000")

@pytest.fixture(scope='session')
def url(request):
    name_value = request.config.option.url
    if name_value is None:
        pytest.skip()
    return name_value    