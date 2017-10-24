def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

def remove_seams(height,seam_paths, matrix):
    """anyadimos la tupla que vayamos a borrar a un set
        y luego cuando borremos los siguientes vigilamos si esa tupla ya ha sido 
    """
    print("preremove seam %d %d " % (len(matrix), len(matrix[0])))
    usados = dict()
    paths_validos = []
    i = 0
    for path in seam_paths:

        # a = input("path > ")
        #comprobamos primero que el camino es valido!
        path_valido = True
        aux = dict()
        for (pos,num) in enumerate(path):
            tupla = (pos, num)
            usado = usados.get(tupla, False)
            if usado:
                path_valido = False
                break;
            # usados[tupla] = True
            aux[tupla] = True
        if path_valido:  #si encontramos un camino que choca con otro, pasamos al siguiente
            print(i)
            i = i + 1
            # for y in range(height):
            #     matrix[y].pop(path[y])
            paths_validos.append(path)
            usados = merge_two_dicts(usados, aux)

    new_paths = []
    for p in range(height):
        new_paths.append([])

    # giramos
    for path in paths_validos:
        for pos, p in enumerate(path):
            new_paths[pos].append(p)
    print("Len %d " % len(paths_validos))


    # for i in range(height):
    #     path_row = new_paths[i]
    #     path_row.sort()
    #     for j in reversed(path_row):
    #         matrix[i].pop(j)
    #         print(j)


    return paths_validos, new_paths

