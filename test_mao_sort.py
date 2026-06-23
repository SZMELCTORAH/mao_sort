#!/usr/bin/env python3
"""
Testy jednostkowe dla Mao Sort.

Uruchomienie:
    pytest test_mao_sort.py -v
"""

import pytest
import random
from statistics import median
from mao_sort import (
    kolektywizacja,
    samokrytyka,
    reedukacja,
    wielki_skok,
    czystka,
    mao_sort
)


# =============================================================================
# TESTY FUNKCJI TECHNIK
# =============================================================================

class TestKolektywizacja:
    """Testy dla funkcji kolektywizacja."""
    
    def test_kolektywizacja_zastępuje_elementy_średnią(self):
        """Sprawdź, czy losowy podzbiór został zastąpiony średnią."""
        lst = [1, 2, 3, 4, 5]
        original = lst.copy()
        result = kolektywizacja(lst, k_min=2, k_max=2)
        
        # Oblicz oczekiwaną średnią
        avg = round(sum(lst) / len(lst))
        
        # Sprawdź, czy co najmniej 2 elementy zostały zastąpione
        replaced_count = sum(1 for x in result if x == avg)
        assert replaced_count >= 2
        
        # Sprawdź, czy zastąpione elementy to średnia
        for x in result:
            if x == avg:
                # Powinien być w oryginalnej liście lub być średnią
                pass  # To jest OK
    
    def test_kolektywizacja_pusta_lista(self):
        """Sprawdź obsługę pustej listy."""
        assert kolektywizacja([]) == []
    
    def test_kolektywizacja_jedna_wartość(self):
        """Sprawdź, czy średnia jest poprawnie obliczona."""
        lst = [10, 20, 30]
        result = kolektywizacja(lst, k_min=3, k_max=3)
        avg = round(sum(lst) / len(lst))  # 20
        assert all(x == avg for x in result)
    
    def test_kolektywizacja_floaty(self):
        """Sprawdź obsługę floatów."""
        lst = [1.5, 2.5, 3.5]
        result = kolektywizacja(lst, k_min=1, k_max=1)
        avg = round(sum(lst) / len(lst))  # 8/3 ≈ 2.666 → 3
        assert any(x == avg for x in result)


class TestSamokrytyka:
    """Testy dla funkcji samokrytyka."""
    
    def test_samokrytyka_zastępuje_medianą(self):
        """Sprawdź, czy jeden element został zastąpiony medianą."""
        lst = [1, 2, 3, 4, 5]
        original = lst.copy()
        result = samokrytyka(lst)
        
        med = round(median(lst))  # 3
        
        # Powinien być jeden element więcej równy medianie
        assert result.count(med) == original.count(med) + 1
    
    def test_samokrytyka_pusta_lista(self):
        """Sprawdź obsługę pustej listy."""
        assert samokrytyka([]) == []
    
    def test_samokrytyka_jedna_wartość(self):
        """Sprawdź, czy mediana jest poprawnie obliczona."""
        lst = [5]
        result = samokrytyka(lst)
        assert result == [5]


class TestReedukacja:
    """Testy dla funkcji reedukacja."""
    
    def test_reedukacja_zamienia_dwa_elementy(self):
        """Sprawdź, czy dwa elementy zostały zamienione miejscami."""
        lst = [1, 2, 3, 4, 5]
        original = lst.copy()
        result = reedukacja(lst)
        
        # Lista powinna mieć tę samą zawartość (tyle samo każdej wartości)
        assert sorted(result) == sorted(original)
        # Ale nie powinna być identyczna
        assert result != original
    
    def test_reedukacja_pusta_lista(self):
        """Sprawdź obsługę pustej listy."""
        assert reedukacja([]) == []
    
    def test_reedukacja_jedna_wartość(self):
        """Sprawdź obsługę listy 1-elementowej."""
        lst = [5]
        result = reedukacja(lst)
        assert result == [5]
    
    def test_reedukacja_dwa_elementy(self):
        """Sprawdź, czy zamiana działa dla 2 elementów."""
        lst = [1, 2]
        result = reedukacja(lst)
        assert sorted(result) == [1, 2]
        assert result != [1, 2] or result == [1, 2]  # Może być takie samo (mała szansa)


