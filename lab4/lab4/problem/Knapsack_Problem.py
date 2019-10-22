from lab4.problem.problem_template import ProblemTemplate, ProblemObjective
from lab4.problem.solution import LinearSolution, Encoding
from copy import deepcopy
from random import choice
from random import randint




dv_knapsack_template = {
    "Index": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
    "Values": [23.30, 43.70, 24.70, 35.70, 34.70, 21.80, 24.70, 35.70, 34.70, 21.80, 23.30, 43.70, 24.70, 35.70, 34.70, 21.80, 24.70, 35.70, 34.70, 21.80, 34.20, 12.50, 34.70, 21.80, 24.70, 35.70, 34.70, 19.60, 23.60, 21.80, 24.70, 35.70, 34.70, 21.80, 23.30, 43.70, 24.70, 35.70, 34.70, 21.80, 24.70, 23.30, 43.70, 32.00, 35.70, 34.70, 21.80, 24.70, 35.70, 34.70],
    'Weights': [23.40, 24.10, 24.40, 25.60, 23.10, 12.90, 23.60, 19.60, 24.40, 25.60, 23.10, 12.90, 23.60, 19.60, 23.40, 24.10, 24.40, 25.60, 23.10, 12.90, 23.60, 19.60, 24.40, 25.60, 23.10, 12.90, 23.60, 19.60, 23.10, 24.40, 25.60, 23.10, 12.90, 23.60, 19.60, 23.40, 24.10, 24.40, 25.60, 23.10, 12.90, 23.10, 12.90, 40.00, 19.60, 24.40, 25.60, 23.10, 12.90, 23.60]
}

# encoding 1: The elements cannot be repeated
knapsack_encoding1 = {
    "Size"         : 50,
    "Is ordered"   : True,
    "Can repeat"   : True,
    "Data"         : [0,1], # in the constructor must get the data from the Dvs (as it is DV dependent)
    "Data Type"    : "Choices"
}


class KnapSackProblem(problem_template):
    def __init__(self, decision_variables = dv_knapsack_template, constraints={}, encoding_rule = knapsack_encoding1):
        super().__init__(decision_variables = decision_variables, constraints = constraints, encoding_rule = encoding_rule)
        self._name = "Knapsack Problem"


def build_solution(self, decision_variables):
    solution = []

    for i in range(50):
        solution.append(0)
        
    while is_admissible(solution, decision_variables):
        random_nr = randint(0,49)
        new_solution = solution
        new_solution[random_nr] == 1
        if is_admissible(new_solution):
            if solution[random_nr] == 0:
                solution[random_nr] = 1
        else:
            break
    
    return solution




def is_admissible(self, solution, decision_variables):

    total_weight = 0
    weight = decision_variables['Weights']

    for i in range(len(solution)):
        if solution[i] == 1:
            total_weight += weight[i]

    if total_weight <= 250:
        return True
    else:
        return False







