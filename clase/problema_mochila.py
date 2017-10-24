
def mochila(W,v,w):
    V = {}
    for c in range(W+1):
        V[0,c] = 0

    for i in range(len(v)+1):
        V[i,0] = 0

    for i in range(1,len(v)): #items, el 0 es el caso base

        for c in range(1,W+1):
            if(w[i] > c):
                V[i,c] = V[i-1,c]
            else: # w[i] >= c (cabe el item)
                if v[i] + V[i-1,c-w[i]] > V[i-1,c]: # si beneficia mas que el anterior
                    #es decir, si le restamos lo que pesa (para el sobrante) y le sumamos lo que nos da, da mayor beneficio
                    V[i,c] = max(V[i-1,c], V[i-1,c-w[i]] + v[i])
                else: #cabe pero no beneficia
                    V[i, c] = V[i - 1, c]

    return V[W-1,len(v)],V

def mochila_desplegada(W,v,w):
    V = {}
    for c in range(W+1):
        V[0,c] = 0
    for i in range(len(v)+1):
        V[i,0] = 0

    for i in range(1,len(v)): #items, el 0 es el caso base

        for c in range(1,w[i]):
            V[i,c] = V[i-1,c]
        for c in range(w[i],W+1):
            V[i, c] = max(V[i - 1, c], V[i - 1, c - w[i]] + v[i])

    return V[W-1,len(v)],V

"""Corregido"""
def mochila_desplegada_con_camino(W,v,w):
    V = {}; B={}
    for c in range(W+1):
        V[0,c], B[0,c] = 0, None
    for i in range(len(v)+1):
        V[i,0], B[i,0] = 0, (i-1,0)
    B[0,0] = None
    for i in range(1,len(v)): #items, el 0 es el caso base

        for c in range(1,w[i]):
            V[i,c], B[i,c] = V[i-1,c], (i-1,c)
        for c in range(w[i],W+1):
            # se desgrana la linea V[i, c] = max(V[i - 1, c], V[i - 1, c - w[i]] + v[i])
            if (V[i - 1, c] >= V[i - 1, c - w[i]] + v[i]):
                V[i, c], B[i, c] = V[i - 1, c], (i-1, c)
            else:
                V[i, c], B[i, c] = V[i - 1, c - w[i]] + v[i], (i-1, c-w[i])

    dibujar_matriz_V_mochila(B)
    dibujar_matriz_V_mochila(V)
    path = []
    (i,c) = (len(v)-1,W)
    while(B[i,c] != None):
        # print(B[i,c])
        if B[i, c] != (i - 1, c): path.append(1)
        else: path.append(0)
        (i, c) = B[i, c]

    path.reverse()

    return V[W-1,len(v)],V,path

def dibujar_matriz_V_mochila(V):
    for i in range(len(v)):
        for c in range(W+1):
            print(V[i,c],end='\t', flush=True)
        print()
    print("FIN")

if __name__ == "__main__":
    # v = [0,3,4,5,6]
    v = [0,90, 75, 60, 20, 10]
    # w = [0,2,3,4,5]
    w = [0,4, 3, 3, 2, 2]
    # W = 5
    W = 6
    # m,V = mochila(W,v,w)
    # m,V = mochila_desplegada(W,v,w)
    print("V ", v)
    print("w ", w)
    print("W ", W)
    m,V,path = mochila_desplegada_con_camino(W,v,w)

    print(m)

    print(path)