# serviceapi.py

import random

import generator_simple

from satlib.problem import Problem


# the actual functions that can be called either by WSGI or command line (or as a lib?)



def generate(var_count, clause_count=None, generator_name="SIMPLE", generator_version=1, count=1, generator_params=None):
    if clause_count is None:
        f = 4.2 * float(var_count)
        clause_count = int(f)

    g = generator_simple.SimpleGenerator(random.Random())
    return g.generate(var_count, clause_count)