from lab4.algorithm.hill_climbing import HillClimbing
from lab4.problem.mastermind_problem import MastermindProblem, mastermind_get_neighbors
from lab4.util.observer           import LocalSearcObserver
from lab4.util.terminal           import Terminal, FontColor

master_mind_problem = MastermindProblem()
secret = master_mind_problem.build_solution()

# Hill Climbing 1 - Classical Stop Condition
hc1 = HillClimbing( 
    problem_instance = master_mind_problem , 
    neighbohood_function = mastermind_get_neighbors,
    params = { 
        "Maximum-Iterations" : 10, 
        "Stop-Conditions" : "Alternative-01", 
        "Neighborhood-Size" : -1 
    },
    feedback = secret
)

observer1 = LocalSearcObserver( hc1 )
hc1.register_observer( observer1 )

hc1.search()

Terminal.print_box( messages = [ f"Secret: {secret.representation}"], font_color=FontColor.Cyan)
