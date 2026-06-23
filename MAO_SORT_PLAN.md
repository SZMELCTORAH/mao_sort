# Mao Sort – Plan Implementacji

---

## Potwierdzone wymagania

1. Poprawki bledow w technikach -> TAK (priorytet wysoki)
2. Rozszerzenia technik -> TAK (parametryzacja, statystyki)
3. Kejsy -> Już w tekście (pomijamy na razie)
4. Testowanie -> TAK
5. Licznik iteracji -> Goła liczba (np. 42)
6. Historia technik -> Tylko ostatnia technika (np. "poprzednio użyta technika: czystka")
7. Optymalizacje -> NIE
8. Filozofia -> NIE
9. Dokumentacja -> TAK, ale na końcu (zwarta, w README.md)

---

## Konkrety: Co i jak zrobić?

---

### 1. Poprawki błędów w technikach

#### Kolektywizacja
Problem: int() obcina ułamek zamiast zaokrąglać.
Rozwiązanie:
```python
avg = round(sum(lst) / len(lst))  # Zamiast int()
```

#### Samokrytyka
Problem: int() obcina ułamek zamiast zaokrąglać.
Rozwiązanie:
```python
med = round(median(lst))  # Zamiast int()
```

#### Wielki Skok
Problem: Kod zastępuje całą listę jednym elementem, a specyfikacja mówi o losowej części listy.
Rozwiązanie:
```python
def wielki_skok(lst, k_min=1, k_max=None):
    if k_max is None:
        k_max = len(lst)
    k = random.randint(k_min, k_max)
    chosen = random.choice(lst)
    indices = random.sample(range(len(lst)), k)
    new_lst = lst.copy()
    for i in indices:
        new_lst[i] = chosen
    return new_lst
```

#### Czystka
Problem: Kod używa mody zamiast median/mean i losuje z całego zakresu, a nie z podzbioru niepoddanego czystce.
Rozwiązanie:
```python
def czystka(lst, direction=None):
    threshold = median(lst)
    lower_half = [x for x in lst if x <= threshold]
    upper_half = [x for x in lst if x > threshold]
    
    if not lower_half or not upper_half:
        return lst
    
    if direction == 'up':
        return [random.choice(lower_half) if x > threshold else x for x in lst]
    elif direction == 'down':
        return [random.choice(upper_half) if x < threshold else x for x in lst]
    else:
        if random.choice([True, False]):
            return [random.choice(lower_half) if x > threshold else x for x in lst]
        else:
            return [random.choice(upper_half) if x < threshold else x for x in lst]
```

#### Edge Cases
Problem: Pusta lista, lista 1-elementowa, floaty.
Rozwiązanie:
```python
def mao_sort(lst, max_iterations=10000, ...):
    if not lst:
        return {'result': [], 'iterations': 0, 'last_technique': None}
    lst = [float(x) if isinstance(x, int) else x for x in lst]
```

---

### 2. Rozszerzenia technik (parametryzacja)

#### Parametry dla mao_sort
```python
def mao_sort(
    lst,
    max_iterations=10000,
    technique_weights=None,
    kolektywizacja_k_min=1,
    kolektywizacja_k_max=None,
    wielki_skok_k_min=1,
    wielki_skok_k_max=None,
    czystka_direction=None,
):
```

#### Domyślne wagi technik
```python
default_weights = {
    'kolektywizacja': 0.2,
    'samokrytyka': 0.2,
    'reedukacja': 0.2,
    'wielki_skok': 0.2,
    'czystka': 0.2,
}
```

#### Losowanie techniki z wagami
```python
if technique_weights is None:
    technique_weights = default_weights

techniques = list(technique_weights.keys())
weights = list(technique_weights.values())
technique = random.choices(techniques, weights=weights, k=1)[0]
```

#### Parametry k_min i k_max
```python
k = random.randint(k_min, k_max if k_max is not None else len(lst))
```

---

### 3. Zwracane wartości
Format:
```python
{
    'result': lst,
    'iterations': count,
    'last_technique': last_technique,
}
```

Przykład:
```python
{
    'result': [5.0, 5.0, 5.0],
    'iterations': 42,
    'last_technique': 'wielki_skok',
}
```

---

### 4. Testowanie

#### Testy jednostkowe (pytest)

##### Kolektywizacja
```python
def test_kolektywizacja():
    lst = [1, 2, 3, 4]
    result = kolektywizacja(lst, k_min=2, k_max=2)
    avg = round(sum(lst) / len(lst))
    assert sum(1 for x in result if x == avg) >= 2
```

##### Samokrytyka
```python
def test_samokrytyka():
    lst = [1, 2, 3, 4, 5]
    original = lst.copy()
    result = samokrytyka(lst)
    med = round(median(lst))
    assert result.count(med) == original.count(med) + 1
```

