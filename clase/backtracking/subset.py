
def factible(w,W,x,i,sum_w):
    return W - x[i]*w[i] >=0 and sum_w[i+1] >= W-x[i]*w[i]

def completo(W):
    return W==0

def subset_sum(w,W):
    w.sort()
    x = [0]*len(w)
    sum_w = [0]*len(w)
    sum_w[len(w)-1] = w[len(w)-1]
    for i in range(len(w)-2,-1,-1):
        sum_w[i] = sum_w[i+1] + w[i]
    print(sum_w)
    def backtracking(i,W):
        if completo(W):
            for j in range(i,len(w)):
                x[j] = 0
            return x
        elif i <= len(w):
            for x[i] in 1,0:
                if factible(w,W,x,i,sum_w):
                    found = backtracking(i+1,W-x[i]*w[i])
                    if found is not None: return found
                else:
                    return None

    return backtracking(0, W)






"""E = euros
C = calorias
p = precio por producto
c = calorias por producto"""
def calorias(p,c,E,C):
    n = len(p) #numero de productos
    sol = [None]*n
    sum_p = [sum(p[i:]) for i in range(1,len(p))]
    sum_c = [sum(c[i:]) for i in range(1,len(c))]
    sum_c.append(0)
    sum_p.append(0)

    def backtracking(longSol, E,C):
        if longSol == n: #es completo
            return True

        #metemos objeto
        #si cabe (factible) y es prometedor
        if p[longSol] <= E and sum_p[longSol]+p[longSol] >= E \
            and c[longSol] <= C and sum_c[longSol]+c[longSol] >= C:
            sol[longSol] = 1
            if backtracking(longSol+1, E-p[longSol], C-c[longSol]):
                return True

        #no metemos objeto
        if sum_p[longSol] >= E and sum_c[longSol] >= C:
            sol[longSol] = 0
            if backtracking(longSol + 1, E , C):
                return True

        return False

    backtracking(0,E,C)
    return sol



if __name__ == "__main__":
    # W, w = 8, [4, 5, 3, 6]
    # res = subset_sum(w,W)
    # print("El resultado es, con {0}, la combinacion {1}".format(sorted(w),res))
    p = [5, 3, 4, 2, 1]
    c = [200, 110, 100, 80, 50]
    E = 10
    C = 350
    print(calorias(p,c,E,C))
