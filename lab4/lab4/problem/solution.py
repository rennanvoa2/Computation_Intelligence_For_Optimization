# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------------------------
"""
Solution
---------

Content:

▶ class LinearSolution

▶ class Encoding

▶ class EncodingDataType

─────────────────────────────────────────────────────────────────────────

CIFO - Computation Intelligence for Optmization

Author: Fernando A J Peres - fperes@novaims.unl.pt - (2019) version L4.0

"""
# -------------------------------------------------------------------------------------------------

# import
from copy import deepcopy

# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
# C O D E
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

# -------------------------------------------------------------------------------------------------
# Class: LinearSolution
# -------------------------------------------------------------------------------------------------
class LinearSolution:
    """
    Solutions that can be represented as a linear solution (as an array or a list)
    """
    # Constructor
    #----------------------------------------------------------------------------------------------
    def __init__(self, representation, encoding_rule, is_single_objective = True ):

        self._representation        = representation
        self._encoding_rule         = encoding_rule
        self._fitness_list          = []
        self._is_fitness_calculated = False
        self._encoding              = Encoding(encoding_rule)

    # representation
    #----------------------------------------------------------------------------------------------
    @property
    def representation(self):
        return self._representation

    @representation.setter
    def representation(self, representation):
        self._representation = representation

    # encoding_rule
    #----------------------------------------------------------------------------------------------
    @property
    def encoding_rule(self):
        return self._encoding_rule

    @encoding_rule.setter
    def encoding_rule(self, encoding_rule):
        self._encoding_rule = encoding_rule
        self._encoding = Encoding(encoding_rule)

    # Fitness
    #----------------------------------------------------------------------------------------------
    @property
    def fitness(self):
        return self._fitness_list[0]

    @property
    def fitness_list(self):
        return self._fitness_list

    def reset_fitness(self):
        self._fitness_list = []

    def clone(self):
        return deepcopy(self)

    @property
    def encoding(self):
        return self._encoding


# -------------------------------------------------------------------------------------------------
# Class: Encoding Definition
# -------------------------------------------------------------------------------------------------
class Encoding():
    # constructor
    #----------------------------------------------------------------------------------------------
    '''"""encoding_rule = {
"Size"         : 1,
"Is ordered"   : False,
"Can repeat"   : True,
"Data"         : [ 1, 15 ],
"Data Type"    : "Interval"
}"""'''
    def __init__(self, encoding_rule ):
        """
        Encoding Contructor

        It creates an Encoding using the encoding rule dictionary:
        {
            "Size"         : <INTEGER-NUMBER>,
            "Is ordered"   : <BOOLEAN>,
            "Can repeat"   : <BOOLEAN>,
            "Data"         : <LIST>
            "Data Type"    : <STRING: "Choices" or "Interval">
        }

        """
        self._size = 0
        if "Size" in encoding_rule:
            self._size = encoding_rule["Size"]

        self._is_ordered = False
        if "Is ordered"  in encoding_rule:
            self._is_ordered = encoding_rule["Is ordered"]

        self._can_repeat = True
        if "Can repeat" in encoding_rule: self._can_repeat = encoding_rule["Can repeat"]

        self._encoding_data = []
        if "Data" in encoding_rule: self._encoding_data = encoding_rule["Data"]

        self._encoding_type = ""
        if "Data Type" in encoding_rule: self._encoding_type = encoding_rule["Data Type"]

    # size
    #----------------------------------------------------------------------------------------------
    @property
    def size(self):
        """
        size of the solution representation
        """
        return self._size

    @property
    def is_ordered(self):
        """
        The order of the elements matter to define a solution?
        """
        return self._is_ordered

    @property
    def can_repeat_elements(self):
        """
        The elements can be repeated in a solutio representation
        """
        return self._can_repeat

    @property
    def encoding_data(self):
        """
        The encoding data, can be the possible elements or an interval (min-max)
        """
        return self._encoding_data

    @encoding_data.setter
    def encoding_data(self, data):
        self._encoding_data = data

    @property
    def encoding_type(self):
        """
        The type of the encoding: choices or interval(min..max)
        """
        return self._encoding_type

class EncodingDataType:
    choices = "Choices"
    min_max = "Interval" # "Min_Max"