# -*- coding: utf-8 -*-

# COMPLETAR PARA LA ENTREGA DE ESTA PRÁCTICA:
# Fecha:
# Alumno(s):

from PIL import Image, ImageTk
import tkinter
import random
import numpy
import sys
import time
import math

def compute_gradient(grad,img):
    """
    img  is a 2-dimensional grayscale image in a list of list format
    grad is the output represented in the same way
    path is None during the first iteration and contains the previous seam path afterwards
    observe that the gradient is not computed for the first and last rows 
    so that you do not have to use these first and last rows
    """
    width, height = len(grad[0]), len(grad)

    # do not modify this function in this template

    # first and last rows compute a different, simpler, gradient
    for y in (0, height-1): # just first and last rows
        for x in range(1, width-1): # first and last columns are excluded
            grad[y][x] = abs(img[y][x-1] - img[y][x+1])

    for y in range(1,height-1): # gradient for the rest of rows is based on Sobel operator
        for x in range(1, width-1): # first and last columns are excluded
            gx = -img[y-1][x-1]-2*img[y][x-1]-img[y+1][x-1]+img[y-1][x+1]+2*img[y][x+1]+img[y+1][x+1]
            gy =  img[y-1][x-1]+2*img[y-1][x]+img[y-1][x+1]-img[y+1][x-1]-2*img[y+1][x]-img[y+1][x+1]
            grad[y][x] = math.sqrt(gx*gx+gy*gy)

"""Aux method"""
def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

def remove_seams(height,seam_paths, matrix):
    """anyadimos la tupla que vayamos a borrar a un set
        y luego cuando borremos los siguientes vigilamos si esa tupla ya ha sido 
    """

    # print("preremove seam %d %d " % (len(matrix), len(matrix[0])))
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
            # print(i)
            i = i + 1
            # for y in range(height):
            #     matrix[y].pop(path[y])
            paths_validos.append(path)
            usados = merge_two_dicts(usados, aux)
    #ahora guardaremos aqui los pixels a borrar pero por filas

    new_paths = []
    for p in range(height):
        new_paths.append([])

    #giramos
    for path in paths_validos:
        for pos,p in enumerate(path):
            new_paths[pos].append(p)
    # print("Len %d "% len(paths_validos))

    print("Voy a borrar {0} paths".format(len(paths_validos)))

    for i in range(len(new_paths)):
        path_row = new_paths[i]
        path_row.sort()
        path_row.reverse()
        for j in path_row:
            matrix[i].pop(j)

    print(len(new_paths) == len(paths_validos[0]))
    print(len(new_paths[0]) == len(paths_validos))
    # print("removing seam %d %d " % (len(matrix), len(matrix[0])))


def dp_seam_carving_multi(grad,mat,N,pscore=0.8):
    """
    dynamic programming version which finds many paths/seams and
    returns them as a list of paths

    N is the maximum number of seams to be returned, the actual number
    of returned paths might be lower if they are not found.

    A path is discarded if it has a pixel in common with a previous path
    or if its total score multiplied by pscore is not <= best_score
    """
    width, height = len(grad[0]), len(grad)
    infty=1e99
    # first row deserves special treatment:
    mat[0][0]       = infty
    mat[0][width-1] = infty
    for x in range(1,width-1):
        mat[0][x] = grad[0][x]
    # the rest of rows
    for y in range(1,height):
        mat[y][0]       = infty
        mat[y][width-1] = infty
        # COMPLETE (ed)
        for j in range(1,width-1):
            mat[y][j] = grad[y][j] + min(mat[y-1][j-1], mat[y-1][j], mat[y-1][j+1])


    # min_val, min_point = COMPLETE
    # retrieve the best path from min_point
    min_scores = []  # el orden de las semillas que iremos cogiendo
    """
    aux = list(mat[height-1])
    
    for i in list(range(min(N, width))):
        p = aux.index(min(aux))
        aux[p] = infty
        min_scores.append(p)
    """

    aux = sorted([(j,i) for (i,j) in enumerate(mat[height-1])])
    for i in list(range(min(N, width))):
        min_scores.append(aux[i][1])

    #path = [mat[height-1].index( min(mat[height-1]) )] # aqui tenemos el mas pequenyo
    paths = [] # aqui tendremos una lista de paths (lista de listas)
    bscore = mat[height-1].index( min(mat[height-1]) ) #el mejor score es mas pequenyo
    score = bscore

    #condicion de parada
    while (score*pscore <= bscore and len(paths) < min(N, width)):

        #se va a nyadir un camino a path y quitar una semilla en min_scores cada iteracion
        path = [min_scores.pop(0)]


        #cogemos un camino
        for y in reversed(range(0, height-1)):
            ult_el = path[-1]
            aux = [mat[y][ult_el -1], mat[y][ult_el], mat[y][ult_el +1]]
            pos_minimo = aux.index(min(aux)) - 1 # Nos indica quien de sus superiores es minimo, si el -1 / 0 o +1

            #pos_minimo se le sumara para decidir la posicion que anyadir
            path.append(ult_el+pos_minimo)
        path.reverse()
        paths.append(path)
    if not(score*pscore <= bscore and len(paths) < min(N, width)):
        print("--------------------------------------------")
    # a = input("efewwef ")
    # paths.reverse()
    #print(paths)
    # print("Min_scores {0}".format(min_scores))
    # [print(x) for x in paths]
    return paths


