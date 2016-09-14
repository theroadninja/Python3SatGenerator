# serviceapi.py

from satlib.problem import Problem

# the actual functions that can be called either by WSGI or command line (or as a lib?)



def generate(var_count, clause_count, generator_name="SIMPLE", generator_version=1, count=1, generator_params=None):
    p = Problem()
    return p