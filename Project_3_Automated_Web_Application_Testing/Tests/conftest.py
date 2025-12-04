
import pytest
import re
from playwright.sync_api import Page, expect

# Technické fixture:
@pytest.fixture
def js_error_collector(page):
    """
    Zachytí JS chyby během testu.
    Pokud se nějaké vyskytnou, test na konci selže s výpisem chyb.
    """
    errors = []
    page.on("pageerror", lambda e: errors.append(e))
    yield errors
    if errors:
        pytest.fail(f"Na stránce se vyskytly JS chyby: {errors}")

# Pricing fixture:
@pytest.fixture
def open_pricing(page: Page) -> Page:
    """
    Otevře hlavní stránku ROUVY a přejde na sekci Pricing.
    Zajistí, že sekce je načtena a viditelná.
    """
    print("Otevírám hlavní stránku ROUVY...")
    page.goto("https://www.rouvy.com")
    print("Stránka se načetla správně.")

    # Kliknutí na Pricing
    pricing_link = page.get_by_role("link", name=re.compile("pricing", re.IGNORECASE)).first
    pricing_link.wait_for(state="visible", timeout=10000)
    pricing_link.click()

    # Ověření, že pricing sekce je načtená
    pricing_section = page.locator("text=/full monthly or yearly price/i")
    expect(pricing_section).to_be_visible(timeout=10000)
    print("Sekce Pricing je viditelná.")

    return page

@pytest.fixture
def pricing_tabs(page: Page) -> dict:
    """
    Vrací locatory pro měsíční a roční taby.
    Umožňuje testům snadno přistupovat k jednotlivým tlačítkům.
    """
    return {
        "monthly": page.get_by_role("button", name=re.compile("monthly", re.IGNORECASE)),
        "yearly": page.get_by_role("button", name=re.compile("yearly", re.IGNORECASE))
    }

@pytest.fixture
def assert_tab_state():
    """
    Ověří, že aktivní tab má správnou třídu (aktivní) 
    a pasivní tab má třídu pasivní.
    """
    def _assert(active_tab, inactive_tab):
        # Kontrola aktivního tab
        expect(active_tab).to_be_visible(timeout=5000)
        expect(active_tab).to_have_class(re.compile("fill-button-default-text-default"))

        # Kontrola pasivního tab
        expect(inactive_tab).to_be_visible(timeout=5000)
        expect(inactive_tab).to_have_class(re.compile("fill-button-alternative-text-default"))
    return _assert

# Language switch fixture:
@pytest.fixture
def home_page(page: Page):
    """
    Otevře homepage ROUVY pro testy přepínání jazyků.
    Zajišťuje načtení DOM, aby byly elementy dostupné.
    """
    page.goto("https://www.rouvy.com")
    page.wait_for_load_state("domcontentloaded")
    return page

@pytest.fixture
def lang_dropdown(page: Page):
    """
    Spolehlivě otevře language dropdown v horní liště.
    Pokud se menu po kliknutí neotevře (Čeština způsobuje reload),
    provede fallback kliknutí.
    """
    def _open():

        # Lokátor tlačítka jazykového menu
        lang_button = page.locator(
            "button[aria-haspopup='menu']:has(svg), "
            "button:has(svg[data-testid='icon-language'])"
        ).first

        expect(lang_button).to_be_visible(timeout=8000)

        # Klik 1 – standardní
        lang_button.click(force=True)

        # Lokátor menu (různé verze DOM)
        dropdown = page.locator(
            "div[role='menu'][data-state='open'], "
            "div[data-state='open'][class*='DropdownMenu'], "
            "[role='menu']"
        )

        # Čekáme max 2 sekundy – pokud se neotevře, zkusíme znovu
        try:
            dropdown.first.wait_for(state="visible", timeout=2000)
        except:
            # Čeština způsobí reload? Zkusíme klik 2.
            lang_button.click(force=True)
            dropdown.first.wait_for(state="visible", timeout=6000)

        return dropdown.first

    return _open
