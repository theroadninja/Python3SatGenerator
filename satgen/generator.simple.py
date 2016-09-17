
import random

from satlib.problem import Problem
from satlib.clause import Clause
from satlib.lit import Lit


class SimpleGenerator:
    def __init__(self, rand_source=None):
        if rand_source is None:
            rand_source = random.Random()

        self.rand_source = rand_source

    def rand_lit(self, var_count):
        return Lit(self.rand_source.randint(0, var_count-1), 1 == self.rand_source.randint(0,1))

    def rand_clause(self, var_count):
        return Clause(self.rand_lit(var_count), self.rand_lit(var_count), self.rand_lit(var_count))

    def generate(self, var_count, clause_count=None):

        if clause_count is None:
            f = 4.2 * float(var_count)
            clause_count = int(f)

        p = Problem()


        #TODO
        for i in range(clause_count):
            c = self.rand_clause(var_count)
            p.add(c)

        print(p.to_cnf())


        return p



if __name__ == "__main__":
    SimpleGenerator().generate(5)