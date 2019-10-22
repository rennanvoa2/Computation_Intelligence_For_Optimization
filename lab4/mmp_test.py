from lab4.problem.mastermind_problem import MastermindProblem, mastermind_encoding1, mastermind_encoding2, mastermind_get_neighbors
from lab4.problem.solution import LinearSolution
from lab4.problem.problem_template import ProblemTemplate 
from lab4.util.terminal import Terminal, FontColor
# The problem instance must define the 

mastermind_problem_instance1 = MastermindProblem()
mastermind_problem_instance2 = MastermindProblem(encoding_rule = mastermind_encoding2)

Terminal.print_box( messages = [ "MASTERMIND PROBLEM" ])
print( f" Objective       = {mastermind_problem_instance1.objective}" )
print( f" Multi-objective = {mastermind_problem_instance1.is_multi_objective}" )


# -----------------------------------------------------------------------------------------------
# Build Solution Function: build_solution() TESTS
# -----------------------------------------------------------------------------------------------

# Can-Repeat = False - Objetive Function: evaluate_solution() TESTS
# -----------------------------------------------------------------------------------------------
Terminal.print_box( messages = ["CanRepeat = False | Build Solution" ])
for _ in range(0,8):
    solution = mastermind_problem_instance1.build_solution()
    print(f"solution = {solution.representation}")

# Can-Repeat = False - Objetive Function: evaluate_solution() TESTS
# -----------------------------------------------------------------------------------------------
Terminal.print_box( messages = ["CanRepeat = False | Build Solution" ])
for _ in range(0,8):
    solution = mastermind_problem_instance2.build_solution()
    print(f"solution = {solution.representation}")

# -----------------------------------------------------------------------------------------------
# Objetive Function: evaluate_solution() TESTS
# -----------------------------------------------------------------------------------------------
Terminal.print_box( messages = ["Objective Function" ] )
feedback = [1,3,4,6]

solution.representation = [1,2,3,4]
mastermind_problem_instance1.evaluate_solution( solution = solution  , feedback = feedback )
print( f" solution = {solution.representation} | feedback = { feedback } | fitness = {solution.fitness}" )

solution.representation = [1,3,4,6]
mastermind_problem_instance1.evaluate_solution( solution = solution  , feedback = feedback )
print( f" solution = {solution.representation} | feedback = { feedback } | fitness = {solution.fitness}" )

solution.representation = [1,3,3,4]
mastermind_problem_instance1.evaluate_solution( solution = solution  , feedback = feedback )
print( f" solution = {solution.representation} | feedback = { feedback } | fitness = {solution.fitness}" )

solution.representation = [1,3,4,4]
mastermind_problem_instance1.evaluate_solution( solution = solution  , feedback = feedback )
print( f" solution = {solution.representation} | feedback = { feedback } | fitness = {solution.fitness}" )

solution.representation = [2,6,5,1]
mastermind_problem_instance1.evaluate_solution( solution = solution  , feedback = feedback )
print( f" solution = {solution.representation} | feedback = { feedback } | fitness = {solution.fitness}" )

# -----------------------------------------------------------------------------------------------
# Neighborhood Function: get_neighbords() TESTS
# -----------------------------------------------------------------------------------------------

# Can-Repeat = False - Neighborhood Function: get_neighbords() TESTS
# -----------------------------------------------------------------------------------------------
Terminal.print_box( messages = [ "CanRepeat = False | Neighborhood Function" ] )

solution.representation = [2,4,3,6]

solution.encoding_rule = mastermind_encoding1
neighbors = mastermind_get_neighbors( solution = solution,  problem = mastermind_problem_instance1)

Terminal.print_line( message = f"neighbors of {solution.representation} are:" )
for neighbor in neighbors:
    print(f"             {neighbor.representation}")

# Can-Repeat = True - Neighborhood Function: get_neighbords() TESTS
# -----------------------------------------------------------------------------------------------
Terminal.print_box( messages = [ "CanRepeat = True | Neighborhood Function"  ] )

solution.encoding_rule = mastermind_encoding2
neighbors = mastermind_get_neighbors( solution = solution, problem = mastermind_problem_instance2)
print()
Terminal.print_line( message = f"neighbors of {solution.representation} are:" )

for neighbor in neighbors:
    print(f"             {neighbor.representation}")



