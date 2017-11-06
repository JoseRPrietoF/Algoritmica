def tramos(K,L,C):
    F, inf = [0], 2**31
    for k in range(1,K+1):
        F.append(min((F[k-li]+ci for li,ci in zip(L,C) if li<=k),default=inf))
    return F[K], F

def tramos2(K,L,C,S):
    # K es un entero
    # L, C, S son listas de longitud N
    N, inf = len(L), 2**31
    M = { (t, 0): 0 for t in range(N)}
    for k in range(1, K+1):
        M[0, k] = inf

    for t in range(1,N): # tipo de tramo
        for k in range(1,K+1): # distancia
            M[t, k] = min((M[t - 1, k - x * L[t]] + x * C[t] for x in range(min(S[t], k // L[t])+1) ) )
    dibujar_matriz_M(M,N,K)
    return M[N-1,K]

def dibujar_matriz_M(M,Q,v):
    for i in range(0,Q+1):
        print(i, end='\t')
    print('\n')
    for i in range(1,v):
        for q in range(Q+1):
            print(M[i,q],end='\t', flush=True)
        print()
    print("FIN")

if __name__ == "__main__":
    K = 20
    L = [5,9,18,30,50]
    C = [1,2,5,8,10]
    S = [10,10,10,10,10]
    # res, F = tramos(K, L, C)
    #
    # print(res)
    # print(F)
    # print(len(F))

    res = tramos2(K, L, C,S)

    print(res)
