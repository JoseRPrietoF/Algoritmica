def number_of_coins(Q, v, infinity=2**31):
    M = dict(((0, q), infinity) for q in range(1, Q + 1))
    M[0, 0] = 0
    for i in range(1, len(v) ):
        for q in range(Q + 1):
            a = [M[i - 1, q - x * v[i]] + x for x in range(0, q // v[i] +1) ]
            M[i, q] = min(a)
            # dibujar_matriz_M(M, q,i)
            # a = input('<')
    dibujar_matriz_M(M,Q,len(v))
    return M[len(v)-1, Q]

def number_of_coins_backpointers(Q, v, infinity=2**31):
    M = dict(((0, q), infinity) for q in range(1, Q + 1))
    B = dict(((0, q), infinity) for q in range(1, Q + 1))
    M[0, 0],B[0,0] = 0,None
    for i in range(1, len(v) ):
        for q in range(Q + 1):
            a = infinity
            for x in range(0, q // v[i] + 1):
                b = M[i - 1, q - x * v[i]] + x
                if(b < a):
                    a = b
                    M[i, q] = b
                    B[i,q] = (i - 1, q - x * v[i],x)

    dibujar_matriz_M(M,Q,len(v))
    dibujar_matriz_M(B,Q,len(v))
    change = []
    q = (len(v)-1, Q)
    while B[q] != None:
        tripla = B[q]

        change.append(tripla[2])
        q = (tripla[0],tripla[1])
    change.reverse()
    return M[len(v)-1, Q], change

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
    Q = 24
    v = [0,1, 2, 5, 10, 20, 50]
    res,change = number_of_coins_backpointers(Q,v)

    print(res)
    print(change)