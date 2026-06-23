#!/usr/bin/env python3
"""
Mao Sort – algorytm sortujący przez chaotyczną homogenizację.

Filozofia:
----------
MAO SORT to algorytm, którego celem jest osiągnięcie listy maksymalnie ujednoliconej,
zgodnie z ideą "w komunizmie wszystkie zmienne są równe". Ostatecznym sukcesem
jest lista złożona z n kopii tej samej wartości (ideologiczna jedność).

Metoda:
-------
W każdej iteracji algorytm losowo wybiera jedną z 5 technik rewolucyjnych:
1. Kolektywizacja – zastąp losowy podzbiór elementów ich średnią (zaokrągloną)
2. Samokrytyka – zastąp losowy element medianą listy
3. Reedukacja – zamień losowe 2 elementy miejscami
4. Wielki Skok – zastąp losową część listy kopiami losowo wybranego elementu
5. Czystka – zastąp elementy odstające losowymi wartościami z przeciwnej połowy

Autor: Inspirowany polityką Mao Zedonga
"""

import random
from statistics import median
from typing import List, Dict, Union, Optional, Any


# =============================================================================
# FUNKCJE TECHNIK REWOLUCYJNYCH
# =============================================================================

def kolektywizacja(
    lst: List[Union[int, float]],
    k_min: int = 1,
    k_max: Optional[int] = None
) -> List[Union[int, float]]:
    """
    Kolektywizacja: Zastąp losowy podzbiór elementów ich średnią (zaokrągloną).
    
    Args:
        lst: Lista liczb do przetworzenia
        k_min: Minimalna liczba elementów do zastąpienia
        k_max: Maksymalna liczba elementów do zastąpienia (domyślnie len(lst))
    
    Returns:
        Nowa lista z zastąpionymi elementami
    """
    if len(lst) == 0:
        return lst
    
    if k_max is None:
        k_max = len(lst)
    
    k = random.randint(k_min, k_max)
    avg = round(sum(lst) / len(lst))
    indices = random.sample(range(len(lst)), k)
    
    new_lst = lst.copy()
    for i in indices:
        new_lst[i] = avg
    
    return new_lst


