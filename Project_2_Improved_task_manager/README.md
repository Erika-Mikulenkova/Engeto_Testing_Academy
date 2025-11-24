# **Engeto_projekt_2: Vylepšený Task Manager**

## Popis projektu:
V tomto projektu bylo úkolem vylepšit správce úkolů z prvního projektu tak, aby úkoly nebyly ukládány v seznamu v paměti, ale aby se ukládaly do MySQL databáze. Program bude provádět operace CRUD (Create, Read, Update, Delete) . Po dokončení projektu napíšete automatizované testy pomocí pytest a MySQL Workbench.

## Požadavky na projekt:
Použití MySQL databáze: Vytvořit databázovou tabulku ukoly, která bude obsahovat: id, nazev, popis, stav (nezahájeno, hotovo, probíhá) a datum vytvoreni. Je potřeba vytvořit i samotnou DB, kde bude tabulka ukoly uložena.

## Funkce programu:
**pripojeni_db()**  - Připojení k databázi
- Funkce vytvoří připojení k MySQL databázi.  
- Pokud připojení selže, zobrazí chybovou zprávu.

**vytvoreni_tabulky()** - Vytvoření tabulky, pokud neexistuje
- Funkce vytvoří tabulku ukoly, pokud ještě neexistuje.  
- Ověří existenci tabulky v databázi.

**hlavni_menu()** – Hlavní nabídka, která zobrazí možnosti:
1. Přidat úkol  
2. Zobrazit úkoly  
3. Aktualizovat úkol  
4. Odstranit úkol  
5. Ukončit program

- Pokud uživatel zadá špatnou volbu, program ho upozorní a nechá ho vybrat znovu.

**pridat_ukol()** – Přidání úkolu
- Uživatel zadá název a popis úkolu.  
- Povinné údaje: Název i popis jsou povinné, nesmí být prázdné.  
- Automatické hodnoty:  
    1. Úkol dostane ID automaticky.  
    2. Výchozí stav ukolu: Nezahájeno

- Po splnění všech podmínek se úkol uloží do databáze.

**zobrazit_ukoly()** – Zobrazení úkolů
- Seznam všech úkolů s informacemi: ID, název, popis, stav.  
- Filtr: Zobrazí pouze úkoly se stavem "Nezahájeno" nebo "Probíhá".  
- Pokud nejsou žádné úkoly, zobrazí informaci, že seznam je prázdný.

**aktualizovat_ukol()** – Změna stavu úkolu
- Uživatel vidí seznam úkolů (ID, název, stav).  
- Vybere úkol podle ID.  
- Dostane na výběr nový stav: "Probíhá" nebo "Hotovo"  
- Po potvrzení se aktualizuje DB.  
- Pokud zadá neexistující ID, program ho upozorní a nechá ho vybrat znovu.

**def odstranit_ukol()** – Odstranění úkolu
- Uživatel vidí seznam úkolů.  
- Vybere úkol podle ID.  
- Po potvrzení bude úkol trvale odstraněn z databáze.  
- Pokud uživatel zadá neexistující ID, program ho upozorní a nechá ho vybrat znovu.

## Testovací případy:
### Popis projektu:
V druhé části projektu bylo potřeba vytvořit testovací případy pro každou funkci v projektu Task manager. Tyto případy by měly pokrýt všechny možné cesty a okrajové případy pro každou z funkcí. Testovací případy budou sloužit jako návrh pro automatické testy nebo manuální ověření správnosti programu.
Pro každou funkci (hlavni_menu, pridat_ukol, zobrazit_ukoly, odstranit_ukol) byly vytvořeny samostatné sady testovacích případů (pozitivní, negativní, hraniční). Každý test obsahuje: Testovaná funkce, Název testovacího případu, Popis, Vstupní podmínky, Kroky testu, Očekávaný výsledek, Skutečný výsledek, Stav, Poznámky a Typ testu.