array = [
    [1,1,2,1,2],
    [3,3,3,2,3],
    [1,2,3,2,1]
]
array = [[252, 253, 254, 255, 256, 257, 256, 255, 256, 257, 256, 255, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 265, 265, 265, 264, 263, 264, 263, 262, 261, 260, 259, 258, 258, 257, 256, 255, 254, 253, 253, 254, 255, 256, 256, 255, 255, 256, 257, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 263, 262, 261, 260, 259, 259, 259, 258, 257, 256, 255, 254, 255, 256, 255, 254, 254, 253, 252, 251, 252, 251, 250, 249, 250, 251, 252, 253, 254, 255, 254, 253, 254, 255, 256, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 263, 262, 261, 260, 260, 261, 262, 261, 260, 259, 259, 258, 257, 256, 255, 254, 253, 252, 251, 250, 249, 248, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 261, 260, 260, 260, 261, 262, 263, 264, 265, 266, 267, 268, 268, 267, 267, 268, 268, 267, 266, 266, 266, 265, 266, 267, 268, 267, 268, 267, 267, 268, 267, 268, 269, 268, 268], [252, 253, 254, 255, 256, 257, 256, 255, 256, 257, 256, 255, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 265, 265, 265, 264, 263, 264, 263, 262, 261, 260, 259, 258, 258, 257, 256, 255, 254, 253, 253, 254, 255, 256, 256, 255, 255, 256, 257, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 263, 262, 261, 260, 259, 259, 259, 258, 257, 256, 255, 254, 255, 256, 255, 254, 254, 253, 252, 251, 252, 251, 250, 249, 250, 251, 252, 253, 254, 255, 254, 253, 254, 255, 256, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 263, 262, 261, 260, 260, 261, 262, 261, 260, 259, 259, 258, 257, 256, 255, 254, 253, 252, 251, 250, 249, 248, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 261, 260, 260, 260, 261, 262, 263, 264, 265, 266, 267, 268, 268, 267, 267, 268, 268, 267, 266, 266, 266, 265, 266, 267, 268, 267, 268, 267, 267, 268, 267, 268, 269, 268, 267], [252, 253, 254, 255, 256, 257, 256, 255, 256, 257, 256, 255, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 265, 265, 265, 264, 263, 264, 263, 262, 261, 260, 259, 258, 258, 257, 256, 255, 254, 253, 253, 254, 255, 256, 256, 255, 255, 256, 257, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 263, 262, 261, 260, 259, 259, 259, 258, 257, 256, 255, 254, 255, 256, 255, 254, 254, 253, 252, 251, 252, 251, 250, 249, 250, 251, 252, 253, 254, 255, 254, 253, 254, 255, 256, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 263, 262, 261, 260, 260, 261, 262, 261, 260, 259, 259, 258, 257, 256, 255, 254, 253, 252, 251, 250, 249, 248, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 261, 260, 260, 260, 261, 262, 263, 264, 265, 266, 267, 268, 268, 267, 267, 268, 268, 267, 266, 266, 266, 265, 266, 267, 268, 267, 268, 267, 267, 268, 267, 268, 269, 268, 269], [252, 253, 254, 255, 256, 257, 256, 255, 256, 257, 256, 255, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 265, 265, 265, 264, 263, 264, 263, 262, 261, 260, 259, 258, 258, 257, 256, 255, 254, 253, 253, 254, 255, 256, 256, 255, 255, 256, 257, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 263, 262, 261, 260, 259, 259, 259, 258, 257, 256, 255, 254, 255, 256, 255, 254, 254, 253, 252, 251, 252, 251, 250, 249, 250, 251, 252, 253, 254, 255, 254, 253, 254, 255, 256, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 263, 262, 261, 260, 260, 261, 262, 261, 260, 259, 259, 258, 257, 256, 255, 254, 253, 252, 251, 250, 249, 248, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 261, 260, 260, 260, 261, 262, 263, 264, 265, 266, 267, 268, 268, 267, 267, 268, 268, 267, 266, 266, 266, 265, 266, 267, 268, 267, 268, 267, 267, 268, 267, 267, 268, 267, 266], [252, 253, 254, 255, 256, 257, 256, 255, 256, 257, 256, 255, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 265, 265, 265, 264, 263, 264, 263, 262, 261, 260, 259, 258, 258, 257, 256, 255, 254, 253, 253, 254, 255, 256, 256, 255, 255, 256, 257, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 263, 262, 261, 260, 259, 259, 259, 258, 257, 256, 255, 254, 255, 256, 255, 254, 254, 253, 252, 251, 252, 251, 250, 249, 250, 251, 252, 253, 254, 255, 254, 253, 254, 255, 256, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 263, 262, 261, 260, 260, 261, 262, 261, 260, 259, 259, 258, 257, 256, 255, 254, 253, 252, 251, 250, 249, 248, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 261, 260, 260, 260, 261, 262, 263, 264, 265, 266, 267, 268, 268, 267, 267, 268, 268, 267, 266, 266, 266, 265, 266, 267, 268, 267, 268, 267, 267, 268, 267, 268, 269, 269, 270], [252, 253, 254, 255, 256, 257, 256, 255, 256, 257, 256, 255, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 265, 265, 265, 264, 263, 264, 263, 262, 261, 260, 259, 258, 258, 257, 256, 255, 254, 253, 253, 254, 255, 256, 256, 255, 255, 256, 257, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 263, 262, 261, 260, 259, 259, 259, 258, 257, 256, 255, 254, 255, 256, 255, 254, 254, 253, 252, 251, 252, 251, 250, 249, 250, 251, 252, 253, 254, 255, 254, 253, 254, 255, 256, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 263, 262, 261, 260, 260, 261, 262, 261, 260, 259, 259, 258, 257, 256, 255, 254, 253, 252, 251, 250, 249, 248, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 261, 260, 260, 260, 261, 262, 263, 264, 265, 266, 267, 268, 268, 267, 267, 268, 268, 267, 266, 266, 266, 265, 266, 267, 268, 267, 268, 267, 267, 268, 267, 266, 265, 264, 264], [252, 253, 254, 255, 256, 257, 256, 255, 256, 257, 256, 255, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 265, 265, 265, 264, 263, 264, 263, 262, 261, 260, 259, 258, 258, 257, 256, 255, 254, 253, 253, 254, 255, 256, 256, 255, 255, 256, 257, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 263, 262, 261, 260, 259, 259, 259, 258, 257, 256, 255, 254, 255, 256, 255, 254, 254, 253, 252, 251, 252, 251, 250, 249, 250, 251, 252, 253, 254, 255, 254, 253, 254, 255, 256, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 263, 262, 261, 260, 260, 261, 262, 261, 260, 259, 259, 258, 257, 256, 255, 254, 253, 252, 251, 250, 249, 248, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 261, 260, 260, 260, 261, 262, 263, 264, 265, 266, 267, 268, 268, 267, 267, 268, 268, 267, 266, 266, 266, 265, 266, 267, 268, 267, 268, 267, 267, 268, 267, 266, 267, 266, 265], [252, 253, 254, 255, 256, 257, 256, 255, 256, 257, 256, 255, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 265, 265, 265, 264, 263, 264, 263, 262, 261, 260, 259, 258, 258, 257, 256, 255, 254, 253, 253, 254, 255, 256, 256, 255, 255, 256, 257, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 263, 262, 261, 260, 259, 259, 259, 258, 257, 256, 255, 254, 255, 256, 255, 254, 254, 253, 252, 251, 252, 251, 250, 249, 250, 251, 252, 253, 254, 255, 254, 253, 254, 255, 256, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 263, 262, 261, 260, 260, 261, 262, 261, 260, 259, 259, 258, 257, 256, 255, 254, 253, 252, 251, 250, 249, 248, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 261, 260, 260, 260, 261, 262, 263, 264, 265, 266, 267, 268, 268, 267, 267, 268, 268, 267, 266, 266, 266, 265, 266, 267, 268, 267, 268, 267, 267, 268, 267, 268, 269, 270, 271], [252, 253, 254, 255, 256, 257, 256, 255, 256, 257, 256, 255, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 265, 265, 265, 264, 263, 264, 263, 262, 261, 260, 259, 258, 258, 257, 256, 255, 254, 253, 253, 254, 255, 256, 256, 255, 255, 256, 257, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 263, 262, 261, 260, 259, 259, 259, 258, 257, 256, 255, 254, 255, 256, 255, 254, 254, 253, 252, 251, 252, 251, 250, 249, 250, 251, 252, 253, 254, 255, 254, 253, 254, 255, 256, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 263, 262, 261, 260, 260, 261, 262, 261, 260, 259, 259, 258, 257, 256, 255, 254, 253, 252, 251, 250, 249, 248, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 261, 260, 260, 260, 261, 262, 263, 264, 265, 266, 267, 268, 268, 267, 267, 268, 268, 267, 266, 266, 266, 265, 266, 267, 268, 267, 268, 267, 267, 268, 267, 266, 265, 264, 263], [252, 253, 254, 255, 256, 257, 256, 255, 256, 257, 256, 255, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 265, 265, 265, 264, 263, 264, 263, 262, 261, 260, 259, 258, 258, 257, 256, 255, 254, 253, 253, 254, 255, 256, 256, 255, 255, 256, 257, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 263, 262, 261, 260, 259, 259, 259, 258, 257, 256, 255, 254, 255, 256, 255, 254, 254, 253, 252, 251, 252, 251, 250, 249, 250, 251, 252, 253, 254, 255, 254, 253, 254, 255, 256, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 263, 262, 261, 260, 260, 261, 262, 261, 260, 259, 259, 258, 257, 256, 255, 254, 253, 252, 251, 250, 249, 248, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 261, 260, 260, 260, 261, 262, 263, 264, 265, 266, 267, 268, 268, 267, 267, 268, 268, 267, 266, 266, 266, 265, 266, 267, 268, 267, 268, 267, 268, 269, 269, 270, 271, 272, 272], [252, 253, 254, 255, 256, 257, 256, 255, 256, 257, 256, 255, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 265, 265, 265, 264, 263, 264, 263, 262, 261, 260, 259, 258, 258, 257, 256, 255, 254, 253, 253, 254, 255, 256, 256, 255, 255, 256, 257, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 263, 262, 261, 260, 259, 259, 259, 258, 257, 256, 255, 254, 255, 256, 255, 254, 254, 253, 252, 251, 252, 251, 250, 249, 250, 251, 252, 253, 254, 255, 254, 253, 254, 255, 256, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 263, 262, 261, 260, 260, 261, 262, 261, 260, 259, 259, 258, 257, 256, 255, 254, 253, 252, 251, 250, 249, 248, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 261, 260, 260, 260, 261, 262, 263, 264, 265, 266, 267, 268, 268, 267, 267, 268, 267, 266, 265, 264, 263, 262, 261, 260, 259, 259, 260, 261, 260, 259, 258, 257, 256, 256, 256], [252, 253, 254, 255, 256, 257, 256, 255, 256, 257, 256, 255, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 265, 265, 265, 264, 263, 264, 263, 262, 261, 260, 259, 258, 258, 257, 256, 255, 254, 253, 253, 254, 255, 256, 256, 255, 255, 256, 257, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 263, 262, 261, 260, 259, 259, 259, 258, 257, 256, 255, 254, 255, 256, 255, 254, 254, 253, 252, 251, 252, 251, 250, 249, 250, 251, 252, 253, 254, 255, 254, 253, 254, 255, 256, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 263, 262, 261, 260, 260, 261, 262, 261, 260, 259, 259, 258, 257, 256, 255, 254, 253, 252, 251, 250, 249, 248, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 261, 260, 260, 260, 261, 262, 263, 264, 265, 266, 267, 268, 268, 267, 267, 268, 267, 266, 265, 264, 263, 262, 261, 260, 259, 259, 260, 261, 260, 259, 258, 257, 256, 256, 257], [252, 253, 254, 255, 256, 257, 256, 255, 256, 257, 256, 255, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 265, 265, 265, 264, 263, 264, 263, 262, 261, 260, 259, 258, 258, 257, 256, 255, 254, 253, 253, 254, 255, 256, 256, 255, 255, 256, 257, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 263, 262, 261, 260, 259, 259, 259, 258, 257, 256, 255, 254, 255, 256, 255, 254, 254, 253, 252, 251, 252, 251, 250, 249, 250, 251, 252, 253, 254, 255, 254, 253, 254, 255, 256, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 263, 262, 261, 260, 260, 261, 262, 261, 260, 259, 259, 258, 257, 256, 255, 254, 253, 252, 251, 250, 249, 248, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 261, 260, 260, 260, 261, 262, 263, 264, 265, 266, 267, 268, 268, 267, 267, 268, 268, 267, 266, 266, 266, 265, 266, 267, 268, 267, 268, 267, 267, 267, 266, 265, 264, 263, 262], [252, 253, 254, 255, 256, 257, 256, 255, 256, 257, 256, 255, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 265, 265, 265, 264, 263, 264, 263, 262, 261, 260, 259, 258, 258, 257, 256, 255, 254, 253, 253, 254, 255, 256, 256, 255, 255, 256, 257, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 263, 262, 261, 260, 259, 259, 259, 258, 257, 256, 255, 254, 255, 256, 255, 254, 254, 253, 252, 251, 252, 251, 250, 249, 250, 251, 252, 253, 254, 255, 254, 253, 254, 255, 256, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 263, 262, 261, 260, 260, 261, 262, 261, 260, 259, 259, 258, 257, 256, 255, 254, 253, 252, 251, 250, 249, 248, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 261, 260, 260, 260, 261, 262, 263, 264, 265, 266, 267, 268, 268, 267, 267, 268, 267, 266, 265, 264, 263, 262, 261, 260, 259, 259, 260, 261, 260, 259, 258, 257, 256, 256, 255], [252, 253, 254, 255, 256, 257, 256, 255, 256, 257, 256, 255, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 265, 265, 265, 264, 263, 264, 263, 262, 261, 260, 259, 258, 258, 257, 256, 255, 254, 253, 253, 254, 255, 256, 256, 255, 255, 256, 257, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 263, 262, 261, 260, 259, 259, 259, 258, 257, 256, 255, 254, 255, 256, 255, 254, 254, 253, 252, 251, 252, 251, 250, 249, 250, 251, 252, 253, 254, 255, 254, 253, 254, 255, 256, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 263, 262, 261, 260, 260, 261, 262, 261, 260, 259, 259, 258, 257, 256, 255, 254, 253, 252, 251, 250, 249, 248, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 261, 260, 260, 260, 261, 262, 263, 264, 265, 266, 267, 268, 268, 267, 267, 268, 267, 266, 265, 264, 263, 262, 261, 260, 259, 259, 260, 261, 260, 259, 258, 257, 256, 255, 254], [252, 253, 254, 255, 256, 257, 256, 255, 256, 257, 256, 255, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 265, 265, 265, 264, 263, 264, 263, 262, 261, 260, 259, 258, 258, 257, 256, 255, 254, 253, 253, 254, 255, 256, 256, 255, 255, 256, 257, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 263, 262, 261, 260, 259, 259, 259, 258, 257, 256, 255, 254, 255, 256, 255, 254, 254, 253, 252, 251, 252, 251, 250, 249, 250, 251, 252, 253, 254, 255, 254, 253, 254, 255, 256, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 263, 262, 261, 260, 260, 261, 262, 261, 260, 259, 259, 258, 257, 256, 255, 254, 253, 252, 251, 250, 249, 248, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 261, 260, 260, 260, 261, 262, 263, 264, 265, 266, 267, 268, 268, 267, 267, 268, 267, 266, 265, 264, 263, 262, 261, 260, 259, 259, 260, 261, 260, 259, 258, 257, 256, 257, 258], [252, 253, 254, 255, 256, 257, 256, 255, 256, 257, 256, 255, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 265, 265, 265, 264, 263, 264, 263, 262, 261, 260, 259, 258, 258, 257, 256, 255, 254, 253, 253, 254, 255, 256, 256, 255, 255, 256, 257, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 263, 262, 261, 260, 259, 259, 259, 258, 257, 256, 255, 254, 255, 256, 255, 254, 254, 253, 252, 251, 252, 251, 250, 249, 250, 251, 252, 253, 254, 255, 254, 253, 254, 255, 256, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 263, 262, 261, 260, 260, 261, 262, 261, 260, 259, 259, 258, 257, 256, 255, 254, 253, 252, 251, 250, 249, 248, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 261, 260, 260, 260, 261, 262, 263, 264, 265, 266, 267, 268, 268, 267, 267, 268, 268, 267, 266, 266, 266, 265, 266, 267, 268, 267, 268, 267, 267, 266, 265, 264, 263, 262, 261], [252, 253, 254, 255, 256, 257, 256, 255, 256, 257, 256, 255, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 265, 265, 265, 264, 263, 264, 263, 262, 261, 260, 259, 258, 258, 257, 256, 255, 254, 253, 253, 254, 255, 256, 256, 255, 255, 256, 257, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 263, 262, 261, 260, 259, 259, 259, 258, 257, 256, 255, 254, 255, 256, 255, 254, 254, 253, 252, 251, 252, 251, 250, 249, 250, 251, 252, 253, 254, 255, 254, 253, 254, 255, 256, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 263, 262, 261, 260, 260, 261, 262, 261, 260, 259, 259, 258, 257, 256, 255, 254, 253, 252, 251, 250, 249, 248, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 261, 260, 260, 260, 261, 262, 263, 264, 265, 266, 267, 268, 268, 267, 267, 268, 267, 266, 265, 264, 263, 262, 261, 260, 259, 259, 260, 260, 259, 258, 257, 256, 255, 254, 253], [252, 253, 254, 255, 256, 257, 256, 255, 256, 257, 256, 255, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 265, 265, 265, 264, 263, 264, 263, 262, 261, 260, 259, 258, 258, 257, 256, 255, 254, 253, 253, 254, 255, 256, 256, 255, 255, 256, 257, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 263, 262, 261, 260, 259, 259, 259, 258, 257, 256, 255, 254, 255, 256, 255, 254, 254, 253, 252, 251, 252, 251, 250, 249, 250, 251, 252, 253, 254, 255, 254, 253, 254, 255, 256, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 263, 262, 261, 260, 260, 261, 262, 261, 260, 259, 259, 258, 257, 256, 255, 254, 253, 252, 251, 250, 249, 248, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 261, 260, 260, 260, 261, 262, 263, 264, 265, 266, 267, 268, 268, 267, 267, 268, 268, 267, 266, 266, 266, 265, 266, 267, 268, 267, 266, 265, 264, 263, 262, 261, 261, 261, 260], [252, 253, 254, 255, 256, 257, 256, 255, 256, 257, 256, 255, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 265, 265, 265, 264, 263, 264, 263, 262, 261, 260, 259, 258, 258, 257, 256, 255, 254, 253, 253, 254, 255, 256, 256, 255, 255, 256, 257, 257, 257, 258, 259, 260, 261, 262, 263, 262, 262, 263, 264, 264, 263, 262, 261, 260, 259, 259, 259, 258, 257, 256, 255, 254, 255, 256, 255, 254, 254, 253, 252, 251, 252, 251, 250, 249, 250, 251, 252, 253, 254, 255, 254, 253, 254, 255, 256, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 263, 262, 261, 260, 260, 261, 262, 261, 260, 259, 259, 258, 257, 256, 255, 254, 253, 252, 251, 250, 249, 248, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 257, 258, 259, 260, 261, 262, 261, 260, 260, 260, 261, 262, 263, 264, 265, 266, 267, 268, 268, 267, 267, 268, 268, 267, 266, 266, 266, 265, 266, 267, 267, 266, 265, 264, 263, 262, 261, 260, 259, 258, 259]]
print(len(array))
res,m = remove_seams(len(array[0]),array,array)
print(res)
print(m)
