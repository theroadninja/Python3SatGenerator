import unittest

from satlib.problem import Problem
from satlib.clause import Clause
from satlib.lit import Lit

class TestProblem(unittest.TestCase):

    def test_problem_equals(self):
        p1 = Problem()
        p2 = Problem()

        c = Clause( Lit(0, "T"), Lit(1, "F"), Lit(2, "T"))

        p1.add(c)
        p2.add(c)

        self.assertEqual(p1, p2)

        p2.add( Clause( Lit(5), Lit(-6), Lit(7)))

        self.assertNotEqual(p1, p2)

    def test_problem_from_cnf(self):
        import os, inspect

        folder = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        with open(folder + "/samples/sample.small.cnf") as f:
            p = Problem.from_cnf(f.read())

        self.assertTrue(p.hasClause(Clause.fromCnfArray([1, 2, 3, 0])))
        self.assertTrue(p.hasClause(Clause.fromCnfArray([-1, 4, 3, 0])))
        self.assertTrue(p.hasClause(Clause.fromCnfArray([-3, 5, 6, 0])))
        self.assertTrue(p.hasClause(Clause.fromCnfArray([-3, -30, 8, 0])))
        self.assertTrue(p.hasClause(Clause.fromCnfArray([-7, -1, 5, 0])))
        self.assertTrue(p.hasClause(Clause.fromCnfArray([8, 5, 1, 0])))

        self.assertFalse(p.hasClause(Clause.fromCnfArray([1, 2, 99, 0])))

        pass #TODO

if __name__ == '__main__':
    unittest.main()
