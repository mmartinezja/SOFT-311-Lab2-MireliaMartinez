# StoreDemo TestDino Automation Project

## Description

QA Automation project developed using Python, Playwright and Pytest.

The project automates functional test cases for the StoreDemo TestDino application using the Page Object Model (POM) design pattern.

## Technologies

* Python
* Playwright
* Pytest
* pytest-html
* Page Object Model (POM)

## Automated Test Cases

### Positive Test Cases

1. Home validation
2. About Us navigation
3. Contact Us form submission
4. All Products page validation
5. Valid login
6. Sign Up
7. Add product to cart
8. Add product to favorites

### Negative Test Cases

1. Invalid login
2. Contact Us without Subject
3. Contact Us without Message
4. Sign Up with invalid email
5. Sign Up without password

## Project Structure

```text
pages/
│
├── home_page.py
├── about_us_page.py
├── contact_page.py
├── all_products_page.py
├── login_page_td.py
├── signup_page.py
├── cart_page.py
└── favorites_page.py

tests/
│
├── home_test.py
├── about_us_test.py
├── contact_us_test.py
├── all_products_test.py
├── login_valid_test.py
├── login_invalid_test.py
├── signup_test.py
├── signup_invalid_email_test.py
├── signup_no_password_test.py
├── cart_test.py
├── favorites_test.py
├── contact_us_no_subject_test.py
└── contact_us_no_message_test.py

report.html
README.md
```

## Features

* Functional test automation
* Positive and negative test scenarios
* Assertions and validations
* Automatic screenshots
* HTML report generation
* Error handling
* Playwright browser automation
* Page Object Model architecture

## Installation

Install project dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

## Running Tests

Run all tests:

```bash
pytest tests/ -v
```

Run a specific test:

```bash
pytest tests/signup_test.py -v
```

## Generate HTML Report

```bash
pytest tests/ --html=report.html --self-contained-html
```

## Deliverables

* Automated functional test scripts
* Positive and negative test cases
* Execution screenshots
* HTML report
* Updated README
* GitHub repository

## Results

* Positive Test Cases: 8
* Negative Test Cases: 5
* Total Automated Test Cases: 13

```
```
