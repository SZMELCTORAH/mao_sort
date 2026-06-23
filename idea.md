# Mao Sort — specyfikacja filozoficzna

README
=======================================
MAO SORT to algorytm sortujący, którego cele jest osiągnięcie listy maksymalnie ujednoliconej, zgodnie z ideą "w komunizmie wszystkie zmienne są równe". Ostatecznym sukcesem jest lista mająca tyle samo elementów, ale jednowartościowa. Inaczej mówiąc -- cel: lista złożona z n kopii tej samej wartości (ideologiczna jedność). Kryterium sukcesu: wszystkie elementy równe. Metoda: w każdej iteracji algorytm losowo wybiera jedną z 5 technik rewolucyjnych, z których każda w różny sposób niszczy strukturę listy, dążąc chaotycznie do homogenizacji. 
MISJA:
"cel ideologicznie spójny (lista jednorodna, wszyscy równi) osiągany metodami losowo destrukcyjnymi albo nieskutecznymi. To jest właściwie bardzo wierna metafora Wielkiego Skoku i Rewolucji Kulturalnej — kierunek był „określony", metody były chaotyczne i katastrofalne, wynik był przewidywalny tylko w tym sensie, że zawsze był zły."
Zasadniczą idea jest podobna do polityki Mao: algorytm losowymi działaniami powoduje serię katastrof, za nic jednak nie chce osiągać zamierzonej równości -- ostateczny sukces nie wynika z iteracji ani z skuteczności samych technik. "MAO SORT W TEORII MA 5 METODAMI SZYBKO OSIAGAĆ RÓWNOŚĆm W PRAKTYCE JEDNAK DZIAŁANIA TAK SAMO PRZYBLIŻAJĄ JAK I ODDALAJĄ CEL" 
MAO SORT nie stosuje jednej deterministycznej (skryptowej) metody sortowania listy, zamiast tego stosuje 5 technik rewolucyjnych: 
  kolektywizację (zastąp losowy podzbiór elementów ich średnią, zaokrągloną), 
    np [1,2,4,6,8,10] -> kolektywizacja -> 4+6+8+10=28/4=7 -> [1,2,7,7,7,7]
  samokrytykę (losowy element zastępuje się medianą listy)
   np [1,2,4,6,8,10] -> samokrytyka -> mediana=5 -> [1,5,4,6,8,10]
  reedukację (zamień losowe n elementów miejscami — operacja neutralna ideologicznie, ale pochłaniająca zasoby)
    np [1,2,4,6,8,10] -> reedukacja -> [4,2,1,6,8,10]
  Wielki Skok (zastąp losową część listy kopiami losowo wybranego elementu — może jednym skokiem osiągnąć cel, może całkowicie zniszczyć postęp),
    np [1,2,4,6,8,10] -> wielki skok -> [1,1,1,1,8,10]
  oraz czystkę (zastąp (usuń) wszystkie elementy odstające w dół albo w górę, losowymi wartościami z zakresu przeciwnego: 
    czystka wszystkich elementów większych od średniej/mediany, czyli losowe zastąpienie ich wartościami z połowy niepoddanej czystce
    np [1,2,4,6,8,10] -> czystka w górę od średniej (>5) -> 6, 8 i 10 zostają zastąpione losowymi liczbami z zakresu [1,2,4] 

KOMENATRZ:
Algorytm może zakończyć się błyskawicznie przez Wielki Skok (jeden krok, przypadkowa homogenizacja) lub nigdy — jeśli czystka i reedukacja wzajemnie się neutralizują. Złożoność jest niedefiniowalna w klasycznym sensie, bo zależy od losowości. Można ją opisać tylko probabilistycznie, a rozkład prawdopodobieństwa zakończenia jest ciężkoogonowy — czasem koniec jest natychmiastowy, czasem nigdy nie następuje.
Warto dodać licznik iteracji i wizualizację historii technik — algorytm jako narracja historyczna.

KEJSY
=======================================
1. jak wprowadzić losowość stosowania metod sortowania? żeby każda iteracja losowała technikę, a w ramach techniki losowość np zmian czy elementów?
2. czy uda się utrzymać odpowiednią prostotę MAO SORT? 


WSTĘPNE KONCEPCJE KODU
=======================================

pythonimport random
from statistics import median, mode
from collections import Counter

def mao_sort(lst, max_iterations=10000):
    lst = lst.copy()
    history = []

    for iteration in range(max_iterations):
        if len(set(lst)) == 1:
            return lst, iteration, history

        technique = random.choice([
            'kolektywizacja',
            'samokrytyka',
            'reedukacja',
            'wielki_skok',
            'czystka'
        ])
        history.append(technique)

        if technique == 'kolektywizacja':
            avg = int(sum(lst) / len(lst))
            indices = random.sample(range(len(lst)),
                                    k=random.randint(1, len(lst)))
            for i in indices:
                lst[i] = avg

        elif technique == 'samokrytyka':
            med = int(median(lst))
            i = random.randint(0, len(lst) - 1)
            lst[i] = med

        elif technique == 'reedukacja':
            i, j = random.sample(range(len(lst)), 2)
            lst[i], lst[j] = lst[j], lst[i]

        elif technique == 'wielki_skok':
            chosen = random.choice(lst)
            lst = [chosen] * len(lst)

        elif technique == 'czystka':
            modal = Counter(lst).most_common(1)[0][0]
            lst = [x if x == modal
                   else random.randint(min(lst), max(lst))
                   for x in lst]

    return lst, max_iterations, history
