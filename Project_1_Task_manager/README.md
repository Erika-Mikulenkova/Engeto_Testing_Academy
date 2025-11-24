# **Engeto_projekt_1: Task Manager**

## Vytvoření programu pomocí Python:
### Popis projektu:
V tomto projektu bylo úkolem vytvořit Task manager pro správu úkolů. Program by měl umožnit přidávat, zobrazovat a odstraňovat úkoly. Každá funkce má svůj specifický úkol, který je popsán níže. Úkoly budou ukládány do seznamu ukoly = []. 

**def hlavni_menu()**  
Funkce hlavního menu, která poskytuje možnosti pro přidání, zobrazení a odstranění úkolu. Pokud uživatel zadá neplatnou volbu, program ho upozorní a nechá uživatele opakovat znovu volbu.

**def pridat_ukol()**  
Tato funkce má uživateli umožnit zadat název a popis nového úkolu a uložit jej do seznamu úkolů. Zde platí volba 1 v hlavním menu. Po zadání úkolu program pokračuje dál nabídkou hlavního menu. Při zadání prázdného vstupu do Zadejte název úkolu nebo Popis úkolu, program upozorní uživatele, že zadal prázdný vstup a nechá ho zadat název i popis znovu.

**def zobrazit_ukoly()**  
Tato funkce má zobrazit všechny úkoly v seznamu. Zde platí volba 2 v hlavním menu. Po zobrazení úkolů program pokračuje dál nabídkou hlavního menu.

**def odstranit_ukol()**  
Tato funkce má uživateli umožnit zadat číslo úkolu, který chce odstranit, a tento úkol odstranit. Zde platí volba 3 v hlavním menu. Po odstranění úkolu program pokračuje dál nabídkou hlavního menu. Zde je potřeba, aby uživatel viděl všechny uložené úkoly a při výběru neexistujícího úkolu byl upozorněn.

Pokud uživatel zadá volbu 4 v hlavním menu program se ukončí.

## Testovací případy:
### Popis projektu:
V druhé části projektu bylo potřeba vytvořit testovací případy pro každou funkci v projektu Task manager. Tyto případy by měly pokrýt všechny možné cesty a okrajové případy pro každou z funkcí. Testovací případy budou sloužit jako návrh pro automatické testy nebo manuální ověření správnosti programu.
Pro každou funkci (hlavni_menu, pridat_ukol, zobrazit_ukoly, odstranit_ukol) byly vytvořeny samostatné sady testovacích případů (pozitivní, negativní, hraniční). Každý test obsahuje: Testovaná funkce, Název testovacího případu, Popis, Vstupní podmínky, Kroky testu, Očekávaný výsledek, Skutečný výsledek, Stav, Poznámky a Typ testu.
