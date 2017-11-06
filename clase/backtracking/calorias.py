
def calorias(p,c,E,C):
    n = len(p)  # numero de productos
    sol = [None] * n
    sum_p = [sum(p[j] for j in range(i + 1, n)) for i in range(n)]  # ineficiente
    sum_c = [sum(c[j] for j in range(i + 1, n)) for i in range(n)]  # ineficiente
    print(sum_p)
    print(sum_c)
    def backtracking(longSol, E, C):
        if longSol == n:  # es completa
            return True  # en este caso, no hace falta comprobar factible

        # no completa, ramificar
        # 1) consideramos primero que se compra este objeto:
        if (E >= p[longSol] and p[longSol] + sum_p[longSol] >= E and
                    C >= c[longSol] and c[longSol] + sum_c[longSol] >= C):  # prometedor
            sol[longSol] = 1
            if backtracking(longSol + 1, E - p[longSol], C - c[longSol]):
                return True
        # 2) ahora consideramos que no se compra:
        if sum_p[longSol] >= E and sum_c[longSol] >= C:  # prometedor
            sol[longSol] = 0
            if backtracking(longSol + 1, E, C):
                return True
        return False
    if backtracking(0, E, C):
        return sol
    else:
        return None

if __name__ == "__main__":
    p = [5, 3, 4, 2, 1]
    c = [200, 110, 100, 80, 50]
    E = 10
    C = 350

    res = calorias(p,c,E,C)
    print(res)