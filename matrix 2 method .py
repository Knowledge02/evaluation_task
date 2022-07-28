#funcion calling method
#2


def rev_matrix(n,m):
	k=0
	arr = [[0 for i in range(m)] for j in range(n)]
	vals = list(range(n*m))
	for i in range(1-m,n):
		for c in range(m):
			for r in range(n):
				if c-r==i:
					arr[r][c]=vals[k]+1
					k+=1

	return arr[::-1]


