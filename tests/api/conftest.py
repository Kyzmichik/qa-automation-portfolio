import pytest

from utils.api_client import ApiClient
from utils.config import BOOKER_ADMIN, BOOKER_URL, JSONPLACEHOLDER_URL


@pytest.fixture(scope="session")
def posts_api() -> ApiClient:
    return ApiClient(JSONPLACEHOLDER_URL)


@pytest.fixture(scope="session")
def booker_api() -> ApiClient:
    return ApiClient(BOOKER_URL)


@pytest.fixture(scope="session")
def booker_token(booker_api) -> str:
    response = booker_api.post("/auth", json=BOOKER_ADMIN)
    assert response.status_code == 200
    return response.json()["token"]


@pytest.fixture
def booking_payload() -> dict:
    return {
        "firstname": "Ihor",
        "lastname": "Koval",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {"checkin": "2027-01-10", "checkout": "2027-01-15"},
        "additionalneeds": "Breakfast",
    }


@pytest.fixture
def created_booking(booker_api, booking_payload):
    """Creates a booking before the test and returns its id."""
    response = booker_api.post("/booking", json=booking_payload)
    assert response.status_code == 200
    return response.json()["bookingid"]
