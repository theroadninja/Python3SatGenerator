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
        pass #TODO

if __name__ == '__main__':
    unittest.main()
