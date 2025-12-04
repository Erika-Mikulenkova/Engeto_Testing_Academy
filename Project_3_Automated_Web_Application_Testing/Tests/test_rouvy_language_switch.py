import re
import pytest
from playwright.sync_api import expect

@pytest.mark.parametrize(
    "lang, url_pattern, login_text",
    [
        ("English", r"^https://rouvy\.com/?$", "Login"),        # Testuje anglickou verzi stránky
        ("Deutsch", r"/de/?$", "Anmeldung"),                    # Testuje německou verzi stránky
        ("Español", r"/es/?$", "Iniciar Sesión"),               # Testuje španělskou verzi stránky
        ("Italiano", r"/it/?$", "Accedi"),                      # Testuje italskou verzi stránky
        ("Čeština", r"/cs/?$", "Přihlášení"),                   # Testuje českou verzi stránky
        ("Français", r"/fr/?$", "Connexion")                    # Testuje francouzskou verzi stránky
    ]
)

def test_language_switch_param(home_page, lang_dropdown, lang, url_pattern, login_text):
    """
    Testuje přepínání jazyků, kontroluje URL a hlavní text na stránce.
    Používá re.escape pro názvy jazyků s diakritikou, aby Playwright locator našel správně element.
    """
    page = home_page

    # 1. Otevření dropdownu a výběr jazyka
    dropdown = lang_dropdown()
    lang_option = dropdown.get_by_role(
        "menuitem",
        name=re.compile(re.escape(lang), re.IGNORECASE | re.UNICODE)
    )
    expect(lang_option).to_be_visible(timeout=10000)
    lang_option.click()

    # 2. Ověření URL
    expect(page).to_have_url(re.compile(url_pattern))

    # 3. Ověření textu na stránce
    login_button = page.get_by_role(
        "link",
        name=re.compile(login_text, re.IGNORECASE | re.UNICODE)
    )
    expect(login_button).to_be_visible()

    # 4. Informativní výpis do konzole
    print(f"ROUVY Language switch test pro {lang}: úspěšně ověřeno.")

