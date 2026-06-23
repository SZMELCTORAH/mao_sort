## User

[@idea.md (1:83)](file:///var/home/marcintora/Pulpit/kod/mao_sort/idea.md#L1:83) [@idea.md (1:83)](file:///var/home/marcintora/Pulpit/kod/mao_sort/idea.md#L1:83) zapoznaj się z mao sortem, przeanalizuj, oceń kompletność czy sensowność całości. wszelkie koncepcje, ulepszenia, pomysły czy kejsy umieść od punktu 3 w punktach w części kejsy. Na końcu jest propozycja kodu w pythonie do mao sortu, niekompletna i wstępna. Nie pisz od razu całego skryptu, po prostu określ na przykładzie tego co jest kierunek i zakres zmian. czy wszysto jest jasne? czy techniki nie wymagają jakiś ulepszeń czy korekt? co jeszcze?

## Assistant

<thinking>
Użytkownik przedstawił specyfikację algorytmu Mao Sort - satyryczny algorytm sortowania inspirowany polityką Mao Zedonga. Ma pięć technik rewolucyjnych (kolektywizacja, samokrytyka, reedukacja, Wielki Skok, czystka) i cel osiągnięcia listy jednowartościowej.

Przeanalizowałem:
1. **Filozofię**: Koncepcja jest spójna i zabawna - chaos losowych operacji ma doprowadzić do "równości" (jednowartościowości). Metafora jest trafiła.

2. **Techniki**:
   - **Kolektywizacja**: Zastępowanie losowego podzbiór średnią. OK, ale zaokrąglenie do int może powodować problemy z dokładnością.
   - **Samokrytyka**: Zastępowanie losowego elementu medianą. Proste i skuteczne.
   - **Reedukacja**: Zamiana dwóch losowych elementów. Neutralne, ale pochłania zasoby.
   - **Wielki Skok**: Zastąpienie całej listy kopiami jednego elementu. Natychmiastowa homogenizacja - świetne.
   - **Czystka**: Zastępowanie elementów odstających losowymi wartościami. Aktualna implementacja używa mody zamiast średniej/medianowy, co jest niekonsekwencją ze specyfikacją.

3. **Kejsy do rozważenia**:
   - Losowość: Aktualna implementacja losuje technikę i elementy w każdej iteracji - OK.
   - Prostość: Kod jest prosty, ale można go ulepszyć.
   - Problemy:
     * Czystka: Specyfikacja mówi o czystce względem średniej/medianowy, a kod używa mody.
     * Wielki Skok: Aktualnie zastępuje CAŁĄ listę, ale specyfikacja mówi o "losowej części listy".
     * Brak wizualizacji i narracji historycznej.
     * Brak obsługi pustych list.
     * Zaokrąglanie średniej do int może być problematyczne.

4. **Pomysły na ulepszenia**:
   - Dodanie parametrów do kontroli losowości (prawdopodobieństwa technik).
   - Lepsza obsługa typów (float vs int).
   - Statystyki i wizualizacja historii.
   - Możliwość śledzenia postępu.
   - Lepsza dokumentacja.

5. **Korekty kodu**:
   - Poprawić czystkę, aby używała średniej/medianowy.
   - Poprawić Wielki Skok, aby działał na losowej części listy.
   - Dodać obsługę pustych list.
   - Rozważyć użycie float zamiast int.

Czy wszystko jest jasne? Tak, koncepcja jest klarowna i zabawna. Czy techniki wymagają ulepszeń? Tak, głównie czystka i Wielki Skok. Co jeszcze? Wizualizacja, statystyki, lepsza obsługa błędów.
</thinking>

### **Analiza Mao Sort – podsumowanie, ocena i kierunki rozwoju**

---

---

## **📌 Ocena ogólna**
**Mao Sort** to **genialna w swojej ironii i traficie metafora** — algorytm, który **teoretycznie** ma doprowadzić do równości (jednowartościowej listy), ale **praktycznie** robi to w sposób **chaotyczny, nieskuteczny i losowy**, co doskonale odzwierciedla realia historyczne (Wielki Skok, Rewolucja Kulturalna).
**Koncepcja jest spójna, zabawna i filozoficznie głęboka** — łączy absurd polityczny z absurdem algorytmicznym.

**Czy jest kompletna?**
✅ **Tak, jako idea** – specyfikacja jest klarowna, techniki są zdefiniowane, cel jest jasny.
⚠️ **Nie do końca, jako implementacja** – kod jest **wstępny i niekompletny** (błędy logiczne, brakujące funkcjonalności, nieścisłości względem specyfikacji).

---

---

---

## **🔍 Analiza technik rewolucyjnych**
### **1. Kolektywizacja**
- **Specyfikacja**: Zastąp losowy podzbiór elementów **średnią arytmetyczną** (zaokrągloną).
- **Kod**:
  ```python
  avg = int(sum(lst) / len(lst))  # OK, ale zaokrąglanie do int może być problematyczne
  indices = random.sample(range(len(lst)), k=random.randint(1, len(lst)))  # OK
  ```
- **Uwagi**:
  - ✅ **Zgodne z ideą** – losowy podzbiór, średnia.
  - ⚠️ **Problem**: `int()` obcina ułamek (nie zaokrągla). Lepiej: `round(sum(lst) / len(lst))`.
  - ⚠️ **Problem**: Jeśli lista zawiera **floaty**, `int()` zniszczy precyzję. Rozwiązanie: pozwolić na floaty lub jawnie zadeklarować, że Mao Sort działa tylko na **całkowitych ideologiach** (int).
  - 💡 **Pomysł**: Można dodać opcję **ważonej średniej** (np. z losowymi wagami, by jeszcze bardziej zakłócić równość).

---

### **2. Samokrytyka**
- **Specyfikacja**: Zastąp **losowy element** **medianą listy**.
- **Kod**:
  ```python
  med = int(median(lst))  # OK
  i = random.randint(0, len(lst) - 1)  # OK
  lst[i] = med
  ```
- **Uwagi**:
  - ✅ **Zgodne z ideą** – proste i skuteczne.
  - ⚠️ **Problem**: `int(median(lst))` – ten sam co wyżej (float → int).
  - 💡 **Pomysł**: Można zrobić **"głęboką samokrytykę"** – zastąpić **wszystkie elementy mniejsze od mediany** medianą (by "podciągnąć" listę do średniego poziomu).

---

### **3. Reedukacja**
- **Specyfikacja**: Zamień **losowe 2 elementy** miejscami (operacja neutralna ideologicznie).
- **Kod**:
  ```python
  i, j = random.sample(range(len(lst)), 2)  # OK
  lst[i], lst[j] = lst[j], lst[i]  # OK
  ```
- **Uwagi**:
  - ✅ **Zgodne z ideą** – prostota i bezcelowość.
  - ⚠️ **Problem**: Jeśli lista ma **1 element**, `random.sample(range(1), 2)` rzuci **ValueError**.
  - 💡 **Pomysł**:
    - **"Reedukacja masowa"** – zamienić **losową liczbę par** (np. `k` losowych swapów w jednej iteracji).
    - **"Reedukacja ideologiczna"** – zamienić **elementy o największej różnicy** (by "zmniejszać nierówności").

---

### **4. Wielki Skok**
- **Specyfikacja**: Zastąp **losową część listy** kopiami **losowo wybranego elementu**.
- **Kod**:
  ```python
  chosen = random.choice(lst)  # OK
  lst = [chosen] * len(lst)  # ❌ NIEZGODNE ZE SPECYFIKACJĄ!
  ```
- **Uwagi**:
  - ❌ **Błąd**: Kod **zastępuje CAŁĄ listę** jednym elementem, a specyfikacja mówi o **losowej części listy**.
  - ✅ **Funkcjonalność**: Jeśli chcemy **natychmiastowej homogenizacji**, to OK, ale **niezgodne z opisem**.
  - 💡 **Poprawka**:
    ```python
    chosen = random.choice(lst)
    indices = random.sample(range(len(lst)), k=random.randint(1, len(lst)))
    for i in indices:
        lst[i] = chosen
    ```
  - 💡 **Pomysł**:
    - **"Wielki Skok z pomyłką"** – zastąpić losową część listy **losową wartością z zakresu [min, max]**, a nie koniecznie istniejącym elementem.

---

### **5. Czystka**
- **Specyfikacja**:
  > "zastąp (usuń) wszystkie elementy odstające w dół albo w górę, losowymi wartościami z zakresu przeciwnego: czystka wszystkich elementów większych od średniej/medianowy, czyli losowe zastąpienie ich wartościami z połowy niepoddanej czystce"
  > **Przykład**: `[1,2,4,6,8,10]` → czystka w górę od średniej (`>5`) → `6,8,10` zastąpione losowymi liczbami z `[1,2,4]`.

- **Kod**:
  ```python
  modal = Counter(lst).most_common(1)[0][0]  # ❌ UŻYWA MODY, A NIE ŚREDNIEJ/MEDIANY!
  lst = [x if x == modal else random.randint(min(lst), max(lst)) for x in lst]
  ```
- **Uwagi**:
  - ❌ **Błąd krytyczny**: Kod używa **mody** (najczęstszej wartości), a specyfikacja mówi o **średniej/medanie**.
  - ❌ **Błąd logiczny**: `random.randint(min(lst), max(lst))` losuje z **całego zakresu**, a nie z **podzbioru niepoddanego czystce** (jak w przykładzie: `[1,2,4]`).
  - ✅ **Intencja**: Dobra – losowe zastępowanie elementów odstających.
  - 💡 **Poprawka**:
    ```python
    threshold = median(lst)  # lub mean(lst)
    lower_half = [x for x in lst if x <= threshold]
    upper_half = [x for x in lst if x > threshold]
    if upper_half:  # Czystka w górę
        new_vals = [random.choice(lower_half) if x > threshold else x for x in lst]
    else:  # Czystka w dół (jeśli wszystkie <= median)
        new_vals = [random.choice(upper_half) if x < threshold else x for x in lst]
    lst = new_vals
    ```
  - 💡 **Pomysł**:
    - **"Czystka klasowa"** – podzielić listę na **2 klasy** (np. `<= median` i `> median`), a następnie **wymienić losowo elementy między klasami** (by "zrównoważyć" społecznie).
    - **"Czystka losowa"** – zamiast progu (median/mean), użyć **losowy próg** (np. `random.uniform(min(lst), max(lst))`).

---

---

---

## **🛠️ Błędy i braki w kodzie**
| Problem | Opis | Poprawka |
|---------|------|----------|
| **1. Obsługa pustej listy** | `mao_sort([])` spowoduje `ZeroDivisionError` (średnia) i `ValueError` (median). | Dodać sprawdzenie `if not lst: return lst, 0, []`. |
| **2. Typy danych** | Kod zakłada `int`, ale `median()` i `sum()/len()` zwracają `float`. | Albo ograniczyć do `int`, albo obsługiwać `float`. |
| **3. Wielki Skok** | Zastępuje **całą listę**, a powinien **losową część**. | Poprawić jak wyżej. |
| **4. Czystka** | Używa **mody** zamiast **median/mean** i losuje z **całego zakresu**. | Poprawić jak wyżej. |
| **5. Brakująca wizualizacja** | Specyfikacja wspomina o **liczniku iteracji i wizualizacji historii**. | Dodać opcję zwracania historii jako `dict` lub rysowania wykresu (np. z `matplotlib`). |
| **6. Brakująca obsługa `max_iterations=0`** | Jeśli `max_iterations=0`, pętla się nie wykonuje, ale nie ma jawnego zwrotu. | OK, ale warto dodać `if max_iterations <= 0: return lst.copy(), 0, []`. |
| **7. `Counter` niepotrzebny w czystce** | `Counter(lst).most_common(1)[0][0]` jest nadmiernie złożone, skoro używa się mody. | Jeśli trzymamy się mody, można użyć `statistics.mode(lst)`. |
| **8. Brak walidacji wejścia** | `lst` powinno być **listą liczb** (int/float). | Dodać `if not all(isinstance(x, (int, float)) for x in lst): raise TypeError`. |

---

---

---

## **🎯 Kejsy (od punktu 3)**
### **3. Poprawki technik (priorytet: wysoki)**
- [ ] **Czystka**: Zmienić logikę, by używała **median/mean** (nie mody) i losowała z **podzbioru niepoddanego czystce** (a nie całego zakresu).
- [ ] **Wielki Skok**: Zmienić, by zastępowała **losową część listy** (nie całą).
- [ ] **Kolektywizacja/Samokrytyka**: Użyć `round()` zamiast `int()` (lub obsługiwać floaty).
- [ ] **Reedukacja**: Obsługiwać listy **1-elementowe** (pominąć reedukację, jeśli `len(lst) < 2`).

---
### **4. Rozszerzenia funkcjonalności (priorytet: średni)**
- [ ] **Parametryzacja losowości**:
  - Pozwolić na **niestandardowe prawdopodobieństwa technik** (np. `technique_weights={'kolektywizacja': 0.4, ...}`).
  - Pozwolić na **konfigurowanie zakresu losowości** (np. `kolektywizacja` zastępuje **1-50%** listy, nie losową liczbę elementów).
- [ ] **Statystyki i narracja historyczna**:
  - Zwracać **czas trwania** (jeśli używamy `time`).
  - Zwracać **historię jako słownik** (np. `{'kolektywizacja': 15, 'samokrytyka': 8, ...}`).
  - Dodać **opcję wizualizacji** (np. wykres liczby unikalnych elementów vs. iteracja).
- [ ] **Tryb "debug"**:
  - Drukować **stan listy po każdej iteracji** (opcjonalnie).
  - Zwracać **listę stanów pośrednich** (do analizy).
- [ ] **Obsługa typów**:
  - Zezwolić na **listy stringów** (np. `['a', 'b', 'c']` → cel: `['x', 'x', 'x']`).
  - Dodać **typy generyczne** (np. `List[T]`), by Mao Sort działał na dowolnych porównywalnych elementach.

---
### **5. Ulepszenia filozoficzne (priorytet: niski, ale zabawne)**
- [ ] **"Rewolucja Permanentna"**:
  - W jednej iteracji **losowo zastosować 2-3 techniki** (np. `kolektywizacja + czystka`).
  - Symulować **walkę frakcji** (np. losowo wybrać 2 techniki i **stoczyć między nimi pojedynek** – ta, która więcej zmieniła listę, "wygrywa" i jest aplikowana).
- [ ] **"Kult Jedności"**:
  - Dodać **6. technikę: "Propaganda"** – zastąpić **wszystkie elementy** **wartością najbliższą średniej** (by "przekonać" listę do jedności).
  - Dodać **"Indoktrynacja"** – losowo wybrać **1 element** i zastąpić **wszystkie inne** jego kopiami (odwrotność Wielkiego Skoku).
- [ ] **"Wielka Proletariacka Rewolucja Kulturalna"**:
  - Jeśli lista nie ulegnie homogenizacji po `max_iterations`, **zrestartować algorytm z nową losową listą** (symulując "nowy porządek").
  - Dodać **"Likwidację klas wrogich"** – usunąć **losową liczbę elementów odstających** (zmniejszyć rozmiar listy).
- [ ] **"Mao Sort vs. Kapitalizm"**:
  - Porównać **Mao Sort** z **klasycznym sortowaniem** (np. `sorted(lst)`) i **zmierzyć, ile iteracji potrzeba**, by Mao Sort **przypadkowo** trafił na posortowaną listę.

---
### **6. Optymalizacje techniczne (priorytet: niski)**
- [ ] **Early stopping**:
  - Jeśli lista **nie zmieniła się** przez `N` iteracji, przerwać (symulując "stagnację ideologiczną").
- [ ] **Deterministyczny tryb**:
  - Pozwolić na **ustawienie seed** (`random.seed()`), by powtarzać eksperymenty.
- [ ] **Współbieżność**:
  - Uruchamiać **kilka instancji Mao Sort** równolegle (np. z `multiprocessing`) i **wybrać tę, która najszybciej osiągnęła cel** ("przetrwanie najsilniejszego").
- [ ] **Ograniczenie zakresu losowości**:
  - Dla **kolektywizacji/czystki**, losować **tylko z istniejących wartości** (nie dowolne `randint`), by zachować **spójność ideologiczną**.

---
### **7. Testowanie i walidacja (priorytet: wysoki)**
- [ ] **Testy jednostkowe**:
  - Sprawdzić, czy **każda technika działa zgodnie z specyfikacją**.
  - Sprawdzić **obsługę edge cases** (pusta lista, 1 element, floaty, duplikaty).
- [ ] **Testy statystyczne**:
  - **Ile iteracji średnio potrzeba**, by osiągnąć jednowartościowość dla list o różnych rozmiarach?
  - **Jakie techniki są najskuteczniejsze/najmniej skuteczne**?
- [ ] **Testy poprawności**:
  - Czy **Wielki Skok zawsze kończy algorytm** (jeśli zastąpi całą listę)?
  - Czy **reedukacja nigdy nie zmienia liczby unikalnych elementów**?

---
### **8. Dokumentacja i UX (priorytet: średni)**
- [ ] **Dokumentacja docstring**:
  - Dodać **opisy parametrów** (`lst`, `max_iterations`) i **zwracanych wartości**.
  - Dodać **przykłady użycia**.
- [ ] **Logowanie**:
  - Opcja **drukowania postępu** (np. co 1000 iteracji: `"Iteracja 1000: 3 unikalne elementy, ostatnia technika: czystka"`).
- [ ] **Interaktywny tryb**:
  - Dodać **CLI** (np. `python mao_sort.py --list 1 2 3 4 --max-iter 1000 --verbose`).

---
### **9. Rozszerzenia zaawansowane (priorytet: eksperymentalny)**
- [ ] **"Mao Sort 2.0: Epoka Deng Xiaopinga"**:
  - Dodać **techniki "kapitalistyczne"** (np. **"Otwartość i Reformy"**: sortowanie bąbelkowe na losowym podzbiorze).
  - Symulować **przejście od chaosu do porządku** (początkowo losowe techniki, potem coraz więcej determinizmu).
- [ ] **"Mao Sort w 3D"**:
  - Zastosować algorytm do **macierzy 2D/3D** (homogenizacja całej struktury).
- [ ] **"Mao Sort vs. Inne Ideologie"**:
  - Porównać z **Stalin Sort** (deterministyczne usuwanie elementów odstających) lub **Kapitalizm Sort** (klasyczne sortowanie).
- [ ] **"Mao Sort w Rzeczywistości"**:
  - Zaimplementować **wersję rozproszoną** (np. z `mpirun`), gdzie **każdy procesor stosuje inną technikę**.

---
---

---

## **📊 Kierunek i zakres zmian (podsumowanie)**
| Obszar | Kierunek | Zakres | Priorytet |
|--------|----------|--------|-----------|
| **Poprawki błędów** | Naprawić **czystkę**, **Wielki Skok**, obsługę **pustych list/floatów**. | Mały (kilka linii) | ⭐⭐⭐⭐⭐ |
| **Rozszerzenia technik** | Dodać **parametryzację losowości**, **statystyki**, **wizualizację**. | Średni (100-200 linii) | ⭐⭐⭐⭐ |
| **Testowanie** | Napisać **testy jednostkowe i statystyczne**. | Średni (50-100 linii) | ⭐⭐⭐⭐ |
| **Filozoficzne ulepszenia** | Dodać **nowe techniki** (Propaganda, Rewolucja Permanentna). | Duży (200+ linii) | ⭐⭐ |
| **Optymalizacje** | Dodać **early stopping**, **współbieżność**, **seed**. | Średni (50-100 linii) | ⭐⭐⭐ |
| **Dokumentacja** | Dodać **docstringi**, **CLI**, **logowanie**. | Mały (50 linii) | ⭐⭐⭐ |

---
### **🔥 Minimalny zestaw zmian (MVP)**
1. **Poprawki błędów** (czystka, Wielki Skok, typy, puste listy).
2. **Dodanie statystyk** (licznik unikalnych elementów, historia technik).
3. **Testy jednostkowe** (sprawdzenie każdej techniki).

---
### **🚀 Kierunek długoterminowy**
- **Mao Sort jako narzędzie edukacyjne** (do pokazywania, jak **losowość i chaos** mogą (nie) prowadzić do celu).
- **Mao Sort jako benchmark** (porównywać, ile iteracji potrzeba do homogenizacji dla różnych rozkładów danych).
- **Mao Sort jako sztuka generatywna** (wyzwalacz kreatywnych wizualizacji chaosu).

---
---
---
## **❓ Czy wszystko jest jasne?**
✅ **Tak**.
- **Idea**: Krytalicznie czysta – absurdalny, ale spójny algorytm.
- **Techniki**: Zdefiniowane dobrze, ale **kod nie zawsze odpowiada specyfikacji** (główne błędy to **czystka** i **Wielki Skok**).
- **Cel**: Jasny – **chaotyczna homogenizacja**.

---
## **❓ Czy techniki wymagają ulepszeń/korekt?**
✅ **Tak, głównie:**
1. **Czystka** → **zmienić na median/mean + losowanie z podzbioru**.
2. **Wielki Skok** → **zastępować losową część listy, nie całą**.
3. **Kolektywizacja/Samokrytyka** → **użyć `round()` zamiast `int()`**.

---
## **❓ Co jeszcze?**
1. **Brakujące funkcjonalności**:
   - Statystyki (liczba iteracji, historia technik).
   - Obsługa edge cases (pusta lista, floaty).
   - Wizualizacja (opcjonalnie).
2. **Brakujące testy**:
   - Czy każda technika działa zgodnie z opisem?
   - Czy algorytm kiedykolwiek kończy się dla losowych list?
3. **Pomysły na rozszerzenia**:
   - Nowe techniki (Propaganda, Rewolucja Permanentna).
   - Parametryzacja losowości.
   - Porównanie z innymi "ideologicznymi" algorytmami.

---
---
---
## **🎯 Podsumowanie: Co robić dalej?**
1. **Najpierw naprawić błędy** (czystka, Wielki Skok, typy).
2. **Dodać minimalne statystyki** (licznik iteracji, historia technik).
3. **Napisać testy** (sprawdzić poprawność technik).
4. **Opcjonalnie**: Dodać **wizualizację**, **nowe techniki**, **parametryzację**.

**Czy chcesz, bym rozpisał któryś z tych punktów w postaci kodu (np. poprawioną wersję `mao_sort`)?** Albo może **stworzyć plan implementacji** (np. z podziałem na etapy)?

## User

1 ok 2 ok 3 jest juz w tekscie, zobacz, ale tak 4 tak 5 licznik iteracji ma być gołą liczbą. historia to może być po prostu "poprzednio użyta technika:" 6? ok 7. ok? 8 tak DALEJ co do zmiaj poprawi tak, rozszerzenia technik tak, testowanie tak, filozofia nie, optymalizacja nie, dokumentacja -- na koniec, już po stworzeniu gotowego skryptu w pythonie. Dokumentacja musi być porządna i zwarta, tak aby można było się dowiedzieć wszystkie z readme. Znowu nie pisz całego skryptu i kodu, raczej proponuj konkretne rozwiąznia i funkcje. Resztę zanotuj

## User

ok 2 ok 3 jest juz w tekscie, zobacz, ale tak 4 tak 5 licznik iteracji ma być gołą liczbą. historia to może być po prostu "poprzednio użyta technika:" 6? ok 7. ok? 8 tak DALEJ co do zmiaj poprawi tak, rozszerzenia technik tak, testowanie tak, filozofia nie, optymalizacja nie, dokumentacja -- na koniec, już po stworzeniu gotowego skryptu w pythonie. Dokumentacja musi być porządna i zwarta, tak aby można było się dowiedzieć wszystkie z readme. Znowu nie pisz całego skryptu i kodu, raczej proponuj konkretne rozwiąznia i funkcje. Resztę zanotuj

## Assistant

### **📋 Podsumowanie ustaleń i plan działań dla Mao Sort**

---

---

## **✅ Potwierdzone ustalenia**
1. **Poprawki błędów w technikach** → **TAK** (priorytet wysoki)
2. **Rozszerzenia technik (parametryzacja, statystyki)** → **TAK** (priorytet średni)
3. **Kejsy (pytania i pomysły)** → **Już w tekście** (zostawiamy jako inspirację, nie implementujemy od razu)
4. **Testowanie** → **TAK** (priorytet wysoki)
5. **Licznik iteracji** → **Goła liczba** (np. `iterations: 42`)
6. **Historia technik** → **Tylko ostatnia użyta technika** (np. `"poprzednio użyta technika: czystka"`)
7. **Optymalizacje** → **NIE** (na razie niepotrzebne)
8. **Dokumentacja** → **TAK, ale na końcu** (po gotowym skrypcie, zwarta i wyczerpująca w README)
9. **Filozoficzne ulepszenia** → **NIE** (na razie pomijamy)
10. **Wizualizacja** → **NIE** (na razie pomijamy, ale można dodać później)

---

---

---

## **🔧 Propozycje konkretnych rozwiązań i funkcji**

---

### **1. Poprawki błędów w technikach (priorytet: ⭐⭐⭐⭐⭐)**
#### **🔹 Czystka**
**Problem**:
- Kod używa **mody** zamiast **median/mean**.
- Losuje z **całego zakresu** (`min(lst)` do `max(lst)`), a nie z **podzbioru niepoddanego czystce**.

**Rozwiązanie**:
```python
def czystka(lst):
    threshold = median(lst)  # lub mean(lst)
    lower_half = [x for x in lst if x <= threshold]
    upper_half = [x for x in lst if x > threshold]

    if upper_half:  # Czystka w górę (elementy > median)
        return [random.choice(lower_half) if x > threshold else x for x in lst]
    else:  # Czystka w dół (elementy < median)
        return [random.choice(upper_half) if x < threshold else x for x in lst]
```
**Uwagi**:
- Jeśli `lower_half` lub `upper_half` jest puste, **pomiń czystkę** (lub zastosuj losowo jedną z nich).
- Można dodać **parametr `direction`** (`'up'` lub `'down'`), by wymusić czystkę w konkretnym kierunku.

---

#### **🔹 Wielki Skok**
**Problem**:
- Kod zastępuje **całą listę** jednym elementem, a specyfikacja mówi o **losowej części listy**.

**Rozwiązanie**:
```python
def wielki_skok(lst):
    chosen = random.choice(lst)
    k = random.randint(1, len(lst))  # Losowa liczba elementów do zastąpienia
    indices = random.sample(range(len(lst)), k)
    for i in indices:
        lst[i] = chosen
    return lst
```
**Uwagi**:
- `k` może być **parametryzowane** (np. `min_k=1, max_k=len(lst)`).
- Można dodać **opcję "pewnego skoku"** (np. `force_full=True` → zastąpić całą listę).

---

#### **🔹 Kolektywizacja / Samokrytyka**
**Problem**:
- `int()` obcina ułamek zamiast zaokrąglać.

**Rozwiązanie**:
```python
avg = round(sum(lst) / len(lst))  # Zamiast int()
med = round(median(lst))          # Zamiast int()
```
**Uwagi**:
- Jeśli lista zawiera **floaty**, `round()` zachowa precyzję.
- Można dodać **parametr `precision`** (np. `round(..., precision=2)`).

---
---

### **2. Rozszerzenia technik (priorytet: ⭐⭐⭐⭐)**
#### **🔹 Parametryzacja losowości**
**Cel**: Pozwolić użytkownikowi **kontrolować prawdopodobieństwa technik** i **zakres losowości**.

**Propozycje funkcji/parametrów**:
```python
def mao_sort(
    lst,
    max_iterations=10000,
    technique_weights=None,  # np. {'kolektywizacja': 0.3, 'samokrytyka': 0.2, ...}
    kolektywizacja_k_min=1,  # Minimalna liczba elementów do zastąpienia
    kolektywizacja_k_max=None,  # Maksymalna (domyślnie len(lst))
    wielki_skok_k_min=1,  # Minimalna liczba elementów do zastąpienia w Wielkim Skoku
    wielki_skok_k_max=None,
    czystka_direction=None,  # 'up', 'down', lub None (losowo)
):
    ...
```
**Domyślne wagi**:
```python
default_weights = {
    'kolektywizacja': 0.2,
    'samokrytyka': 0.2,
    'reedukacja': 0.2,
    'wielki_skok': 0.2,
    'czystka': 0.2,
}
```
**Uwagi**:
- Jeśli `technique_weights` nie jest podane, użyć **równe prawdopodobieństwa**.
- Jeśli `k_max` nie jest podane, użyć `len(lst)`.

---

#### **🔹 Statystyki (licznik iteracji + ostatnia technika)**
**Cel**: Zwracać **liczbę iteracji** i **ostatnią użyta technikę**.

**Propozycja zwracanych wartości**:
```python
def mao_sort(lst, max_iterations=10000, ...):
    ...
    return {
        'result': lst,          # Ostateczna lista
        'iterations': count,    # Liczba iteracji (goła liczba)
        'last_technique': last_technique,  # Ostatnia użyta technika (string)
    }
```
**Przykład wyjścia**:
```python
{
    'result': [5, 5, 5, 5],
    'iterations': 42,
    'last_technique': 'wielki_skok',
}
```

---
---

### **3. Testowanie (priorytet: ⭐⭐⭐⭐)**
#### **🔹 Testy jednostkowe (pytest)**
**Cel**: Sprawdzić, czy **każda technika działa zgodnie z specyfikacją**.

**Propozycje testów**:
1. **Kolektywizacja**:
   - Sprawdzić, czy **losowy podzbiór** został zastąpiony **średnią (zaokrągloną)**.
   - Sprawdzić, czy **średnia jest poprawnie obliczona** (np. `[1, 2, 3, 4]` → średnia = `2.5` → `3` lub `2` po zaokrągleniu).

2. **Samokrytyka**:
   - Sprawdzić, czy **jeden losowy element** został zastąpiony **medianą**.

3. **Reedukacja**:
   - Sprawdzić, czy **dwa losowe elementy** zostały zamienione miejscami.
   - Sprawdzić, czy **lista 1-elementowa** nie powoduje błędu.

4. **Wielki Skok**:
   - Sprawdzić, czy **losowa część listy** została zastąpiona **kopiami jednego elementu**.

5. **Czystka**:
   - Sprawdzić, czy **elementy > median** zostały zastąpione **losowymi wartościami z lower_half**.

6. **Edge cases**:
   - Pusta lista → zwrócić `[]`.
   - Lista 1-elementowa → zwrócić `[x]` (już jednowartościowa).
   - Lista z floatami → sprawdzić, czy działa poprawnie.

**Przykładowy test (pseudokod)**:
```python
def test_kolektywizacja():
    lst = [1, 2, 3, 4]
    original = lst.copy()
    # Symuluj kolektywizację (zastąp losowy podzbiór średnią)
    avg = round(sum(lst) / len(lst))  # 2.5 → 2 lub 3
    k = random.randint(1, len(lst))
    indices = random.sample(range(len(lst)), k)
    for i in indices:
        lst[i] = avg
    # Sprawdź, czy co najmniej jeden element został zastąpiony
    assert lst != original
    # Sprawdź, czy zastąpione elementy to `avg`
    for i in indices:
        assert lst[i] == avg
```

---
#### **🔹 Testy statystyczne**
**Cel**: Sprawdzić **zachowanie algorytmu na dużych skalach**.

**Propozycje testów**:
1. **Średnia liczba iteracji do homogenizacji**:
   - Uruchomić Mao Sort **1000 razy** na losowych listach (np. `len=10`) i **uśrednić liczbę iteracji**.

2. **Skuteczność technik**:
   - Zliczyć, **która technika najczęściej kończy algorytm** (np. Wielki Skok powinien być najskuteczniejszy).

3. **Zależność od rozmiaru listy**:
   - Sprawdzić, jak **liczba iteracji** zależy od `len(lst)`.

**Przykładowy test**:
```python
def test_average_iterations():
    results = []
    for _ in range(1000):
        lst = [random.randint(1, 100) for _ in range(10)]
        _, iterations, _ = mao_sort(lst)
        results.append(iterations)
    avg_iterations = sum(results) / len(results)
    print(f"Średnia liczba iteracji: {avg_iterations}")
```

---
---

### **4. Struktura skryptu (propozycja)**
**Plik**: `mao_sort.py`

```python
import random
from statistics import median
from typing import List, Dict, Union, Optional

# --- Funkcje technik ---
def kolektywizacja(lst: List[Union[int, float]], k_min: int = 1, k_max: Optional[int] = None) -> List[Union[int, float]]:
    """Zastąp losowy podzbiór elementów ich średnią (zaokrągloną)."""
    ...

def samokrytyka(lst: List[Union[int, float]]) -> List[Union[int, float]]:
    """Zastąp losowy element medianą listy."""
    ...

def reedukacja(lst: List[Union[int, float]]) -> List[Union[int, float]]:
    """Zamień losowe 2 elementy miejscami."""
    ...

def wielki_skok(lst: List[Union[int, float]], k_min: int = 1, k_max: Optional[int] = None) -> List[Union[int, float]]:
    """Zastąp losową część listy kopiami losowo wybranego elementu."""
    ...

def czystka(lst: List[Union[int, float]], direction: Optional[str] = None) -> List[Union[int, float]]:
    """Zastąp elementy odstające (w górę/dół od mediany) losowymi wartościami z przeciwnej połowy."""
    ...

# --- Główna funkcja ---
def mao_sort(
    lst: List[Union[int, float]],
    max_iterations: int = 10000,
    technique_weights: Optional[Dict[str, float]] = None,
    kolektywizacja_k_min: int = 1,
    kolektywizacja_k_max: Optional[int] = None,
    wielki_skok_k_min: int = 1,
    wielki_skok_k_max: Optional[int] = None,
    czystka_direction: Optional[str] = None,
) -> Dict[str, Union[List[Union[int, float]], int, str]]:
    """
    Mao Sort – algorytm sortujący przez chaotyczną homogenizację.

    Args:
        lst: Lista liczb (int lub float) do posortowania.
        max_iterations: Maksymalna liczba iteracji.
        technique_weights: Słownik wag dla technik (np. {'kolektywizacja': 0.3}).
        kolektywizacja_k_min: Minimalna liczba elementów do zastąpienia w kolektywizacji.
        kolektywizacja_k_max: Maksymalna liczba elementów do zastąpienia w kolektywizacji.
        wielki_skok_k_min: Minimalna liczba elementów do zastąpienia w Wielkim Skoku.
        wielki_skok_k_max: Maksymalna liczba elementów do zastąpienia w Wielkim Skoku.
        czystka_direction: Kierunek czystki ('up', 'down' lub None – losowo).

    Returns:
        Słownik z kluczami:
        - 'result': Ostateczna lista (jednowartościowa lub po max_iterations).
        - 'iterations': Liczba wykonanych iteracji.
        - 'last_technique': Ostatnia użyta technika.
    """
    ...

# --- Testy (opcjonalnie w osobnym pliku) ---
if __name__ == "__main__":
    # Przykład użycia
    result = mao_sort([1, 2, 3, 4, 5], max_iterations=1000)
    print(f"Wynik: {result['result']}")
    print(f"Iteracje: {result['iterations']}")
    print(f"Ostatnia technika: {result['last_technique']}")
```

---
---

### **5. Notatki do zrobienia (TODO)**
1. **Poprawki błędów**:
   - [ ] `czystka` → użyć `median` + losowanie z `lower_half`/`upper_half`.
   - [ ] `wielki_skok` → zastępować **losową część listy** (nie całą).
   - [ ] `kolektywizacja`/`samokrytyka` → użyć `round()` zamiast `int()`.
   - [ ] Obsługa **pustej listy** i **list 1-elementowych**.

2. **Rozszerzenia technik**:
   - [ ] Dodać **parametry `technique_weights`**, `k_min`/`k_max`, `czystka_direction`.
   - [ ] Zwracać **`iterations` (liczba) + `last_technique` (string)**.

3. **Testowanie**:
   - [ ] Napisać **testy jednostkowe** (dla każdej techniki).
   - [ ] Napisać **testy statystyczne** (średnia liczba iteracji, skuteczność technik).

4. **Dokumentacja (na koniec)**:
   - [ ] **README.md** z:
     - Opisem **filozofii Mao Sort**.
     - **Przykładami użycia**.
     - **Opisem technik** (z przykładami).
     - **Parametrami funkcji `mao_sort`**.
     - **Przykładami wyjścia**.

---
---
---
## **🎯 Podsumowanie: Co robić w kolejności?**
1. **Poprawki błędów** (czystka, Wielki Skok, typy, edge cases).
2. **Dodanie parametrów** (`technique_weights`, `k_min`/`k_max`, `czystka_direction`).
3. **Zmiana zwracanych wartości** (`result`, `iterations`, `last_technique`).
4. **Testy jednostkowe** (pytest).
5. **Testy statystyczne** (opcjonalnie).
6. **Dokumentacja (README.md)**.

---
**Czy to jest jasne? Czy chcesz, bym rozpisał któryś punkt bardziej szczegółowo?**
