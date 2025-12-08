# **ENGETO project 3 - Three automated tests**

## Project Description:
This project focuses on creating an automated UI test suite for the ROUVY web application using Python, Pytest, and Playwright.
The goal is to verify key website functionality, cover the main user scenarios, and ensure that essential parts of the site work correctly across different languages.
The tests were written for Chromium. For other browsers, selector and timeout adjustments may be required.

## Main Objectives of the Project:  
- Verify that the ROUVY homepage works correctly.  
- Test the Pricing section and validate the display of pricing plans.  
- Test language-switching functionality, including correct URL changes, translated texts, and element visibility.  
- Create a clear test structure using conftest.py, parameterization, and shared fixtures.  
- Ensure that tests work with diacritics (Čeština, Español, Français, etc.).

## Objectives of Individual Tests:
**1. Smoke test**
- Basic verification that the page loads and key elements are accessible.  
- Simulates a typical website visitor and checks expected behavior.  

**2. Pricing test**
- Verifies the functionality of the Pricing section: presence of plans, correct texts and prices, and valid loading of the pricing page.

**3. Language switch test**
- The most complex part of the project. 
- The test is parameterized, running repeatedly for each language: English, Deutsch, Español, Italiano, Čeština, Français.  
- For each language, it checks: Opening and functionality of the language menu; Ability to select a language – including those with Unicode characters (ñ, č, ç…); Redirect to the correct language-specific URL; Correct display of the “Login” text in the selected language; Robust selectors ensuring cross-browser stability.  

## Technical Implementation:

**The project is structured into:**  
tests/ – contains all test files, conftest.py and `__init__.py`  
conftest.py – contains shared Playwright fixtures  
requirements.txt – list of required packages  
`__init__.py` – marks the directory as a Python module  

**The tests use:**
- Pytest for running tests  
- Playwright for UI automation  
- Regex for text expressions across different languages

**Installation and Test Execution Steps:**  
- `pip install -r requirements.txt` – installs all project dependencies  
  > Note: If an error occurs when installing the `regex` package on Windows, **Microsoft C++ Build Tools** must be installed.

- `playwright install` – installs Playwright for Python  
  > Note: For this test suite, having **Chromium** installed is sufficient, as the tests are written specifically for it.

- `pytest -v` – runs tests in the standard mode

- `pytest -v --browser chromium` – explicitly runs tests using Chromium

## Project Benefits:
- Provides quick verification of critical ROUVY functionalities  
- Detects visual and functional regression issues  
- Suitable for integration into a CI/CD pipeline  
- Uses universal selectors resistant to frontend changes  
- Easily extendable with additional tests  
