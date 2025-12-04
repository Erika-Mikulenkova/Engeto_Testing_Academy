ENGETO projekt 3 - Tři automatizované testy

Popis projektu:
Tento projekt je zaměřený na vytvoření automatizované sady UI testů pro webovou aplikaci ROUVY, a to pomocí nástrojů Python, Pytest a Playwright.
Cílem je ověřit klíčovou funkčnost webu, pokrýt hlavní uživatelské scénáře a zajistit, že základní části webu fungují správně napříč jazyky i prostředími.

Hlavní cíle projektu:
- Ověřit, že domovská stránka ROUVY funguje správně.
- Otestovat sekci Pricing a ověřit zobrazení cenových plánů.
- Otestovat funkčnost přepínání jazyků včetně správné změny URL, textů i viditelnosti prvků.
- Vytvořit přehlednou strukturu testů s využitím conftest.py, parametrizací a sdílených fixture.
- Zajistit fungování testů s diakritikou (Čeština, Español, Français…).

Cíle jednotlivých testů:
1. Smoke test
- Základní ověření, že se stránka načte a klíčové prvky jsou dostupné.
- Test simuluje běžného návštěvníka webu a ověřuje očekávané chování.

2. Pricing test
- Ověřuje fungování sekce cen: existence plánů, správné texty a ceny, validní načtení stránky ceníků
- Tento test pomáhá odhalit změny nebo problémy ve veřejném pricing modelu.

3. Language switch test
- Nejkomplexnější část projektu.
- Test je parametrizovaný, takže běží opakovaně pro každý jazyk: English, Deutsch, Español, Italiano, Čeština, Français.
- U každého jazyka se ověřuje: otevření a funkčnost jazykového menu, možnost vybrat jazyk – funguje i s unicode znaky (ñ, č, ç…), přesměrování na správnou jazykovou verzi URL, ověření, že se na stránce zobrazí text pro přihlášení ve správném jazyce, robustní selektory zajišťují, že test funguje napříč prohlížeči.

Technické provedení:

Projekt je strukturovaný do: 
tests/ – obsahuje všechny testovací soubory
conftest.py – obsahuje sdílené fixture pro Playwright
requirements.txt – seznam potřebných balíčků
__init__.py – označuje adresář jako Python modul

Testy využívají:
pytest pro běh testů
playwright pro UI automatizaci
re a re.UNICODE pro práci s textovými výrazy v různých jazycích

Přínos projektu:
- umožňuje rychlé ověření kritických funkcionalit ROUVY
- odhaluje vizuální i funkční regresní chyby
- vhodné pro začlenění do CI/CD pipeline
- univerzální selektory odolné vůči změnám na frontendu
- snadno rozšiřitelné o další testy
