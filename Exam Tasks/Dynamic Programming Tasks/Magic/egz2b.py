from egz2btesty import runtests

def magic(C):
    n = len(C)
    DP = [-1] * n
    DP[0] = 0

    for i in range(n): 
        if DP[i] == -1: continue

        chest_gold = C[i][0]

        for j in range(1,4): 
            chamber = C[i][j][1]
            gold_required = C[i][j][0]

            if chamber == -1: continue

            if gold_required > chest_gold: 
                if DP[i] >= gold_required - chest_gold:
                    DP[chamber] = max(DP[chamber], DP[i] - gold_required + chest_gold)

            if gold_required < chest_gold: 
                if chest_gold - gold_required <= 10: 
                    DP[chamber] = max(DP[chamber], DP[i] - gold_required + chest_gold)

            if gold_required == chest_gold: 
                DP[chamber] = max(DP[chamber], DP[i])


    return DP[-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True)
