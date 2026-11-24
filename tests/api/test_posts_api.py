"""REST API tests for JSONPlaceholder (https://jsonplaceholder.typicode.com)."""
import pytest

pytestmark = pytest.mark.api

POST_SCHEMA = {"userId": int, "id": int, "title": str, "body": str}


def assert_matches_schema(obj: dict, schema: dict):
    assert set(obj) == set(schema), f"Unexpected fields: {set(obj) ^ set(schema)}"
    for field, expected_type in schema.items():
        assert isinstance(obj[field], expected_type), f"{field} should be {expected_type.__name__}"


@pytest.mark.smoke
def test_get_all_posts(posts_api):
    response = posts_api.get("/posts")

    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]
    assert len(response.json()) == 100


@pytest.mark.regression
def test_get_single_post_schema(posts_api):
    response = posts_api.get("/posts/1")

    assert response.status_code == 200
    post = response.json()
    assert_matches_schema(post, POST_SCHEMA)
    assert post["id"] == 1


@pytest.mark.regression
def test_get_nonexistent_post_returns_404(posts_api):
    response = posts_api.get("/posts/99999")

    assert response.status_code == 404


@pytest.mark.regression
def test_filter_posts_by_user(posts_api):
    response = posts_api.get("/posts", params={"userId": 1})

    assert response.status_code == 200
    posts = response.json()
    assert posts, "Expected at least one post for userId=1"
    assert all(p["userId"] == 1 for p in posts)


@pytest.mark.smoke
def test_create_post(posts_api):
    payload = {"title": "QA portfolio", "body": "Created by an automated test", "userId": 1}

    response = posts_api.post("/posts", json=payload)

    assert response.status_code == 201
    created = response.json()
    assert created["title"] == payload["title"]
    assert created["body"] == payload["body"]
    assert "id" in created


@pytest.mark.regression
def test_update_post(posts_api):
    payload = {"id": 1, "title": "Updated title", "body": "Updated body", "userId": 1}

    response = posts_api.put("/posts/1", json=payload)

    assert response.status_code == 200
    assert response.json()["title"] == "Updated title"


@pytest.mark.regression
def test_delete_post(posts_api):
    response = posts_api.delete("/posts/1")

    assert response.status_code == 200
