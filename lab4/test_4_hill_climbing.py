from lab4.algorithm.hill_climbing import HillClimbing
from lab4.problem.the0s1s_problem import The0s1sProblem, the0s1s_get_decimal_neighbors
from lab4.util.observer           import LocalSearcObserver

# Problem Instance
the0s1s_problem = The0s1sProblem()

# Hill Climbing 1 - Classical Stop Condition
hc1 = HillClimbing( 
    problem_instance = the0s1s_problem , 
    neighbohood_function = the0s1s_get_decimal_neighbors
)

# Observer
observer1 = LocalSearcObserver( hc1 )
hc1.register_observer( observer1 )

# Search
hc1.search()