def paint_seams(height,seam_paths,color_matrix,path_color=[0,0,0]):
    """
    You don't need to modify this function
    """
    for y in range(height):
        for path in seam_paths:
            color_matrix[y][path[y]] = path_color

def matrix_to_color_image(color_matrix):
    """
    You don't need to modify this function
    """
    return Image.fromarray(numpy.array(color_matrix, dtype=numpy.uint8))

def save_matrix_as_color_image(color_matrix,filename):
    """
    You don't need to modify this function
    """
    img = matrix_to_color_image(color_matrix)
    img.save(filename)


######################################################################
#################       GRAPHICAL APPLICATION       ##################
######################################################################

class MyTkApp():
    """
    You don't need to modify this class
    """

    def __init__(self,
                 color_img,
                 removed_colums,
                 max_number_seams):
        self.root = tkinter.Tk()
        self.root.title("Seam Carving")
        self.color_img = color_img
        self.removed_colums = removed_colums
        self.max_number_seams = max_number_seams
        width, height = color_img.size
        height = min(720, height)
        self.root.geometry('%dx%d' % (width, height + 64))
        self.canvas = tkinter.Canvas(self.root.master, width=width, height=height)
        # Image
        imTk = ImageTk.PhotoImage(color_img)
        self.center_x = imTk.width() / 2
        self.center_y = imTk.height() / 2
        self.canvas_img = imTk
        self.canvas.pack()

        l = tkinter.Label(self.root)
        l.pack()
        self.b = tkinter.Button(self.root, text="Begin", command=self.runSeamCarving)
        self.b.pack()
        self.running = True
        self.root.mainloop()

    def showImg(self, im):
        "Updating image"
        imTk = ImageTk.PhotoImage(im)
        width, height = im.size
        self.canvas.delete(self.canvas_img)
        self.canvas_img = imTk
        self.canvas.create_image(self.center_x, self.center_y, image=self.canvas_img)
        self.canvas.update()

    def runSeamCarving(self):
        self.b.config(text="Carving...")
        t0 = time.time()

        color_img = self.color_img
        removed_colums = self.removed_colums
        width, height = color_img.size
        # convert the color image to a numpy array
        color_numpy = numpy.array(color_img.getdata()).reshape(height, width, 3)  # 3 for RGB
        # convert the numpy array into a list of lists, we will use this
        # list of lists (a list of rows) as our data structure during the
        # computations:
        color_matrix = color_numpy.tolist()

        # make the same for the grayscale version of the image:
        grayscale_img = color_img.convert("F")
        grayscale_numpy = numpy.array(grayscale_img.getdata()).reshape(height, width)
        grayscale_matrix = grayscale_numpy.tolist()

        # let's construct the gradient matrix as a list of lists:
        gradient_matrix = [[0.0 for x in range(width)] for y in range(height)]
        # let's construct the dynamic programming matrix as a list of lists:
        infty = 1e99
        dp_matrix = [[infty for x in range(width)] for y in range(height)]

        self.showImg(color_img)  # show image
        while self.removed_colums > 0:
            # compute the gradient
            compute_gradient(gradient_matrix, grayscale_matrix)
            # call the DP algorithm:
            N = min(self.removed_colums, self.max_number_seams)
            seam_paths = dp_seam_carving_multi(gradient_matrix, dp_matrix, N)
            paint_seams(height, seam_paths, color_matrix)
            # paint and show the seam
            self.showImg(matrix_to_color_image(color_matrix))
            # remove the seam path from the color matrix:
            remove_seams(height, seam_paths, color_matrix)
            # remove from the grayscale_matrix
            remove_seams(height, seam_paths, grayscale_matrix)
            # remove from the gradient matrix
            remove_seams(height, seam_paths, gradient_matrix)
            # decrement width
            width -= len(seam_paths)
            self.removed_colums -= len(seam_paths)
            # paint and show the seam
            self.showImg(matrix_to_color_image(color_matrix))

        # finally, save the resulting image:
        output_file = "seam_carved_" + file_name
        save_matrix_as_color_image(color_matrix, output_file)
        t = time.time() - t0
        print('Final time:', t)
        self.b.config(text="Begin")


######################################################################
######################       MAIN PROGRAM       ######################
######################################################################
if __name__ == "__main__":
    """
    You don't need to modify the main function
    """
    if len(sys.argv) != 4:
        print('\n%s image_file {num_column|%%} number_seams\n' \
              % (sys.argv[0],))
        sys.exit()

    file_name = sys.argv[1]
    ncolumns = sys.argv[2]
    N = int(sys.argv[3])

    # open image
    color_img = Image.open(file_name)
    width, height = color_img.size

    # it is required to open image before processing this parameter in
    # case columns are relative
    if ncolumns[-1] == '%':
        ncolumns = int(float(ncolumns[:-1]) * width / 100)
    else:
        ncolumns = int(ncolumns)
    # python allows us to write 3<ncolumns<width
    # but most other programming languages dont
    assert 3 < ncolumns and ncolumns < width
    # number of columns to be removed
    removed_colums = width - ncolumns

    # tkinter
    app = MyTkApp(color_img,
                  removed_colums,
                  N)