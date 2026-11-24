"""Central place for URLs and test data used across the suite."""
import os

UI_BASE_URL = os.getenv("UI_BASE_URL", "https://www.saucedemo.com")
JSONPLACEHOLDER_URL = os.getenv("JSONPLACEHOLDER_URL", "https://jsonplaceholder.typicode.com")
BOOKER_URL = os.getenv("BOOKER_URL", "https://restful-booker.herokuapp.com")

# Public demo credentials published on saucedemo.com
STANDARD_USER = "standard_user"
LOCKED_OUT_USER = "locked_out_user"
PASSWORD = "secret_sauce"

# Public demo credentials published in the restful-booker docs
BOOKER_ADMIN = {"username": "admin", "password": "password123"}

DEFAULT_TIMEOUT = 10
