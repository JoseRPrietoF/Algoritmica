class NQueensSolver1:

    def __init__(self,n):
        self.n = n

    def is_complete(self , s):
        return len(s) == self .n

    def is_promising(self , s, row):
        return all(row != s[i] and len(s) - i != abs(row - s[i]) for i in range(len(s)))

    """Todas las soluciones"""
    def backtracking(self, s):
        if self. is_complete(s): yield s
        for row in range(self.n):
            s0 = s + [row]

            if self.is_promising(s, row):
                for s2 in self.backtracking(s0):
                    yield s2

        return None

    def solve(self):
        return self.backtracking([])

if __name__ == "__main__":
    for n in range(1,10):
        print("Solucion con %d reinas: %s." % (n, [x for x in NQueensSolver1(n).solve()]))
