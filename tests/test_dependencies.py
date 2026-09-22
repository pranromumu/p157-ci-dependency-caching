import pytest
import requests

def test_pytest_available():
    assert pytest.__name__ == "pytest"

def test_requests_available():
    # This proves the dependency from requirements.txt was installed
    assert requests.__name__ == "requests"