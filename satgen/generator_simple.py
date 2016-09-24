
import random

from satlib.problem import Problem
from satlib.clause import Clause
from satlib.lit import Lit


class SimpleGenerator:
    def __init__(self, rand_source=None):
        if rand_source is None:
            rand_source = random.Random()

        self.rand_source = rand_source

    def rand_var(self, var_count):
        return self.rand_source.randint(0, var_count-1)

    def rand_lit(self, var_count):
        return Lit(self.rand_source.randint(0, var_count-1), 1 == self.rand_source.randint(0,1))

    def rand_clause(self, var_count, allow_tautologies=True):
        if var_count is None or var_count < 3:
            raise Exception("var_count is {} - must be at least 3".format(var_count))

        if allow_tautologies:
            return Clause(self.rand_lit(var_count), self.rand_lit(var_count), self.rand_lit(var_count))
        else:
            variables = set()

            safety = 100000
            while(len(variables) < 3 and safety > 0):
                variables.add( self.rand_var(var_count) )
                safety -= 1 #some idiot could call this with two vars

            literals = list()
            for v in variables:
                literals.append( Lit(v, 1 == self.rand_source.randint(0,1)))

            return Clause(*literals)



    def generate(self, var_count, clause_count=None):

        if clause_count is None:
            f = 4.2 * float(var_count)
            clause_count = int(f)

        p = Problem()


        #TODO
        for i in range(clause_count):
            c = self.rand_clause(var_count, allow_tautologies=False)
            p.add(c)

        #print(p.to_cnf())


        return p



if __name__ == "__main__":
    SimpleGenerator().generate(5)