##### Reedukacja
```python
def test_reedukacja():
    lst = [1, 2, 3, 4]
    original = lst.copy()
    result = reedukacja(lst)
    assert sorted(result) == sorted(original)
    assert result != original
```

##### Wielki Skok
```python
def test_wielki_skok():
    lst = [1, 2, 3, 4]
    result = wielki_skok(lst, k_min=2, k_max=2)
    chosen = random.choice(lst)
    assert result.count(chosen) == 2
```

##### Czystka
```python
def test_czystka():
    lst = [1, 2, 4, 6, 8, 10]
    result = czystka(lst, direction='up')
    threshold = median(lst)
    lower_half = [x for x in lst if x <= threshold]
    for x in result:
        if x > threshold:
            assert x in lower_half
```

##### Edge Cases
```python
def test_empty_list():
    assert mao_sort([]) == {'result': [], 'iterations': 0, 'last_technique': None}

def test_single_element():
    assert mao_sort([5]) == {'result': [5], 'iterations': 0, 'last_technique': None}
```

#### Testy statystyczne (opcjonalnie)
```python
def test_average_iterations():
    iterations = []
    for _ in range(100):
        lst = [random.randint(1, 100) for _ in range(10)]
        result = mao_sort(lst, max_iterations=10000)
        iterations.append(result['iterations'])
    avg_iterations = sum(iterations) / len(iterations)
    print(f"Średnia liczba iteracji: {avg_iterations}")
```

---

### 5. Struktura pliku mao_sort.py

```python
import random
from statistics import median
from typing import List, Dict, Union, Optional

# Funkcje technik
def kolektywizacja(lst, k_min=1, k_max=None):
    """Zastąp losowy podzbiór elementów ich średnią (zaokrągloną)."""
    ...

def samokrytyka(lst):
    """Zastąp losowy element medianą listy."""
    ...

def reedukacja(lst):
    """Zamień losowe 2 elementy miejscami."""
    ...

def wielki_skok(lst, k_min=1, k_max=None):
    """Zastąp losową część listy kopiami losowo wybranego elementu."""
    ...

def czystka(lst, direction=None):
    """Zastąp elementy odstające (w górę/dół od mediany) losowymi wartościami z przeciwnej połowy."""
    ...

# Główna funkcja
def mao_sort(
    lst,
    max_iterations=10000,
    technique_weights=None,
    kolektywizacja_k_min=1,
    kolektywizacja_k_max=None,
    wielki_skok_k_min=1,
    wielki_skok_k_max=None,
    czystka_direction=None,
):
    """Mao Sort – algorytm sortujący przez chaotyczną homogenizację."""
    ...

# Przykład użycia
if __name__ == "__main__":
    result = mao_sort([1, 2, 3, 4, 5], max_iterations=1000)
    print(f"Wynik: {result['result']}")
    print(f"Iteracje: {result['iterations']}")
    print(f"Ostatnia technika: {result['last_technique']}")
```

---

## Notatki do zrobienia (TODO)

### Poprawki bledow
- [ ] czystka -> uzyc median + losowanie z lower_half/upper_half
- [ ] wielki_skok -> zastępować losową część listy (parametry k_min, k_max)
- [ ] kolektywizacja/samokrytyka -> uzyc round() zamiast int()
- [ ] Obsluga pustej listy i list 1-elementowych
- [ ] Obsluga floatow (nie tracić precyzji)

### Rozszerzenia technik
- [ ] Dodac parametr technique_weights (wagi dla technik)
- [ ] Dodac parametry k_min/k_max dla kolektywizacji i Wielkiego Skoku
- [ ] Dodac parametr czystka_direction (up, down lub None)
- [ ] Zwracac iterations (liczba) + last_technique (string)

### Testowanie
- [ ] Napisać testy jednostkowe (dla każdej techniki)
- [ ] Napisać testy edge cases (pusta lista, 1 element, floaty)
- [ ] Opcjonalnie: testy statystyczne

### Dokumentacja (na koniec)
- [ ] README.md z:
  - Opisem filozofii Mao Sort
  - Przykładami użycia (z parametrami)
  - Opisem technik (z przykładami)
  - Parametrami funkcji mao_sort
  - Przykładami wyjścia

---

## Kolejność działań
1. Poprawki bledow (czystka, Wielki Skok, typy, edge cases)
2. Dodanie parametrow (technique_weights, k_min/k_max, czystka_direction)
3. Zmiana zwracanych wartosci (result, iterations, last_technique)
4. Testy jednostkowe (pytest)
5. Dokumentacja (README.md)
