# Selenium + pytest UI Test Framework

![tests](https://github.com/YOUR-USERNAME/selenium-pytest-framework/actions/workflows/tests.yml/badge.svg)

Automated UI tests for the public demo shop [saucedemo.com](https://www.saucedemo.com), built with Python, Selenium and pytest using the Page Object Model.

## What is covered
- **Login:** valid login plus four negative cases (locked-out user, wrong password, missing username, missing password)
- **Inventory:** product count, sort by price and by name
- **Cart:** add items, verify cart contents, remove items

## Stack
Python 3.12 · Selenium 4 · pytest · pytest-html · GitHub Actions

## Project structure
```
pages/       Page objects (locators and actions per page)
tests/       Test cases, grouped by feature
conftest.py  Browser fixture, shared fixtures, screenshot on failure
.github/     CI workflow
```

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest                           # headless
pytest --headed                  # visible browser
pytest -m smoke                  # smoke tests only
```
Requires Google Chrome. The matching driver is downloaded automatically.

## Reports
Every run writes an HTML report to `reports/report.html`. Failed tests also save a screenshot to `reports/screenshots/`.

## CI
GitHub Actions runs the full suite on every push and pull request, and uploads the report as a build artifact.

## Design notes
- Explicit waits only, no `time.sleep`
- Locators live in page objects, never in tests
- Tests are independent and each starts from a fresh browser
