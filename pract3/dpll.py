# -*- coding: utf-8 -*-
import sys
import random

def read_cnf_dimacs(filename):
  linenumber = 0
  num_variables = 0
  num_clauses = 0
  clauses = []
  try:
    with open(filename) as f:
      for line in f:
        linenumber += 1
        line = line.split()
        if len(line)==0 or line[0]=='c': continue
        if len(line)==4 and line[0]=='p' and line[1]=='cnf':
          num_variables = int(line[2])
          num_clauses = int(line[3])
          break;
        sys.exit("error reading cnf file '%s' at line %d" % (filename,linenumber))
      for line in f:
        linenumber += 1
        line = line.split()
        if len(line)==0 or line[0]=='c': continue
        clause = [int(x) for x in line]
        if clause[-1] != 0:
          sys.exit("error reading cnf file '%s' at line %d expecting 0 at last position" \
                   % (filename,linenumber))
        del clause[-1] # remove last element
        if any(abs(x)>num_variables for x in clause):
          sys.exit("error reading cnf file '%s' at line %d variable out of range" \
                   % (filename,linenumber))
        clauses.append(clause)
  except ValueError:
      sys.exit("error reading cnf file '%s' at line %d parsing int" % (filename,linenumber))
  if len(clauses) != num_clauses:
      sys.exit("error reading cnf file '%s' number of clauses differ" % (filename,))
  # just in case, remove empty clauses
  clauses = [clause for clause in clauses if len(clauses)>0]
  return num_variables,clauses

def choose_literal(clauses):
  smallest = min(len(clause) for clause in clauses)
  variables = set(y for clause in clauses for y in clause if len(clause)==smallest)
  #return random.choice(tuple(variables))
  return variables.pop()

"""Reci"""
def simplify(clauses,literal):
  # COMPLETAR
  res = []
  for c in clauses:


    """Esto se puede hacer mas bonito con un in y un menos"""
    aux = []
    esta_literal = False
    for a in c:
      if a == literal:
        esta_literal = True
        break;
      else:
        if a != -literal:
          aux.append(a)
    if not esta_literal:
      if len(aux) == 0: return False;
      res.append(aux)
  """Hasta aqui
  TODO mejorar"""
  if len(res) == 0: return True
  return res


def check(formula,listofliterals):
  # determines if the list of literals is able to assign a True value
  # to the formula
  for literal in listofliterals:
    formula = simplify(formula,literal)
    print("Despejando literal",literal)
    print(formula)
    if isinstance(formula,bool):
      return formula
  # at this point, the formula has not been fully simplified
  return False



"""copiar el codigo de las transpas
solo anyadir para busca el camino.
Hy que ir haciendo que el valor que hemos elegido quede "guardado" en algun lado 
Si choice se usa para eliminar, se anyade"""
def backtracking(formula):
  # COMPLETAR
  literal = choose_literal(formula)

  for choice in (literal, -literal):
    f = simplify(formula, choice)

  if f is not False:
    if f is True:
      return True

  resul = backtracking(f)

  if resul:
    return resul

  return None

def unit_propagation(clauses):
  # COMPLETAR
  pass

def pure_literal_elimination(clauses):
  # COMPLETAR
  pass

def dpll(formula):
  # COMPLETAR
  pass

######################################################################
######################       MAIN PROGRAM       ######################
######################################################################
if __name__ == "__main__":
  if len(sys.argv) != 2:
    print('\n%s dimacs_cnf_file\n' % (sys.argv[0],))
    sys.exit()
        
  file_name = sys.argv[1]
  num_variables,clauses = read_cnf_dimacs(file_name)
  print(clauses)
  # replace backtracking by dpll when checking dpll
  # resul = dpll(clauses)
  resul = backtracking(clauses)
  if resul != None:
    print("We have found a solution:",resul)
    print("The check returns:",check(clauses,resul))
  else:
    print("Not solution has been found")

#si una lista se queda vacia, ya devolvemos False en el bucle.
#si la formula se queda vacia > True