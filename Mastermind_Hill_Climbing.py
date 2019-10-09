# -*- coding: utf-8 -*-

#Import Librarys
from random import randint


#Encrypt the colors into 2 lists of colors and numbers
def encrypt_decision_variables(decision_variables):
    encrypted = {'Colors':[], 'Numbers':[]}
    v = 0
    for i in decision_variables:
        encrypted['Colors'].append(i)
        encrypted['Numbers'].append(v)
        v += 1
    return encrypted

#Return the colors for the given numbers
def decrypt_into_colors(list, encrypted_decision_variables):
    decrypted = []
    #find the color by the number on code
    counter = 0
    for i in list:
        for k,v in encrypted_decision_variables.items():
            if k == 'Numbers':
                for item in v:
                        if item == i:
                            decrypted.append(encrypted_decision_variables['Colors'][item])
    return decrypted

#function for checking if the solution is inside the search space
def is_admissible(solution, encoding):
    min = encoding[0]
    max = encoding[-1]
    return (solution >= min and solution <= max)

#function for random the code blank spaces and repeat colors are false by default.
def build_solution(encoding,repeat_colors, decision_variables={}):
    code=[]

    #Random 4 colors. Not allowed to repeat colors.
    if repeat_colors == False:
        while len(code) < 4:
            rint = randint(0,len(decision_variables['Numbers'])-1)
            if decision_variables['Numbers'][rint] not in code and len(code) < 4:
                if is_admissible(decision_variables['Numbers'][rint], encoding):
                    code.append(decision_variables['Numbers'][rint])
                else:
                    raise SystemError("Wrong Search Space !")

    #Random 4 colors. Allowed to repeat  colors.
    elif repeat_colors == True:
        while len(code) < 4:
            rint = randint(0,len(decision_variables['Numbers'])-1)
            if len(code) < 4:
                if is_admissible(decision_variables['Numbers'][rint], encoding):
                    code.append(decision_variables['Numbers'][rint])
                else:
                    raise SystemError("Wrong Search Space !")


    return code

#Check if the encoding is able to use blank spaces or not
def  get_encoding(decision_variables):
    encoding = [0,len(decision_variables)-1]
    return encoding


#function for returning the fitness of the solution
#Max Score: 400 points
#Right Color in the Right place: 90 poins
#Right Color in the wrong place: 10 points
def objective_function(code, solution):
    fitness = 0
    used_numbers = []

    #add 30 fitness for each count of the number in solution
    for i in range(0,len(solution)):
        if solution[i] not in used_numbers:
            count_solution_in_code = code.count(solution[i])
            count_solution_in_solution = solution.count(solution[i])
            if count_solution_in_code == solution.count(solution[i]):
                fitness += count_solution_in_code * 30
            else:
                if min([count_solution_in_code, count_solution_in_solution ]) == 0:
                    used_numbers.append(solution[i])
                    continue
                else:
                    fitness = min([count_solution_in_code, count_solution_in_solution ]) * 30
                    used_numbers.append(solution[i])

    #add 90 fitness if the solution is in the right place
    for i in range(0,len(solution)):
        if solution[i] == code[i]:
                fitness += 90

    return fitness


#get the 4 neighbours
def get_Neighbours(solution, encoding):
    new_neighbours = []

    for i in range(0, len(solution)):
        new_solution = []
        for x in solution:
            new_solution.append(x)
        nr = randint(encoding[0], encoding[-1])
        new_solution[i] = nr
        new_neighbours.append(new_solution)
    return new_neighbours





#Hill climbing Algorithm
def hill_climbing(decision_variables,iterations, repeat_colors=False, blank_spaces=False):
    best_fitness = 0
    best_solution = []
    first_solution = []
    first_fitness = []
    list_of_solutions = []


    if blank_spaces==True:
        decision_variables += ['Blank Space']

    #here we can't define a fixed encoding, becouse the number of colors can change, so i made a function for getting it
    #depending on the numbers of colors entered
    encoding = get_encoding(decision_variables)

    #transform the list of colors into a dict with 2 dics, 1 is the colors and other is the reference number of the color
    encrypted_decision_variables = encrypt_decision_variables(decision_variables)

    #code to be detected
    code = build_solution(encoding,repeat_colors=repeat_colors,
    decision_variables=encrypted_decision_variables)

    #first random solution and the fitness
    first_solution = build_solution(encoding,repeat_colors=repeat_colors,
    decision_variables=encrypted_decision_variables)
    list_of_solutions.append(first_solution)
    first_fitness = objective_function(code, first_solution)
    best_fitness = first_fitness
    best_solution = first_solution


    for i in range(0, iterations):
        neighbours = []
        neighbours_fitness = []
        exploited_neighbours = []
        exploited_neighbours_fitness = []
        best_neighbours = []
        best_neighbours_fitness = []
        better_neighbours = []
        better_neighbours_fitness = 0
        better_neig_solution = []

        #populate neightbours of the first solution
        neighbours = get_Neighbours(best_solution, encoding)

        #populate neightbours fitness
        for neighbour in neighbours:
            neighbours_fitness.append(objective_function(code, neighbour))

        #check if the solution was already used and
        #test which neighbour has the best fitness
        for solution in neighbours:
            if solution in list_of_solutions:
                continue
            if objective_function(code,solution)>=better_neighbours_fitness:
                better_neighbours_fitness = objective_function(code, solution)
                better_neig_solution = solution

        #put on global var (memory) the best result found in this iteration
        if better_neighbours_fitness >= best_fitness:
            best_solution = better_neig_solution
            best_fitness = better_neighbours_fitness
            list_of_solutions.append(best_solution)



    print('Code:',decrypt_into_colors(code, encrypted_decision_variables))
    print('First Solution:',decrypt_into_colors(first_solution, encrypted_decision_variables))

    print(decrypt_into_colors(first_solution, encrypted_decision_variables),
    "was the first solution random selected and its fitness was", first_fitness)
    print(decrypt_into_colors(best_solution, encrypted_decision_variables), "is the Solution and its fitness is",
    best_fitness)
    print("\n","The folowing solutions were found before breaking the code:")

    for i in range(0,len(list_of_solutions)):
        x = i +1
        print(str(x)+ "º", "solution was:", decrypt_into_colors(list_of_solutions[i], encrypted_decision_variables))

#You can choose as many colors as you want, more colors make it harder for the algorithm to solve the problem
#Just add more colors to the list and try it
decision_variables = ['Red', 'Green', 'Dark Blue', 'Yellow', 'Brown', 'Orange','Purple']

#You have 4 parameters:
#Firt is the list of colors
#Second is the number of iterations
#Third is if you want the colors to repeat or not.
#Fourth is if allowed blank spaces or not
hill_climbing(decision_variables,10, repeat_colors=False,blank_spaces=False)