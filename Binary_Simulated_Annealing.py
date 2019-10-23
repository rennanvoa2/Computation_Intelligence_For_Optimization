
"""
Created on Thu Sep 26 10:27:12 2019

@author: renna
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:09:39 2019

@author: renna
"""
from random import randint
import math
import random


encoding = [0, 15]

#function for random the first number
def build_solution(encoding, decision_variables):
    max = encoding[-1]
    min = encoding[0]
    i = randint(min, max) # << generate a random number
    return i

#function for returning the fitness of the solution
def objective_function(solution):
    fitness = 0
    binary_rep = dec2bin(solution)
    if solution == 0:
        fitness = 0
    else:
        for digit in binary_rep:
            if digit == 0:
                fitness = 0
            else:
                fitness += int(digit) #fitness = fitnedd + digit
    return fitness




#function for checking if the solution is inside the search space
def is_admissible(solution):
    min = 0
    max = 15
    return (solution >= min and solution <= max)

#function for getting the neighbours
def get_random_neighbour(solution ,decision_variables):
    neig = []
    if solution == decision_variables[0]:
        neig.append(solution + 1)
    elif solution == decision_variables[-1]:
        neig.append(solution-1)
    else:
        neig.append(solution - 1)
        neig.append(solution + 1)

    nr = randint(0,len(neig)-1)
    neighbour = neig[nr]
    return neighbour


# dec2bin and d2b transforms the number into binary
def dec2bin(n):
    b = ''
    while n != 0:
        b = b + str(n % 2)
        n = int(n / 2)
    x = b[::-1]
    if len(x) == 4:
        return x
    elif len(x) == 3:
        return "0" + x
    elif len(x) == 2:
        return "00" + x
    elif len(x) == 1:
        return "000" + x
# dec2bin and d2b transforms the number into binary
def d2b(n):
    if n == 0:
        return ''
    else:
        return d2b(n//2) + str(n%2)


#fuction for searching the key in a dict from the value
def search(term, dic):
    list = []
    for k, v in dic.items():
        if term == v:
            list.append(k)


#run the hill climbing algorithm
def hill_climbing(encoding, decision_variables, temperature):
    first_solution = randint(encoding[0], encoding[-1])
    first_fitness = 0
    best_fitness = 0
    best_solution = first_solution
    list_of_solutions = []


    #Test if the solution is in the Search space
    if first_solution == 0:
        best_fitness = 0
        best_solution = 0
    elif is_admissible(first_solution):
        first_fitness = objective_function(first_solution)
        best_fitness = first_fitness
        best_solution = first_solution
        list_of_solutions.append(first_solution)
    else:
        raise SystemExit(first_solution, "is out of the search space.")

    c = temperature
    #Loop of iterations that you set on the parameters
    while c >= 0.05:
        better_neig_fitness = best_fitness
        better_neig_solution = best_solution



        for i in range(5):
            neighbour = get_random_neighbour(better_neig_solution, decision_variables)
            neigbour_fitness = objective_function(neighbour)
            if neigbour_fitness >= best_fitness:
                better_neig_solution = neighbour
                better_neig_fitness = neigbour_fitness
            else:
                fit = ((better_neig_fitness - neigbour_fitness)*-1) / c
                percentage_accept = math.exp(fit)
                random_nr = random.uniform(0,1.0)
                if percentage_accept >= random_nr:
                    better_neig_solution = neighbour
                    better_neig_fitness = neigbour_fitness

                else:
                    continue
        c *= 0.95

        #check if the fitness of the best neighbour is bigger than our best solution fitness
        if better_neig_fitness >= best_fitness:
            if better_neig_solution not in list_of_solutions:
                list_of_solutions.append(best_solution)
            best_solution = better_neig_solution
            best_fitness = better_neig_fitness

    print("Number",first_solution, "was the first solution random selected and its fitness was", first_fitness)
    print("Number",best_solution, "is now the best Solution and its fitness is", best_fitness)
    counter = 1
    for i in list_of_solutions:
        print(str(counter)+ "º", "solution was:", i)
        counter+= 1
decision_variables = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
hill_climbing(encoding, decision_variables, temperature=1)
