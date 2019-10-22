# -------------------------------------------------------------------------------------------------
# CIFO - Computation Intelligence for Optmization
# Author: Fernando A J Peres - fperes@novaims.unl.pt - (2019) version L4.0
# -------------------------------------------------------------------------------------------------
# Mastermind Problem Test - for mastermind_encoding2 (Elements can be repeated)
# - Test Problem
# - Test Neighborhood Function
# -------------------------------------------------------------------------------------------------

# import
from lab4.problem.mastermind_problem import MastermindProblem, mastermind_get_neighbors, mastermind_encoding1, mastermind_encoding2
from lab4.problem.solution import LinearSolution
from lab4.problem.problem_template import ProblemTemplate 
from lab4.test.building_blocks_test import ProblemTest, NeighborhoodFunctionTest

# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
# C O D E
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

# Mastermind Problem Test
mastermind_problem = MastermindProblem(encoding_rule=mastermind_encoding2)
mastermind_p_test  = ProblemTest( mastermind_problem, require_feedback = True )
mastermind_p_test.run()

# The 0s1s Problem  Neighborhood Function Test
mastermind_nf_test = NeighborhoodFunctionTest( mastermind_problem, mastermind_get_neighbors )
mastermind_nf_test.run()