import pytest
from playwright.sync_api import expect

# parametrizace pro testování měsíčního a ročního plánu
# plan = aktivní plán, který se testuje
# other_plan = pasivní plán, který by měl být neaktivní
# price_text = očekávaný text s cenou, který se zobrazí po aktivaci plánu

@pytest.mark.parametrize("plan, other_plan, price_text", [
    ("monthly", "yearly", "billed monthly"),    # Testuje měsíční předplatné
    ("yearly", "monthly", "billed yearly")      # Testuje roční předplatné
])

def test_pricing_param(open_pricing, pricing_tabs, assert_tab_state, plan, other_plan, price_text):
    """
    Testuje přepínání mezi měsíčním a ročním předplatným a kontroluje zobrazení cen a stav tabů.
    """
    page = open_pricing
    plan_tab = pricing_tabs[plan]           # Aktivní tab, který se bude testovat
    other_tab = pricing_tabs[other_plan]    # Pasivní tab, který by měl být neaktivní

    # 1. Ověření, že sekce s pricingem je viditelná
    pricing_section = page.locator("text=/full monthly or yearly price/i")
    expect(pricing_section).to_be_visible(timeout=10000)
    print("Stránka s nabídkou cen se načetla správně.") 

    # 2. Kliknutí na aktivní plán a ověření stavu tabů
    plan_tab.wait_for(state="visible", timeout=10000)
    plan_tab.click(timeout=10000)
    assert_tab_state(plan_tab, other_tab)    # Ověření, že aktivní a pasivní tab má správnou třídu

    # 3. Ověření zobrazení správné ceny pro aktivní plán
    prices = page.locator(f"text=/{price_text}/i").first
    expect(prices).to_be_visible(timeout=10000)
    print(f"Stránka s cenami pro {plan} předplatné se načetla správně.")

    # 4. Informativní výpis do konzole
    print(f"ROUVY Pricing test: {plan} ceny a stav tabů ověřeny.")
