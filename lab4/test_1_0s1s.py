# -------------------------------------------------------------------------------------------------
# CIFO - Computation Intelligence for Optmization
# Author: Fernando A J Peres - fperes@novaims.unl.pt - (2019) version L4.0
# -------------------------------------------------------------------------------------------------
# The0s1sProblem Test
# - Test Problem
# - Test Neighborhood Function
# -------------------------------------------------------------------------------------------------

# import
from lab4.problem.the0s1s_problem import The0s1sProblem, the0s1s_get_decimal_neighbors
from lab4.problem.solution import LinearSolution
from lab4.problem.problem_template import ProblemTemplate 
from lab4.test.building_blocks_test import ProblemTest, NeighborhoodFunctionTest

# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
# C O D E
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

# The 0s1s Problem Test
the0s1s_problem = The0s1sProblem()
the0s1s_p_test = ProblemTest( the0s1s_problem, require_feedback = False )
the0s1s_p_test.run()

# The 0s1s Problem  Neighborhood Function Test
the0s1s_nf_test = NeighborhoodFunctionTest( the0s1s_problem, the0s1s_get_decimal_neighbors )
the0s1s_nf_test.run()
