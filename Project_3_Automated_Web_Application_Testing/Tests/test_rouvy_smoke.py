import re
from playwright.sync_api import expect

def test_homepage_smoke(page):
    # 1. Otevře hlavní stránku a ověří správné načtení (HTTP status 200)
    print("Otevírám hlavní stránku ROUVY...")
    response = page.goto("https://www.rouvy.com")
    assert response.ok, "Stránka se nenačetla správně (HTTP status není OK)"
    print("Stránka se načetla správně.")

    # 2. Ověří titul stránky ('rouvy', case-insensitive)
    expect(page).to_have_title(re.compile("rouvy", re.IGNORECASE))
    print("Titulek stránky odpovídá očekávání.")

    # 3. Ověří viditelnost hlavního menu a jeho interaktivitu
    main_menu = page.locator("nav")
    expect(main_menu).to_be_visible(timeout=10000)  # Kontrola viditelnosti menu
    expect(main_menu).to_be_enabled(timeout=10000)  # Kontrola, že menu je interaktivní
    print("Hlavní menu je viditelné a interaktivní.")

    # 4. Ověří hlavní CTA tlačítko (viditelné a připravené k interakci)
    cta_button = page.locator("#header-video-form > div > button")
    cta_button.wait_for(state="visible", timeout=10000)
    expect(cta_button).to_be_visible()
    print("Hlavní CTA tlačítko je viditelné.")

    # 5. Ověří klíčový obsah hero sekce (titulek obsahuje 'cycling')
    hero_title = page.locator("h1")
    expect(hero_title).to_have_text(re.compile("cycling", re.IGNORECASE))
    print("Hero sekce obsahuje očekávaný text.")

    # 6. Shrnutí výsledku smoke testu
    print("ROUVY Smoke test: stránka načtena, menu a CTA viditelné, hero sekce obsahuje 'cycling'.")