
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

#create a dictionary of numbers between min_number and max_number
def make_dict(min_number, max_number, list = [], decision_variables = { }):
    for i in range(min_number,max_number+1):
        list.append(i)
        decision_variables = {"Numbers":list }
    return decision_variables



encoding = [0, 15]

#function for random the first number
def build_solution(encoding, decision_variables):
    max = encoding[-1]
    min = encoding[0]
    i = randint(min, max) # << generate a random number
    return i

#function for returning the fitness of the solution
def objective_function(solution, decision_variables = {}):
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
def get_neighbours(solution, decision_variables):
    numbers = decision_variables["Numbers"]
    neig = []
    if solution == numbers[0]:
        neig.append(solution + 1)
    elif solution == numbers[-1]:
        neig.append(solution-1)
    else:
        neig.append(solution - 1)
        neig.append(solution + 1)
    return neig


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
def hill_climbing(encoding, iterations):
    decision_variables = make_dict(0,15)
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


    #Loop of iterations that you set on the parameters
    for i in range(0,iterations):
        neighbours = []
        neighbour_fitness = {}
        better_neig_fitness = 0
        better_neig_solution = 0

        #populate neightbours
        for i in get_neighbours(best_solution, decision_variables):
            neighbours.append(i)

        #populate neightbours fitness
        for neighbour in neighbours:
            neighbour_fitness.update({neighbour:objective_function(neighbour)})

        #check if the solution was already used and
        #test which neighbour has the best fitness
        for solution, fitness in neighbour_fitness.items():
            if solution in list_of_solutions:
                continue
            if fitness>=better_neig_fitness:
                better_neig_fitness = fitness
                better_neig_solution = solution

        #check if the fitness of the best neighbour is bigger than our best solution fitness
        if better_neig_fitness >= best_fitness:
            best_solution = better_neig_solution
            best_fitness = better_neig_fitness
            list_of_solutions.append(best_solution)

    print("Number",first_solution, "was the first solution random selected and its fitness was", first_fitness)
    print("Number",best_solution, "is now the best Solution and its fitness is", best_fitness)
    for i in list_of_solutions:
        print(i)
hill_climbing(encoding, 10)