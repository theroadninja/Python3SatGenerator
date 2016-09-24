from lit import Lit

class Clause:
    '''
    Normally this would be immutable, but a "feature" of python is that you cant protect anything in a class,
    so instead we will just pretend this shit is immutable.
    '''
    def __init__(self, *literals):
        if literals is None:
            raise ValueError("")
        _ = iter(literals) #make sure its iterable


        self.literals = sorted(literals, key=lambda x: x.variable)

    def __eq__(self, other):
        '''
        >>> Clause( Lit(0,"F"), Lit(1, "T"), Lit(2, "T")) == Clause( Lit(0,"F"), Lit(1, "T"), Lit(2, "T"))
        True
        >>> Clause(Lit(2, "T"), Lit(0,"F"), Lit(1, "T")) == Clause( Lit(0,"F"), Lit(1, "T"), Lit(2, "T"))
        True
        >>> Clause( Lit(0,"F"), Lit(1, "T"), Lit(2, "T")) == Clause( Lit(0,"F"), Lit(1, "T"))
        False
        >>> Clause( Lit(0,"F"), Lit(9, "T"), Lit(2, "T")) == Clause( Lit(0,"F"), Lit(1, "T"), Lit(2, "T"))
        False
        >>> Clause( Lit(0,"F"), Lit(1, False), Lit(2, "T")) == Clause( Lit(0,"F"), Lit(1, "T"), Lit(2, "T"))
        False

        :param other:
        :return:
        '''
        if len(self.literals) != len(other.literals):
            return False

        # TODO maybe be more intelligent in case they are not sorted

        for i in range(len(self.literals)):
            if self.literals[i] != other.literals[i]:
                return False

        return True

    def __lt__(self, other):
        return self.__cmp__(other) < 0


    def __cmp__(self, other):
        '''
        Comparison function for programmers

        functools.cmp_to_key() to use with python3 bullshit
        See https://docs.python.org/3/library/stdtypes.html#list.sort

        >>> Clause( Lit(0, "T"), Lit(1, "T")) < Clause( Lit(0, "T"), Lit(1, "T"))
        False
        >>> Clause( Lit(1, "T"), Lit(2, "T")) < Clause( Lit(0, "T"), Lit(1, "T"))
        False
        >>> Clause( Lit(0, "T"), Lit(1, "T")) < Clause( Lit(1, "T"), Lit(2, "T"))
        True
        >>> Clause( Lit(0, "T"), Lit(5, "T")) < Clause( Lit(0, "F"), Lit(1, "T"))
        True

        '''
        # negative -- self is less
        # zero - equals
        # positive - self is greater

        #first, length domainates
        if len(self.literals) != len(other.literals):
            return len(self.literals) - len(other.literals)

        #then, each literal dominates
        #TODO: be more intelligent about sorting?
        for i in range(len(self.literals)):
            c = self.literals[i].__cmp__(other.literals[i])
            if c != 0:
                return c

        if self == other:
            return 0
        else:
            raise Exception("__cmp__ could not find difference in unequal clauses")


    def __str__(self):
        '''  just seeing if doctest works
        >>> 1
        1
        '''
        return "(" + " v ".join([str(x) for x in self.literals]) + ")"

    def to_cnf_line(self):
        line = ""
        for literal in self.literals:
            line += literal.to_cnf() + " "

        line = line + "0"
        return line

    def __hash__(self):
        return tuple(self.literals).__hash__()

    def all_variables_different(self):
        '''

        :return: True if this clause has all different variables
        '''
        raise "TODO" #not sure I need this


    @staticmethod
    def fromCnfArray(numbers):
        if numbers[-1] != 0:
            raise Exception("clause line does not end with 0; multi-line clauses are not supported")
        else:
            numbers.pop()

        literals = [Lit.fromCnf(i) for i in numbers]
        return Clause(*literals)