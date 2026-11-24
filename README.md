# QA Automation Portfolio — Python · Pytest · Selenium · Requests

![Automated tests](https://github.com/Kyzmichik/qa-automation-portfolio/actions/workflows/tests.yml/badge.svg)

Test automation project by **Ihor Koval** (QA Engineer, Valencia, Spain).  
It shows UI and API test automation built with Python, using practices from real QA work:
Page Object Model, explicit waits, data-driven tests, smoke/regression suites, and CI.

## What is tested

| Suite | Application | What is covered |
|-------|-------------|-----------------|
| **UI** (Selenium) | [SauceDemo](https://www.saucedemo.com) — demo online shop | Login (positive + negative), access control, cart, sorting, checkout form validation, order total, full E2E purchase |
| **API** (requests) | [JSONPlaceholder](https://jsonplaceholder.typicode.com) | GET / POST / PUT / DELETE, response schema, filtering, 404 handling |
| **API** (requests) | [Restful-Booker](https://restful-booker.herokuapp.com/apidoc) | Token auth, full CRUD of bookings, 403 without token, search by name |

## Tech stack
- **Python 3.12**, **pytest** — test runner, fixtures, parametrization, markers
- **Selenium 4** — browser automation (Chrome, headless by default)
- **requests** — REST API testing
- **pytest-html** — HTML test reports
- **GitHub Actions** — tests run automatically on every push and weekly

## Project structure
```
├── pages/              # Page Object Model: one class per page
├── tests/
│   ├── ui/             # Selenium tests
│   └── api/            # REST API tests
├── utils/              # config and API client
├── docs/
│   ├── test-cases.md          # manual test cases linked to automated tests
│   └── bug-report-example.md  # example of a bug report
├── conftest.py         # browser fixture, screenshot on failure
└── .github/workflows/  # CI pipeline
```

## How to run locally
```bash
git clone https://github.com/Kyzmichik/qa-automation-portfolio.git
cd qa-automation-portfolio
python -m venv .venv
.venv\Scripts\activate          # Windows  (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt

pytest                          # all tests
pytest -m api                   # API tests only
pytest -m ui --headed           # UI tests with a visible browser
pytest -m smoke                 # critical path only
pytest --html=reports/report.html --self-contained-html   # HTML report
```
Requires Google Chrome installed. Selenium downloads the matching driver automatically.

## Practices used
- **Page Object Model** — locators and page actions are separate from test logic
- **Explicit waits** (`WebDriverWait`) — no `time.sleep()`, stable tests
- **Data-driven tests** with `@pytest.mark.parametrize` (negative login, form validation, sorting)
- **Fixtures** for preconditions (logged-in user, item in cart, created booking, auth token)
- **Markers** `smoke` / `regression` / `ui` / `api` to run the right suite before a release
- **Screenshot on failure** for fast bug reproduction
- **Schema checks** for API responses
- Manual **test cases** and a **bug report** in `docs/` — linked to the automated tests
