# StoreDemo TestDino Automation Project

## Description
Automation testing project using Python and Playwright.

## Technologies
- Python
- Playwright
- Pytest
- Page Object Model (POM)

## Automated Test Cases
1. Home validation
2. Valid login
3. Add product to cart

## Project Structure

pages/
- home_page.py
- login_page_td.py
- cart_page.py

tests/
- home_test.py
- login_valid_test.py
- cart_test.py

## Requirements

Install dependencies:

pip install -r requirements.txt

Install Playwright browsers:

playwright install

## Run Tests

Run Home Test:

python tests/home_test.py

Run Login Test:

python tests/login_valid_test.py

Run Cart Test:

python tests/cart_test.py

## Features
- Assertions
- Automatic screenshots
- Error handling
- Playwright automation