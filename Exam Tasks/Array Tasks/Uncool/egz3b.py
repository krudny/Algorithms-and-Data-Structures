from egz3btesty import runtests

#O(n^2), using interval trees we can get O(nlogn) time complexity

def is_uncool(i1, i2):
	s1, e1 = i1
	s2, e2 = i2
    
	return s1 < s2 < e1 < e2  or s2 < s1 < e2 < e1 


def uncool( P ):
	n = len(P)

	for i in range(n): 
		for j in range(i + 1, n): 
			if is_uncool(P[i], P[j]): return (i, j)
  

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( uncool, all_tests = True )