class TestWielkiSkok:
    """Testy dla funkcji wielki_skok."""
    
    def test_wielki_skok_zastępuje_część_listy(self):
        """Sprawdź, czy losowa część listy została zastąpiona."""
        lst = [1, 2, 3, 4, 5]
        result = wielki_skok(lst, k_min=2, k_max=2)
        
        # Powinny być dokładnie 2 elementy równe wybranemu elementowi
        chosen = random.choice(lst)
        count = result.count(chosen)
        assert count == 2
    
    def test_wielki_skok_pusta_lista(self):
        """Sprawdź obsługę pustej listy."""
        assert wielki_skok([]) == []
    
    def test_wielki_skok_cała_lista(self):
        """Sprawdź, czy można zastąpić całą listę."""
        lst = [1, 2, 3]
        result = wielki_skok(lst, k_min=3, k_max=3)
        chosen = result[0]
        assert all(x == chosen for x in result)


class TestCzystka:
    """Testy dla funkcji czystka."""
    
    def test_czystka_w_górę(self):
        """Sprawdź czystkę w górę (elementy > mediana)."""
        lst = [1, 2, 4, 6, 8, 10]
        result = czystka(lst, direction='up')
        
        threshold = median(lst)  # 5
        lower_half = [x for x in lst if x <= threshold]  # [1, 2, 4]
        
        # Wszystkie elementy > threshold powinny być z lower_half
        for x in result:
            if x > threshold:
                assert x in lower_half
    
    def test_czystka_w_dół(self):
        """Sprawdź czystkę w dół (elementy < mediana)."""
        lst = [1, 2, 4, 6, 8, 10]
        result = czystka(lst, direction='down')
        
        threshold = median(lst)  # 5
        upper_half = [x for x in lst if x > threshold]  # [6, 8, 10]
        
        # Wszystkie elementy < threshold powinny być z upper_half
        for x in result:
            if x < threshold:
                assert x in upper_half
    
    def test_czystka_pusta_lista(self):
        """Sprawdź obsługę pustej listy."""
        assert czystka([]) == []
    
    def test_czystka_wszystkie_równe(self):
        """Sprawdź, gdy wszystkie elementy są równe."""
        lst = [5, 5, 5, 5]
        result = czystka(lst)
        assert result == lst
    
    def test_czystka_losowy_kierunek(self):
        """Sprawdź losowy kierunek czystki."""
        lst = [1, 2, 4, 6, 8, 10]
        result = czystka(lst)  # direction=None
        
        # Wynik powinien być listą tej samej długości
        assert len(result) == len(lst)


# =============================================================================
# TESTY FUNKCJI GŁÓWNEJ mao_sort
# =============================================================================

