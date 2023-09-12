# Algorytm tworzy tablice kosztow pobytu na danej planecie i posiadając b paliwa i wypelnia ja wartosciami nieskonczonymi poza polem 0,0 (bo koszt przebywania
# na planecie 0 z 0 paliwa wynosi 0). Kazdy wiersz jest wypelniany wartosciami minimalnymi kosztu przebywania na planecie i posiadajac b paliwa,
# obliczanymi nastepujaco:
# Wartoscia pola jest minimum z opcji tankowania na obecnej planecie (za obecny koszt paliwa), badz dotarcia z nadmiarem paliwa
# z poprzedniej planety (tylko jesli jest to mozliwe, tj. nie wymaga tankowania ponad E)
# Nastepnie sprawdzana jest mozliwosc teleportu, wiec pole wskazywane przez cel teleportu, jest nadpisywane wartoscia mniejsza z
# obecnie znajdującej sie na polu, badz wartosci pola i + koszt teleportu.
# Wynikiem jest koszt dotarcia do planety i z pustym bakiem, co jest najtansza opcja, znajdujacy sie w polu F[n-1][0].
# Algorytm ma zlozonosc obliczeniową O(nE), gdyz jednokrotnie przechodzi przez tablice F o wymiarach n na E.
from egz1btesty import runtests

from math import inf

def planets( D, C, T, E ):
    n = len(T)
    F = [[inf for i in range(E+1)] for i in range(n)]

    F[0][0] = 0

    for i in range(n):
        cost = C[i]
        distance = 0

        if i > 0: 
            distance = D[i] - D[i-1]
        
        if i > 0:
            F[i][0] = min(F[i][0], F[i-1][distance])

        for b in range(1, E+1):
            F[i][b] = min(F[i][b], F[i][b-1] + cost)

            if i>0 and b+distance <= E:
                F[i][b] = min(F[i][b], F[i-1][b+distance])

        t_dest, t_cost = T[i]
        F[t_dest][0] = min(F[t_dest][0], F[i][0] + t_cost)

    return F[n-1][0]
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = False )
