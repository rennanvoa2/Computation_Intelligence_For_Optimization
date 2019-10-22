from lab4.algorithm.hill_climbing import HillClimbing
from lab4.problem.the0s1s_problem import The0s1sProblem, the0s1s_get_decimal_neighbors
from lab4.util.observer           import LocalSearcObserver

# Problem Instance
the0s1s_problem = The0s1sProblem()

# Hill Climbing 1 - Alternative Stop Condition
hc2 = HillClimbing( 
    problem_instance = the0s1s_problem, 
    neighbohood_function = the0s1s_get_decimal_neighbors,
    params = { "Maximum-Iterations" : 11, "Stop-Conditions" : "Alternative-01" } 
)

# Observer
observer2 = LocalSearcObserver( hc2 )
hc2.register_observer( observer2 )

# Search
hc2.search()