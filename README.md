# Mao Sort

> *"W komunizmie wszystkie zmienne są równe"*

**Mao Sort** to satyryczny algorytm sortowania inspirowany polityką Mao Zedonga. Zamiast dążyć do posortowania listy w tradycyjnym sensie, Mao Sort stara się osiągnąć **ideologiczną jedność** — listę złożoną z *n* kopii tej samej wartości. Cel jest jasny, ale metody są chaotyczne, losowe i często nieskuteczne — doskonała metafora Wielkiego Skoku i Rewolucji Kulturalnej.

---

## 📚 Spis treści

- [Filozofia](#-filozofia)
- [Techniki Rewolucyjne](#-techniki-rewolucyjne)
- [Instalacja](#-instalacja)
- [Użycie](#-użycie)
- [Parametry](#-parametry)
- [Przykłady](#-przykłady)
- [Testowanie](#-testowanie)
- [Filozoficzne Podsumowanie](#-filozoficzne-podsumowanie)
- [Licencja](#-licencja)

---

## 🎯 Filozofia

### Cel
Ostatecznym sukcesem Mao Sort jest **lista jednowartościowa** — wszystkie elementy równe. To symbolizuje ideologiczną jedność, do której dążył Mao Zedong w Chinach.

### Metoda
Algorytm **nie stosuje deterministycznych metod sortowania**. Zamiast tego, w każdej iteracji **losowo wybiera jedną z 5 technik rewolucyjnych**, z których każda w różny sposób niszczy strukturę listy, dążąc (lub nie) do homogenizacji.

> **"Cel ideologicznie spójny (lista jednorodna, wszyscy równi) osiągany metodami losowo destrukcyjnymi albo nieskutecznymi. To jest właściwie bardzo wierna metafora Wielkiego Skoku i Rewolucji Kulturalnej — kierunek był określony, metody były chaotyczne i katastrofalne, wynik był przewidywalny tylko w tym sensie, że zawsze był zły."**

### Złożoność
- **Niedefiniowalna** w klasycznym sensie (zależy od losowości)
- **Probabilistyczna**: Czasem kończy się błyskawicznie (Wielki Skok), czasem nigdy
- **Rozkład ciężkoogonowy**: Można opisać tylko statystycznie

---

## 🔧 Techniki Rewolucyjne

Mao Sort używa 5 technik, z których każda symuluje inny aspekt polityki Mao:

### 1. 🏭 Kolektywizacja
**"Zjednoczenie środków produkcji"**

- **Działanie**: Zastąp losowy podzbiór elementów ich **średnią arytmetyczną (zaokrągloną)**
- **Przykład**: `[1, 2, 4, 6, 8, 10]` → średnia = 5 → `[1, 2, 5, 5, 8, 10]` (losowe 2 elementy zastąpione 5)
- **Metafora**: Kolektywizacja rolnictwa — średnia wydajność dla wszystkich

### 2. 🎭 Samokrytyka
**"Przyznanie się do błędów i poprawa"**

- **Działanie**: Zastąp **losowy element** **medianą listy**
- **Przykład**: `[1, 2, 4, 6, 8, 10]` → mediana = 5 → `[1, 5, 4, 6, 8, 10]`
- **Metafora**: Publiczne przyznanie się do błędów i dostosowanie do linii partyjnej

### 3. 🎓 Reedukacja
**"Przeszkolenie ideologiczne"**

- **Działanie**: Zamień **losowe 2 elementy** miejscami
- **Przykład**: `[1, 2, 4, 6, 8, 10]` → `[4, 2, 1, 6, 8, 10]`
- **Metafora**: Przeszkolenie kadry — wymiana ludzi, ale bez realnej zmiany systemu
- **Cechy**: Operacja **neutralna ideologicznie**, ale pochłaniająca zasoby

### 4. 🚀 Wielki Skok
**"Przyspieszona modernizacja"**

- **Działanie**: Zastąp **losową część listy** kopiami **losowo wybranego elementu**
- **Przykład**: `[1, 2, 4, 6, 8, 10]` → `[1, 1, 1, 1, 8, 10]` (losowe 4 elementy zastąpione 1)
- **Metafora**: Wielki Skok Naprzód — gwałtowne zmiany, które mogą doprowadzić do sukcesu lub katastrofy
- **Uwaga**: **Może jednym skokiem osiągnąć cel** (jeśli zastąpi całą listę) lub **całkowicie zniszczyć postęp**

### 5. ⚔️ Czystka
**"Eliminacja elementów kontrrewolucyjnych"**

- **Działanie**: Zastąp elementy **odstające** (w górę lub w dół od mediany) **losowymi wartościami z przeciwnej połowy**
- **Przykład**: `[1, 2, 4, 6, 8, 10]` → mediana = 5 → elementy >5 (`6,8,10`) zastąpione losowymi wartościami z `[1,2,4]` → `[1, 2, 4, 1, 2, 4]`
- **Metafora**: Czystki polityczne — eliminacja "wrogów ludu"
- **Kierunki**:
  - `'up'`: Czystka elementów **większych od mediany** (zastępowanie wartościami z dolnej połowy)
  - `'down'`: Czystka elementów **mniejszych od mediany** (zastępowanie wartościami z górnej połowy)
  - `None`: Losowy kierunek

---

## 💻 Instalacja

### Wymagania
- Python 3.7+
- `statistics` (wbudowany w Python 3.4+)
- `pytest` (opcjonalnie, do testów)

### Instalacja z repozytorium
```bash
# Sklonuj repozytorium
git clone https://github.com/twoje-repo/mao_sort.git
cd mao_sort

# Opcjonalnie: Utwórz środowisko wirtualne
python -m venv venv
source venv/bin/activate  # Linux/Mac
# lub
venv\Scripts\activate  # Windows

# Zainstaluj zależności (tylko pytest do testów)
pip install pytest
```

---

## 🚀 Użycie

### Podstawowe użycie
```python
from mao_sort import mao_sort

result = mao_sort([1, 2, 3, 4, 5])
print(result)
# Output: {'result': [3.0, 3.0, 3.0, 3.0, 3.0], 'iterations': 42, 'last_technique': 'wielki_skok'}
```

### Uruchomienie z linii poleceń
```bash
# Uruchom skrypt z przykładami
python mao_sort.py

# Uruchom testy
pytest test_mao_sort.py -v
```

---

## ⚙️ Parametry

Funkcja `mao_sort()` akceptuje następujące parametry:

| Parametr | Typ | Domyślna wartość | Opis |
|----------|-----|------------------|------|
| `lst` | `List[Union[int, float]]` | **Wymagany** | Lista liczb do "posortowania" |
| `max_iterations` | `int` | `10000` | Maksymalna liczba iteracji |
| `technique_weights` | `Optional[Dict[str, float]]` | `None` | Wagi dla technik (muszą sumować się do ~1.0) |
| `kolektywizacja_k_min` | `int` | `1` | Minimalna liczba elementów do zastąpienia w kolektywizacji |
| `kolektywizacja_k_max` | `Optional[int]` | `None` | Maksymalna liczba elementów do zastąpienia w kolektywizacji (domyślnie `len(lst)`) |
| `wielki_skok_k_min` | `int` | `1` | Minimalna liczba elementów do zastąpienia w Wielkim Skoku |
| `wielki_skok_k_max` | `Optional[int]` | `None` | Maksymalna liczba elementów do zastąpienia w Wielkim Skoku (domyślnie `len(lst)`) |
| `czystka_direction` | `Optional[str]` | `None` | Kierunek czystki (`'up'`, `'down'` lub `None` dla losowego) |

### Zwracane wartości
Funkcja zwraca **słownik** z następującymi kluczami:

| Klucz | Typ | Opis |
|-------|-----|------|
| `'result'` | `List[Union[int, float]]` | Ostateczna lista (jednowartościowa lub po `max_iterations`) |
| `'iterations'` | `int` | **Goła liczba** iteracji potrzebnych do osiągnięcia celu (lub `max_iterations`) |
| `'last_technique'` | `Optional[str]` | Ostatnia użyta technika (lub `None`, jeśli nie wykonano żadnej iteracji) |

---

## 📝 Przykłady

### 1. Podstawowe użycie
```python
from mao_sort import mao_sort

result = mao_sort([1, 2, 3, 4, 5], max_iterations=1000)
print(f"Wynik: {result['result']}")
print(f"Iteracje: {result['iterations']}")
print(f"Ostatnia technika: {result['last_technique']}")
```

### 2. Z niestandardowymi wagami technik
```python
weights = {
    'kolektywizacja': 0.1,
    'samokrytyka': 0.1,
    'reedukacja': 0.1,
    'wielki_skok': 0.5,  # Wielki Skok ma 50% szans
    'czystka': 0.2,
}

result = mao_sort([1, 2, 3, 4, 5], technique_weights=weights)
```

### 3. Z parametrami dla Wielkiego Skoku
```python
result = mao_sort(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    wielki_skok_k_min=3,
    wielki_skok_k_max=5  # Wielki Skok zastępuje 3-5 elementów
)
```

### 4. Z kierunkiem czystki
```python
result = mao_sort(
    [1, 2, 4, 6, 8, 10],
    czystka_direction='up'  # Czystka tylko elementów większych od mediany
)
```

### 5. Edge Cases
```python
# Pusta lista
mao_sort([])  # {'result': [], 'iterations': 0, 'last_technique': None}

# Lista 1-elementowa (już jednowartościowa)
mao_sort([5])  # {'result': [5.0], 'iterations': 0, 'last_technique': None}

# Floaty
mao_sort([1.5, 2.5, 3.5])  # {'result': [2.5, 2.5, 2.5], 'iterations': 10, 'last_technique': 'samokrytyka'}
```

---

## 🧪 Testowanie

Projekt zawiera **testy jednostkowe** dla wszystkich technik i głównej funkcji.

### Uruchomienie testów
```bash
# Wszystkie testy
pytest test_mao_sort.py -v

# Tylko szybkie testy (bez statystycznych)
pytest test_mao_sort.py -v -m "not slow"

# Tylko testy statystyczne
pytest test_mao_sort.py -v -m "slow"
```

### Pokrycie testami
- ✅ Kolektywizacja
- ✅ Samokrytyka
- ✅ Reedukacja
- ✅ Wielki Skok
- ✅ Czystka
- ✅ Główna funkcja `mao_sort`
- ✅ Edge Cases (pusta lista, 1 element, floaty)
- ✅ Walidacja wejścia
- ✅ Statystyczne (opcjonalne)

---

## 🎭 Filozoficzne Podsumowanie

Mao Sort to **satyryczna krytyka** podejścia do zarządzania i reform społecznych:

1. **Cel jest szlachetny**: Równość, jedność, homogenizacja
2. **Metody są chaotyczne**: Losowe, niespójne, często szkodliwe
3. **Wynik jest nieprzewidywalny**: Czasem sukces (przypadkowa jednowartościowość), czasem porażka (nieskończona pętla)
4. **Koszt jest wysoki**: Każda iteracja to marnotrawstwo zasobów

> **"MAO SORT W TEORII MA 5 METODAMI SZYBKO OSIĄGAĆ RÓWNOŚĆ. W PRAKTYCE JEDNAK DZIAŁANIA TAK SAMO PRZYBLIŻAJĄ JAK I ODDALAJĄ CEL."**

### Analogia historyczna
| Element algorytmu | Analogia historyczna |
|-------------------|----------------------|
| Cel (jednowartościowość) | Społeczeństwo klasowe → społeczeństwo bezklasowe |
| Kolektywizacja | Kolektywizacja rolnictwa |
| Samokrytyka | Kampanie samokrytyki |
| Reedukacja | Przeszkolenie ideologiczne |
| Wielki Skok | Wielki Skok Naprzód |
| Czystka | Czystki polityczne |
| Losowość | Chaos i brak planu |
| Nieskończona pętla | Stagnacja i brak postępu |

---

## 📜 Licencja

Projekt jest udostępniany na licencji **MIT** — używaj, modyfikuj i rozpowszechniaj swobodnie.

```
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 📬 Kontakt

Jeśli masz pytania, pomysły na ulepszenia lub chcesz podzielić się swoimi doświadczeniami z Mao Sort, **nie wahaj się skontaktować**!

> **"Rewolucja to nie obiad, nie jest dziełem jednego człowieka. Rewolucja to działanie mas.**"
> — Mao Zedong (prawdopodobnie nie o algorytmach sortowania)

---

*Projekt stworzony z miłością do ironii, historii i algorytmów.* 🚀