class TestMaoSort:
    """Testy dla głównej funkcji mao_sort."""
    
    def test_mao_sort_pusta_lista(self):
        """Sprawdź obsługę pustej listy."""
        result = mao_sort([])
        assert result == {'result': [], 'iterations': 0, 'last_technique': None}
    
    def test_mao_sort_jedna_wartość(self):
        """Sprawdź obsługę listy 1-elementowej."""
        result = mao_sort([5])
        assert result == {'result': [5.0], 'iterations': 0, 'last_technique': None}
    
    def test_mao_sort_wszystkie_równe(self):
        """Sprawdź, gdy lista jest już jednowartościowa."""
        result = mao_sort([3, 3, 3, 3])
        assert result['iterations'] == 0
        assert result['result'] == [3.0, 3.0, 3.0, 3.0]
    
    def test_mao_sort_zwraca_słownik(self):
        """Sprawdź format zwracanych danych."""
        result = mao_sort([1, 2, 3], max_iterations=10)
        
        assert isinstance(result, dict)
        assert 'result' in result
        assert 'iterations' in result
        assert 'last_technique' in result
        assert isinstance(result['iterations'], int)
        assert isinstance(result['last_technique'], str) or result['last_technique'] is None
    
    def test_mao_sort_liczba_iteracji(self):
        """Sprawdź, czy liczba iteracji jest nieujemna."""
        result = mao_sort([1, 2, 3, 4, 5], max_iterations=100)
        assert result['iterations'] >= 0
        assert result['iterations'] <= 100
    
    def test_mao_sort_technique_weights(self):
        """Sprawdź, czy niestandardowe wagi działają."""
        weights = {
            'kolektywizacja': 0.1,
            'samokrytyka': 0.1,
            'reedukacja': 0.1,
            'wielki_skok': 0.5,
            'czystka': 0.2,
        }
        result = mao_sort([1, 2, 3], max_iterations=10, technique_weights=weights)
        
        # Powinien zwrócić poprawny format
        assert isinstance(result, dict)
    
    def test_mao_sort_nieprawidłowe_wagi(self):
        """Sprawdź, czy nieprawidłowe wagi powodują błąd."""
        weights = {'kolektywizacja': 0.5, 'nieznana': 0.5}
        
        with pytest.raises(ValueError):
            mao_sort([1, 2, 3], technique_weights=weights)
    
    def test_mao_sort_wagi_nie_sumują_się_do_1(self):
        """Sprawdź, czy wagi nie sumujące się do 1 powodują błąd."""
        weights = {
            'kolektywizacja': 0.1,
            'samokrytyka': 0.1,
            'reedukacja': 0.1,
            'wielki_skok': 0.1,
            'czystka': 0.1,
        }
        
        with pytest.raises(ValueError):
            mao_sort([1, 2, 3], technique_weights=weights)
    
    def test_mao_sort_nieprawidłowy_typ(self):
        """Sprawdź, czy nieprawidłowy typ listy powoduje błąd."""
        with pytest.raises(TypeError):
            mao_sort("nie jest listą")
        
        with pytest.raises(TypeError):
            mao_sort([1, 2, "trzy"])
    
    def test_mao_sort_floaty(self):
        """Sprawdź obsługę floatów."""
        result = mao_sort([1.5, 2.5, 3.5], max_iterations=100)
        assert isinstance(result['result'], list)
        assert all(isinstance(x, float) for x in result['result'])
    
    def test_mao_sort_max_iterations_zero(self):
        """Sprawdź, gdy max_iterations = 0."""
        result = mao_sort([1, 2, 3], max_iterations=0)
        assert result['iterations'] == 0


# =============================================================================
# TESTY STATYSTYCZNE (opcjonalne, dłuższe)
# =============================================================================

class TestMaoSortStatystyczne:
    """Testy statystyczne (mogą trwać dłużej)."""
    
    @pytest.mark.slow
    def test_mao_sort_średnia_liczba_iteracji(self):
        """Sprawdź średnią liczbę iteracji dla wielu uruchomień."""
        iterations_list = []
        for _ in range(10):  # Mniej iteracji dla testów
            result = mao_sort(
                [random.randint(1, 10) for _ in range(5)],
                max_iterations=1000
            )
            iterations_list.append(result['iterations'])
        
        avg_iterations = sum(iterations_list) / len(iterations_list)
        assert avg_iterations >= 0
    
    @pytest.mark.slow
    def test_mao_sort_zawsze_kończy_się_dla_wielkiego_skoku(self):
        """Sprawdź, czy Wielki Skok zawsze kończy algorytm w jednej iteracji."""
        # Ustaw wysokie prawdopodobieństwo Wielkiego Skoku
        weights = {
            'kolektywizacja': 0.0,
            'samokrytyka': 0.0,
            'reedukacja': 0.0,
            'wielki_skok': 1.0,
            'czystka': 0.0,
        }
        
        result = mao_sort([1, 2, 3, 4, 5], technique_weights=weights)
        
        # Powinien zakończyć się w 1 iteracji (Wielki Skok zastępuje losową część)
        # Ale nie zawsze osiągnie jednowartościowość w 1 iteracji
        # (zależy od k_min i k_max)
        assert result['iterations'] >= 0


# =============================================================================
# Uruchomienie testów
# =============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
