

def ejercicio2(lista):
    longs = [1]
    for i in range(1,len(lista)):
        n = lista[i]; aux = 1
        for j in range(i):
            if(lista[j] < n and longs[j] >= aux):
                aux = longs[j]+1
        longs.append(aux)
    return longs

def ejercicio3(lista):
    res = ejercicio2(lista)
    return max(res), res

def ejercicio4(lista):
    m,longs = ejercicio3(lista)
    # print(lista)
    # print(longs)
    res = []
    target = m
    target_num = -1
    first = True
    # print()
    for e in  list(reversed(range(len(longs)))):
        n = longs[e]
        num = lista[e]
        if n == target:
            # print("---- %d n %d " % (target,n))
            if first:
                res.append(num)
                target_num = num
                target = target -1
                first = False
            elif(num < target_num):
                res.insert(0,num)
                target_num = num
                target = target - 1

        # print(n)

        # if (e)
    return res

if (__name__ == '__main__'):

    cad = [10, 3, 5, 12, 7, 20, 18, 5]
    cad2 = [210, 816, 357, 107, 889, 635, 733, 930, 842, 542]

    m,longs = ejercicio3(cad)
    # print(longs)
    # print(m)
    # m,longs = ejercicio3(cad2)
    # print(longs)
    # print(m)

    res = ejercicio4(cad)
    print()
    print(res)

    res = ejercicio4(cad2)
    print()
    print(res)