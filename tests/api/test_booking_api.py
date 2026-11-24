"""CRUD + auth tests for Restful-Booker (https://restful-booker.herokuapp.com/apidoc)."""
import pytest

pytestmark = pytest.mark.api


@pytest.mark.smoke
def test_health_check(booker_api):
    # Restful-Booker documents 201 Created for /ping
    assert booker_api.get("/ping").status_code == 201


@pytest.mark.regression
def test_auth_with_invalid_credentials(booker_api):
    response = booker_api.post("/auth", json={"username": "admin", "password": "wrong"})

    # The API returns 200 with an error message instead of 401 — documented in docs/bug-report-example.md
    assert response.status_code == 200
    assert response.json() == {"reason": "Bad credentials"}


@pytest.mark.smoke
def test_create_booking(booker_api, booking_payload):
    response = booker_api.post("/booking", json=booking_payload)

    assert response.status_code == 200
    body = response.json()
    assert isinstance(body["bookingid"], int)
    assert body["booking"] == booking_payload


@pytest.mark.regression
def test_get_created_booking(booker_api, created_booking, booking_payload):
    response = booker_api.get(f"/booking/{created_booking}")

    assert response.status_code == 200
    assert response.json() == booking_payload


@pytest.mark.regression
def test_update_booking_with_token(booker_api, booker_token, created_booking, booking_payload):
    updated = {**booking_payload, "totalprice": 999, "additionalneeds": "Late checkout"}

    response = booker_api.put(f"/booking/{created_booking}", json=updated,
                              headers={"Cookie": f"token={booker_token}"})

    assert response.status_code == 200
    assert response.json()["totalprice"] == 999


@pytest.mark.regression
def test_update_booking_without_token_is_forbidden(booker_api, created_booking, booking_payload):
    response = booker_api.put(f"/booking/{created_booking}", json=booking_payload)

    assert response.status_code == 403


@pytest.mark.regression
def test_delete_booking(booker_api, booker_token, created_booking):
    delete = booker_api.delete(f"/booking/{created_booking}", headers={"Cookie": f"token={booker_token}"})
    assert delete.status_code == 201  # API quirk: returns 201 instead of 204

    assert booker_api.get(f"/booking/{created_booking}").status_code == 404


@pytest.mark.regression
def test_filter_bookings_by_name(booker_api, created_booking):
    response = booker_api.get("/booking", params={"firstname": "Ihor", "lastname": "Koval"})

    assert response.status_code == 200
    ids = [b["bookingid"] for b in response.json()]
    assert created_booking in ids