def samokrytyka(lst: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Samokrytyka: Zastąp losowy element medianą listy.
    
    Args:
        lst: Lista liczb do przetworzenia
    
    Returns:
        Nowa lista z zastąpionym elementem
    """
    if len(lst) == 0:
        return lst
    
    med = round(median(lst))
    i = random.randint(0, len(lst) - 1)
    
    new_lst = lst.copy()
    new_lst[i] = med
    
    return new_lst


def reedukacja(lst: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Reedukacja: Zamień losowe 2 elementy miejscami.
    
    Args:
        lst: Lista liczb do przetworzenia
    
    Returns:
        Nowa lista z zamienionymi elementami
    """
    if len(lst) < 2:
        return lst.copy()
    
    i, j = random.sample(range(len(lst)), 2)
    new_lst = lst.copy()
    new_lst[i], new_lst[j] = new_lst[j], new_lst[i]
    
    return new_lst


def wielki_skok(
    lst: List[Union[int, float]],
    k_min: int = 1,
    k_max: Optional[int] = None
) -> List[Union[int, float]]:
    """
    Wielki Skok: Zastąp losową część listy kopiami losowo wybranego elementu.
    
    Args:
        lst: Lista liczb do przetworzenia
        k_min: Minimalna liczba elementów do zastąpienia
        k_max: Maksymalna liczba elementów do zastąpienia (domyślnie len(lst))
    
    Returns:
        Nowa lista z zastąpionymi elementami
    """
    if len(lst) == 0:
        return lst
    
    if k_max is None:
        k_max = len(lst)
    
    k = random.randint(k_min, k_max)
    chosen = random.choice(lst)
    indices = random.sample(range(len(lst)), k)
    
    new_lst = lst.copy()
    for i in indices:
        new_lst[i] = chosen
    
    return new_lst


def czystka(
    lst: List[Union[int, float]],
    direction: Optional[str] = None
) -> List[Union[int, float]]:
    """
    Czystka: Zastąp elementy odstające losowymi wartościami z przeciwnej połowy.
    
    Args:
        lst: Lista liczb do przetworzenia
        direction: Kierunek czystki ('up', 'down' lub None dla losowego)
    
    Returns:
        Nowa lista po czystce
    """
    if len(lst) == 0:
        return lst
    
    threshold = median(lst)
    lower_half = [x for x in lst if x <= threshold]
    upper_half = [x for x in lst if x > threshold]
    
    # Jeśli jedna z połówek jest pusta, nie można wykonać czystki
    if not lower_half or not upper_half:
        return lst.copy()
    
    # Wybierz kierunek czystki
    if direction == 'up':
        # Czystka w górę: zastąp elementy > threshold wartościami z lower_half
        return [random.choice(lower_half) if x > threshold else x for x in lst]
    elif direction == 'down':
        # Czystka w dół: zastąp elementy < threshold wartościami z upper_half
        return [random.choice(upper_half) if x < threshold else x for x in lst]
    else:
        # Losowy kierunek
        if random.choice([True, False]):
            return [random.choice(lower_half) if x > threshold else x for x in lst]
        else:
            return [random.choice(upper_half) if x < threshold else x for x in lst]


# =============================================================================
# GŁÓWNA FUNKCJA MAO SORT
# =============================================================================

def mao_sort(
    lst: List[Union[int, float]],
    max_iterations: int = 10000,
    technique_weights: Optional[Dict[str, float]] = None,
    kolektywizacja_k_min: int = 1,
    kolektywizacja_k_max: Optional[int] = None,
    wielki_skok_k_min: int = 1,
    wielki_skok_k_max: Optional[int] = None,
    czystka_direction: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Mao Sort – algorytm sortujący przez chaotyczną homogenizację.
    
    Algorytm losowo wybiera jedną z 5 technik rewolucyjnych w każdej iteracji,
    dążąc do osiągnięcia listy jednowartościowej (ideologicznej jedności).
    
    Args:
        lst: Lista liczb (int lub float) do posortowania
        max_iterations: Maksymalna liczba iteracji (domyślnie 10000)
        technique_weights: Słownik wag dla technik (np. {'kolektywizacja': 0.3}).
                          Jeśli None, używa równych wag (0.2 dla każdej techniki).
        kolektywizacja_k_min: Minimalna liczba elementów do zastąpienia w kolektywizacji
        kolektywizacja_k_max: Maksymalna liczba elementów do zastąpienia w kolektywizacji
        wielki_skok_k_min: Minimalna liczba elementów do zastąpienia w Wielkim Skoku
        wielki_skok_k_max: Maksymalna liczba elementów do zastąpienia w Wielkim Skoku
        czystka_direction: Kierunek czystki ('up', 'down' lub None dla losowego)
    
    Returns:
        Słownik z kluczami:
        - 'result': Ostateczna lista (jednowartościowa lub po max_iterations)
        - 'iterations': Liczba wykonanych iteracji (goła liczba)
        - 'last_technique': Ostatnia użyta technika (string)
    
    Raises:
        TypeError: Jeśli lst nie jest listą liczb
        ValueError: Jeśli wagi technik nie sumują się do ~1.0
    
    Examples:
        >>> mao_sort([1, 2, 3, 4, 5], max_iterations=1000)
        {'result': [3, 3, 3, 3, 3], 'iterations': 42, 'last_technique': 'wielki_skok'}
        
        >>> mao_sort([1.5, 2.5, 3.5], technique_weights={'czystka': 0.5})
        {'result': [2.5, 2.5, 2.5], 'iterations': 15, 'last_technique': 'czystka'}
    """
    # Walidacja wejścia
    if not isinstance(lst, list):
        raise TypeError("lst musi być listą")
    
    if not all(isinstance(x, (int, float)) for x in lst):
        raise TypeError("Wszystkie elementy listy muszą być liczbami (int lub float)")
    
    # Obsługa edge cases
    if len(lst) == 0:
        return {'result': [], 'iterations': 0, 'last_technique': None}
    
    if len(lst) == 1:
        return {'result': lst.copy(), 'iterations': 0, 'last_technique': None}
    
    # Konwersja do float dla spójności (zachowuje int jeśli wszystkie są int)
    if all(isinstance(x, int) for x in lst):
        lst = [float(x) for x in lst]
    
    # Domyślne wagi technik
    default_weights = {
        'kolektywizacja': 0.2,
        'samokrytyka': 0.2,
        'reedukacja': 0.2,
        'wielki_skok': 0.2,
        'czystka': 0.2,
    }
    
    if technique_weights is None:
        technique_weights = default_weights
    else:
        # Walidacja wag
        if not set(technique_weights.keys()).issubset(set(default_weights.keys())):
            raise ValueError(f"Nieprawidłowe nazwy technik. Dostępne: {list(default_weights.keys())}")
        
        if not (0.99 <= sum(technique_weights.values()) <= 1.01):
            raise ValueError("Wagi technik muszą sumować się do ~1.0")
    
    # Inicjalizacja
    current_lst = lst.copy()
    last_technique = None
    
    # Główna pętla
    for iteration in range(max_iterations):
        # Sprawdź warunek zakończenia (wszystkie elementy równe)
        if len(set(current_lst)) == 1:
            return {
                'result': current_lst,
                'iterations': iteration,
                'last_technique': last_technique
            }
        
        # Wybierz technikę z uwzględnieniem wag
        techniques = list(technique_weights.keys())
        weights = list(technique_weights.values())
        technique = random.choices(techniques, weights=weights, k=1)[0]
        last_technique = technique
        
        # Zastosuj wybraną technikę
        if technique == 'kolektywizacja':
            current_lst = kolektywizacja(
                current_lst,
                k_min=kolektywizacja_k_min,
                k_max=kolektywizacja_k_max
            )
        elif technique == 'samokrytyka':
            current_lst = samokrytyka(current_lst)
        elif technique == 'reedukacja':
            current_lst = reedukacja(current_lst)
        elif technique == 'wielki_skok':
            current_lst = wielki_skok(
                current_lst,
                k_min=wielki_skok_k_min,
                k_max=wielki_skok_k_max
            )
        elif technique == 'czystka':
            current_lst = czystka(current_lst, direction=czystka_direction)
    
    # Jeśli nie osiągnięto jednowartościowości w max_iterations
    return {
        'result': current_lst,
        'iterations': max_iterations,
        'last_technique': last_technique
    }


# =============================================================================
# PRZYKŁAD UŻYCIA
# =============================================================================

if __name__ == "__main__":
    # Przykład 1: Podstawowe użycie
    print("=== Przykład 1: Podstawowe użycie ===")
    result = mao_sort([1, 2, 3, 4, 5], max_iterations=1000)
    print(f"Wynik: {result['result']}")
    print(f"Iteracje: {result['iterations']}")
    print(f"Ostatnia technika: {result['last_technique']}")
    print()
    
    # Przykład 2: Z niestandardowymi wagami
    print("=== Przykład 2: Z niestandardowymi wagami ===")
    weights = {
        'kolektywizacja': 0.1,
        'samokrytyka': 0.1,
        'reedukacja': 0.1,
        'wielki_skok': 0.5,  # Wielki Skok ma większe szanse
        'czystka': 0.2,
    }
    result = mao_sort([1, 2, 3, 4, 5], max_iterations=1000, technique_weights=weights)
    print(f"Wynik: {result['result']}")
    print(f"Iteracje: {result['iterations']}")
    print(f"Ostatnia technika: {result['last_technique']}")
    print()
    
    # Przykład 3: Z parametrami dla Wielkiego Skoku
    print("=== Przykład 3: Z parametrami dla Wielkiego Skoku ===")
    result = mao_sort(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        max_iterations=1000,
        wielki_skok_k_min=3,
        wielki_skok_k_max=5
    )
    print(f"Wynik: {result['result']}")
    print(f"Iteracje: {result['iterations']}")
    print(f"Ostatnia technika: {result['last_technique']}")
    print()
    
    # Przykład 4: Z kierunkiem czystki
    print("=== Przykład 4: Z kierunkiem czystki (w górę) ===")
    result = mao_sort(
        [1, 2, 4, 6, 8, 10],
        max_iterations=1000,
        czystka_direction='up'
    )
    print(f"Wynik: {result['result']}")
    print(f"Iteracje: {result['iterations']}")
    print(f"Ostatnia technika: {result['last_technique']}")
    print()
    
    # Przykład 5: Edge case - pusta lista
    print("=== Przykład 5: Edge case - pusta lista ===")
    result = mao_sort([])
    print(f"Wynik: {result['result']}")
    print(f"Iteracje: {result['iterations']}")
    print(f"Ostatnia technika: {result['last_technique']}")
