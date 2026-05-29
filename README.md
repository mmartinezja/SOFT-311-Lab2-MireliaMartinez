# StoreDemo TestDino Automation Project

## Description

QA Automation project developed using Python, Playwright and Pytest.

The project automates functional test cases for the StoreDemo TestDino application using the Page Object Model (POM) design pattern.

The framework includes automated assertions, screenshot evidence generation, and HTML reporting.

---

## Technologies

* Python
* Playwright
* Pytest
* pytest-html
* Page Object Model (POM)

---

## Automated Functional Test Cases

1. Home validation
2. Valid login
3. Invalid login
4. Add product to cart
5. Add product to favorites

---

## Project Structure

```text
pages/
├── home_page.py
├── login_page_td.py
├── cart_page.py
└── favorites_page.py

tests/
├── assertions.py
├── home_test.py
├── login_valid_test.py
├── login_invalid_test.py
├── cart_test.py
└── favorites_test.py

artifacts/
└── screenshots/

report.html
requirements.txt
README.md
```

---

## Features

* Playwright browser automation
* Page Object Model (POM)
* Automated assertions
* Automatic screenshot generation on failures
* Success screenshots for test evidence
* HTML report generation
* Error handling and validation

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Playwright Browsers

```bash
playwright install
```

---

## Run All Tests

```bash
pytest -v
```

---

## Generate HTML Report

```bash
pytest -v --html=report.html --self-contained-html
```

The report will be generated in the project root:

```text
report.html
```

---

## Test Evidence

Successful executions generate screenshots in:

```text
artifacts/screenshots/
```

Examples:

```text
home_success.png
cart_success.png
favorites_success.png
login_success.png
login_invalid_success.png
```

Assertion failures automatically generate timestamped screenshots for troubleshooting.

---

## Results

Current automated test suite:

* Total Tests: 5
* Passed: 5
* Failed: 0

All test cases execute successfully using Playwright and Pytest.
